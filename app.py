from flask import Flask, jsonify, render_template

app = Flask(__name__)

# This is the global memory keeping track of the queue
current_token = 0

# The route that loads the student's HTML frontend
@app.route('/')
def home():
    return render_template('index.html')

# The route that loads the clerk's dashboard
@app.route('/admin')
def admin():
    return render_template('admin.html')

# The API that the student's phone will check every 5 seconds
@app.route('/api/status')
def get_status():
    return jsonify({"token": current_token})

# The API the clerk uses to call the next student
@app.route('/api/advance', methods=['POST'])
def advance_token():
    global current_token
    current_token += 1
    return jsonify({"message": "Token advanced", "new_token": current_token})

if __name__ == '__main__':
    app.run(debug=True)