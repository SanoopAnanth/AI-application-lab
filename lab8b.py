# def rearrange(input_string):
#     sentence=input_string.split()
#     sentence.sort()
#     new=' '.join(sentence)
#     return new
# ss=rearrange('Hi how are you. I am fine. bye')
# print(ss)
def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    sorted_sentence = ' '.join(words)
    return sorted_sentence
ss=sort_sentence(input("Enter the sring:"))
print(ss)
