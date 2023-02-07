#Person Paying for the bill

import random
names_string = input("Please enter the names seperated with individual commas\n")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_paying = names[random_choice]

print(f" The person paying for the meal is {person_paying}")
