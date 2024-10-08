let gameArea = document.getElementById('gameArea');
let racer = document.getElementById('racer');
let scoreDisplay = document.getElementById('score');
let score = 0;
let isJumping = false;
let gameSpeed = 5;

// Create and move the obstacle
function createObstacle() {
    let obstacle = document.createElement('div');
    obstacle.classList.add('obstacle');
    obstacle.style.right = '0px';
    gameArea.appendChild(obstacle);

    let obstacleInterval = setInterval(function() {
        let obstacleLeft = parseInt(window.getComputedStyle(obstacle).right);
        if (obstacleLeft < gameArea.clientWidth) {
            obstacle.style.right = (obstacleLeft + gameSpeed) + 'px';
        } else {
            clearInterval(obstacleInterval);
            gameArea.removeChild(obstacle);
            score++;
            scoreDisplay.innerText = 'Score: ' + score;
        }

        if (detectCollision(obstacle)) {
            clearInterval(obstacleInterval);
            alert('Game Over! Your score: ' + score);
            resetGame();
        }
    }, 20);
}

// Racer jump logic
document.addEventListener('keydown', function(event) {
    if (event.code === 'Space' && !isJumping) {
        jump();
    }
});

function jump() {
    isJumping = true;
    let jumpHeight = 0;
    let jumpInterval = setInterval(() => {
        if (jumpHeight >= 100) {
            clearInterval(jumpInterval);
            let fallInterval = setInterval(() => {
                if (jumpHeight <= 0) {
                    clearInterval(fallInterval);
                    isJumping = false;
                } else {
                    jumpHeight -= 5;
                    racer.style.bottom = (50 + jumpHeight) + 'px';
                }
            }, 20);
        } else {
            jumpHeight += 5;
            racer.style.bottom = (50 + jumpHeight) + 'px';
        }
    }, 20);
}

// Detect collision between racer and obstacle
function detectCollision(obstacle) {
    let racerRect = racer.getBoundingClientRect();
    let obstacleRect = obstacle.getBoundingClientRect();

    return !(
        racerRect.bottom < obstacleRect.top ||
        racerRect.top > obstacleRect.bottom ||
        racerRect.right < obstacleRect.left ||
        racerRect.left > obstacleRect.right
    );
}

// Reset the game
function resetGame() {
    score = 0;
    scoreDisplay.innerText = 'Score: ' + score;
    // Remove all obstacles
    let obstacles = document.querySelectorAll('.obstacle');
    obstacles.forEach(obstacle => gameArea.removeChild(obstacle));
}

// Start generating obstacles
setInterval(createObstacle, 1500);
