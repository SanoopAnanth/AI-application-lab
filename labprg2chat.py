def ChatBot(user_input):
    greeting=["hi","hello","howdy","bonjour","hey"]
    farewell=["bye","good bye","see you","take care"]
    if user_input in greeting:
        return("Hello, how can i help you")
    elif(user_input in farewell):
        return("Bye, it was nice to help you")
    else:
        return("Sorry, i'm just a simple chatbot.I'm not trained with that")
print("I'm a simple chat bot, type bye to exit")
while True:
    user_input=input("You: ").lower()
    if user_input == 'bye':
        print("ChatBot: Bye, Have a nice day")
        break
    response=ChatBot(user_input)
    print(response)
