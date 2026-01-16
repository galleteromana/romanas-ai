import os
import re
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

try:
    client = InferenceClient(model = "meta-llama/Meta-Llama-3-8B-Instruct", token = HF_TOKEN)
except Exception as e:
    client = None
    print(f"Warning: Error initializing HF client: {e}")

def calculate(expression: str) -> str:
    """
    Evaluates a mathematical expression in natural language.
    Supports basic operations: +, -, *, /, **
    """
    replacements = {
        'plus': '+',                'mais': '+', 
        'minus': '-',               'menos': '-', 
        'times': '*',               'vezes': '*', 
        'divided by': '/',          'dividido por': '/', 
        'multiplied by': '*',       'multiplicado por': '*', 
        'sum of': '+',              'soma de': '+',
        'to the power of': '**',    'elevado a': '**',
        '^': '**'
    }
    expression = expression.lower()
    
    for word, symbol in replacements.items():
        expression = expression.replace(word, symbol)
    
    clean_expression = re.sub(r'[^0-9+\-*/().\s]', '', expression)
    
    try:
        result = eval(clean_expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def is_math_question(user_input: str) -> bool:
    """
    Determines if the user input is a mathematical question.
    Smartly excludes Documents, Phone numbers, and Dates.
    """
    # Exclusion patterns
    patterns = [
        r'\d{3}\.\d{3}\.\d{3}-\d{2}',       # CPF
        r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', # CNPJ
        r'\d{1,2}\.\d{3}\.\d{3}-[\dXx]',    # RG
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',   # Dates
        r'(\(?\d{2}\)?\s?)?9?\d{4,5}-\d{4}' # Phone numbers
    ]
    for pattern in patterns:
        if re.search(pattern, user_input):
            return False
        
    keywords = ['calculate', 'compute', 'plus', 'minus', 'times', 'divided by', 
                'multiplied by', 'sum of', 'calcule', 'compute', 'mais', 'menos', 
                'vezes', 'dividido por', 'multiplicado por', 'soma de', 
                'to the power of', 'elevado a']
    math_pattern = r'(\d+[\s]*[+\-*/%^**]+[\s]*\d+)'
    
    has_math_symbols = bool(re.search(math_pattern, user_input))
    has_keywords = any(keyword in user_input.lower() for keyword in keywords)
    
    return has_math_symbols or has_keywords

def get_ai_response(prompt: str) -> str:
    """
    Gets a response from the LLM for general questions.
    """
    if not client:
        return "Error: AI Client not configured."
    
    try:
        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI model: {str(e)}"