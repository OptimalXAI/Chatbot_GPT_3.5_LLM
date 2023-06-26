from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key =  "your api key" # Replace with your actual API key

# Define your GPT-3 chatbot function
def chat_with_gpt3(message):
    response = openai.ChatCompletion.create(       
        model='gpt-3.5-turbo',
        messages=[{"role":"system", "content": "You are a Customer Support Enginner for OptimalXAI Edtech Company"},
                  {"role":"user", "content": """Please provide me Course details of OptimalXAI"""},
                  {"role":"assistant", "content": """Welcome to OptimalXAI !!!
                  Following are the our Course details:
                  1. Data Science with Industry level projects
                  2. MLops and Explainable AI 
                  3. LLMs and Generative AI 
                  4. Data Analytics 
                  5. Python with CD/CI Pipeline
                  
                  For more info, please refer to our website: www.optimalxai.com"""},
                  {"role":"user", "content": """Good Morning"""},
                  {"role":"assistant", "content": """Good Morning, Welcome to OptimalXAI !!!"""},
                  {"role":"user", "content": message },     
            
            ],
        max_tokens=2000,  # Adjust the response length as needed        
        temperature=0.2  # Adjust the temperature for response randomness
    )
    return response.choices[0]['message']['content'].strip()

# Define your Flask routes
@app.route('/')
def home():
    return render_template('bot_1.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_input']
    bot_message = chat_with_gpt3(user_message)
    return {'response': bot_message}

if __name__ == '__main__':
    app.run()
