'''
    print()  打印的方法，可以将你想要打印的数据写到print方法里
'''

# "记录了第一个水果详细信息"
name1 = "砂糖橘子"
price1 = 6
quanlity1 = 'A+'
num1 = 25
unit1 = '个'

# 记录了第二个水果详细信息
name2 = "苹果   "
price2 = 3
quanlity2 = 'C+'
num2 = 10
unit2 = '个'

#记录了第三个水果详细信息
name3 = "香蕉   "
price3 = 3
quanlity3 = 'B+'
num3 = 15
unit3 = "斤"

#记录了第四个水果的详细信息
name4 = "葡萄   "
price4 = 10
quanlity4 = "A+"
num4 = 5
unit4 = "斤"

#记录了第5个水果详细信
name5 = "西瓜   "
price5 = 3
quanlity5 = 'A++'
num5 = 3
unit5 = "斤" 





print('-----------------欢迎来到水果商城--------------------')
print('水果名称      价格     品质    数量    单位')
print('----------------------------------------------------')
print(name1,"    ",price1,"    ",quanlity1,"    ",num1,"    ",unit1)
print(name2,"    ",price2,"    ",quanlity2,"    ",num2,"    ",unit2)
print(name3,"    ",price3,"    ",quanlity3,"    ",num3,"    ",unit3)
print(name4,"    ",price4,"    ",quanlity4,"    ",num4,"    ",unit4)
print(name5,"    ",price5,"    ",quanlity5,"    ",num5,"    ",unit5)
print('----------------------------------------------------')
print('总金额为：',(price1*num1+price2*num2+price3*num3+price4*num4+price5*num5),'￥')
