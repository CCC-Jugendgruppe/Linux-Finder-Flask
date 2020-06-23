from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route("/test")
def index():
    questions = ["Wie viel Ram hat dein Pc? ", "Wie viel Erfahrung hast du bereits"]
    i = 0
    for i in range(len(questions)):
        question = {"question" : questions[i]}
        answ1 = {"answ1" : "10GB"}
        return render_template('dropdown.html', question = question, answ1 = answ1)




#Note in production please use debug False
if __name__ == "__main__":
    app.run(debug=True)