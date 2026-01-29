import random

default_subject = [
    "Virat kohli",
    "Prime Minister Modi Ji",
    "Nirmala SitaRaman",
    "Micheal",
    "Oliviya",
    "Oggy",
    "Jack",
    "Bob",
    "Yogi Ji"
]

default_action = [
    "launches",
    "dance with",
    "playing",
    "running",
    "cycling",
    "riding",
    "climbing",
    "declare's war on",
    "eat",
    "celebrates"
]

default_place_or_thing = [
    "at red fort",
    "in mumbai local train",
    "at Ganga Ghat",
    "inside Parliament",
    "at tapri",
    "during IPL match",
    "plate of samosa"
]

print("WELCOME TO FAKE NEWS HEADLINE GENERATOR!")

# Get user input for subject, action, and place/thing
while True:
    print("\nPlease provide the following information to generate headlines:")
    print("(Press Enter without input to use random selection)")

    user_subject = input("\nEnter Subject (person/entity): ").strip()
    user_action = input("Enter Action (verb): ").strip()
    user_place = input("Enter Place/Thing: ").strip()

    # Check if user provided at least one input, otherwise ask again
    if not user_subject and not user_action and not user_place:
        print("\n No input provided. Please provide at least one field!\n")
        continue
    break

# Use user input if provided, otherwise use default random selection
subject = [user_subject] if user_subject else default_subject
action = [user_action] if user_action else default_action
place_or_thing = [user_place] if user_place else default_place_or_thing

headlines = []

while True:
    selected_subject = random.choice(subject)
    selected_action = random.choice(action)
    selected_place = random.choice(place_or_thing)
    fack_news = f"BREAKING NEWS: {selected_subject} {selected_action} {selected_place}"
    print("\n" + fack_news)
    headlines.append(fack_news)
    
    user_input = input("\nDo You Want Another Headline? (Yes/No): ").strip().lower()
    if user_input == "no":
        break

# Ask user if they want to save headlines to file
save_choice = input("\n\nDo You Want To Save These Headlines In A Text File? (Yes/No): ").strip().lower()

if save_choice == "yes":
    filename = input("Enter filename (without .txt extension): ").strip()
    if filename:
        try:
            with open(f"{filename}.txt", "w") as file:
                for headline in headlines:
                    file.write(headline + "\n")
            print(f"Headlines saved successfully to '{filename}.txt'")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("Headlines not saved.")
        continue_gen = input("\nDo You Want To Continue Generating? (Yes/No): ").strip().lower()
        if continue_gen == "yes":
            print("Restarting headline generation...")
        else:
            print("Thank You For Using Fake-News Headline Generator!")
            exit()
else:
    continue_gen = input("\nDo You Want To Continue Generating? (Yes/No): ").strip().lower()
    if continue_gen == "yes":
        print("Restarting headline generation...")
    else:
        print("\nThank You For Using Fake-News Headline Generator!")
        exit()

print("Thank You For Using Fake-News Headline Generator!")
