<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>连接数据库</title>
</head>

<body>
<?php
	$servername="127.0.0.1:8888";
	$username="root";
	$password="abc123*+/";
	$db="yandere";
	$con=new MySQLi($servername,$username,$password,$db);
	if(!$con){
		die("连接失败".mysql_connect_error());
	}
	?>
	
</body>
</html>