import nltk
import random
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# nltk.download('movie_reviews')
# nltk.download('punkt')
def extract_features(words):
    return dict([(word, True) for word in words])

documents = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

featuresets = [(extract_features(words), category) for (words, category) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]
classifier = SklearnClassifier(MultinomialNB())
classifier.train(train_set)

print("Accuracy:", nltk.classify.accuracy(classifier, test_set))
input_sentence = input("Enter a sentence: ")
words = word_tokenize(input_sentence) 
features =extract_features(words)
print("Predicted sentiment:", classifier.classify(features))
