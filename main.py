from engine import engine

#Please follow the sceam: rather Gui[1] or Bash?[2]

questions = ["Das ist eine Frage: bitte nur bis 1 und 5 ", "Das ist noch eine Fragenur bis null und 2"]
min_points = [1, 0]
max_points = [5, 2]
# first Version only wit a CMD overlay

#try out the help
#help(engine)

engine(questions, min_points)
