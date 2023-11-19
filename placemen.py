from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot("CarRecommendationBot",
               logic_adaptor=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdaptor',
        'chatterbot.lofic.BestMatch',
        {
            'import_path':'chatterbot.logic.BestMatch',
            'default_response':'I am Sorry, I do not understand',
            'maximun_similarity_threshold':0.80
        }
    ])
bot.storage.drop()
trainer = ListTrainer(bot)
trainercorpus=ChatterBotCorpusTrainer(bot)
with open("auto.json", "r") as file:
    data = json.load(file)
for item in data:
    input_text = item["input"]
    output_text = item["output"]
    if isinstance(output_text, dict):
        recommendations = output_text["recommendations"]
        for recommendation in recommendations:
            response = f"{recommendation['make']} {recommendation['model']}:\n"
            response += f"Price: {recommendation['price']}\n"
            response += f"KMPL: {recommendation['KMPL']['city']} city / {recommendation['KMPL']['highway']} highway\n"
            response += f"Safety Rating: {recommendation['safety_rating']}\n"
            response += f"Description: {recommendation['description']}"
            trainer.train([input_text, response])
    else:
        trainer.train([input_text, output_text])
print("Training complete. You can start using the bot.")
name=input("Enter your name: ")
print("Welcome to our Cars3600 {} Let me now how can I help you? ".format(name))
while True:
    request=input(name+':')
    if request=='Bye'or request=='bye':
        print("Bot:Bye")
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)