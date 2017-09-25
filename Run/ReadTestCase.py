# /usr/bin python
#coding=utf-8
import yaml,logging,requests

# a = open('F:\\test\\study\\yaml\\Testcase\\testcase.yaml')
# e = yaml.load(a)
#
# def read_test_case():
#     print u'test gogogo'
#     a = open('F:\\test\\study\\yaml\\test.yaml')
#     e = yaml.load(a)
#
#     # print(e['name'])
#     # print e['children'][1]['name1']
#     c=len(e)
#     # print(c)
#     for i in range(0,c):
#     # 先获取到需要的测试数据
#         a = open('F:\\test\\study\\yaml\\test.yaml')
#         e = yaml.load(a)
#         testdata = e[i]
#         c = testdata['test']
#         request = c['request']
#         url = request['url']
#         headers = request['headers']
#         method = request['method']
#         name = c['name']
#         # print(e[i])
#         data = request['json']
#         logging.info('-'*5+'测试的接口是'+name+'-'*5)
#         re = requests.request(method,url,headers=headers,data=data)
#         status_code = re.status_code
#         s = str(status_code)
#         assert status_code == 200
def test_case():
    #获取测试用例
    a = open('F:\\test\\study\\yaml\\Testcase\\testcase.yaml')
    e = yaml.load(a)
    c= len(e)
    #遍历执行用例
    for i in range(0,c):
        testdata = e[i]
        t = testdata['test']
        request = t['request']
        name = t['name']
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

if __name__ == '__main__':
    test_case()