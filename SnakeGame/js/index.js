var BOARD = [];
var ROWS, COLS;
var SQAURE_SIZE = 30;

var UP = 4;
var RIGHT = 1;
var DOWN = 2;
var LEFT = 3;

var PLAYER_X, PLAYER_Y;

var EMPTY = 0, SNAKE_HEAD = 1, SNAKE_BODY = 2, FOOD = 3;

var DIR;

// 0 is nothing, 1 is snake head, 2 is snake body, 3 is food

function start() {
    COLS = 44;
    ROWS = 21;
    DIR = RIGHT;
    for(var i = 0; i < ROWS; i++){
        var arr = [];
        for(var j = 0; j < COLS; j++){
            arr.push(EMPTY);
        }
        BOARD.push(arr);
    }
    PLAYER_Y = Math.floor(ROWS/2);
    PLAYER_X = Math.floor(COLS/2);
    BOARD[PLAYER_Y][PLAYER_X] = SNAKE_HEAD;

    stroke(0, 255, 0);
}

function drawBoard() {
    for(var y = 0; y < ROWS; y++){
        for(var x = 0; x < COLS; x++){
            if(BOARD[y][x] == EMPTY){
                fill(255);
            }else if(BOARD[y][x] == SNAKE_HEAD){
                fill(0, 0, 255);
            }

            rect(x * SQAURE_SIZE, y*SQAURE_SIZE, SQAURE_SIZE, SQAURE_SIZE);
        }
    }
}

function setup() {
    frameRate(10);
    start();
    createCanvas(COLS * SQAURE_SIZE+1, ROWS * SQAURE_SIZE+1);
    background(119, 120, 120);
}

function draw() {
    drawBoard();
    // player direction
    if ((key == 'd' || key == 'D') && DIR != LEFT){
        DIR = RIGHT;
    }else if((key == 'a' || key == 'A') && DIR != RIGHT){
        DIR = LEFT;
    }else if((key == 'w' || key == 'W') && DIR != DOWN){
        DIR = UP;
    }else if((key == 's' || key == 'S') && DIR != UP){
        DIR = DOWN;
    }
    // player movement
    if(DIR == RIGHT){
        BOARD[PLAYER_Y][PLAYER_X++] = EMPTY;
        BOARD[PLAYER_Y][PLAYER_X] = SNAKE_HEAD;
    }

 
     if(DIR == LEFT){
        BOARD[PLAYER_Y][PLAYER_X--] = EMPTY;
        BOARD[PLAYER_Y][PLAYER_X] = SNAKE_HEAD;
    }
     if(DIR == UP){
        BOARD[PLAYER_Y--][PLAYER_X] = EMPTY;
        BOARD[PLAYER_Y][PLAYER_X] = SNAKE_HEAD;
    }
     if(DIR == DOWN){
        BOARD[PLAYER_Y++][PLAYER_X] = EMPTY;
        BOARD[PLAYER_Y][PLAYER_X] = SNAKE_HEAD;
    }
}