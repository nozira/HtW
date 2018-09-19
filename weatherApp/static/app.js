var map;
var control;
window.onload = function() {
    map = new Y.Map("map");
    map.drawMap(new Y.LatLng(35.680840,139.767009), 5, Y.LayerSetId.NORMAL);

    control = new Y.ZoomControl();
    map.addControl(control);

    //クリックイベントを設定
    map.bind("click", function(latlng){onClicked(latlng);});
    
}
//クリックイベントを定義
function onClicked(latlng){
    document.getElementById("lat").value = latlng.lat();
    document.getElementById("lng").value = latlng.lng();
    var lat = latlng.lat();
    var lng = latlng.lng();
    window.location.href = "http://localhost:5000/weather?lat="+lat+"&lng="+lng;
}