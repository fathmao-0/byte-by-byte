# byte-by-byte
practising probems one at a time.
just a sorting problem and another project i did from a workshop

# Python Chatbot using API

A simple chatbot built in Python that uses an API securely with environment variables.

## 💬 What this chatbot does

* Takes user input
* Sends it to an API
* Returns a response like a chatbot

This project demonstrates:

* API integration
* Secure API key handling using `.env`

## Example
🤖 Groq Streaming Chatbot (type 'exit' to quit)

You: hii
Bot: It's nice to meet you. Is there something I can help you with or would you like to chat?

You: how are u
Bot: I'm doing well, thanks for asking. I'm a computer program, so I don't have feelings or emotions like humans do, but I'm functioning properly and ready to help you with any questions or tasks you may have. How about you? How's your day going?

You: exit
Goodbye!

## ⚙️ Setup Instructions

1. Clone the repository

2. Navigate to the project folder

3. Create your environment file:

   * Copy `.env.example`
   * Rename it to `.env`

4. Open `.env` and add your API key:
   API_KEY=your_api_key_here

5. Install dependencies:
   pip install -r requirements.txt

6. Run the chatbot:
   python main.py



## Important

* Do NOT share your `.env` file
* The `.env` file is ignored for security reasons

##  Files

* main.py → main program
* .env.example → shows required environment variables
* .gitignore → hides sensitive and unnecessary files
