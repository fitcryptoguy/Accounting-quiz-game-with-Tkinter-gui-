from tkinter import *
import random
from creating_dataset import *
import time
questions_already_asked = []

###########################################################################################################################################################
def questions_and_option_generator():
    answer, question = random.choice(list(question_bank_dictionary.items()))
    if question in questions_already_asked:
        pass

    else:
        random_options_generator()
        if answer not in random_options_that_are_generated:
            random_options_that_are_generated[random.randint(0, 3)] = answer

        question_label.config(text=f"{question}")
        questions_already_asked.append(question)
        option1.config(text=random_options_that_are_generated[0])
        option2.config(text=random_options_that_are_generated[1])
        option3.config(text=random_options_that_are_generated[2])
        option4.config(text=random_options_that_are_generated[3])
        sumbit_button.config(text="Submit")

    # radio_selection = radio_state.get()
    #
    # if radio_selection == random_key_list.index(key):
    #     sumbit_button.config(text="correct", bg="green")
    # print(radio_selection)
    # print(random_key_list.index(key))


##############################################################################################################################################
def cheater():
    current_question = question_label["text"]

    current_answer = list(question_bank_dictionary.keys())[list(question_bank_dictionary.values()).index(current_question)]
    cheat_button.config(text=current_answer)
    window.after(3000, change_back_cheat_button)


def change_back_cheat_button():
    cheat_button.config(text="Cheat Button")


def counter(seconds, minutes):
    if sumbit_button["text"] == "Submit":
        if seconds < 60:
            time_label.config(text=f"Timer {seconds}")
        else:
            minutes = int(seconds / 60)
            secundu = seconds % 60
            time_label.config(text=f"Timer {minutes}:{secundu}")

        window.after(1000, counter, seconds + 1, minutes)


###############################################################################################################################################################
#                                          LAYOUT START
my_font = ("Arial", 24, "bold")
window = Tk()
window.title("Guessing Game")
window.minsize(width=600, height=600)

heading_label = Label(text="Indian Accounting Standard", background="green", font=my_font)
heading_label.pack(padx=40, pady=40)

question_label = Label(text="Welcome To The Test", font=("Arial", 17, "bold"))
question_label.pack(padx=30, pady=30)

time_label = Label(text="Timer", font=("Arial", 17, "bold"))
time_label.pack(side="bottom", padx=10, pady=20)

radio_state = IntVar()
option1 = Radiobutton(text="Option A", value=0, variable=radio_state, font=("Arial", 13, "bold"))
option1.pack(padx=10, pady=10)
option2 = Radiobutton(text="Option B", value=1, variable=radio_state, font=("Arial", 13, "bold"))
option2.pack(padx=10, pady=10)
option3 = Radiobutton(text="Option 3", value=2, variable=radio_state, font=("Arial", 13, "bold"))
option3.pack(padx=10, pady=10)
option4 = Radiobutton(text="Option 4", value=3, variable=radio_state, font=("Arial", 13, "bold"))
option4.pack(padx=10, pady=10)
sumbit_button = Button(text="Let's start", command=questions_and_option_generator, font=("Arial", 13))
sumbit_button.pack(pady=20, padx=15)
cheat_button = Button(text="Cheat Button", font=("Arial", 13), bg="red", command=cheater)
cheat_button.pack()
counter(0, 0)
window.mainloop()
