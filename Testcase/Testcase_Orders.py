#coding: utf-8

"""
作者：大石
功能：待执行的接口测试用例
环境：python2.7.6
用法：通过框架自动触发调用
"""
import unittest,requests,datetime,sys,logging,BSTestRunner,time,os
from Log import Log
class Testcase_Orders(unittest.TestCase):
    u"""待测试接口：/login"""
    def setUp(self):
        logging.info('-'*5+"begin test"+"-"*5)

    def tearDown(self):
        logging.info('-'*5+"end test"+'-'*5)

    
    def test_login(self):
        u"""测试登录"""
        headers = {'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        data = {'uname': '187071484771', 'pwd': '123456'}
        re = requests.post(url='http://www.senbaba.cn/login',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'返回状态码是'+s+'-'*5)
        logging.info('-'*5+'返回结果集是'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'

    def test_login_failed(self):
        u"""测试登录"""
        headers = {'Accept-Language': 'zh-CN', 'content-type': 'application/json', 'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        data = {'uname': '187071484771', 'pwd': '123457'}
        re = requests.post(url='http://www.senbaba.cn/login1',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'返回状态码是'+s+'-'*5)
        logging.info('-'*5+'返回结果集是'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'


if __name__ == "__main__":
    #解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Testcase_Orders("test_login_failed"))
    # suite.addTest(Testcase_Orders("login_failed"))
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
            logging.error(u'当前路径已经存在')
    filename=path+'Report.html'
    fp=file(filename,'wb')
    #日志记录
    Log.log()
    #执行测试
    runner =BSTestRunner.BSTestRunner(stream=fp,title=u'下单平台接口测试用例',description=u'接口用例列表：')
    runner.run(suite)
    fp.close()
