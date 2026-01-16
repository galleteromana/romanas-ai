import logic 

def assistant(user_input: str):
    """
    Logic to decide if the reply will use LLM or calculator.
    Uses functions imported from logic.py
    """
    if logic.is_math_question(user_input):
        result = logic.calculate(user_input)
        print(f"૮꒰˶ᵔ ᵕ ᵔ˶꒱ა    The result is {result}.\n")
    else:
        response = logic.get_ai_response(user_input)
        print(f"૮꒰˶ᵔ ᵕ ᵔ˶꒱ა    {response}\n")

if __name__ == "__main__":
    print("~~~ Welcome to Romana's AI Assistant and Calculator! ૮꒰˶• ༝ •˶꒱ა ~~~")
    print("Type 'sair' or 'exit' to finish the program.\n")
    
    if not logic.HF_TOKEN:
         print("Error: HF_TOKEN not found. Verify .env file.")

    while True:
        try:
            query = input(">> ")
            if query.lower() in ['sair', 'exit', 'quit']:
                print("Bye bye!")
                break
            if not query.strip():
                continue
            assistant(query)
            
        except KeyboardInterrupt:
            print("\nClosing...")
            break