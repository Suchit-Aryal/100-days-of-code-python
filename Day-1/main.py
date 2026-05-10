import random
from question_model import question
from data import question_data
from quiz_brain import QuizBrain
print(len(question_data))
question_bank=[]
for i in range(0,len(question_data)-1):
    new_question=question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(new_question)
print(question_bank)
random.shuffle(question_bank)
quiz=QuizBrain(question_bank)
q_number=quiz.question_number
while quiz.still_has_question():
    quiz.next_question()
print(f"Congralution for finishing the quiz with a score of '{quiz.score}'")