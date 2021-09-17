import random
import time

number_of_questions = 10
tries = 3
start_time = 0
correct_answers = 0
i = 0

for question_number in range(number_of_questions):
    multiplier = random.randint(0, 9)
    multiplicand = random.randint(0, 9)

    result = multiplier * multiplicand

    while tries > 0:
        if start_time == 0:
            start_time = time.time()

        while True:
            answer = input(f"{question_number + 1}: {multiplier} * {multiplicand} = ? ")
            try:
                answer = int(answer)
                break
            except ValueError:
                print("Not a number, please try again!")

        if answer == result:
            print("Correct!")
            correct_answers += 1
            time.sleep(1)
            break
        elif (time.time() - start_time) >= 8:
            print("Time's up!")
            break
        else:
            print("Incorrect, please try again!")
            tries -= 1
    question_number += 1

time.sleep(1)
print("Score: %s / %s" % (correct_answers, number_of_questions))
