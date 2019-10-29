let map = L.map('mapid').setView([40, -8], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiY2F0YXJpbmFzaWx2YSIsImEiOiJjazF1dHAwNmgxMXhuM29udTAyMGU4c3dnIn0.xskWNOn6ZoSHGU6i7UGyEA', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'your.mapbox.access.token'
}).addTo(map);

//var current_position, current_accuracy;

function onLocationFound(e) {

	if (current_position) {
        map.removeLayer(current_position);
        map.removeLayer(current_accuracy);
    }

	console.log('on location...')

    //var radius = e.accuracy / 2;
    //current_position = L.marker(e.latlng).addTo(map); //.bindPopup("You are within " + radius + " meters from this point").openPopup();
    //current_accuracy = L.circle(e.latlng, radius).addTo(map);
}

function onLocationError(e) {
    alert(e.message);
}

//map.on('locationfound', onLocationFound);
//map.on('locationerror', onLocationError);

// wrap map.locate in a function
function locate() {
    map.locate({setView: true, maxZoom: 16});
}

locate();

// call locate every 3 seconds... forever
// setInterval(locate, 3000);