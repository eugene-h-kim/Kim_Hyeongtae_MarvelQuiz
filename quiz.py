from components.quizQuestions import questions
from components import vars, quizTally

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("*********************************************\n")


answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("*********************************************\n")


answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print("*********************************************\n")


answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print("*********************************************\n")


answer5 = questions["q5"][input(questions["q5"]["question"])]
print(answer5)

vars.quizTotal += answer5
print("*********************************************\n")


answer6 = questions["q6"][input(questions["q6"]["question"])]
print(answer6)

vars.quizTotal += answer6
print("*********************************************\n")


answer7 = questions["q7"][input(questions["q7"]["question"])]
print(answer7)

vars.quizTotal += answer7
print("*********************************************\n")


answer8 = questions["q8"][input(questions["q8"]["question"])]
print(answer8)

vars.quizTotal += answer8
print("*********************************************\n")



print("total so far: " + str(vars.quizTotal) + "\n")


# after answer all the questions, figure out who your character is
quizTally.total(vars.quizTotal)


