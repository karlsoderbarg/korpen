<?php 
	if(!empty($_POST)){
		session_start();
		require("db_connect.php");
		$query = "SELECT * FROM hantverkare WHERE email = '".$_POST["email"]."'";
		$result = pg_query($con, $query);
		$row    = pg_fetch_assoc($result);
		if(!empty($row)){
			$pass = $_POST["password"];
			$pass = hash('sha256',$pass);
			if(strcmp($pass,$row["password"])==0){
			  $_SESSION['email'] = $row['email'];
			  require("db_close.php");
			  if(strcmp($row["is_admin"],"t") == 0){
			  	  $_SESSION["is_admin"] = TRUE;
			  	  require("db_close.php");        
				  header("Location: admin.php");
				  exit;
			  }
			  else{
			    require("db_close.php");        
			    header("Location: index.php");
			    exit;
			  }
			}
		}
		$incorrect = true;
		require("db_close.php");
	}
	else{
		$incorrect = false;
	}
	require("loginpage.php");
?>