//Setting reference
var database = firebase.database().ref();

//button's action
function sendMessage(){
  var name = $("#name").val();
  var message = $("#message").val();
  //send to your database
  database.push({
    'NAME':name,
    'MESSAGE':message
  });
}

//At the start, and whenever a new row is added, this API method grabs each row, or child, and does the function inside
database.on('child_added',function(dataRow){
	//getting raw values
  	var row = dataRow.val();
  	//adding to the div
    $("#messageBoard").append("<p>" + row.NAME + ": " + row.MESSAGE);
})
