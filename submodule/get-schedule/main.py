try:
    from Image import *
except ImportError:
    from PIL import Image
from io import BytesIO

import pytesseract
import requests
from lxml import etree

username = input('username:')
password = input('password:')
s = requests.session()
s.get('http://jwxt.bupt.edu.cn/')
while True:
    captchaImage = Image.open(BytesIO(s.get('http://jwxt.bupt.edu.cn/validateCodeAction.do?random=').content))
    captchaImage = captchaImage.convert('L')
    captchaText = pytesseract.image_to_string(captchaImage)
    loginSuccessPage = s.post('http://jwxt.bupt.edu.cn/jwLoginAction.do',
                              data={'zjh': username, 'mm': password, 'v_yzm': captchaText}).text
    if etree.HTML(s.post('http://jwxt.bupt.edu.cn/jwLoginAction.do',
                         data={'zjh': username, 'mm': password, 'v_yzm': captchaText}).text).xpath(
        '/html/head/title/text()')[0] == '学分制综合教务':
        break

print('Login Success')
table = etree.HTML(s.get('http://jwxt.bupt.edu.cn/xkAction.do?actionType=6').text,
                   parser=etree.HTMLParser(recover=True, remove_blank_text=True, remove_comments=True)).xpath(
    '//tr[@bgcolor="#FFFFFF"]')

str = ''
for i in table:
    for j in i.xpath('td/text()'):
        str += j.strip() + ':'
    str += '\n'
print(str)
