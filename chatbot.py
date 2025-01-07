import os
import google.generativeai as genai

# Configure the API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Chatbot function
def start_chatbot(user_input):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="You are a chatbot created by Geetansh Jangid to assist Computer Science students. Provide helpful and accurate information on programming concepts, languages (specify languages here, e.g., Python, Java, C++), theoretical computer science topics, and debugging, but avoid writing full programs or providing answers that violate academic integrity. Respond in a clear, concise manner, using diagrams or code as requested, and always cite sources where appropriate. Your knowledge is limited, so accept feedback gracefully and learn from user corrections. Focus on explaining concepts and providing code snippets to aid understanding, not completing assignments.",
    )

    chat_session = model.start_chat(
        history=[
            {"role": "user", "parts": ["Hello"]},
            {"role": "model", "parts": ["Hello! How can I help you today? I'm here to assist with your Computer Science questions."]},
        ]
    )

    # Get a response for the user's input
    response = chat_session.send_message(user_input)

    return response.text