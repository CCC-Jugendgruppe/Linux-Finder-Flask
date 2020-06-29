from flask import Flask, request, render_template, url_for
import json 

#import everything from the param.json 
json_file = open("param.json", "r", encoding="utf-8")
param = json.load(json_file)
json_file.close()

#assing the values to work with them 
questions = param["questions"]
answers = param["answers"]

#Flask startup routine
app = Flask(__name__)


#First the questions
@app.route("/test/1")
def index():
    answ_1 = answers["1"]
    num_answ = answ_1[-1]
    quest = {"question" : questions[0]}
    type_answ = answ_1[-2] 
    if type_answ == "radio":
        return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ)
    else:
        return "else "

@app.route("/test/2")
def index_1():
    answ_1 = answers["2"]
    num_answ = answ_1[-1]
    quest = {"question" : questions[1]}
    type_answ = answ_1[-2] 
    if type_answ == "radio":
        return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ)
    else:
        return "else "
@app.route("/test/3")
def index_2():
    answ_1 = answers["3"]
    num_answ = answ_1[-1]
    quest = {"question" : questions[2]}
    type_answ = answ_1[-2] 
    if type_answ == "radio":
        return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ)
    else:
        return "else "


@app.route("/input/<inp>", methods=["GET", "POST"])
def inputfun(inp):
    dictionarry = {'Test': "Mein name", "noch ein Name":"mein Name", "True": None}

    return dictionarry #json.dumps(inp)

@app.route("/json")
def jsonfun(dictionarry):
    return json.dumps(dictionarry)



#Note in production please use debug False
if __name__ == "__main__":
    app.run(debug=True)