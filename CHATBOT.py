def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a computer program, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure how to respond to that. Can you ask me something else?"
    }
    
    # Convert user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()
    
    # Check if the user input matches any predefined responses
    for key in responses:
        if key in user_input_lower:
            return responses[key]
    
    # If no match, return the default response
    return responses["default"]

def main():
    print("Welcome to the ChatBot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # Check for exit condition
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        
        # Get the chatbot's response
        response = get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
