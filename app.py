from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Deploying Flask App at Vercel lets go"

if __name__ == '__main__':
    app.run(debug=True)
