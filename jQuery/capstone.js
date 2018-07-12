var player1Name = prompt("Player One: Enter your name, you will be Blue");
var player2Name = prompt("Player Two: Enter your name, you will be Red");

var blueTurn = true;
var gameOver = false;
var cells = [];
var table = $('table tr');

const NCOLS = 7;
const NROWS = 6;

function printHeader() {
  var pName = player2Name;
  var pColor = "Red";
  if (blueTurn) {
    pName = player1Name;
    pColor = "Blue";
  }
  $("h3").text(pName + ": it is your turn, please pick a column to drop your " + pColor + " chip");
  $("h3").css("color", pColor);
}

function setCellsColor() {
  //$('table').eq(rowIndex).find('td').eq(colIndex)
  for (var col = 0; col < NCOLS; col++) {
    for (var row = 0; row < cells[col].length; row++) {
      if (cells[col].length > row) {
        var cellColor = "darkblue";
        if (cells[col][row] == -1) {
          cellColor = "darkred";
        }
        table.eq(NROWS - 1 - row).find("td").eq(col).find("button").css("background", cellColor);
      }
    }
  }
}

function checkGameOver() {
  //check 4 similar cells in a column
  for (var col = 0; col < NCOLS; col++) {
    for (var row = 3; row < cells[col].length; row++) {
      if (cells[col][row-3] == cells[col][row-2] && cells[col][row-2] == cells[col][row-1] &&
            cells[col][row-1] == cells[col][row]) {
              return 1;
            }
    }
  }
  //check 4 similar cells in a row
  for (var col = 3; col < NCOLS; col++) {
    for (var row = 0; row < NROWS; row ++) {
      if (cells[col-3][row] == cells[col-2][row] && cells[col-2][row] == cells[col-1][row] &&
          cells[col-1][row] == cells[col][row] &&
          row < cells[col-3].length && row < cells[col-2].length &&
          row < cells[col-1].length && row < cells[col].length) {
            return 1;
          }
    }
  }
  //check 4 similar cells in a diagonal?

  //check tie
  var filledCells = 0;
  for (var i = 0; i < NCOLS; i++) {
    filledCells += cells[i].length;
  }
  if (filledCells >= NCOLS*NROWS) {
    return 2;
  }
  return 0;
}

function checkWin() {
  var winner = "Blue"
  gameResult = checkGameOver();
  if (gameResult == 1) {
    if (blueTurn) {
      winner = "Red";
      winnerColor = "red";
    } else {
      winnerColor = "blue";
    }
    $("h3").text(winner + " player won. Refresh the browser to start new game");
    $("h3").css("color", winnerColor);
    gameOver = true;
  } else if (gameResult == 2) {
    //tie
    $("h3").text("It's a tie. Refresh the browser to start new game");
    $("h3").css("color", "black");
    gameOver = true;
  }
}

for (var i = 0; i < NCOLS; i++) {
  cells.push([]);
}
printHeader();

//$(".board button").on("click", printHeader);

$(".board button").on("click", function(){
  if (!gameOver) {
    ncol = $(this).closest("td").index();
    if (blueTurn) {
      pushval = 1;
    }
    else {
      pushval = -1;
    }
    if (cells[ncol].length < NROWS) {
      cells[ncol].push(pushval);
      blueTurn = !blueTurn;
      printHeader();
      setCellsColor();
    }
    checkWin();
  }
});
