<?php

$servername = "localhost";
$username = "application";
$password = "database2017";
$db="korpen";

$con = pg_connect("host=$servername port=5432 dbname=$db user=$username password=$password");
 if(!$con){
	 echo "ERROR";
 }
// echo "Connected successfully";
?>
