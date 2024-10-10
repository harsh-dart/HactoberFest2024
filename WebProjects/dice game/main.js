let image1 = document.querySelector(".dice1 img");
let image2 = document.querySelector(".dice2 img");

function Refresh(){
    let num1=Math.floor(Math.random()*6+1);
    let newsrc1="images/"+num1+".jpg";
    image1.setAttribute("src",newsrc1);
    let num2=Math.floor(Math.random()*6+1);
    let newsrc2="images/"+num2+".jpg";
    image2.setAttribute("src",newsrc2);
   
    win(num1,num2)
}
let el=document.querySelector(".result")
function win(num1,num2){ 
    el.classList.add("winningmessage");
    
    if (num1 > num2) {
        
        el.innerText = "Player 1 is the winner";
       
    } else if (num1 < num2) {
       
        el.innerText = "Player 2 is the winner"; 
    } else {
        
        el.innerText= "It is a draw"; 
        
    }
   
}

let btn=document.querySelector(".btn");
btn.addEventListener("click",()=>{

    el.innerText="";
    Refresh();
})



