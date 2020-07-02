from flask import Flask, request, render_template, url_for, make_response, redirect
import json 
#Config 

global maxquestion 
maxquestion = 2


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

@app.route("/test/0")
# the first Question 
def index_0():
    #fill in the num of the question
    num_quest = 0
    #only the first question needs that 
    test = request.cookies.get("prog")
    if test == None:
        prog_1 = 0 
    else:
         
        prog_1 = int(request.cookies.get("prog"))
    if prog_1 != num_quest:
        return redirect("/test/{}".format(prog_1))
    else:
        #extracting the list from the json dict
        answ_1 = answers["{}".format(num_quest)]
        prog = {"prog" : num_quest + 1}
        cat = {"cat" : answ_1[-3]}
        num_answ = answ_1[-1]
        quest = {"question" : questions[num_quest]}
        type_answ = answ_1[-2] 
       
    if type_answ == "radio":
            return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ, prog = prog, cat = cat) 
    else:
            return "nothing to see here"

@app.route("/test/1")
# the first Question 
def index_1():
    #fill in the num of the question
    num_quest = 1
    #only the first question needs that 
    test = request.cookies.get("prog")
    if test == None:
        prog_1 = 0 
    else:
         
        prog_1 = int(request.cookies.get("prog"))
    if prog_1 != num_quest:
        return redirect("/test/{}".format(prog_1))
    else:
        #extracting the list from the json dict
        answ_1 = answers["{}".format(num_quest)]
        prog = {"prog" : num_quest + 1}
        cat = {"cat" : answ_1[-3]}
        num_answ = answ_1[-1]
        quest = {"question" : questions[num_quest]}
        type_answ = answ_1[-2] 
       
    if type_answ == "radio":
            return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ, prog = prog, cat = cat) 
    else:
            return "nothing to see here"

@app.route("/test/2")
# the first Question 
def index_2():
    #fill in the num of the question
    num_quest = 2
    #only the first question needs that 
    test = request.cookies.get("prog")
    if test == None:
        prog_1 = 0 
    else:
         
        prog_1 = int(request.cookies.get("prog"))
    if prog_1 != num_quest:
        return redirect("/test/{}".format(prog_1))
    else:
        #extracting the list from the json dict
        answ_1 = answers["{}".format(num_quest)]
        prog = {"prog" : num_quest + 1}
        cat = {"cat" : answ_1[-3]}
        num_answ = answ_1[-1]
        quest = {"question" : questions[num_quest]}
        type_answ = answ_1[-2] 
       
    if type_answ == "radio":
            return render_template('dropdown.html', question = quest, answ1 = answ_1, num_answ = num_answ, prog = prog, cat = cat) 
    else:
            return "nothing to see here"

#please note you need the third one for routing
@app.route("/test/2/")
def index3():
    return redirect("/")

@app.route("/input/<int:prog>/<string:cat>/", methods=["GET", "POST"])
def inputfun(prog, cat):
    answer = ""
    #checks wether the user is at the end
    if prog > maxquestion:
        return redirect("/") 
    #standart data recieve 
    elif request == 'POST':
        answer = int(request.form["answer"])
    else:
        answer = int(request.args.get("answer"))
    #firts of get all of the categorie cookies
    cookie_test = request.cookies.get("{}".format(cat))
    #check wether its null dependent on the state of the user
    if cookie_test == None:
        answer =+ 1
    #when the cookie is set bring all values to > 1 then calc
    else:
        cur_cookie = int(request.cookies.get("{}".format(cat))) + 1
        answer = answer + cur_cookie
    #configure the redirekt
    domain = "/test/{}".format(prog) 
    resp = make_response(redirect(domain))
    #finaly set and return the cookie
    
    resp.set_cookie(cat, str(answer), max_age = 1000)
    resp.set_cookie("prog", str(prog), max_age = 1000)
    return resp


@app.route("/")
#the final Webpage for a result 
def home():
    return render_template("final.html",cookie = "TEST")


#Note in production please use debug False
if __name__ == "__main__":
    app.run(debug=True)