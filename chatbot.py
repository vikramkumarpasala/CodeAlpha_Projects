#!/usr/bin/env python3
"""
Basic Rule-Based Chatbot in Python
----------------------------------
Demonstrates core Python concepts:
- Functions (def)
- Loops (while)
- Conditional Logic (if, elif, else)
- Input and Output (input(), print())
"""

def get_bot_response(user_input):
    """
    Returns a chatbot response based on rules using if-elif statements.
    """
    # Normalize input to lowercase to handle capitalization like 'Hello' or 'BYE'
    cleaned_input = user_input.strip().lower()
    
    if "hello" in cleaned_input or "hi" in cleaned_input:
        return "hi"
    elif "how are you" in cleaned_input:
        return "im fine thanks"
    elif "bye" in cleaned_input:
        return "good bye"
    else:
        return "Sorry, I can only respond to 'hello', 'how are you', or 'bye'."

def chatbot():
    """
    Main function to run the chatbot loop and handle input/output.
    """
    print("========================================")
    print("       Basic Rule-Based Chatbot         ")
    print("========================================")
    print("Talk to the bot! (Try saying: 'hello', 'how are you', or 'bye')\n")
    
    # Loop to keep the chatbot running until the user says 'bye'
    while True:
        # Input from user
        user_message = input("You: ")
        
        # Get response from rule function
        response = get_bot_response(user_message)
        
        # Output response to console
        print(f"Bot: {response}\n")
        
        # Exit loop if the user says bye
        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    chatbot()
