class QuizBrain:
    def __init__(self,list):
        self.question_number=0
        self.question_list=list
        self.score=0

    def still_has_question(self):
        if self.question_number==len(self.question_list)-1:
            return False
        else:
            return True

    def next_question(self):
        current_question=self.question_list[self.question_number]
        print(f"Current Score:{self.score}")
        user_answer=input(f"Q.no{self.question_number+1}.{current_question.text}.(true/false):").lower()
        while user_answer!='true' and user_answer!='false':
            print("Only correct inputs please   ie 'true'/'false' ")
            user_answer = input(f"Q.no{self.question_number + 1}.{current_question.text}.(true/false):").lower()
        if user_answer.title()==current_question.answer:
            self.score+=1
            self.question_number+=1
            print("Correct answer. \n")
        else:
            print("L wrong answer\n")
            self.question_number+=1