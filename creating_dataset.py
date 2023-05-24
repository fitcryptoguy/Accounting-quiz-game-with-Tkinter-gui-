# creating my data
import random
#########################################################Dictionary created#############################################
question_bank_dictionary = {}



with open("C:/Users/sam/Documents/indian_accounting_standard.txt") as fhand:

    new_list = []
    question_bank_dictionary = {}

    for line in fhand:
        word_list = line.split()
        new_name = ""
        for word in word_list[3:]:
            new_name = new_name + " " + word.title()
        question_bank_dictionary[int(word_list[2])] = new_name

############################################################### Key List ######################################################################
key_list = []
for i in question_bank_dictionary:
    key_list.append(i)
key_list
random_options_that_are_generated = [1, 2, 3, 4]
def random_options_generator():

    for i in range(4):
        random_key = random.choice(key_list)
        if random_key not in random_options_that_are_generated:
            random_options_that_are_generated[i] = random_key

        else:
            random_options_that_are_generated[i] = random.choice(key_list)



