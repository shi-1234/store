# 导入pymysql
# import pymysql
# # 通过pymysql获取连接
# con = pymysql.connect(host="localhost",user="root",password="1234",database="company")
# # 获取游标
# cursor = con.cursor() # 获取一个游标
#
# # 准备一条sql语句
# sql = "insert into t_dept values('120','后勤部','天津'),('110','财务部门','甘肃')"
#
# # 执行sql语句
# num = cursor.execute(sql)
#
# print("影响了",num,"行数据")
# # 提交实际数据
# con.commit()  # 将缓存的数据真正的提交给数据库
#
# # 关闭资源
# cursor.close()
# con.close()
# import pymysql
#
# con = pymysql.connect(host="localhost",user="root",password="1234",database="company")
#
# cursor = con.cursor()
# # 数据库和sql模板分离方式来执行
# sql = "insert into t_dept values(%s,%s,%s)"
# param= ["160","财务部","北京"]
# num = cursor.execute(sql,param) # sql 模板， param是要填充的数据
# print("影响了",num,"行数据")
# con.commit()
# cursor.close()
# con.close()


# import pymysql
# con = pymysql.connect(host="localhost",user="root",password="1234",database="company")
# cursor = con.cursor()
# sql = "select * from t_employees where ename = %s" # account = %s
# param = ["张飞"] # [1345600]
# num = cursor.execute(sql,param)
# # 查询的数据依然在游标里,获取游标里的数据
# data = cursor.fetchall()
#
# print("影响了",num,"行数据")
# # print(data)
# for i in data:
#     print(i)
# con.commit()
#
# cursor.close()
# con.close()


# import pymysql
# con = pymysql.connect(host="localhost", user="root", password="1234", database="company")
# cursor = con.cursor()
# sql = "delete from t_dept where depton=%s"
# param= ["160"]
# num = cursor.execute(sql,param) # sql 模板， param是要填充的数据
# print("影响了",num,"行数据")
# con.commit()
# cursor.close()
# con.close()

# import pymysql
# con = pymysql.connect(host="localhost", user="root", password="1234", database="company")
# cursor = con.cursor()
# sql = "updata from t_dept set sal=sal+500 where ename=%s"
# param= ["关二爷"]
# num = cursor.execute(sql,param) # sql 模板， param是要填充的数据
# print("影响了",num,"行数据")
# con.commit()
# cursor.close()
# con.close()