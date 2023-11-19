
# from chatterbot.trainers import ListTrainer
# from chatterbot import ChatBot
# chatbot = ChatBot("New_Bot")
# conversation = [
#     "Hello",
#     "Hi, there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "how can i help you?",
#     "Thank you.",
#     "You're welcome.",
#     "Recommend me a sports car",
#     "Do you need a family sports car, or a sports car for fun",
#     "Family Car",
#     "BMW X7 M sport",
#     "Fun",
#     "BMW M5 COMP CLS"
# ]

# trainer = ListTrainer(chatbot)

# trainer.train(conversation)

# print("enter 'quit' to stop")
# while True:
#     text_input=input("You: ")
#     if text_input == 'quit':
#         break
#     print("Bot: ",chatbot.get_response(text_input))
def chatbot_response(user_input):
    greetings = ["hi", "hello", "hey", "howdy"]
    farewells = ["bye", "goodbye", "see you", "take care"]
    user_input = user_input.lower()
    if user_input in greetings:
        return "Hello! How can I assist you?"
    elif user_input in farewells:
        return "Goodbye! Have a great day!"
    else:
        return "I'm just a simple chatbot and I'm not sure how to respond to that."
print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a nice day.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
