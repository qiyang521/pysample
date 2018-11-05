d=[
{'Mobile_phone':'小米手机','phone_models':'MIX3',
           'phone_price':3599,'phone_numbers':100,
           'phone_version':'128g'},
{'Mobile_phone':'华为手机','phone_models':'华为P20',
           'phone_price':3999,'phone_numbers':100,
           'phone_version':'128g'},
{'Mobile_phone':'苹果手机','phone_models':'Aphone10',
           'phone_price':12800,'phone_numbers':100,
           'phone_version':'128g'}

]
# 管理员
def admin():
    print('欢迎来到手机管理系统!')
    user=input('请输入管理员账号:')
    passwd=input('请输入密码:')
    if user=='qqy' and passwd=='123':
        print('登陆成功')
    else:
        print('登录失败!!!')
        exit()
# 菜单栏
menu=('''
********************************
*  1.手机录入                  *
*  2.根据手机品牌查询手机信息   *
*  3.查询全部手机信息           *          
*  4.根据手机编号修改手机价格   *
*  5.根据手机编号删除手机记录   * 
*  6.退出                      *
********************************
''')
# 添加一个手机信息
def add():
    Mobile_phone=input('请输入手机品牌:')
    phone_models=input('请输入手机型号:')
    phone_price=input('请输入手机价格:')
    phone_numbers=input('请输入手机数量:')
    phone_version=input('请输入手机版本:')
    phone={'Mobile_phone':Mobile_phone,'phone_models':phone_models,
           'phone_price':phone_price,'phone_numbers':phone_numbers,
           'phone_version':phone_version}
    d.append(phone)
    print('添加成功!')
# 查询所有手机数据
def check_all_phone():
    print('序号\t\t\t品牌\t\t\t型号\t\t\t价格\t\t\t数量\t\t\t版本')
    for i,phone in enumerate(d):
        print('{0}\t\t\t{1}\t\t\t{2}\t\t\t{3}\t\t\t{4}\t\t\t{5}'
              .format(i+1,phone['Mobile_phone'],phone['phone_models'],phone['phone_price'],
                      phone['phone_numbers'],phone['phone_version']))
# 查询单条手机数据
def check_one_phone():
    hehe = input('请输入手机品牌:')
    for phone in d:
        if hehe in phone['Mobile_phone']:
                print(phone)
# 查询价格
def change_phone_price():
    Mobile_phone = input('请输入手机品牌:')
    for phone in d:
        if Mobile_phone in phone['Mobile_phone']:
            phone['phone_price']=input('请输入新的价格:')
            phone_price=phone['phone_price']
            print('修改成功!!!')
# 删除单条手机记录
def phone_deptno():
    number=int(input('请输入您要删除的编号:'))
    d.pop(number-1)
    for i,phone in enumerate(d):
        print('{0}\t\t\t{1}\t\t\t{2}\t\t\t{3}\t\t\t{4}\t\t\t{5}'
              .format(i+1,phone['Mobile_phone'],phone['phone_models'],phone['phone_price'],
                      phone['phone_numbers'],phone['phone_version']))
    print('删除成功!')
# 测试部分
if __name__=='__main__':
    admin()
    while True:
        c=input(menu)
        if c=='1':
            add()
        elif c=='2':
            check_one_phone()
        elif c=='3':
            check_all_phone()
        elif c=='4':
            change_phone_price()
        elif c=='5':
            phone_deptno()
        elif c=='6':
            exit()



