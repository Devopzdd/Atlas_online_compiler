from flask import Flask, request, jsonify, render_template
import sys
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code')
    input_data = data.get('input')

    output = io.StringIO()
    sys.stdout = output
    try:
        exec(code, {'input': input_data})
    except Exception as e:
        return jsonify({'output': str(e)})
    finally:
        sys.stdout = sys.__stdout__

    return jsonify({'output': output.getvalue()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)






