"use strict";

var input_lat = $("#input-lat"), 
  input_lng = $("#input-lng"), 
  map = new GMaps({ 
    div: '#map',
    lat: -6.5637928,
    lng: 106.7535061
  });


var marker = map.addMarker({
  lat: -6.5637928,
  lng: 106.7535061,
  draggable: true,
});


map.addListener("click", function(e) {
  var lat = e.latLng.lat(), 
    lng = e.latLng.lng();

  
  marker.setPosition({
    lat: lat,
    lng: lng
  });
  update_position();       
});


marker.addListener('drag', function(e) {
  update_position();
});


update_position();
function update_position() {
  var lat = marker.getPosition().lat(), lng = marker.getPosition().lng();
  input_lat.val(lat);
  input_lng.val(lng);
}


$("#input-lat,#input-lng").blur(function() {
  var lat = parseInt(input_lat.val()), 
    lng = parseInt(input_lng.val());

  marker.setPosition({
    lat: lat,
    lng: lng
  });
  map.setCenter({
    lat: lat,
    lng: lng
  });
});
