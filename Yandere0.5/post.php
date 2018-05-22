<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>无标题文档</title>
	<style type="text/css">
		#left{width: 300px; float: left}
		#right{width: 300px; float: left}
		#foot{height: 100px;width: 100%;position: absolute;bottom: -250px;left: 0;}
		#hh{
			word-wrap: break-word;
			word-break: break-all;
			width: 300px; float: left;
		}
			</style>
</head>
<?php
	include "addsql.php";
	$post=isset($_GET["post"])?$_GET["post"]:1;
	$sql="select * from img_message where post='$post'";
	$sqlcount=mysqli_query($con,$sql)or die("查询失败");
	$row=mysqli_fetch_array($sqlcount);
	$tags=urldecode($row[2]);
	$tags=explode(" ",$tags);
	mysqli_free_result($sqlcount);
	#print_r($tags);
	?>
<body>
	<div id="hh">
			<form method="get" action="/selecttags.php">
				<a href="index.php">首页</a><br>
				按关键字搜索:<br>
<input type="text" name="tags" style="width: 150px"><br>
				<input type="submit" value="提交"><br>
				<a>数据库ID:<?php echo $row[0]?></a><br>
				<a>图片编号:<?php echo $row[1]?></a><br>
				<a>关键字:<br><?php foreach($tags as $tag){echo "<a href=/selecttags.php?tags=".$tag.">#".$tag."</a><br>";}?></a><br>
				<?php echo "<a href=".explode(":/",$row[3])[1].">JPG</a>"?><br>
				<a>JPGwidth:<?php echo $row[8]?></a><br>
				<a>JPGheiht:<?php echo $row[9]?></a><br>
				<?php if($row[4]==1){
	echo "<a href=".explode(":/",$row[5])[1].">PNG</a><br><a>PNGwidth:".$row[10]."</a><br>
				<a>PNGheiht:".$row[11]."</a><br>";
}
				else{ echo '<a>这图没有PNG</a>';}?><br>
				
				
				<a>记录创建时间:<?php echo $row[13]?></a><br>
				<a>最后更新时间:<?php echo $row[14]?></a><br>
				<a>图片状态:<?php echo $row[15]?></a><br>
				</form>
		</div>
	<div id=right>
		<img src="<?php echo explode(":/",$row[3])[1];?>" width="700";height="700";>
	</div>
</body>
</html>