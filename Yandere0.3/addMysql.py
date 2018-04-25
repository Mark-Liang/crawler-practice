import pymysql
import time
import datetime
#localtime=time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
#localtime=time.strftime('%Y-%m-%d %H:%M:%S')
def create_database():
	database()
	TABLE()



def database():
	try:
		db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/')
		cursor=db.cursor()
		db.cursor().execute('create database yandere')
		db.close()
	except :
		print('数据库已经存在')

def TABLE():
	try:
		db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere')
		db.cursor().execute("""CREATE TABLE img_message (
			`Id` int(11) NOT NULL AUTO_INCREMENT,
			`post` int(11) DEFAULT NULL,
			`tags` varchar(255) DEFAULT NULL,
			`paths` varchar(255) DEFAULT NULL,
			`in_png` tinyint(3) DEFAULT NULL,
			`png_path` varchar(255) DEFAULT NULL,
			`md5` varchar(255) DEFAULT NULL,
			`png_md5` varchar(255) DEFAULT NULL,
			`Create_time` datetime DEFAULT NULL COMMENT 'YYYY-MM-DD HH:MM:SS',
			`updata_time` datetime DEFAULT NULL,
			`Status` tinyint(3) DEFAULT NULL,
			PRIMARY KEY (`Id`)
			) ENGINE=InnoDB DEFAULT CHARSET=utf8;
			""")
		db.close()
	except:
		print('表已经存在')

def add_database(addpost,addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addCreate_time,addupdata_time,addStatus=1):
	db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere',charset='utf8')
	cursor=db.cursor()
	sql="INSERT INTO img_message(post,tags,paths,in_png,png_path,md5,png_md5,Create_time,updata_time,Status)\
	VALUES (%s,'%s','%s',%s,'%s','%s','%s','%s','%s',%s)" % \
	(addpost,addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addCreate_time,addupdata_time,addStatus)
	cursor.execute(sql)
	db.commit()
	db.close()


def updata_database(addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addupdata_time,addpost):
	db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere',charset='utf8')
	cursor=db.cursor()
	sql="update img_message set \
	tags='%s',paths='%s',in_png='%s',png_path='%s',md5='%s',png_md5='%s',updata_time='%s' \
	where (post='%s')"  %\
	(addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addupdata_time,addpost)
	cursor.execute(sql)
	db.commit()
	db.close()


def select_post(post):
	db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere',charset='utf8')
	cursor=db.cursor()
	sql="select post from img_message \
	where post='%s'" % (post)	
	cursor.execute(sql)
	try:
		results=cursor.fetchall()
		for (data,) in results:
			oldpost=data
			return oldpost
	except:
		db.close()
	#return oldpost

#print(select_post(383756))



#create_database()
#create_database()
#dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print (localtime)
#add_database(1,'2','1',1,'4','4','4',localtime,localtime,1)
#updata_database('3','4',1,'1','5','6',localtime,2)
#(post,path,in_png,png_path,md5,png_path,md5,png_md5,Create_time,updata_time,Status)

#db.cursor().execute('if not exists create_TABLE()')
#create_TABLE()
#print(cursor)
#localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#create_database()