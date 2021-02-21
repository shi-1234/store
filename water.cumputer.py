'''
高度，容积，颜色，材质
能存放液体
'''

class Glass:
    __h = ""
    __v = ""
    __color = ""
    __textrue = ""

    def setH(self,h):
        if h >12 or h < 0:
            print("您的输入存在异常！")
        else:
            self.__h = h
    def getH(self):
        return self.__h

    def setV(self,v):
        if v > 12 or v < 0:
            print("容积不能超过高度！")
        else:
            self.__v = v
    def getV(self):
        return self.__v

    def color(self,name):
        print(name,"的杯子在桌子上，里面有",self.__v,"ml水")

    def textrue(self,name):
        print(name,"材质的杯子在桌子上,它的高度为",self.__h,"cm")

a = Glass()

a.setV(10)
a.setH(12)
a.color("蓝色")
a.textrue("玻璃")


'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''

class Computer:
    __size = ""
    __price = ""
    __cpu = ""
    __memory = ""
    __time = ""

    def __init__(self,size,price,cpu,memory,time):
        self.__size = size
        self.__price = price
        self.__cpu = cpu
        self.__memory = memory
        self.__time = time

    def playGames(self,name):
        print("您的CPU为：",self.__cpu,"您的内存大小为：",self.__memory,"您可以玩",name)
    def watchingTV(self):
        print("您的内存为：",self.__memory,"您正在看电视！")
    def typing(self):
        print("CPU为：",self.__cpu,"您的内存大小为：",self.__memory,"正在打字！")



a = Computer(15.6,5000,"64G","500G","24h")
a.playGames("绝地求生")
a.watchingTV()
a.typing()