
var cells = document.querySelectorAll("td");
var btn = document.querySelector("#button");

function setText() {
  if (this.textContent === " ") {
    this.textContent = "X";
  } else if (this.textContent === "X") {
    this.textContent = "O";
  } else {
    this.textContent = " ";
  }
}

for (c of cells) {
  c.addEventListener("click", setText);
}

btn.addEventListener("click", function(){
    for (c of cells) {
      c.textContent = " ";
    };
  });
