#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Gets names from invited_names.txt and puts them in a list.
names = open("./Input/Names/invited_names.txt", "r")
invited_names = names.readlines()

for name in invited_names:
    name = name.strip()
    # replaces [name] placeholder
    with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
        template = starting_letter.read()
        ready_to_send = template.replace("[name]", f"{name}")
        print(ready_to_send)
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as ready:
        ready.write(f"{ready_to_send}")