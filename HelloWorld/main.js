function helloWorld(){
    alert("Hello Mohammed how is your day?");
} 


var para = $('p');

para.click(updateName);
function updateName(){
	var name = prompt('Enter new name');

	para.text("And the new name is " + name);
}