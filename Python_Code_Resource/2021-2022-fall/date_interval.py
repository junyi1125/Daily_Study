import datetime
from time import sleep
d1 = datetime.datetime(int(input('请输入年')),int(input('请输入月')),int(input('请输入日')))
d2 = datetime.datetime(int(input('请输入年')),int(input('请输入月')),int(input('请输入日')))
interval = d2 - d1
print('间隔了%d天' %(interval.days))
sleep(5)