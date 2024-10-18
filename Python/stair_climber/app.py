from flask import Flask, render_template, request, jsonify
import json
import sys
sys.setrecursionlimit(2000)  # Set to a higher value if needed


app = Flask(__name__)

def count_ways(k):
    if k == 0:
        return 2, [['D']]  # D for Down
    if k == 1:
        return 4, [['S'], ['D', 'U0'], ['U1', 'D'], ['D', 'U0']]  # S for Stay, D for Down, U for Up

    # Initialize a dp array for counts and a list for sequences
    dp = [0] * (k + 1)
    sequences = [[] for _ in range(k + 1)]

    # Base cases
    dp[0] = 1
    sequences[0] = [['D']]  # Down to stair 0 from stair 1
    dp[1] = 4
    sequences[1] = [
        ['S'],  # Stay at stair 1
        ['D', 'U0'],  # Down to 0 and up to 1
        ['U1', 'D'],  # Up to 2 and back down to 1
        ['D', 'U0']   # Down to 0 and up to 1 again
    ]

    for i in range(2, k + 1):
        dp[i] = dp[i - 1]  # Coming down from i to i-1
        sequences[i] += [seq + ['D'] for seq in sequences[i - 1]]  # Adding Down sequences

        jump = 1
        while (2 ** jump) <= i:  # Handle jumps
            dp[i] += dp[i - (2 ** jump)]
            for seq in sequences[i - (2 ** jump)]:
                sequences[i].append(seq + [f'U{jump}'])  # Adding Up sequences
            jump += 1

    return dp[k], sequences[k]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = json.loads(request.data)
    k = data['k']
    if k < 0:
        return jsonify({'error': 'k must be a non-negative integer'}), 400
    ways_count, ways_list = count_ways(k)
    return jsonify({'ways_count': ways_count, 'ways_list': ways_list})

if __name__ == '__main__':
    app.run(debug=True)