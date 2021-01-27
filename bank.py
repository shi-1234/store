import random
# 银行的名称
bank_name = "北京市工商银行昌平支行"

# 银行的库
users = {}
'''
{"张三":
    {account:"12345",
    "国家":"中国"}
}

'''

# 欢迎界面
welcome  = '''
*********************************
*    欢迎来到中国工商银行管理系统 *
*********************************
*    1.开户                      *
*    2.存钱                      *
*    3.取钱                      *
*    4.转账                      *
*    5.查询                      *
*    6.bye！                     *
*********************************
'''
# 专门来获取8位随机账号
def getRandom():
    li = [1,2,3,4,5,6,7,8,9,0]
    # 循环8次
    string = ""
    for i in range(8): # 循环8次获取随机字符
        ch = li[random.randint(0,9)]
        string = string + str(ch)
    return string

# 银行的核心开户方法
def bank_addUser(account,username,password,money,country,province,street,door):
    # 先判断银行库是否已满 ： 100个最大
    if len(users) >= 100:
        return 3
    # 判断是否已经存在
    elif username in users: # 这种方式只判断是否在字典的键里存在
        return 2
    # 可以正常开户：将个人数据存到用户库里
    else:
        users[username] = {
            "account":account,
            "password":password,
            "money":money,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "bank_name":bank_name
        }
        return 1





# 普通的开户方法
def addUser():
    # 完成具体的开户输入
    # 姓名(str)、密码(int:6位数字)、地址、存款余额(int)、国家(str)、省份(str)、街道(str)、门牌号(str)
    username = input("请输入姓名：")
    password = input("请输入初始取款密码：")
    money =  int(input("请输入您的初始金额：")) # 金额是整数形式
    print("接下来输入地址信息：")
    country =  input("请输入您所在国家：")
    province = input("亲输入您所在省份：")
    street = input("请输入您所在的街道：")
    door = input("请输入您地址的门牌号：")
    account =  getRandom() # 获取随机账号

    # 将数据传给银行
    status = bank_addUser(account,username,password,money,country,province,street,door)
    if status == 3:
        print("对不起，银行用户已满！请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，您的个人信息已存在！请勿重复开户！")
    elif status == 1:
        print("恭喜，开户成功！以下是您的个人开户信息：")
        print("-------------------------------------")
        print("您的账号为:",users[username]["account"])
        print("您的密码为:", users[username]["password"])
        print("您的余额为:", users[username]["money"])
        print("您的用户名为:", username)
        print("您所在国家为:", users[username]["country"])
        print("您所在省份为:", users[username]["province"])
        print("您所在街道为:", users[username]["street"])
        print("您所在门牌号为:", users[username]["door"])
        print("开户行名为:", users[username]["bank_name"])


def save(account,password):
    while True:
        for account in users:
            if password in users[account]["password"]:
                return account
            else:
                print("请输入正确的密码！")
                break
        else:
            print("请输入正确的账号！")
            break


def bank_moneyIn(moneyIn_num,username):
    if username in users:
        return True
    else:
        return False

# 存钱   李文秀
def bank_moneyIn(moneyIn_num,username):
    if username in users:
        return True
    else:
        return False

def moneyIn():
    username=input("请输入您的用户名")
    moneyIn_num=int(input("请输入您要存入的金额"))

    status1 = bank_moneyIn(moneyIn_num,username)
    if status1==True:
        print("您的账号",users[username]["account"],"用户名",username)
        print("存款", moneyIn_num, "元成功,""您现在的余额为",users[username]["money"]+moneyIn_num)

    elif status1==False:
        print("对不起，您的账户不存在,请重新输入")
        return moneyIn()

#取钱  石明亮
def getout():
    account = input("请输入账号：")
    password = input("请输入密码：")
    account = save(account,password)
    while True:
        outmoney = int(input("请输入取款金额："))
        state = bankgetout(account,outmoney)
        if outmoney > 0 :
            if state == 1:
                print("取款成功，当前余额为：",users[account]["money"])
                break
            elif state == 2:
                print("余额不足！")
        else :
            print("请输入正确金额！")
#银行取钱
def bankgetout(account,outmoney):
    if users[account]["money"] > outmoney:
        users[account]["money"] =  int(users[account]["money"]) - outmoney
        return 1
    elif users[account]["money"] < outmoney:
        return 2

def bank_moneyChange(username1,username2,password,moneyChange_num):
    if username1 in users:
        if username2 in users:
            if password==users[username1]["password"]:
                if moneyChange_num<=users[username1]["money"]:
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    else:
        return 1




def moneyChange():
    username1=input("请输入转出账户用户名")
    username2=input("请输入转入账户用户名")
    password=int(input("请输入转出账户的密码"))
    moneyChange_num=int(input("请输入转出的金额"))

    status3=bank_moneyChange(username1,username2,password,moneyChange_num)
    if status3==0:
        print("转出",moneyChange_num,"元成功")
        print("您的转出账户",username1,"",users[username1]["account"],"余额为",users[username1]["money"]-moneyChange_num)
        print("您的转入账户", username2, "", users[username2]["account"], "余额为", users[username2]["money"]+moneyChange_num)
    elif status3==1:
        print("您的账户不存在")
    elif status3==2:
        print("您的密码不正确,请重新输入")
        return moneyChange()
    elif status3==3:
        print("您的余额不足")

#查询   付光旭
def bank_query(username,password):
    if username in users:
        if password==users[username]["password"]:
            print("您的账户",username,users[username]["account"],"余额为",users[username]["money"])
        else:
            print ("您输入的密码不正确，请重新输入")
            return query()
    else:
        print("您的账户不存在")

def query():
    username=input("请输入用户名")
    password=int(input("请输入密码"))

    status4=bank_query(username,password)


while True:
    print(welcome) # 打印欢迎信息
    chose = input("请输入您的业务编号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        moneyIn()
    elif chose == "3":
        getout()
    elif chose == "4":
        moneyChange()
    elif chose == "5":
        query()
    elif chose  == "6":
        print("退出成功！欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入！")