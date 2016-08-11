
function grabData(){
    //the $ assigns the value of 'title' element to movie 'name'
    var name = $('#title').val();
    $.ajax({
        url:'https://pokeapi.co///?t=' + name, //whatever is searched
        //if it returns something
        success: function(result){
            //print whatever movie title we have in json format
            print_result(result);
        }
    })
}

function print_result(obj){
	//Remove previous content displayed in web browser
	$('#content').text('');

	//iterate through objects stored in result and print to screen
	for(var i in obj){
		$('#content').append('<p>' + i + ': ' + obj[i] + '</p>')
	}
}

$('#submit').click(function(){
	grabData();
})