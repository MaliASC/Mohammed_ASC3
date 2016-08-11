var url = "http://maps.googleapis.com/maps/api/staticmap?center=75+9TH+AVE&zoom=19&scale=false&size=600x300&maptype=roadmap&format=png&visual_refresh=true&markers=size:mid%7Ccolor:0xff0000%7Clabel:1%7C75+9TH+AVE"
var markerStar ="&markers=icon:http://orig11.deviantart.net/9adf/f/2014/019/7/4/charizard_hgss_sprite_64x64_by_15crashbandicoot15-d72tiya.png" 

var charizard = [1000 75 9th AVE];                                                      

url = url+markert+encodeURI(charizard[0]);

var htmlIMG = document.createElement("img");
$("body").append(htmlIMG);
$"img"