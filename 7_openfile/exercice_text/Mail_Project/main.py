NAME_TO_REPLACE = "[name]"

with open("./Input/Names/invited_names.txt","r") as names_files:
    names = names_files.readlines()

with open("./Input/Letters/starting_letter.txt","r") as letters_files:
    letters = letters_files.read()
    for name in names:
        stripped_names = name.strip()
        new_letters = letters.replace(NAME_TO_REPLACE,stripped_names)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}","w") as final_letters:
            final_letters.write(new_letters)
