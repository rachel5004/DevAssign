const copyTextarea = document.querySelector(fieldId);
copyTextarea.focus();
copyTextarea.select();

try {
  navigator.clipboard.writeText(copyTextarea.value);
  console.log('복사된 텍스트 내용: ' + copyTextarea.value);
} catch (err) {
  console.log('복사할 수 없음!');
}
