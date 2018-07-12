var player1Name = prompt("Player One: Enter your name, you will be Blue");
var player2Name = prompt("Player Two: Enter your name, you will be Red");

var blueTurn = true;
var cells = [];
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

}

for (var i = 0; i < NCOLS; i++) {
  cells.push([]);
}
printHeader();

//$(".board button").on("click", printHeader);

$(".board button").on("click", function(){
  ncol = $(this).closest("td").index();
  if (blueTurn) {
    pushval = 1;
  }
  else {
    pushval = -1;
  }
  if (cells[ncol].length < NROWS) {
    cells[ncol].push(pushval);
  }
  blueTurn = !blueTurn;
  printHeader();
  setCellsColor();
  console.log(cells);
});
