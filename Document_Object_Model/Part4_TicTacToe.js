
var cells = document.querySelectorAll("td");
var btn = document.querySelector("#button");

function getText(chr) {
  if (chr === " ") {
    return "X";
  }
  if (chr === "X") {
    return "O";
  }
  return " ";
}

for (c of cells) {
  c.addEventListener("click",
            function() {
                this.textContent = getText(this.textContent);
            });
}

btn.addEventListener("click", function(){
    for (c of cells) {
      c.textContent = " ";
    };
  });
