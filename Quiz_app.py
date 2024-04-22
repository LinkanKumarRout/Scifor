questions = [
  {
    'question': 'Python is high level language ?',
    'options': ['true', 'false'],
    'answer': 'true'
  },
  {
    'question': 'Python is an interpreted language ?',
    'options': ['true', 'false'],
    'answer': 'true'
  },
  {
    'question': 'Python is only procedural oriented language ?',
    'options': ['true', 'false'],
    'answer': 'false'
  }
]

class Quiz:
  def __init__(self, questions):
    self.questions = questions
    self.current_question = 0
    self.score = 0

  def display_question(self):
    self.current_question = self.questions.pop(0)
    print(f"Your Question is: {self.current_question['question']}")
    for i, option in enumerate(self.current_question['options']):
      print(f"{i+1}) {option}")

  def check_answer(self, answer):
    correct_answer = self.current_question['answer']
    if answer == correct_answer:
      print("Correct Answer !")
      self.score += 1
    else:
      print("Incorrect Answer !")

  def next_question(self):
    if self.questions:
      self.display_question()
    else:
      self.display_score()

  def display_score(self):
    print("Quiz Completed !!")
    print(f"Your Score is: {self.score}")

obj = Quiz(questions)

obj.display_question()
while True:
  answer = input("Enter your answer: ")
  if answer == 'exit':
    print("Quiz Stopped\nBye.....")
    break
  obj.check_answer(answer)
  obj.next_question()