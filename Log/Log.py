# coding=utf-8
#此处使用python自带的logging模块，用来作为测试日志，记录测试中系统产生的信息。
import logging,os,time
#定义date为日期，time为时间
def log():
    # date=time.strftime("%Y%m%d")
    # time1=time.strftime("%H%M%S")
    # path = 'F:\\test\\study\\yaml\\Log'
    # log_file = os.path.join(os.getcwd(),'sas.log')
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #创建路径
    path='F:/test/study/yaml/test_log/'+now+"/"
    #解决多次执行时报路径已存在的错误
    try:
        os.makedirs(path)
    except:
        if path!= None:
            print u'当前路径已经存在'
    log_file = path+'Run.log'
    log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
    #配置log格式
    logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)