# -*- coding: utf-8 -*-
from requests.api import get

url='http://192.168.1.5:8080/recruit.students/login/in'
params={
    'account':'admin',
    'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
}
cookies={
    'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
}
response = get(url,params,cookies=cookies)
print(response)
print(response.text)


