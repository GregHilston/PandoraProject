$tracks = $('div#track_like_pages div.section');

for (var i = 0; i < $tracks.length; i++) {
	var t = $tracks.eq(i);
	var title = $.trim($('h3.normal', t).text());
	var artist = $.trim($('div.infobox-body p.s-0 a', t).eq(0).text());
	console.log(title + ' - ' + artist);
}
