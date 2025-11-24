import time
import json
import random

def load_questions():
    with open(r"C:\Users\HP\Desktop\macu\questions.json", "r") as f:
        questions = json.load(f)["questions"]
    return questions



def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)

    random_questions = random.sample(questions, num_questions)
    return random_questions

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ".", option)

    number = input("Select the correct number: ")
    number = int(number)
    while True:
        if number < 1 or number > len(question["options"]):
            print("Invalid choice, defaulting wrong answer!")
        else:
            break
         
questions = load_questions()
total_questions = int(input("Enter the number of questions: "))
random_questions = get_random_questions(questions, total_questions)
correct = 0
start_time = time.time()
for question in random_questions:
    is_correct = ask_question(question)
    if is_correct:
        correct += 1
    print("-----------------")
end_time = time.time()
total_time = end_time - start_time

print("Summary")
print(f"Total questions is: {total_questions}")
print(f"Correct answer is: {correct}")
print(f"time finished is: {total_time:.2f} seconds")