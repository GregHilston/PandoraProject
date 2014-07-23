number_of_thumbed_up_songs = 713;
max = Math.ceil(number_of_thumbed_up_songs / 5); // Pandora shows thumbed up songs in units of 5 songs per click of "show more"
counter = 0;

console.log("Total Iterations: " + max);

var showMore = function(){
	$('.backstage .show_more').trigger('click');
	
	console.log("Iterations Complete: " + counter + " / " + max);
	counter++;
	
	if(counter < max) {
		setTimeout(showMore, 1500); // Check again
	}
	else {
		console.log("Grabbing Tracks!");
		$tracks = $('div#track_like_pages div.section');

		for (var i = 0; i < $tracks.length; i++) {
			var t = $tracks.eq(i);
			var title = $.trim($('h3.normal', t).text());
			var artist = $.trim($('div.infobox-body p.s-0 a', t).eq(0).text());
			console.log(title + ' - ' + artist);
		 }
		 
		 $("html, body").animate({ scrollTop: $(document).height() }, "fast");
		 alert(number_of_thumbed_up_songs + " tracks recorded");
		 
	}
}

showMore()
