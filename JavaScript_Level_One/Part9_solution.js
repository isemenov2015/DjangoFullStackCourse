var name = prompt("Hi! Your name:");
var surname = prompt("Surname:");
var height = prompt("Height in cm:")
var age = prompt("Age:")
var pet = prompt("Pet name:")

alert("Thanks for your time!")
if (name[0] === surname[0] && height >= 170 && age > 20 && age < 30 && pet[pet.length-1] === "y") {
  console.log("Spy test passed. Welcome to the club!");
}
else {
  console.log("No interesting info provided. Go away!");
}
