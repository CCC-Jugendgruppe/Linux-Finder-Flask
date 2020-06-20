class engine():
    def __init__(self, questions):

        self.questions = questions
        for i in range(len(questions)):

            if i == 0:
                print("First Question:")
            elif i == 1:
                print("Second Question:")
            elif i == 2:
                print("Third Question:")
            else:
                print(i)
                print(" Question")

            print(questions[i] , "\n")
            int(input())