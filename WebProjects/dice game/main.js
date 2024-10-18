// Get the image elements
let image1 = document.querySelector(".dice1 img");
let image2 = document.querySelector(".dice2 img");

// Generate random numbers for the dice
let num1 = Math.floor(Math.random() * 6) + 1; // Random number between 1-6
let newSrc1 = "images/" + num1 + ".jpg";
image1.setAttribute("src", newSrc1);

let num2 = Math.floor(Math.random() * 6) + 1; // Random number between 1-6
let newSrc2 = "images/" + num2 + ".jpg";
image2.setAttribute("src", newSrc2);

// Create a div for the winning message
let messageDiv = document.createElement("div");
messageDiv.classList.add("winningmessage");
messageDiv.style.backgroundColor = "yellow";
messageDiv.style.fontFamily = "cursive";
messageDiv.style.fontSize = "50px";
messageDiv.style.textAlign = "center";
document.body.app
