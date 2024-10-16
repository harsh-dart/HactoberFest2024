const paddle = document.getElementById("paddle");
const ball = document.getElementById("ball");
const scoreDisplay = document.getElementById("score");

let score = 0;
let ballSpeed = 2;
let ballPosition = { x: Math.random() * 280, y: 0 };
let paddlePosition = 110;

function updateGame() {
  // Ball movement
  ballPosition.y += ballSpeed;
  if (ballPosition.y >= 380) {
    if (
      ballPosition.x > paddlePosition &&
      ballPosition.x < paddlePosition + 80
    ) {
      score++;
      ballSpeed += 0.2; // Increase speed with every successful catch
      resetBall();
    } else {
      resetGame();
    }
  }
  if (ballPosition.y > 400) {
    resetBall();
  }
  ball.style.top = ballPosition.y + "px";
  ball.style.left = ballPosition.x + "px";
}

function resetBall() {
  ballPosition.y = 0;
  ballPosition.x = Math.random() * 280;
}

function resetGame() {
  score = 0;
  ballSpeed = 2;
  resetBall();
}

function movePaddle(event) {
  if (event.key === "ArrowLeft" && paddlePosition > 0) {
    paddlePosition -= 20;
  } else if (event.key === "ArrowRight" && paddlePosition < 220) {
    paddlePosition += 20;
  }
  paddle.style.left = paddlePosition + "px";
}

// Game loop
function gameLoop() {
  updateGame();
  scoreDisplay.innerText = `Score: ${score}`;
  requestAnimationFrame(gameLoop);
}

// Event listener for paddle movement
document.addEventListener("keydown", movePaddle);

// Start the game loop
gameLoop();
