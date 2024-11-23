from Quiz_data import question_and_answers
from quiz_brain import QuizBrain
from question_model import QuestionModel
question_bank=[]
for item in question_and_answers:
    question = item['question']
    answer = item['correct_answer']
    new_question = QuestionModel(question=question,answer=answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
# quiz.start_quiz()
while quiz.still_has_questions():
    quiz.nex_question()