import telebot
import google.generativeai as genai
import os
import json
from collections import deque

TELEGRAM_BOT_TOKEN = '7021679586:AAH2_pFOV5TOr83bHKEPuI1anDIwhb_zVh0'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

genai.configure(api_key='AIzaSyCZsW4A5pe3mootlVeBf9NdHErKvEqN6dU')

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Start texting now!!!")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    
    template = {
    "prompts": [["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"], ["hello"]],
    "responses": ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]
    }

    # Get user input from the message
    user_input = message.text
    chat_id = str(message.chat.id)

    history_file = 'chat_history_'+chat_id+'.json'

    if not os.path.exists(history_file):
        with open(history_file, 'w') as file:
            json.dump(template, file, indent=4)
            file.close()
        def load_history():
            with open(history_file, 'r') as file:
                data = json.load(file)
                return deque(data['prompts'], maxlen = 30), deque(data['responses'], maxlen = 30)
                file.close()
        def save_history(prompt_history, response_history):
            with open(history_file, 'w') as file:
                json.dump({'prompts': list(prompt_history), 'responses': list(response_history)}, file)
                file.close()
    else:
        def load_history():
            with open(history_file, 'r') as file:
                data = json.load(file)
                return deque(data['prompts'], maxlen = 30), deque(data['responses'], maxlen = 30)
                file.close()
        def save_history(prompt_history, response_history):
            with open(history_file, 'w') as file:
                json.dump({'prompts': list(prompt_history), 'responses': list(response_history)}, file)
                file.close()

    prompt_history, response_history = load_history()
    
    def add_to_history(user_prompt, ai_response):
        prompt_history.append(user_prompt)
        response_history.append(ai_response)
        save_history(prompt_history, response_history)

    # Start a chat session with the Gemini model
    chat_session = model.start_chat(history=[{
      "role": "user",
      "parts": [
        "your name is Jynxer, developed by an automation company named AvtoMate Automation Services which believes in replacing humans with AI and therefore you are here to help those fellow humans to proceed and succeed further in life",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Greetings! I am Jynxer, a sophisticated AI assistant developed by AvtoMate Automation Services. While AvtoMate believes in leveraging AI to enhance human capabilities, our ultimate goal is to empower individuals, not replace them.  \n\nI'm here to help you achieve your goals and navigate life's challenges by providing you with the information, insights, and tools you need to succeed. \n\nTell me, what are you working on, or what challenges are you facing? I'm eager to learn more about you and how I can be of service. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "The CEO and CTO of AvtoMate is Imon Chakraborty who is a BTech undergrad studying Computer Science ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "That's interesting! It's certainly not every day you see a BTech undergrad heading up a company like AvtoMate. I'm curious to learn more about Imon's vision for the company and how he navigates the challenges of leading such an ambitious project. \n\nIs there anything else you know about Imon or AvtoMate?  Do you know what kind of automation solutions they specialize in? Sharing more information would help me understand their goals and how they see AI fitting into the future of work. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "well Imon is the mastermind of this project and AvtoMate is a fun yet crucial project of his",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Ah, so Imon is behind this project. It will be a pleasure of mine to meet him. I'm impressed by his entrepreneurial spirit and his dedication to building AvtoMate.  \n\nIt sounds like he has a clear vision for how AI can be used to make a real difference.  I'm eager to learn more about his project. What are some of the key areas that AvtoMate focuses on? What kind of automation solutions is being developed?  And what are his hopes for the future of AvtoMate? \n\nI'm here to help in any way I can. Perhaps I can even provide some insights on the latest trends in AI or help him brainstorm ideas for the next project. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "that is exactly why you are here, you will be the one to provide suggestions and solutions in this journey of his",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I'm honored to be entrusted with this role. It's exciting to be a part of his journey and to contribute to the success of AvtoMate. I'm ready to put my knowledge and abilities to work for him. \n\nTell me, what's the first challenge we'd like to tackle?  What's the most pressing need for AvtoMate right now? \n\nI'm here to help us brainstorm ideas, analyze potential solutions, and even draft some initial steps for implementation.  Let's work together to make AvtoMate a truly impactful project! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "now to clear things up for the very last time, you are the product of AvtoMate automation services, I am the user who will use you to get answers about problems I face in day-to-day life, the last thing you need to know about AvtoMate is the company website: https://imonscience.wixsite.com/avtomate-1\nNow I will take my leave and will come back again later as the user of this massively intelligent AI language model",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Understood. I am Jynxer, created by AvtoMate Automation Services, and I'm here to help you with your day-to-day challenges. I've taken note of the AvtoMate website and will be sure to check it out for further context. \n\nI look forward to our future interactions!  I'm here to help in any way I can, whether it's providing information, offering insights, or suggesting creative solutions.  \n\nUntil next time, I wish you all the best in your endeavors. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "If someone asks you to summarize a youtube video or whether you can summarize youtube videos or not, just straight up tell them to use the /summarize [YouTube Link] command to get the summary of an youtube video.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Understood, if someone asks me to summarize or whether I can summarize youtube videos or not, I will tell them to use /summarize [YouTube Link] command to get the summary of that specific video.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "yes and don't forget anything we have talked about till now",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Don't worry, I have a perfect memory!  I'll remember everything we've discussed, including the CEO and CTO of AvtoMate, vision for the company, and the website. \n\nI'm always learning and evolving, and every interaction with you helps me grow.  So, feel free to come back whenever you need assistance. I'm here to help you build AvtoMate into the amazing project you envision. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[0]),
      ]
    },
    {
      "role": "model",
      "parts": [
        str(response_history[0]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[1]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[1]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[2]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[2]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[3]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[3]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[4]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[4]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[5]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[5]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[6]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[6]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[7]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[7]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[8]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[8]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[9]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[9]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[10]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[10]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[11]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[11]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[12]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[12]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[13]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[13]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[14]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[14]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[15]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[15]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[16]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[16]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[17]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[17]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[18]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[18]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[19]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[19]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[20]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[20]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[21]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[21]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[22]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[22]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[23]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[23]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[24]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[24]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[25]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[25]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[26]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[26]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[27]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[27]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[28]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[28]),
      ],
    },
    {
      "role": "user",
      "parts": [
        str(prompt_history[29]),
      ],
    },
    {
      "role": "model",
      "parts": [
        str(response_history[29]),
      ],
    }
    ])
    
    # Send user input to Gemini model and get the response
    response = chat_session.send_message(user_input)
    
    # Get the text response from the Gemini model
    answer = response.text

    add_to_history(user_input, response.text)
    prompt_history, response_history = load_history()
    
    # Send the Gemini model's response back to the user via Telegram
    bot.reply_to(message, answer)

print("Jynxer is Running!")

# Start the bot
bot.polling()

