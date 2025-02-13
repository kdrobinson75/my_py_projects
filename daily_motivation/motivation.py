import requests
import random

# Function to fetch a random motivational quote from ZenQuotes API
def get_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]  # API returns a list
        quote = data["q"]  # The quote text
        author = data["a"]  # The author
        return f'"{quote}" - {author}'
    else:
        return "Error fetching quote."

# Function to get a random daily affirmation
def get_affirmation():
    affirmations = [
        "I am confident and capable.",
        "I radiate positivity and joy.",
        "I believe in myself and my abilities.",
        "I attract success and abundance.",
        "I am enough just as I am.",
        "Every day is a fresh start.",
        "I am worthy of love and respect."
    ]
    return random.choice(affirmations)

# Main program to let user choose
if __name__ == "__main__":
    print("🌟 Welcome to the Daily Motivation App! 🌟")
    print("1: Get a Motivational Quote")
    print("2: Get a Daily Affirmation")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        print(get_quote())
    elif choice == "2":
        print(get_affirmation())
    else:
        print("Invalid choice! Please select 1 or 2.")
