from flask import Flask, render_template, request, jsonify
from chatbot_logic import generate_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_response():
    user_msg = request.args.get("msg")
    bot_response = generate_response(user_msg)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
