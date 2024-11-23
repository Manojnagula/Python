import requests
import json
# class Quiz_data:    
#     def __init__(self):
#         self.question_and_answers=[]

#     def get_data(self,request):
        # request_ = requests.get(request)
        # response =json.loads(request_.text)
        # result = response['results']
        # question_and_answers = [{'question':dictionary['question'],'correct_answer':dictionary['correct_answer']} for dictionary in result]
#         # question_and_answers = []
#         # for dictionary in result[:][:]:
#         #     question_and_answers.append({'questiuon':dictionary['question'],'correct_answer':dictionary['correct_answer']})
#         self.question_and_answers=question_and_answers
URL="https://opentdb.com/api.php?amount=10&category=27&type=boolean"
request=URL
request_ = requests.get(request)
response =json.loads(request_.text)
result = response['results']
question_and_answers = [{'question':dictionary['question'],'correct_answer':dictionary['correct_answer']} for dictionary in result]
