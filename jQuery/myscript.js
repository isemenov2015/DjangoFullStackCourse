$("h1").click(function() {
  $(this).text("Changed header")
})

$("li").click(function(){
  console.log("List element clicked");
})

//Keyboard events processing
$("input").eq(0).keypress(function(event){
  //$("h3").toggleClass("turnBlue");
  if (event.which === 13) {
    $("h3").toggleClass("turnBlue");
  }
  if (event.which === 99) {
    $("h3").toggleClass("turnRed");
  }
})

$("h1").on("dblclick", function(){
  $(this).toggleClass("turnBlue");
})

$("h2").on("mouseenter", function(){
  $(this).toggleClass("turnRed");
})

$("input").eq(1).on("click", function(){
  $(".container").fadeOut(1000); // Also available: slideUp
})
