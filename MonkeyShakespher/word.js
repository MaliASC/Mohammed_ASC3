// TO DO LIST
// if tar Phrase == Random Phrase: End
// 	Else: pick new rand Phrase

// Globals Var
var tarPhrase = "To be or Not to Be";
var alphabet = "abcdefghijklmnopqrstuvwxyz `1234567890=~!@#$%^&*()_+]{};,./<>?";

var letters =[];
for(var i=0;i<alphabet.length;i++){
	letters.push(alphabet[i]);
}

function randLetter(){
	if (random()<.5){
		return random(letters);
	}else{
		return random(letters).toUpperCase();
	}
}

function randPhrase(){
	var blank="";
	for(var v =0; v<tarPhrase.length;v++){
		blank = blank.concat(randLetter());
	}
	return blank;
}
var badPhrase, loopNum;

function setup(){
	createCanvas(800,800);
	badPhrase =randPhrase();
	loopNum=0;
}

function julian(){
	var blank="";
	for (var j = 0; j<tarPhrase.length;j++){
		if(badPhrase[j]==tarPhrase[j]){
			blank = blank.concat(tarPhrase[j]);
		}else{
			blank = blank.concat(randLetter());
		}
	}
	return blank;
}

function draw(){
	background(0);
	loopNum++;
	fill(225);
	textAlign(CENTER,CENTER);
	textSize(40);
	text(tarPhrase, width/2,100);
	text(badPhrase, width/2,200);
	text("LoopNum: " + loopNum, width/2, 300);

	if(badPhrase==tarPhrase){
		text("DONE!", width/2, 500);
		noLoop();
	}else{
		// badPhrase =randPhrase();
		badPhrase=julian();
	}
}