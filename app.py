from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<html>
    <h1>CICD Pipeline</h1>
    </html>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
