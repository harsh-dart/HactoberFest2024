let image1 = document.querySelector(".dice1 img");
let image2 = document.querySelector(".dice2 img");
let num1=Math.floor(Math.random()*6+1);
let newsrc1="images/"+num1+".jpg";
image1.setAttribute("src",newsrc1);
let num2=Math.floor(Math.random()*6+1);
let newsrc2="images/"+num2+".jpg";
image2.setAttribute("src",newsrc2);
let el = document.createElement("div"); 
el.classList.add("winningmessage");
el.style.backgroundColor = "yellow";
el.style.fontFamily = "cursive";
el.style.fontSize = "50px";
el.style.textAlign = "center";
document.body.appendChild(el);
if (num1 > num2) {
    el.innerHTML = "Player 1 is the winner"; 
} else if (num1 < num2) {
    el.innerHTML = "Player 2 is the winner"; 
} else {
    el.innerHTML = "It is a draw"; 
}