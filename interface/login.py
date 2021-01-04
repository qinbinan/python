# -*-coding:UTF-8 -*-
from requests.api import get
url = 'http://192.168.1.5:8080/recruit.students/login/in'
params = {
    'account':'admin',
    'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
}
cookies = {
    'JSESSIONID':'53F7CEDF986BC9223EAFD91348A400BA',
}
response = get(url, params, cookies=cookies)
print(response.status_code)
