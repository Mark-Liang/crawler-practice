<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>无标题文档</title>
	<style type="text/css">
<!--
.thumbnail span{position:relative;z-index:0;}
.thumbnail:hover{background-color:transparent;z-index:50;}
.thumbnail span{}
.thumbnail span img{border-width:0;padding:2px;position:absolute;background-color:#FFFFE0;left:-50px;border:1px dashed gray;visibility:hidden;color:#000;text-decoration:none;padding:5px;}
.thumbnail:hover img{visibility:visible;top:-20px;left:10px;}
p{margin-top:0px}
-->
		
		
		#left{width: 100%; float: left}
		#right{float: left}
		#foot{height: 100px;width: 100%;position: absolute;bottom: -50px;left: 0;}
		.th{
			width: 50px;
			white-space: nowrap;
		}
		.ta{
			width: 1300px;
			height: 20px;
			word-wrap: break-word;
			word-break: break-all;
		}
</style>
 
	

</head>
	
	<body>
		<?php
	
	$page=isset($_GET["page"])?$_GET["page"]:1;
    $tags=isset($_GET['tags'])?$_GET["tags"]:$tags;
	$tags=urlencode($tags);
	include "addsql.php";
	$pagesize=20;
	$sql="select count(*) from img_message where tags like '%{$tags}%'";
	$sqlcount=mysqli_query($con,$sql)or die("查询失败");
	$row=mysqli_fetch_array($sqlcount);
	#$pagecount=$pagecount['paths'];
	
	$MAXpage=$row[0]/40;
	mysqli_free_result($sqlcount);
	#$page=20;
	#$jpage=$_POST['page'];
	$MAXpage=ceil($MAXpage);
	#$sql="select thumbnail_path from img_message limit $pageshow,$pagesize"
	$prevpage=$page-1;
	if($page<=0){
		$prevpage=1;
		echo "<script>alert('页数不能小于1');history.back();</script>";
	}
	$nextpage=$page+1;
	if($page>$MAXpage){
		echo "<script>alert('超过最大值,又或者并没此关键字');history.back()</script>";
	}
	
	#$page=1;
	$pageshow=40;
	$pagesize=($page-1)*$pageshow;
	$sql1="select post,tags,thumbnail_path from img_message where tags like '%{$tags}%' order by post desc limit $pagesize,$pageshow";
	$sqlinfo=mysqli_query($con,$sql1);
	while($divide=mysqli_fetch_row($sqlinfo)){
		$path[]=$divide;
	}
	mysqli_free_result($sqlinfo);
	#print_r($path);

	#mysqli_free_result($divide);
	?>
		<div id="left" align="center">
			<form method="get" action="/selecttags.php">
				<a href="index.php">首页</a><br>
				按关键字搜索:<br>
<input type="text" name="tags" style="width: 400px"><br>
				<input type="submit" value="提交">
				</form>
		</div>

		<table border="1" align="center">
			<thead>
			<tr>
				<th class="th">缩略图</th>
				<th class="th">编号</th>
				<th class="ta">关键字</th>
			</tr>
		  </thead>
			<tr>
				
<?php for($row=0;$row<count($path);$row++){
	echo '<tr>';
	echo '<td><a class="thumbnail" href=/post.php?post='.$path[$row][0].'>缩略图<span><img src="'.(explode(":/",$path[$row][2])[1]).'" /></span></a></td>';
	echo '<td><a href=/post.php?post='.$path[$row][0].'>'.$path[$row][0].'</a></td><td>';
	$tagss=urldecode($path[$row][1]);
	$tagss=explode(" ",$tagss);
	foreach($tagss as $tag){echo "<a href='/selecttags.php?tags=".$tag."'style=text-decoration:none;>#".$tag."&nbsp&nbsp</a>";}"</td>";
	echo '</tr>';
}#<a href="#" onmouseover="displayImg()" onmouseout="vanishImg()" onmousemove="displayImg()" >缩略图</a><div id="image"><img src="'.(explode(":/",$path[$row][2])[1]).'" alt=""></div>

			?>
		</table>

<div align="center" style="height: 300px">
		<a href="?tags=<?php echo $tags?>&page=1">首页</a>
		<a href="?tags=<?php echo $tags?>&page=<?php echo $prevpage?>">上一页</a>
		<a href="?tags=<?php echo $tags?>&page=<?php echo $nextpage?>">下一页</a>
		<a href="?tags=<?php echo $tags?>&page=<?php echo $MAXpage?>">尾页</a>
	<a>...<?php echo $MAXpage?></a>
    </div>
		</body>

</html>