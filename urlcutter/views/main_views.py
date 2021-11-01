from flask import Blueprint, render_template,abort, request, Response,redirect
from flask_restful import Resource, reqparse
from datetime import datetime
from urlcutter import db,api
from urlcutter.models import Url
import log
from secrets import token_urlsafe

bp = Blueprint('main',__name__, url_prefix="/")

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/<shortcut>')
def redirectShortcut(shortcut):
    log.log(request,"redirect shortcut")
    data = Url.query.filter(Url.shortcut==shortcut).all()
    if data: return redirect(data[0].original, code=302)
    else: abort(404)

@bp.route('/url',methods=['GET', 'POST'])
def getShortCut():
    url=''
    # fetch default method=GET
    if request.method == 'GET': url=request.args.get('url')
    elif request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.get_json()
            url=data['url']
        elif request.content_type.startswith('multipart/form-data'):
            url = request.form.get('url')
    # check if shortcut already exist
    object = Url.query.filter(Url.original==url).all()
    if object: return {'shortcut':object[0].shortcut}
    else: shortcut = Generate(url)
    return {'shortcut':shortcut}


def base62(index):
    result = ""
    words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while index % 62 > 0 or result == "": # index가 62인 경우에도 적용되기 위해 do-while 형식이 되도록 구현했다.
        result += words[index % 62]
        index = int(index / 62)
    return result

def Generate(URL):
    # DB에 원본 URL Insert
    url = Url(original=URL,create_date=datetime.now())
    db.session.add(url)
    db.session.commit()

    # URL이 등록 된 Index를 Base62로 인코딩하여 shortcut 생성
    index = url.id
    # shortURL = base62(index)
    # or with secrets
    shortURL = token_urlsafe(6)

    # 생성된 shortcut 정보 DB에 갱신
    url.shortcut=shortURL
    db.session.commit()
    return shortURL

# class urlRestApi(Resource):
#     def get(self):
#         shortcut=""
#         data = Url.query.filter(Url.shortcut == shortcut).all()
#         if data: return Response(302, data[0].original)
#         else: return Response(404)
#     def post(self):
#         try:
#             parser = reqparse.RequestParser()
#             parser.add_argument('url', type=str)
#             args = parser.parse_args()
#             url = args['url']
#             # check if shortcut already exist
#             object = Url.query.filter(Url.original == url).all()
#             if object:
#                 return object[0].shortcut
#             else:
#                 shortcut = Generate(url)
#                 return shortcut
#         except Exception as e:
#             log.error_log(e)
#
# api.add_resource(urlRestApi, '/')