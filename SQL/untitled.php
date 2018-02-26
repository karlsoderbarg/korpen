
<div class='w3-container w3-card w3-light-grey w3-margin-bottom w3-margin-left w3-margin-right'>
		<div class='w3-row-padding'>
			<div class='w3-container w3-medium w3-half'>
				<h5 class='w3-opacity'><i class='fa fa-location-arrow fa-fw w3-margin-right w3-large w3-text-black'></i><i class='w3-margin-right w3-text-teal'>Företagsnamn</i>".$row['name']."</h5>
				<h5 class='w3-opacity'><i class='fa fa-map-marker fa-fw w3-margin-right w3-large w3-text-black'></i><i class=' w3-margin-right w3-text-teal'>Rating</i>".$row['ratingSum']."</h5>
				<h5 class='w3-opacity'><i class='fa fa-calendar fa-fw w3-margin-right w3-large w3-text-black'></i><i class='w3-margin-right w3-text-teal'>Antal reviews</i>".$row['antalRatings']."</h5>
		
				<form class='w3-container w3-margin-bottom' name='rideDetails' action='rideDetails.php' method='POST'>
				<input type='hidden' name='rideid' value='".$row['email']."' />
				<div class='w3-center'>
				<button class='w3-button w3-small w3-white w3-border w3-border-teal w3-round-small' type='submit' value='s'>Details</button>
				</div>
				</form>
			</div>
			<div class='w3-half w3-container'>
				<h5 class='w3-opacity'><b class='w3-margin-right w3-margin-left w3-text-teal'>Minimum Price</b>".$minBid."<i class='fa fa-dollar fa-fw w3-margin-right w3-large w3-text-black'></i></h5>
				<div class='w3-container w3-margin-bottom'>
					<form class='w3-container w3-card' name='newBid' action='newBid.php' method='POST'>
					<input type='hidden' name='rideid' value=".$row['rideid'].">
					<input type='hidden' type='text' name='returnPage' value='ride.php'>
					<label class='w3-text-teal'>Make an offer</label>
					<input class='w3-input' type='number' name='bid' step=0.5 min='".$minBid."' />
					<div class='w3-right w3-margin-bottom'>
						<input class='w3-btn w3-teal' type='submit' value='New Bid'>
					</div>
					</form>
					
				</div>
			</div>
		</div>
		</div>