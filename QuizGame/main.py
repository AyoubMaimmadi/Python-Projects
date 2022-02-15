from Questions import Question

question_promts = [
    "Whats the best phone? \n(a) Iphone\n(b) Samsung\n(c) Nokia\n\n",
    "Whose is 5 times 3?\n(a) 25\n(b) 50\n(c) 15\n\n",
    "Whose the worst professor?\n(a) Abid\n(b) Harroud\n(c) Mourir\n"

]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    # print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
    print(f'You got {score}/{len(questions)} Correct')


if __name__ == '__main__':
    print(f'***Wlcome to the quiz game***')
    if input('Do you want to Play? y/n: ').lower() == 'y':
        run_test(questions)
    while True:
        n = input('try again? y/n: ').lower()
        if n == 'n':
            break
        else:
            run_test(questions)

    print('~'*22)
    print(f'Thank you for playing!')
    print('~'*22)
    

