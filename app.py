# app.py
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/health', methods=['GET'])
def health():    
	return jsonify({
    	'response' : True,
	})

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='::', port=port)
