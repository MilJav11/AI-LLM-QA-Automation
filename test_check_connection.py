import ollama
import sys

def check_ai_status():
    """Checks the connection between Python and the local Ollama server."""
    print("Checking system status...")
    print(f"Python version: {sys.version}")
    
    try:
        # Simple request to verify the bridge
        response = ollama.chat(model='llama3.2:1b', messages=[
            {
                'role': 'user',
                'content': 'Say "Connection successful" in one sentence.',
            },
        ])

        print("\n--- AI DIAGNOSTIC OUTPUT ---")
        print(response['message']['content'].strip())
        print("-----------------------------\n")
        print("SUCCESS: Python can communicate with Ollama.")
        
    except Exception as e:
        print(f"ERROR: Connection failed. Details: {e}")
        print("Make sure Ollama is running in your system tray.")

if __name__ == "__main__":
    check_ai_status()