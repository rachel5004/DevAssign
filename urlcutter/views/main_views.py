from flask import Blueprint, render_template
from urlcutter.models import Url

bp = Blueprint('main',__name__, url_prefix="/")

@bp.route('/hello')
def hello():
    return 'Hello, world!'


@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/url')
def getShortCut(url):
    # check if shortcut already exist
    data = DB.select('encoded', url.data)
    # generate shortcut
    shortcut = Url.query.get_or_
    # Insert DB

    return shortcut

def base62(index):
    result = ""
    words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while index % 62 > 0 or result == "": # index가 62인 경우에도 적용되기 위해 do-while 형식이 되도록 구현했다.
        result = result + words[index % 62]
        index = int(index / 62)
    return result

def Generate(URL):
    # DB에 URL Insert
    index = DB.insert(URL)
    # URL이 등록 된 Index를 Base62로 인코딩
    shortURL = base62(index)
    # 인코딩 된 정보 DB에 갱신
    DB.update(index, shortURL)
    return shortURL

