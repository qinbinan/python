# -*- coding: utf-8 -*-
from requests.api import get
from utils.Logger import Logger
from cgi import log

logger = Logger('TestEducation').getlog()


class TestEducation():

    def test_login(self):
        url = 'http://192.168.1.5:8080/recruit.students/login/in'
        params = {
            'account':'admin',
            'pwd':'660B8D2D5359FF6F94F8D3345698F88C'
        }
        cookies = {
            'JSESSIONID':'4C7F9900296CCF401EA453523988978F'
        }
        logger.info('url为：' + url)
        response = get(url, params, cookies=cookies)
        logger.info('我的状态码为%s' % response.status_code)
        # print(response)
        # print(response.text)
        # print(response.status_code)
        assert response.status_code == 200

