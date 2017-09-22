# /usr/bin python
#coding=utf-8
import yaml

# a = open('F:\\test\\study\\yaml\\Testcase\\testcase.yaml')
# e = yaml.load(a)

def read_test_case():
    print u'test gogogo'
    a = open('F:\\test\\study\\yaml\\test.yaml')
    e = yaml.load(a)

    # print(e['name'])
    # print e['children'][1]['name1']

    # 先获取到需要的测试数据
    testdata = e[1]
    c = testdata['test']
    request = c['request']
    url = request['url']
    header = request['headers']
    print(e[0])
    print(e[1])
    print(c)
    print(request)
    # print(age)

if __name__ == '__main__':
    read_test_case()