from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_condition', methods=['POST'])
def check_condition():
    data = request.get_json()
    symptoms = int(data.get('symptoms', 0))

    if symptoms >= 8:
        result = "Critical Condition – Send patient to ICU immediately"
    elif 4 <= symptoms <= 7:
        result = "Patient should stay in hospital for observation"
    elif 2 <= symptoms <= 3:
        result = "Doctor checkup required, patient can go home with medicine"
    else:
        result = "No serious symptoms"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)