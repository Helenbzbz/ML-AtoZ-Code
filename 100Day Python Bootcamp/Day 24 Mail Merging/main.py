#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("100Day Python Bootcamp/Day 24 Mail Merging/Input/Names/invited_names.txt") as names:
    name_content  = names.read()
    name_list = name_content.split("\n")

with open("100Day Python Bootcamp/Day 24 Mail Merging/Input/Letters/starting_letter.txt") as template:
    template_lines = template.readlines()

for name in name_list:
    new_letter = template_lines
    new_first_line = f"Dear {name},\n"
    new_letter[0] = new_first_line
    with open(f'100Day Python Bootcamp/Day 24 Mail Merging/Output/ReadyToSend/{name}.txt', 'x') as f:
        f.write("".join(new_letter))