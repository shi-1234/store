import random
import time

num = random.randint(1,100)
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
