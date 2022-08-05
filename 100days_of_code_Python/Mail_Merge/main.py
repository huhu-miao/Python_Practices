# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    

name_list = []
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        name_list.append(name.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as start:
    greeting = start.read()
    for name in name_list:
        new_letter = greeting.replace("[name]", f"{name}")
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)




