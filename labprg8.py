#remove puntuation from the sentence
#sort the sentence in ascending
import string
input_string=input("Enter a string:")
final_string=""
for i in input_string:
    if i not in string.punctuation:
        final_string+=i
print(final_string)
