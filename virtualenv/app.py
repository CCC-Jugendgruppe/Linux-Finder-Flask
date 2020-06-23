from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return"""Welcome to Linux-Finder
    <br>
    Erste Frage:
    <br>
    <form action="http://localhost:1337/answers" method = "get"> 
    <input type = "text" name = "name"/>
    <p> 
    <input type="submit" value="submit"/>
    </form>
    
    """
@app.route("/answers", methods=["POST", "GET"])
def answer():
    
    name = request.args.get('name')
    return "Hello" + name

#Note in production please use debug False
if __name__ == "__main__":
    app.run(debug=True)