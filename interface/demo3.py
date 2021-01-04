# -*-coding:UTF-8 -*-
from requests.api import get
from utils.Logger import Logger

logger = Logger('TestEdc').getlog()


class Edc:

    def te_login(self):
        url = 'http://192.168.1.5:8080/recruit.students/login/in'
        params = {
            'account':'admin',
            'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
        }
        cookies = {
            'JSESSIONID':'53F7CEDF986BC9223EAFD91348A400BA',
        }
        response = get(url, params, cookies=cookies)
        logger.info('状态码为%s' % response.status_code)
        #assert response.status_code == 200

ed = Edc()
ed.te_login()
