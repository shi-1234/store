i = 9

while i <=9 :
    j = 1
    while j >= i:
        print(i,"x",j,"=",(j*i),"   ",end="")
        j = j + 1
    print()
    i = i -1





import random
import time

num = random.randint(50,150)
counter = 0

while True:
    if counter >= 3:
        print("您3次没有猜中，系统锁定5秒钟")
        f = 1
        while f <= 5:
            print(".",end="")
            time.sleep(1)
            f = f+1
    counter = counter+1
    n = input("请输入您要猜的数字：")
    n = int(n)
    if n > num:
        print("大了，请继续努力！")
    elif n < num:
        print("小了，请继续努力！")
    else:
        print("恭喜您，猜对了，您本次猜了：",counter,"次！")
        break





i=1
while i<=7:
    j = 1

    while j <= 7-i:
        print('  ', end='')
        j += 1
    k = 1
    while k <= i:
        print(' *  ',end='')
        k += 1
    print()

    i+=1



a = input("请输入a：")
b = input("请输入b：")
c = input("请输入c：")
a = int(a)
b = int(b)
c = int(c)

if a+b>c and b+c>a and a+c>b:
    if a==b and a!=c or b==c and b!=a or a==c and a!=b:
        print("构成等腰三角形")
    elif a==b==c:
        print ("构成等边三角形")
    else:
        print("构成普通三角形")
else:
    print ("不构成三角形")




username="石明亮"
userpassword="147258369"
count=0
name = input("登录用户名：")
if name == username:
    # 如果密码连续输错了三次，锁定账号
    while count < 3:
        password = input("登录密码：")
        if name == username and password == userpassword:
            print("欢迎%s!" % name)
            break
        else:
            print("账号和密码不匹配")
            count += 1
    else:
        print("对不起，您的账号连续输错三次密码已被锁定，请联系管理员。")
        f = open("aaa.txt")
        f.close()
else:
    print("用户名不存在，请输入正确的用户名。")



a = 56
b = 78

a = a + b
b = a - b
a = a - b

print(a)
print(b)


h = 20
s = 0
day = 0

while True:
    day = day + 1
    s = s + 3
    if s>=h:
        break
    else:
        s = s - 2
print("需要:",day,"天！")