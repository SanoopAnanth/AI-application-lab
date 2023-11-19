from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk
nltk.download('averaged_perceptron_tagger')

def posfunc(input_sen):
    words=word_tokenize(input_sen)
    final_sen=pos_tag(words)
    return final_sen

result=posfunc(input("Enter the input string: "))
print(result)