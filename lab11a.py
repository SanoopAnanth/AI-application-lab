from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
def remove_stop(input_passage):
    stop_words=set(stopwords.words('english'))
    token=word_tokenize(input_passage)
    wlist=[w for w in token if w not in stop_words]
    return ' '.join(wlist)
input_path=input("Enter the input path:")
output_path=input("enter the output path:")
with open(input_path,"r") as fd:
    passage=fd.read()
final_word=remove_stop(passage)
with open(output_path,"w") as fd1:
    fd1.write(final_word)

