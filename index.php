<?php
  session_start();
  if(!isset($_SESSION['email'])){
    header("Location: login.php");
    exit;
  }
?>

<!DOCTYPE html>
<html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="w3.css">
<body>
	
<!-- Navigation -->
<?php require('header.php'); ?>

<!-- Slide Show -->
<section>
  <img class="mySlides" src="snickare.jpg"
  style="width:100%">
</section>

<!-- Band Description -->
<section class="w3-container w3-center w3-content" style="max-width:600px">
  <h2 class="w3-wide">HANTVERK</h2>
  <p class="w3-opacity"><i>Hitta lokala entreprenörer och hantverkare</i></p>
</section>

<script>
// Automatic Slideshow - change image every 3 seconds
var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("mySlides");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}
    x[myIndex-1].style.display = "block";
    setTimeout(carousel, 3000);
}
</script>

</body>
</html>
