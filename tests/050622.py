identifier = 1

class Question:
    def __init__(self):
        global identifier
        self.id = identifier
        identifier += 1

question_1 = Question()
question_2 = Question()
question_3 = Question()

latest_question_list = [question_1, question_2, question_3]
id_list = [question.id for question in latest_question_list]
print(id_list)

#--------------------------------------------------------------



from faker import Faker

faker = Faker()

class Question:
    identifier = 1

    def __init__(self):
        self.id = Question.identifier
        Question.identifier += 1
        self.question_text = faker.sentence()

question_1 = Question()
question_2 = Question()
question_3 = Question()

latest_question_list = [question_1, question_2, question_3]

if latest_question_list:
    print("<ul>")
    for question in latest_question_list:
        print(f"<li><a href='/polls/{question.id}/'>{question.question_text}</a></li>")
    print("</ul>")
else:
    print("<p>No polls are available.</p>")