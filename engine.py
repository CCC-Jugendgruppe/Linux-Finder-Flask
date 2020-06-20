import sys
class engine():
    def __init__(self, questions, min_points,max_points):
        """We all love Tux aren't we."""
        self.questions = questions
        self.max_points = max_points
        self.min_points = min_points
        print("              a8888b.")
        print("             d888888b.")
        print('             8P"YP"Y88')
        print("             8|o||o|88")
        print("             8'    .88")
        print("             8`._.' Y8.")
        print("            d/      `8b.")
        print("           dP   .    Y8b.\n")
        print("Welcome to the Linux-Finder: \nThis Program helps you find the right Distro for you! \n\n")

        """Please only insert questions with this scheme for design reasons:
        Gui[1] or Bash?[2]
        note that only the first 3 Questions will have special beginnings."""
        anw = 0
        for i in range(len(self.questions)):
            if i == 0:
                print("First Question:")
            elif i == 1:
                print("Second Question:")
            elif i == 2:
                print("Third Question:")
            else:
                print(i)
                print(" Question")
            print(self.questions[i], "\n")
            anw += int(input())
            if anw > min_points[i]:
                print("Pleas follow the instrucktion in the question!")
                sys.exit(0)
            elif anw > max_points[i]:
                print("Pleas follow the instrucktion in the question!")
                sys.exit(0)
        if i < len(self.questions):
            print("""             .-.\n         .-'``(   )\n      ,`\ \    `-`.\n     /   \ '``-.   `   \n   .-.  ,       `___:  \n  (   ) :        ___   \n   `-`  `       ,   :\n     \   / ,..-`   ,\n      `./ /    .-.`\n         `-..-(   )\n               `-`""")
            print("Ubuntu seems a good choice.")
        elif i == len(self.questions):

            print("Manjaro seemes good here.")
