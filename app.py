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


@app.route('/board')
def hex_board():
    # Add your training logic here
    return render_template('board.html', board=board_data)


@app.route('/agent_control')
def agent_control():
    # Add your agent control logic here
    return "Agent Control page"


@app.route('/manage_gameplays')
def manage_gameplays():
    # Add your manage gameplays logic here
    return "Manage gameplays page"

@app.route('/generate_gameplays')
def generate_gameplays():
    # Add your generate gameplays logic here
    return "Generate gameplays page"

@app.route('/preview_gameplays')
def preview_gameplays():
    # Add your preview gameplays logic here
    return "Preview gameplays page"

@app.route('/load_gameplays')
def load_gameplays():
    # Add your load gameplays logic here
    return "Load gameplays page"

@app.route('/save_gameplays')
def save_gameplays():
    # Add your save gameplays logic here
    return "Save gameplays page"


if __name__ == '__main__':
    app.run()
