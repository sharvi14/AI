import matplotlib.pyplot as plt

# Function to ask questions in a chatbot style
def ask_question(question):
    print(f"Chatbot: {question}")
    response = input("You: ").lower()
    if response in ["yes", "y"]:
        return True
    elif response in ["no", "n"]:
        return False
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Please answer with 'yes' or 'no'.")
        return ask_question(question)

# Chatbot for choosing vacation
def vacation_chatbot():
    print("Chatbot: Hi! I’m your Vacation Expert! Let me help you choose the perfect vacation.")
    print("Chatbot: I'll ask a few questions about your preferences, and I’ll recommend a vacation type based on your answers.")
    
    # Step 1: Chatbot asks questions to gather preferences
    preferences = {
        "Adventure": ask_question("Do you enjoy adventurous activities like hiking or rock climbing?"),
        "Relaxation": ask_question("Are you looking for a relaxing vacation?"),
        "Cultural Experience": ask_question("Are you interested in learning about new cultures or history?"),
        "Beach": ask_question("Do you want to go to the beach?"),
        "City": ask_question("Do you prefer exploring cities with attractions and nightlife?"),
        "Nature": ask_question("Do you prefer being surrounded by nature and scenic views?")
    }
    
    # Count the responses for each preference
    response_count = {key: 1 if value else 0 for key, value in preferences.items()}

    # Step 2: Chatbot gives vacation recommendation based on the user's responses
    print("\nChatbot: Based on your answers, here's my recommendation:")
    if preferences["Adventure"] and preferences["Nature"]:
        print("Chatbot: You should try a Mountain Trekking or Safari Adventure!")
    elif preferences["Relaxation"] and preferences["Beach"]:
        print("Chatbot: A Beach Resort or Island Getaway would be perfect for you!")
    elif preferences["Cultural Experience"]:
        if preferences["City"]:
            print("Chatbot: How about a Historical City Tour in cities like Rome, Paris, or Kyoto?")
        else:
            print("Chatbot: You could enjoy a Cultural Heritage Trip to smaller towns and historical sites.")
    elif preferences["City"]:
        print("Chatbot: You might love exploring cities like New York, Tokyo, or London on a City Tour!")
    elif preferences["Nature"]:
        print("Chatbot: How about a National Park visit or a Scenic Road Trip?")
    else:
        print("Chatbot: A Staycation or Spa Retreat might be the relaxing break you're looking for!")

    # Step 3: Plot preferences as a bar chart to visualize responses
    plot_preferences(response_count)

    print("\nChatbot: I hope you found this helpful! Have a great vacation!")

# Function to plot user's preferences
def plot_preferences(response_count):
    categories = list(response_count.keys())
    responses = list(response_count.values())
    
    plt.bar(categories, responses, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])
    plt.xlabel('Vacation Preferences')
    plt.ylabel('Response (1=Yes, 0=No)')
    plt.title('Your Vacation Preferences')
    plt.ylim(0, 1)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Run the chatbot expert system
if __name__ == "__main__":
    vacation_chatbot()
