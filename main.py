jokes = [
    ["robbers", "Calder police — I've been robbed!"], # Lists of lines used in joke picked
    ["tanks", "You're welcome!"],                     
    ["pencils", "Never mind — it's pointless!"]
]
def tell_joke(topic, punchline): # A paramter which stores and empty value that can be changed later
    input("Knock knock!  ") # Allows user to input a response
    input(topic.capitalize()) # Makes joke begin with an uppercased letter
    print(punchline)
def find_joke(choice): # 
    for joke in jokes:
        if joke[0] == choice:
            return joke
    return None
def run_joke():
    play = input("Do you want to hear a joke? ").lower().strip()
    while play == "yes":
        choice = input("Choose a joke (robbers, tanks, pencils): ").lower().strip()
        joke = find_joke(choice)
        if joke:
            tell_joke(joke[0], joke[1])
        else:
            print("That joke does not exist.")
            add = input("Do you want to add your own joke? (yes or no): ").lower().strip()
            if add == "yes":
                new_topic = input("Enter a joke topic: ").lower().strip()
                new_punchline = input("Enter the punchline: ")
                jokes.append([new_topic, new_punchline])
                print("Your joke was added!")
        play = input("Do you want to hear another joke? (yes or no): ").lower().strip()
    print("Thanks for playing!")
run_joke()