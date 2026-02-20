import ollama
import pytest
import json
import time

def load_test_data():
    with open('data.json', 'r') as f:
        return json.load(f)

@pytest.mark.parametrize("item", load_test_data())
def test_ai_facts(item):
    question = item['question']
    expected_list = item['expected'] # Teraz je to zoznam ["8", "eight"]
    
    start_time = time.time()
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': f"Answer with one word only: {question}"},
    ])
    
    duration = time.time() - start_time
    # Vyčistíme odpoveď od bodiek a medzier
    answer = response['message']['content'].lower().strip().replace(".", "")
    
    print(f"\nQ: {question} | A: {answer} ({duration:.2f}s)")
    
    # Overíme, či ASPOŇ JEDNO z očakávaných slov je v odpovedi
    success = any(variant in answer for variant in expected_list)
    
    assert success, f"Expected one of {expected_list} but got '{answer}'"