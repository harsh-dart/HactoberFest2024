const image1 = document.querySelector(".dice1 img");
const image2 = document.querySelector(".dice2 img");
const rollButton = document.getElementById("rollButton");

rollButton.addEventListener("click", function() {
    // Add rotation class
    rollButton.classList.add("rotating");
    
    // Remove rotation class after animation completes
    setTimeout(() => {
        rollButton.classList.remove("rotating");
    }, 500); // Duration should match the animation duration in CSS

    // Roll the dice
    const num1 = Math.floor(Math.random() * 6 + 1);
    const newsrc1 = "images/" + num1 + ".jpg";
    image1.setAttribute("src", newsrc1);

    const num2 = Math.floor(Math.random() * 6 + 1);
    const newsrc2 = "images/" + num2 + ".jpg";
    image2.setAttribute("src", newsrc2);

    // Display the winning message
    let el = document.querySelector(".winningmessage");
    if (!el) {
        el = document.createElement("div");
        el.classList.add("winningmessage");
        document.body.appendChild(el);
    }

    if (num1 > num2) {
        el.innerHTML = "Player 1 is the winner"; 
    } else if (num1 < num2) {
        el.innerHTML = "Player 2 is the winner"; 
    } else {
        el.innerHTML = "It is a draw"; 
    }
});
