import ollama
import pytest

def test_check_grass_color():
    """Test if the AI correctly identifies the color of grass."""
    
    prompt = "What is the typical color of healthy grass? Answer with one word only."
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': prompt},
    ])
    
    answer = response['message']['content'].strip().lower()
    
    print(f"\nAI Response: {answer}")
    
    # Profesionálny QA assertion
    assert "green" in answer