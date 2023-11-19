from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot=ChatBot(
    'Cars3600',
    storage_adaptor='chatterbot.storage.SQLStorageAdaptor',
    logic_adaptor=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdaptor',
        'chatterbot.lofic.BestMatch',
        {
            'import_path':'chatterbot.logic.BestMatch',
            'default_response':'I am Sorry, I do not understand',
            'maximun_similarity_threshold':0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)
trainer=ListTrainer(chatbot)
trainingdata=open('auto.json').read().splitlines()
trainercorpus=ChatterBotCorpusTrainer(chatbot)
trainercorpus.train(
    'chatterbot.corpus.english'
)
name=input("Enter your name: ")
print("Welcome to our Cars3600 {} Let me now how can I help you? ".format(name))
while True:
    request=input(name+':')
    if request=='Bye'or request=='bye':
        print("Bot:Bye")
        break
    else:
        response=chatbot.get_response(request)
        print('Bot:',response)