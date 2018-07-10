function helloYou(name) {
  console.log("Hello, " + name);
}

function addNum(n1, n2) {
  console.log(n1+n2);
}

function helloSomeone(name = "Julie") {
  console.log("Hello, " + name);
}

function formal(name = "Sam", title = "Sir") {
  return title + " " + name;
}
