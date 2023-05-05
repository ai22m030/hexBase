from flask import Flask, render_template

app = Flask(__name__)

board_data = [
    [-1, 0, -1, 0, -1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, -1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [-1, 1, 1, 0, 0, 0, 0],
    [1, -1, 0, 0, 0, -1, 0],
    [1, 0, 0, 0, 0, -1, 0]
]


@app.route('/')
def dashboard():  # put application's code here
    gameplay_count = 42
    training_sessions = 15
    win_rate = 75

    return render_template('dashboard.html', gameplay_count=gameplay_count, training_sessions=training_sessions,
                           win_rate=win_rate)


@app.route('/gameplays')
def gameplays():  # put application's code here
    return render_template('gameplays.html', board=board_data)


@app.route('/train_cnn')
def train_cnn():
    # Add your training logic here
    return "Train CNN page"


@app.route('/hex_board')
def hex_board():
    # Add your training logic here
    return "hex_board"


@app.route('/agent_control')
def agent_control():
    # Add your agent control logic here
    return "Agent Control page"


if __name__ == '__main__':
    app.run()
