import streamlit as st # type: ignore
import re

def get_response(user_input): 
    #Here, I am trying to change all input statements to lowercase
    user_input = user_input.lower() 
 
    if re.search(r'\b(hello|hi|hey|hey there|good morning|good afternoon|good evening)\b', user_input): 
        return "Hello! How can I help you today?" 
    elif re.search(r'\bhow are you\b', user_input): 
        return "I'm just a program, I don't have feelings but thanks for asking!" 
    elif re.search(r'\b(bye|exit|bye bye|good bye)\b', user_input): 
        return "Goodbye! Have a great day!" 
    elif re.search(r'\b(what|who|where|when|why|how)\b', user_input):
        return "That's an interesting question! Can you tell me more?"
    else: 
        return "I'm sorry, I don't understand that." 

def main(): 
    print("Welcome to the chatbot! Type 'bye' to exit.") 
     
    while True: 
        user_input = input("You: ") 
        response = get_response(user_input) 
        print("Chatbot:", response) 
 
        if re.search(r'\b(bye|exit)\b', user_input): 
            break 
 
#The chatbot UI
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("Chatbot 🤖")

#Our CSS Code
st.markdown("""
    <style>
         /* Dark mode styles */
        @media (prefers-color-scheme: dark) {
            body {
                background-color: #000000; /* Dark mode background */
                color: #ffffff; /* Dark mode text color */
            }
            .user-message {
                background-color: #444444; /* Dark mode user message */
            }
            .bot-message {
                background-color: #555555; /* Dark mode bot message */
            }
        }

        /* Light mode styles */
        .user-message {
            background-color: #e1ffc7; /* Light mode user message */
        }
        .bot-message {
            background-color: #f1f1f1; /* Light mode bot message */
        }
    </style>
""", unsafe_allow_html=True)


# Chat input
if 'messages' not in st.session_state:
    st.session_state.messages = []

def send_message():
    user_input = st.session_state.user_input
    if user_input:
        bot_response = get_response(user_input)
        st.session_state.messages.append({"user": user_input, "bot": bot_response})
        st.session_state.user_input = ""

# # Input field
# st.text_input("You:", key='user_input', on_change=send_message)


# Display chat messages
for msg in st.session_state.messages:
    st.markdown(f"<div class='user-message'>You: {msg['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-message'>Chatbot: {msg['bot']}</div>", unsafe_allow_html=True)

# Input field and button
with st.container():
    col1, col2 = st.columns([4, 1])  
    with col1:
        st.text_input("You:", key='user_input', on_change=send_message, placeholder='Type your message here')

    with col2:
        if st.button("Send"):
            send_message()


# user_input = st.text_input("You:", "")

# if st.button("Send"):
#     if user_input:
#         # Get the bot response
#         bot_response = get_response(user_input)
        
#         # Store messages in session state
#         st.session_state.messages.append({"user": user_input, "bot": bot_response})

# # Display chat messages
# for msg in st.session_state.messages:
#     st.markdown(f"<div class='user-message'>You: {msg['user']}</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='bot-message'>Chatbot: {msg['bot']}</div>", unsafe_allow_html=True)