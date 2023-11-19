from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stemit(input_sen):
    stemmer=PorterStemmer()
    words=word_tokenize(input_sen)
    final_list=[stemmer.stem(word) for word in words]
    return ' '.join(final_list) 
result=stemit(input("Enter the sentence for stemming it: "))
print(result)