from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

QuestionBank = []
for QandA in question_data:
    question_text = QandA["question"]
    question_answer = QandA["correct_answer"]
    new_question = Question(question_text, question_answer)
    QuestionBank.append(new_question)
    
quiz = QuizBrain(QuestionBank)
while quiz.still_has_question():
    print(quiz.next_question())

print("You've completed the quiz")
print(f"Your total score is {quiz.score}/{quiz.question_number}")

