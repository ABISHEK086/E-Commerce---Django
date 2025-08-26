"use strict";


var map = new GMaps({
  div: '#map',
  lat: -6.5637928,
  lng: 106.7535061
});

GMaps.geolocate({
  
  success: function(position) {
    
    map.setCenter(position.coords.latitude, position.coords.longitude);
    
    map.addMarker({
      lat: position.coords.latitude,
      lng: position.coords.longitude,
      title: 'You'
    });
  },
  
  error: function(error) {
    toastr.error('Geolocation failed: '+error.message);
  },
  
  not_supported: function() {
    toastr.error("Your browser does not support geolocation");
  }
});
