jokes = ["Robbers", "Calder police ive been robbed!",],
["tanks", "Youre welcome"],
["pencil", "Nevermind its pointless!"]

def tell_joke(topic, punchline): 
    input("Knock knock")
    input(topic.capitalize()) # Topic of the joke 
    print(punchline) # Signifies the joke is ending 
def find_joke(choice):
    for joke in jokes:
        if jokes[0] == choice:
            return joke 
        return None
play = input("Do you want to hear a joke?")

while play == "yes":
    choice = input("Choose a joke: Robbers, Tanks, or Pencils: ")
    joke = find_joke(choice)
    if joke:
        tell_joke(joke[0],joke[1])
    else: 
        print("That joke doesnt exist")
    
    play = input("Do you want to hear another joke or are you finished?:  ")

    print("Thanks for hearing our jokes!")

    # This function tells people the knock knock joke
if joke == "finished":
    rate = int(input("Please rate our game 1-10! "))
    final_score = int(rate * 10)
    print(str(final_score) + " percent satisfaction rate")
    friend = input("Would you recommend this game to a friend? ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it. ")
    else:
        print("Sorry you did not enjoy it. ")