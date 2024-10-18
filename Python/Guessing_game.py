from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize the game variables
lower_bound = 1
upper_bound = 100
random_number = random.randint(lower_bound, upper_bound)
attempts = 7

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global attempts, random_number
    if attempts > 0:
        user_guess = int(request.form['guess'])
        message = ""
        if user_guess < lower_bound or user_guess > upper_bound:
            message = f"Please guess a number between {lower_bound} and {upper_bound}."
        elif user_guess == random_number:
            message = f"Congratulations! You guessed the correct number {random_number}!"
            random_number = random.randint(lower_bound, upper_bound)  # Reset for next round
            attempts = 7  # Reset attempts
        elif user_guess < random_number:
            attempts -= 1
            message = "Too low! Try a higher number."
        else:
            attempts -= 1
            message = "Too high! Try a lower number."

        if attempts == 0:
            message += f" Sorry, you've used all your attempts. The correct number was {random_number}. Starting a new game."
            random_number = random.randint(lower_bound, upper_bound)
            attempts = 7  # Reset the attempts for new game

        return jsonify({'message': message, 'attempts_left': attempts})

if __name__ == '__main__':
    app.run(debug=True)
