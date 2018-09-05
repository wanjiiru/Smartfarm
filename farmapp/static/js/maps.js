        var venues;
        var mymap;
        var venues;
        var events;''
        var ctrRouting;
        var mypoint;

        $(document).ready(function(){
             mymap = L.map('mapid').setView([-1.3, 36.78], 5);
                 L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            {
              attribution: 'Tiles by openstreetmap'
                }).addTo(mymap);

            venues = L.geoJSON.ajax('http://127.0.0.1:8000/venues', {onEachFeature: function (feature, layer) {

                  layer.bindPopup('<h1>'+feature.properties.name+'</h1>')
                }
            }
            ).addTo(mymap);

             events = L.geoJSON.ajax('http://127.0.0.1:8000/events', {onEachFeature: function (feature, layer) {

                  layer.bindPopup('<h1>'+feature.properties.name+'</h1>')
                }
            }
            ).addTo(mymap);





           mymap.locate();
           mymap.on('locationfound', function(e){
               console.log(e.latlng)
               ctrRouting = L.Routing.control({
                  waypoints: [
                    L.latLng(e.latlng.lat,e.latlng.lng),
                    L.latLng(-1.34,36.8)
                  ],
                 router: L.Routing.mapbox('pk.eyJ1IjoiZGVyeSIsImEiOiJjaWY5anJyN3YwMDI5dGNseHoyZzM4Z3R4In0.dToOXYIZ30LH_7VtFbKW4A')
                }).addTo(mymap);

           })
            mymap.on('locationerror', function(e){
                alert('turn on your location!')
           })
            });
