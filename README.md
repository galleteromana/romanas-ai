# Romana's AI Assistant ૮꒰ ˶• ༝ •˶꒱ა
Welcome to my little AI project! This is a smart assistant that can distinguish between mathematical expressions and general conversation. Whether you need to solve an equation or just want to talk, this bunny is ready to help!

## Features
* Shared Brain: the core logic is isolated, powering both the web and terminal apps efficiently.
* Smart Math Mode: automatically detects math questions (and ignores dates, phone numbers or IDs) to solve them locally.
* AI Chat Mode: connects to Meta-Llama-3 via Hugging Face for conversations when no math is detected.
* Dual Interface:
    * Terminal Mode: for a classic command-line experience.
    * Streamlit Web App: for a visual chat interface.

## Project Structure
* ```logic.py```: handles API calls and math logic.
* ```main.py```: terminal interface for the assistant.
* ```app.py```: Streamlit interface.
* ```requirements.txt```: dependencies.

## Implementation Logic
The application relies on a shared brain, located in ```logic.py```, which allows both the Terminal and Web interfaces to behave identically.

### The Decision Engine ```is_math_question```
Before calling the API, the application needs to determine the user's intent. It is made by the use of a Two-Pass Filter strategy:

* **Negative Filtering:** the system first checks for patterns that look like math but aren't. By using regular expressions it's possible to ignore:
    * Dates: 12/12/2024..
    * IDs (CPF/CNPJ/RG).
    * Phone Numbers: (11) 91234-5678. 
If any of these are found, the function immediately returns False to prevent the calculator from trying to "divide" a date.

* **Positive Identification:** if the input survives the negative filter, it is checked for actual math signals:
    * Keyword Matching: checks for natural language terms in English and Portuguese (e.g., "calculate", "sum of", "vezes", "elevado a").
    * Symbol Pattern Matching: Uses Regex to find numerical operations (e.g., \d+[\s]*[+\-*/%^**]) to detect raw equations.


### The Natural Language Calculator ```calculate```
If the decision engine flags the input as math, the request is processed locally without external APIs.

* **Mapping:** the function maps natural language words to Python operators. It iterates through a dictionary to replace "plus" with +, "minus" with -, "times" with *, "divided by" with /, and "^" with **.

* **Sanitization:** security is prioritized by stripping all characters that are not numbers or operators. The Regex [^0-9+\-*/().\s] ensures that no malicious code can be passed to the evaluator.

* **Evaluation:** the cleaned expression is safely computed using Python's ```eval()``` function and the result is returned as a string.

### The AI Integration ```get_ai_response```
If the input is not math, it is routed to the Large Language Model.

* **Client Connection:** the app uses the ```InferenceClient``` from the ```huggingface_hub``` library, authenticated via the ```HF_TOKEN``` environment variable.

* **Model Specification:** requests are sent to Meta-Llama-3-8B-Instruct, a open-source model for chat instructions.

* **Error Handling:** the function includes a ```try-except``` block to catch connection errors (e.g., invalid tokens or network issues) and return a user-friendly error message instead of crashing the application.

## How to Run
1. Clone the Repository
``` 
git clone https://github.com/galleteromana/romanas-ai.git
cd romanas-ai
```

2. Prepare the Environment:
```
pip install -r requirements.txt
```

3. Set up the Token: 
Create a .env file in the root folder and add your Hugging Face token:
```
HF_TOKEN = replace_with_your_huggingface_token
```

4. Run it:
* Option A: the Terminal Bunny
```
python main.py  
```

* Option B: the Web Bunny
```
streamlit run app.py
```

## Usage Examples
* Math Mode:
    * User: Calculate 50 times 10 divided by 2
    * Bunny: The result is 250.0.

* Chat Mode
    * User: Tell me a joke about carrots.
    * Bunny: Why is the carrot the most respected vegetable? Because it's outstanding in its field!


## Smart Filters
The ```is_math_question``` function igmores common non-math numbers, so it won't try to divide your birthday!
* Math: "10 + 10"
* Date: "10/10/2024" (Ignored)
* Phone: "99999-9999" (Ignored)


## Credits
Made with love, Python, and lots of coffee.

Enjoy the AI! ૮ ˶ᵔ ᵕ ᵔ˶ ა
