let map = L.map('mapid').setView([40, -8], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiY2F0YXJpbmFzaWx2YSIsImEiOiJjazF1dHAwNmgxMXhuM29udTAyMGU4c3dnIn0.xskWNOn6ZoSHGU6i7UGyEA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoibWFyaW9scGFudHVuZXMiLCJhIjoiY2syYzhkcjdpMHpxbzNibWpjN3F2aDU3dyJ9.FklIUy73dB7yzL7NSYLvWA'
}).addTo(map);

if (navigator.geolocation) {
	navigator.geolocation.getCurrentPosition(function (position) {
		lat = position.coords.latitude;
		lng = position.coords.longitude;
		var newLatLng = new L.LatLng(lat, lng);
		map.panTo(newLatLng);
	});
}