import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Retrieve the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")
client = None

if api_key:
    client = OpenAI(api_key=api_key)

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and return bot response"""
    try:
        if not client:
            return jsonify({'error': 'OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable.'}), 500
            
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Call OpenAI API using the existing fine-tuned model
        response = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-0125:personal::BZnAK2Ts",
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=0.9,
            frequency_penalty=0.5,    
            presence_penalty=0.3  
        )
        
        bot_response = response.choices[0].message.content.strip()
        
        return jsonify({'response': bot_response})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)