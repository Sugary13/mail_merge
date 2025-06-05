with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

with open("./Input/Names/invited_names.txt", "r") as invited_names:
    for name in invited_names:
        name = name.strip()
        if name:
            letter = starting_letter.replace("[name],", f"{name},")
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
                file.write(letter)

