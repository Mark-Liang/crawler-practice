import pymysql
import Function


def create_database():
    database()
    TABLE()




def database():
    try:
        db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/')
        cursor=db.cursor()
        db.cursor().execute('create database yandere')

    except :
        print('数据库已经存在')
    db.close()
def TABLE():
    try:
        db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere')
        db.cursor().execute("""CREATE TABLE `img_message` (
            `Id` int(11) NOT NULL AUTO_INCREMENT,
            `post` int(11) DEFAULT NULL,
            `tags` text,
            `paths` varchar(255) DEFAULT NULL,
            `in_png` tinyint(3) DEFAULT NULL,
            `png_path` varchar(255) DEFAULT NULL,
            `md5` varchar(255) DEFAULT NULL,
            `png_md5` varchar(255) DEFAULT NULL,
            `width` int(11) DEFAULT NULL,
            `height` int(11) DEFAULT NULL,
            `png_width` int(11) DEFAULT NULL,
            `png_height` int(11) DEFAULT NULL,
            `thumbnail_path` varchar(255) DEFAULT NULL,
            `Create_time` datetime DEFAULT NULL COMMENT 'YYYY-MM-DD HH:MM:SS',
            `updata_time` datetime DEFAULT NULL,
            `Status` tinyint(3) DEFAULT NULL,
            PRIMARY KEY (`Id`)
            )
            ENGINE=InnoDB AUTO_INCREMENT=69517 DEFAULT CHARSET=utf8;
            """)
    except:
        print('表已经存在')
    db.close()


def add_database(addpost,addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addwidth,addheight,addpng_width,addpng_height,addthumbnail,addCreate_time,addupdata_time,addStatus=1):
    db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere',charset='utf8')
    cursor=db.cursor()
    sql="INSERT INTO img_message(post,tags,paths,in_png,png_path,md5,png_md5,width,height,png_width,png_height,thumbnail_path,Create_time,updata_time,Status)\
    VALUES (%s,'%s','%s',%s,'%s','%s','%s',%s,%s,%s,%s,'%s','%s','%s',%s)" % \
    (addpost,addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addwidth,addheight,addpng_width,addpng_height,addthumbnail,addCreate_time,addupdata_time,addStatus)
    cursor.execute(sql)
    db.commit()
    db.close()



def updata_database(addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addwidth,addheight,addpng_width,addpng_height,addthumbnail,addupdata_time,addpost):
    db=pymysql.connect(host='127.0.0.1',port=8888,user='root',passwd='abc123*+/',db='yandere',charset='utf8')
    cursor=db.cursor()
    sql="update img_message set \
    tags='%s',paths='%s',in_png='%s',png_path='%s',md5='%s',png_md5='%s',width=%s,height=%s,png_width=%s,png_height=%s,thumbnail_path='%s',updata_time='%s' \
    where (post='%s')"  %\
    (addtags,addpaths,addin_png,addpng_path,addmd5,addpng_md5,addwidth,addheight,addpng_width,addpng_height,addthumbnail,addupdata_time,addpost)
    cursor.execute(sql)
    db.commit()
    db.close()