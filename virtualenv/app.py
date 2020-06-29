from flask import Flask, request, render_template, url_for, make_response, redirect
import json 

#Config 

global maxquestion 
maxquestion = 1




#import everything from the param.json 
json_file = open("param.json", "r", encoding="utf-8")
param = json.load(json_file)
json_file.close()

#assing the values to work with them 
questions = param["questions"]
answers = param["answers"]

#Flask startup routine
app = Flask(__name__)

#for the progress of the user 
global prog 

#First the questions


@app.route("/test/0")
# the first Question 
def index():
    answ_1 = answers["1"]
    prog = {"prog" : 1}
    num_answ = answ_1[-1]
    quest = {"question" : questions[0]}
    type_answ = answ_1[-2] 
    if type_answ == "radio":
        return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ, prog = prog)
    else:
        return "else "

@app.route("/test/1")
def index_2():
    answ_1 = answers["1"]
    prog = {"prog" : 2}
    num_answ = answ_1[-1]
    quest = {"question" : questions[1]}
    type_answ = answ_1[-2] 
    if type_answ == "radio":
        return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ, prog = prog)
    else:
        return "else "


@app.route("/input/<int:prog>/", methods=["GET", "POST"])
def inputfun(prog):
    answer = ""
    if prog > maxquestion:
        prog = 0 
        return redirect("/") 
    if request == 'POST':
        answer = request.form["answer"]
    else:
        answer = request.args.get("answer")
    domain = "/test/{}".format(prog) 
    resp = make_response(redirect(domain))
    resp.set_cookie(str(prog), answer)
    return resp 

@app.route("/")
#the final Webpage for a result 
def home():
    cookie = request.cookies.get("1")
    cookie1 = request.cookies.get("2")
    cookie2 = request.cookies.get("3")
    return render_template("final.html",cookie = cookie, cookie1= cookie1 )
    
#Note in production please use debug False
if __name__ == "__main__":
    app.run(debug=True)