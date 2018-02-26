<!DOCTYPE html>
<html lang="en">
<head>
  <title>Hantverk</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="error_msg.css">
  <link rel="stylesheet" href="w3.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="index.php">Hantverk</a>
    </div>
    <ul class="nav navbar-nav">
      <li><a href="hantverkarLista.php">Lokala Hantverkare</a></li>
      <li><a href="bids.php">My Bids</a></li>
      <li><a href="offerRide.php">Offer Rides</a></li>
      <li><a href="offeredRides.php">Offered Rides</a></li>
      <li><a href="profile.php">Edit Profile</a></li>
	  <li><a href="logout.php">Logout</a></li>
    </ul>
    <?php
      if(isset($_SESSION['is_admin'])){
    ?>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="admin.php">Admin</a></li>
    </ul>
    <?php
      }
    ?>
  </div>
</nav>
