class QuizBrain:
    def __init__(self,question_bank):
        self.score = 0
        self.question_number = 0
        self.question_bank = question_bank

    
    def start_quiz(self):
        for item in self.question_bank:
            answer = input(str(self.question_number+1)+ " "+ item.question)
            if answer == item.answer:
                self.score+=1
                print(f"corect answer. Your current score is {self.score}/{len(self.question_bank)}")
                self.question_number+=1
            else:
                print(f"Wrong answer. Your current score is {self.score}/{len(self.question_bank)}")
                self.question_number+=1

    def still_has_questions(self):
        return self.question_number<len(self.question_bank)
    
    def nex_question(self):
        # for item in self.question_bank[]:
        #     answer = input(str(self.question_number+1)+ " "+ item.question)
        #     if answer == item.answer:
        #         self.score+=1
        #         print(f"corect answer. Your current score is {self.score}/{len(self.question_bank)}")
        #         self.question_number+=1
        #     else:
        #         print(f"Wrong answer. Your current score is {self.score}/{len(self.question_bank)}")
        #         self.question_number+=1
        answer = input(str(self.question_number+1)+ " "+ self.question_bank[self.question_number].question)
        if answer == self.question_bank[self.question_number].answer:
            self.score+=1
            print(f"corect answer. Your current score is {self.score}/{len(self.question_bank)}")
            self.question_number+=1
        else:
            print(f"Wrong answer. Your current score is {self.score}/{len(self.question_bank)}")
            self.question_number+=1
