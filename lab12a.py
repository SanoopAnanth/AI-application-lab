from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('wordnet')
def wordlem(input_sen):
    lem=WordNetLemmatizer()
    words=word_tokenize(input_sen)
    final_sen=[lem.lemmatize(word) for word in words]
    return ' '.join(final_sen)
result=wordlem(input("Enter the input statement: "))
print(result)