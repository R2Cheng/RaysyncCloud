# coding=utf-8
import requests
import json
import xlrd,xlwt
import datetime,logging
from xlutils.copy import copy
import os
pwd = os.path.dirname(os.path.abspath(__file__))
# def public_path():
#     '''一些公共路径'''
#     path_datas = '../datas/'              #测试数据
#     path_testcase = '../testcase/'        #测试用例
#     path_report = '../report/'            #测试报告
#     return path_datas,path_testcase,path_report


def read_excel(sheet,row,col):
    '''读取excel表公共方法'''
    a = xlrd.open_workbook(os.path.dirname(pwd)+'\datas/apiTestCase1.xls')
    b = a.sheet_by_name(sheet)
    c = b.cell_value(row,col)
    print(c)
    return c

def write_excel(list,row,col,data):
    '''写入excel表公共方法'''
    file = os.path.dirname(pwd)+'\datas/apiTestCase1.xls'
    rb = xlrd.open_workbook(file, formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(list)
    ws.write(row, col, data)
    wb.save(file)
    print('写入数据成功')
    #list 第几章表0开始，row几行, col几列, data写入的数据



def Headers(userkey):
    '''公共headers'''
    headers = {
        'channel': "2",
        'platform': "2",
        'signature': "rayvision2017",
        'version': "1.0.0",
        'userkey': userkey,
        'content-type': "application/json",
        'languageflag': "1"
    }
    return headers

# def assert_num(self,sheet,row,col,result,url):
#     '''判断每个接口用例执行几次断言'''
#     a = read_excel(sheet,row,col).split('\n')       #获取预期结果
#     b = read_excel(sheet, row, col+1).split('\n')   #获取结果解释
#     for i,j in zip(a,b):
#         r = result[i.split(':')[0]]                 #r就是从返回值中取出的要进行校验的字段
#         if type(r) is int:                                #如果返回值取出的数据为int格式，把他转为str，方便跟excel中取出的字符串比较,此框架从excel表中取出的内容为str格式
#             r = str(r)
#         else:
#             pass
#         self.assertIn(i.split(':')[1], r,msg='['+j+'校验有误]'+url)

def assert_num(self,sheet,row,col,result,url):
    '''判断每个接口用例执行几次断言'''
    a = read_excel(sheet,row,col).split('\n')       #获取预期结果
    b = read_excel(sheet, row, col+1).split('\n')   #获取结果解释
    for i,j in zip(a,b):
        x = i.split(':')[0]                         #x就是从返回值中取出的要进行校验的字段
        if '-' in x:                                #判断若excel里面额字段不是一层，则转换成字典连续取值的格式
            y = x.split('-')
            for key in y:
                result = result[key]
            r = result
        else:
            r = result[x]
        if type(r) is int:                                #如果返回值取出的数据为int格式，把他转为str，方便跟excel中取出的字符串比较,此框架从excel表中取出的内容为str格式
            r = str(r)
        if type(r) is bool:
            r = str(r)
        else:
            pass
        self.assertIn(i.split(':')[1], r,msg='['+j+'校验有误]'+url)



def shift(a, b, c, d):
    '''
    将excel中取出的请求参数转换成字典并修改字段值
    四个参数分别是：替换后的参数值、需要替换的字段名、原str格式数据、需要转换成的对应格式
    '''
    shift = eval(c)
    if d == 1:
        shift[b] = int(a)
    elif d == 2:
        shift[b] = [int(a)]
    elif d == 3:
        for i, j in zip(a, b):
            if '_' in i:
                shift['paramMap'][j] = i
            else :
                shift['paramMap'][j] = int(i)
    elif d == 4:
        shift[b] = [a]
        shift = str(shift)
        shift = shift.replace('\'', '\"')
		
#将需要替换的值转换为list
    elif d == 5:
        shift[b] = list(a)
    elif d == 6:
        shift[b]=str(a).split('.',1)[0]
    elif d == 7:
        for i, j in zip(a, b):
            shift[j] = int(i)
            if 'ids' in j:
                shift[j] = [int(i)]
            else :
                shift[j] = int(i)
    
    return shift




def setlogging():
    '''打印日志公共方法'''
    t = str(datetime.datetime.now()).split(' ')[0]    # 创建一个logger

    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)
    handler = logging.FileHandler(os.path.dirname(pwd)+'/logs/' + t + ".log") # log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # 定义handler的输出格式
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    logger.addHandler(handler)  # 给logger添加handler
    logger.addHandler(console)

    return logger


#日志的公共方法
logger = setlogging()

# def request():

def clean_log(path):
    if os.path.exists(path) and os.path.isdir(path):
        before_yesterday = (datetime.date.today() + datetime.timedelta(-15)).strftime('%Y-%m-%d')
        print(before_yesterday)
        for file in os.listdir(path):
            if len(file) > 5:
                if file < before_yesterday:
                    abs_path = os.path.join(path, file)
                    print('删除的文件是%s,' % abs_path)
                    os.remove(abs_path)
                else:
                    print('没有删除的文件是%s' % file)
    else:
        print('路径不存在/不是目录')


# clean_log('C:/foxrenderfarmApi\logs')

def clean_result(path):
    if os.path.exists(path) and os.path.isdir(path):
        before_yesterday = (datetime.date.today() + datetime.timedelta(-15)).strftime('%Y-%m-%d')
        for file in os.listdir(path):
            file_date = file.split('_')[0]
            if len(file_date) > 5:

                if file_date < before_yesterday:
                    abs_path = os.path.join(path, file)
                    print('删除的文件是%s,' % abs_path)
                    os.remove(abs_path)
                else:
                    print('没有删除的文件是%s' % file)
    else:
        print('路径不存在/不是目录')

# def request_post(url,data,headers,data_type):
#     self.result = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head,verify=False).json()
#     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
#     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)