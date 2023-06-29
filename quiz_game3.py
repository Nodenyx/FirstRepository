import time

def new_game():

    guesses = []
    question_num = 1
    correct_guesses = 0

    for x in questions:
        print("---------------------------------------------------------------------------")
        print(x)
        print("----------")
        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter your answer here, A, B, C or D: ").upper()
        guesses.append(guess)
        question_num += 1
        correct_guesses += check_answer(guess,questions.get(x))

    print(len(guesses))
    display_score(guesses, correct_guesses)

def check_answer(guess,answer):
    if guess == answer:
        print("CORRECT")
        return 1
    else:
        print("INCORRECT")
        return 0
def display_score(guesses, correct_guesses):
    print("---------------------------------------------------------------------------")
    print("Your answers: ")
    for x in guesses:
        print(x, end=" ")
    print("")
    print("Your score is: "+str(correct_guesses*100/len(guesses))+"%")
    play_again()
def play_again():
    again = input("Do you want to play again? (yes or no): ").lower()
    if again == "yes":
        new_game()
    else:
        print("Goodbye!")


questions = {
            "What are floating point numbers?": "C",
            "Syntax is?": "C",
            "Are integers mutable in python?": "D",
            "The intel C4004 was a incredibly impressive why?": "A",
            "Can a turing machine do all computations given enough memory and time?": "A",
            'What does "PCB" (computer science) stand for?': "C",
            'What does "IDE" stand for and what is it?': "D",
            'What does "API" stand for and what is it?': "C",
            "Why are objects useful? (Object oriented programming)": "D",
            "What famous computer scientist worked at Bletchley park during world war 2?": "A"
            }

options = [
            ["Floating point numbers are whole numbers with base 10","Floating points are floating values that change randomly","Floating points are numbers that can include decimals","Floating point numbers include only whole numbers"],
            ["Syntax is the order in which the CPU executes a program","Syntax is a youtuber","Syntax is the order in which a programming language is written","Syntax is the arrangement of the transistors in the cpu"],
            ["Yes, because they can be modified without changing their identity","Yes, because they can be converted to different data types","No, because they are primitive data types","No, because once they are created, their value cannot be changed."],
            ["It was the first CPU contained within a single IC","It had the fastest clock speed of any processor at the time","It was the smallest microprocessor available.","It was the first processor to support multitasking"],
            ["Yes, it can compute anything that can be computed, given enough time and memory.","No, because there are some problems that are unsolvable by any computational device","No, because it can only solve problems that can be described by a finite algorithm","Yes, it can compute anything including problems that are inherently uncomputable"],
            ["Personal Computer Binary","Program Control Block","Printed Circuit Board","Process Control Block"],
            ["Integrated Development Editor; a software tool for testing code","Interactive Developer Environment; a collaborative tool for developers","Internal Development Engine; a tool for creating software engines","Integrated Development Environment; a software application that provides comprehensive facilities to programmers for software development"],
            ["Application Programming Instruction; a set of rules for building software applications","Automated Programming Interface; a tool for automating programming tasks","Application Programming Interface; A software intermediary that allows two applications to talk to each other","Application Process Integration; a tool for integrating different software components"],
            ["They allow for faster execution of code","They enable the use of high-level programming languages","They make it easier to write procedural code.","They group related data and functions, enabling abstraction, encapsulation, inheritance, and polymorphism."],
            ["Alan Turing","John von Neumann","Charles Babbage","Grace Hopper"],
           ]


new_game()