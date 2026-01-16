# Romana's AI Assistant ૮꒰ ˶• ༝ •˶꒱ა
Welcome to my little AI project! This is a smart assistant that can distinguish between mathematical expressions and general conversation. Whether you need to solve an equation or just want to talk, this bunny is ready to help!

## Features
* Shared Brain: The core logic is isolated, powering both the web and terminal apps efficiently.
* Smart Math Mode: Automatically detects math questions (and ignores dates, phone numbers, or IDs) to solve them locally.
* AI Chat Mode: Connects to Meta-Llama-3 via Hugging Face for intelligent conversations when no math is detected.
* Dual Interface:
    * Terminal Mode: For a classic, fast command-line experience.
    * Streamlit Web App: For a beautiful, visual chat interface.

## Project Structure
.

├── logic.py           # Handles API calls, math logic, and regex

├── main.py            # CLI interface for the assistant

├── app.py             # Streamlit interface

└── requirements.txt   # Dependencies

## How to Run
1. Clone the Repository
``` 
git clone https://github.com/galleteromana/romanas-ai.git
cd romanas-ai
```

2. Prepare the Environment: Make sure you have the dependencies installed:
```
pip install -r requirements.txt
```

3. Set up the Secret Token
Create a .env file in the root folder and add your Hugging Face token:
```
HF_TOKEN = your_huggingface_token_here
```

4. Run it:
* Option A: The Terminal Bunny
```
python main.py  
```

* Option B: The Web Bunny
```
streamlit run app.py
```

## Usage Examples
* Math Mode:
    * User: "Calculate 50 times 10 divided by 2"
    * Bunny: "The result is 250.0"

* Chat Mode
    * User: "Tell me a joke about carrots."
    * Bunny: "Why is the carrot the most respected vegetable? Because it's outstanding in its field!"


## Smart Filters
The is_math_question function igmores common non-math numbers, so it won't try to divide your birthday!
* Math: "10 + 10"
* Date: "10/10/2024" (Ignored)
* Phone: "99999-9999" (Ignored)


## Credits
Made with love, Python, and lots of coffee.

Enjoy the AI! ૮ ˶ᵔ ᵕ ᵔ˶ ა
