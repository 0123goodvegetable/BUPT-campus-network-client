try:
    from Image import *
except ImportError:
    from PIL import Image
from io import BytesIO

import pytesseract
import requests
from lxml import etree

# Login
username = '2016211938'  # input('username:')
password = 'mhtt1123'  # input('password:')
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

zxjs = s.get('http://jwxt.bupt.edu.cn/xszxcxAction.do?oper=xszxcx_lb').text
postData = {'zxxnxq': '', 'zxXaq': '', 'zxJxl': '', 'zxZc': '', 'zxJc': '', 'zxxq': '', 'pageSize': '20', 'page': '1',
            'currentPage': '1', 'pageNo': ''}

# Choose semesters
xnxq = etree.HTML(zxjs).xpath(
    '/html/body/form/table[@class="titleTop1"]/tr/td/table[@class="titleTop1"]/tr/td/table/tr/td/select[@name="zxxnxq"]/option')
semesters = []
for i in xnxq:
    for key, value in i.items():
        if key == 'value' and len(value) != 0:
            semesters.append((value, i.text))
print('Please choose semesters:')
for i in range(0, len(semesters)):
    print(i, semesters[i])
choice = 16  # int(input('Your choice:'))
print('Your choice is:', semesters[choice][1])
postData['zxxnxq'] = semesters[choice][0]

# Choose schools
xq = etree.HTML(zxjs).xpath(
    '/html/body/form/table[@class="titleTop1"]/tr/td/table[@class="titleTop1"]/tr/td/table/tr/td/select[@name="zxXaq"]/option')
schools = []
for i in xq:
    for key, value in i.items():
        if key == 'value' and len(value) != 0:
            schools.append((value, i.text))
for i in range(0, len(schools)):
    print(i, schools[i])
choice = 1  # int(input('Your choice:'))
print('Your choice is:', schools[choice][1])
postData['zxXaq'] = schools[choice][0]

jxl = etree.HTML(s.post('http://jwxt.bupt.edu.cn/xszxcxAction.do?oper=ld', data=postData).text).xpath(
    '/html/body/form/table[@class="titleTop1"]/tr/td/table[@class="titleTop1"]/tr/td/table/tr/td/select[@name="zxJxl"]/option')
buildings = []
for i in jxl:
    for key, value in i.items():
        if len(value) != 0:
            buildings.append((value, i.text))
print('Please choose buildings:')
for i in range(0, len(buildings)):
    print(i, buildings[i])
choice = 1  # int(input('Your choice:'))
print('Your choice is:', buildings[choice][1])
postData['zxJxl'] = buildings[choice][0]
print(postData)
f = open('tests.html', 'w')
f.write(s.post('http://jwxt.bupt.edu.cn/xszxcxAction.do?oper=ld', postData).text)
f.close()
