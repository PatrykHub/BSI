import random

ALPHABET = ["a) ", "b) ","c) ","d) ","e) ","f) ","g) ","h) ","i) ","j) ","k) ","l) ",]
TRUTH = "-true"

class Question:
    def __init__(self, text: str):
        self.text = text
        self.answers = []

    def add_answer(self, answer: str, isTrue: bool):
        self.answers.append((answer, isTrue))

    def rearrange_answers(self):
        random.shuffle(self.answers)


def load_questions(filename: str):
    questions = []
    file = open(filename, 'r', encoding='utf-8')
    count = 1
    number = str(count) + ". "
    for line in file:
        if line == "\n":
            continue
        if number in line:
            if count != 1:
                question.rearrange_answers()
                questions.append(question)

            question = Question(line.replace(number, ''))               
            count += 1
            number = str(count) + ". "
        else:
            answer = line
            for prefix in ALPHABET:
                answer = answer.replace(prefix, '')
            
            if TRUTH in answer:
                question.add_answer(answer.replace(TRUTH, ''), True)
            else:
                question.add_answer(answer, False)
    question.rearrange_answers()
    questions.append(question)
    file.close()
    return questions


def print_question(question: Question):
    print(question.text)
    count = 1
    number = str(count) + ". "
    truths = []
    for answer in question.answers:
        print(number + answer[0])
        if answer[1] == True:
            truths.append(count)
        count += 1
        number = str(count) + ". "
    return truths


def quiz():
    questions = load_questions("./questions.txt")
    random.shuffle(questions)
    score = 0.0
    mx = len(questions)
    print("Select level: \n1. Twórca quizu - 10 pytań\n2. Twórcy docsa - 100 pytań\n3. Prowadzący - 200 pytań \n4. KERBEROS - wszystkie pytania \n5. Własna ilosc pytań")
    choice = int(input())

    if choice == 1:
        length = 10
    elif choice == 2:
        length = 100
    elif choice == 3:
        length = 200
    elif choice == 4:
        length = 10000
    elif choice == 5:
        print("Podaj własną ilość pytań: ")
        length = int(input())

    if mx > length:
        mx = length

    counter = 1
    for question in questions:
        print(str(counter) + "/" + str(mx))
        counter += 1
        truths = print_question(question)
        answer = [int(x) for x in input().split()]
        answer.sort()
        if answer == truths:
            print("DOBRZE!")
            score += 1
        else:
            print("ŻLE! Poprawne odpowiedzi to: ", truths)
            score_in_question = 0.0
            for x in answer:
                if x in truths:
                    score_in_question += 1.0/len(truths)
                else:
                    score_in_question -= 1.0/len(truths)
            if score_in_question > 0:
                score += score_in_question
        if counter > length:
            break
    print("Koniec! Twój wynik to: " + str(round(score, 2)) + "/" + str(mx))


quiz()