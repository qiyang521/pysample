# 编写装饰器，为函数加上统计时间的功能
import time
def wrap(f):
    def wrapper(*args,**kwargs):
        startTime=time.time()
        print('********'*2)
        f(*args,**kwargs)
        print('********'*2)
        endTime=time.time()
        time_difference=endTime-startTime
        print('函数运行时间是:%d s'%time_difference)
    return wrapper
@wrap
def f(a,b,c):
    time.sleep(3)
    print('三个数的和是:%d'%(a+b+c))
f(10,10,10)
# 编写装饰器，为函数加上认证的功能
def user_confirm(f):
    def wapper(*args,**kwargs):
        username=input('请输入用户名:').strip()
        password=input('请输入密码:').strip()
        if username=='qqy' and password=='123456':
            res=f(*args,**kwargs)
            return res
        else:
            print('用户名密码不匹配,登录失败!')
    return wapper
@user_confirm
def f(username,password):
    print('登陆成功')
f('qqy','123456')
# 定义一个名为Vehicles 交通工具 的基类 该类中应包含str类型
# 的成员属性brand 商标 和 color 颜色 还应包含对象方法run 行驶
# 在控制台显示“我已经开动了” 和show_info 显示信息 在控制
# 台显示商标和颜色 并编写构造方法初始化其成员属性。 编写Car
# 小汽车 类继承于Vehicles类 增加int型成员属性seats 座位
# 还应增加成员方法show_car 在控制台显示小汽车的信息 并编写
# 构造方法。 编写Truck 卡车 类继承于Vehicles类 增加float型
# 成员属性load 载重 还应增加成员方法show_truck 在控制台显示
# 卡车的信息 并编写构造方法
class Vehicles:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def run(self):
        pass
    def show_info(self):
        pass
class Car(Vehicles):
    def __init__(self, brand, color, seat):
        super().__init__(brand, color)
        self.seat = seat
    def show_car(self):
        pass

class Truck(Vehicles):
    def __init__(self, brand, color, load):
        super().__init__(brand, color)
        self.load = load

def show_truck():
    pass