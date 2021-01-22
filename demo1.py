#实现输入10个数字，并打印10个数的求和结果
# li = [1,2,3,5,6,8,10,11,12,16]
# s=0
# for i in range(0,10):
#     s = s + li[i]
# print("求和结果为：",s)


# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数

# shu=input("请输入10个数，用空格隔开:")
# list1=shu.split(' ')
# list2=[]
# for a in list1:
#     list2.append(int(a))
# max = list2[0]
# for i in list2:
#     if i > max:
#         max = i
# avg = 0
# for j in list2:
#     avg = avg + j
# p=0
# for b in list2:
#     p=avg/b
# print("最大值：",max,"和：",avg,"平均值：",p)

# 请编程统计列表中的每个数字出现的次数

# import collections
# a = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# b = collections.Counter(a)
# for c in b:
#        print(c,"出现的次数为：",b[c])

# 请编程实现列表的数据翻转
# alist = list(map(int, [1,2,3,4,5,6,7,8,9]))
# alist.reverse()
# print(alist)


# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
#	  ["刘备,"45","男",“alibaba”,“500”,“30"]
# ]
# sal=[500,501,600,700]
# sum = 0
# avg = 0
# avg = float(avg)
# for i in range(0,4):
#     sum = sum + sal[i]
#     avg = sum/4
# print("平均薪资为：",avg)

# age=[56,19,19,45]
# sum = 0
# avg = 0
# avg = float(avg)
# for i in range(0,4):
#     sum = sum + age[i]
#     avg = sum/4
# print("平均年龄为：",avg)

#男女人数



# 部门人数


#5的倍数的和

# a = [1,5,21,30,15,9,30,24]
# s1=0
# for i in a:
#     if i%5==0:
#         s1=s1+i
# print(s1)


# #求阶乘
# res=1
# for i in range(20,1,-1):
#     res=i*res+1
# print(res)


# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？

# def suml(l):
#     l=[]
#     s1=0
#     for i in l:
#         s1 = s1 + i
#     print(s1)
#
# l1=[23 ,35 ,44]
# l2=[60, 77 ,68 ,88, 90]
# l3= [97 ,99 ,89 ,91, 95, 90]
# l4=[100, 85 ,90]
# print("罗恩的成绩为：",sum(l1))
# print("哈利的成绩为：",sum(l2))
# print("赫敏的成绩为：",sum(l3))
# print("马尔福的成绩为：",sum(l4))
