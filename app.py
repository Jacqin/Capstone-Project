from flask import Flask, render_template, request, jsonify
from game_logic import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    position = data.get('position')
    result = game.make_move(position)
    result['board'] = game.board.copy()  # Include a copy of the board state in the response
    return jsonify(result)

@app.route('/reset_game', methods=['POST'])
def reset_game():
    game.reset()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True) 