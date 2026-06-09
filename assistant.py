import datetime

def simple_ai_assistant():
    print("AI Assistant: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Greetings
        if user_input in ['hi', 'hello', 'hey']:
            print("AI Assistant: Hey there! How can I help you today?")
        
        # Weather inquiry
        elif 'weather' in user_input:
            print("AI Assistant: It's currently sunny and 28°C. Perfect weather to code outside!")
            # Note: This is mocked. Real weather needs an API like OpenWeatherMap
        
        # Time inquiry
        elif 'time' in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print(f"AI Assistant: It's {current_time} on {current_date}")
        
        # Goodbye message
        elif user_input in ['bye', 'goodbye', 'exit', 'quit']:
            print("AI Assistant: Goodbye! Have a great day coding!")
            break
        
        # Unknown input
        else:
            print("AI Assistant: I can help with greetings, weather, and time. Try asking 'what's the time?'")

if __name__ == "__main__":
    simple_ai_assistant()
