# /usr/bin python
#coding=utf-8
import logging
import HTMLTestRunner
import os
import requests
import sys
import time
import unittest
import yaml
from Email import SendEmail
from Log import Log
from ReadTestCase import read_test_case

a = open('F:\\test\\study\\yaml\\Testcase\\testcase.yaml')
e = yaml.load(a)

class TestSuit(unittest.TestCase):

    # @read_test_case
    def test_login(self):
        logging.info('-'*5+"begin test"+"-"*5)
        testdata = e[0]
        c = testdata['test']
        request = c['request']
        name = c['name']
        method = request['method']
        url = request['url']
        headers = request['headers']
        data = request['json']
        logging.info('-'*5+'测试的接口是'+name+'-'*5)
        re = requests.request(method,url,headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        logging.info('-'*5+'返回状态码是'+s+'-'*5)
        assert status_code == 200

    def test_login_failed(self):
        logging.info('-'*5+"begin test"+"-"*5)
        testdata = e[1]
        #先获取需要的用例
        c = testdata['test']
        #再取到用例里面的请求体
        request = c['request']
        #然后获取到请求体里面的各个字段
        name = c['name']
        method = request['method']
        url = request['url']
        headers = request['headers']
        data = request['json']
        logging.info('-'*5+'测试的接口是'+name+'-'*5)
        re = requests.request(method,url,headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        logging.info('-'*5+'返回状态码是'+s+'-'*5)
        assert status_code == 200

if __name__ == "__main__":
    #解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestSuit("test_login"))
    suite.addTest(TestSuit("test_login_failed"))
    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time1=time.strftime("%H%M%S")
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #创建路径
    path='F:/test/study/yaml/test_log/'+now+"/"
    #解决多次执行时报路径已存在的错误
    try:
        os.makedirs(path)
    except:
        if path!= None:
            logging.info(u'当前路径已经存在')
    filename=path+'Report.html'
    fp=file(filename,'wb')
    #日志记录
    Log.log()
    #执行测试
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'下单平台接口测试用例',description=u'接口用例列表：')
    runner.run(suite)
    fp.close()

    # SendEmail.sendMail()
