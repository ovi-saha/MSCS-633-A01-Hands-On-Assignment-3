# Import the chatbot instance from the bot.py file
from bot import chatbot

# Function to start the terminal-based chat
def start_chat():
    # Display initial greeting message from the bot
    print("TerminalBot: Hello! I am your chatbot. Type 'exit' to end the conversation.")
    
    # Start an infinite loop to keep the chat going until the user types 'exit'
    while True:
        # Take user input from the terminal
        user_input = input("You: ")
        
        # Check if the user wants to exit the chat
        if user_input.lower() == 'exit':
            # Print goodbye message and break the loop to end the chat
            print("TerminalBot: Goodbye!")
            break
        
        # Get the chatbot's response to the user's message
        response = chatbot.get_response(user_input)
        
        # Display the chatbot's response
        print(f"TerminalBot: {response}")

