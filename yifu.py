#记录第一件衣服品牌
name1 = "李宁"
price1 = 300
num1 = 20
unit1 = '件'


#记录第二件衣服的品牌
name2 = "乔丹"
price2 = 400
num2 = 20
unit2 = '件'

#记录第三件衣服的品牌
name3 = "尔克"
price3 = 500
num3 = 20
unit3 = '件'

#记录第四件衣服的品牌
name4 = "安踏"
price4 = 200
num4 = 20
unit4 = '件'

#记录第5件衣服的品牌
name5 = "耐克"
price5 = 800
num5 = 20
unit5 = '件'


print("-----------------欢迎光临A+服装店-------------------")
print("品牌            单价            数量            单位")
print("-------------------------------------------------")
print(name1,'          ',price1,'           ',num1,'           ',unit1,'         ')
print(name2,'          ',price2,'           ',num2,'           ',unit2,'         ')
print(name3,'          ',price3,'           ',num3,'           ',unit3,'         ')
print(name4,'          ',price4,'           ',num4,'           ',unit4,'         ')
print(name5,'          ',price5,'           ',num5,'           ',unit5,'         ')
print("-------------------------------------------------")
print('总金额为：',(price1*num1+price2*num2+price3*num3+price4*num4+price5*num5),"￥")