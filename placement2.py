# grade=int(input("enter the score: "))
# if grade>=90:
#     print("Grade A")
# elif grade >= 80:
#     print(" Grade B")
# elif grade >=70:
#     print("Grade C")
# else:
#     print("Grade D")
# year=int(input("enter the year: "))
# if(year%4==0 and year%100!=0):
#     print("Year {} is a leap year".format(year))
# elif(year%400==0 and year%100==0):
#     print("Year {} is a leap year".format(year))
# else:
#     print("Year is not a leap year")
# password=input("enter a password: ")
# length_condition=len(password) >= 8
# uppercondit=any(char.isupper() for char in password)
# lowercondit=any(char.islower() for char in password)
# digicondit=any(char.isdigit() for char in password)
# if length_condition and uppercondit and lowercondit and digicondit:
#     print("Valid condition")
# else:
#     print("Invalid")
# import random as rand
# number=rand.randint(0,100)
# while True:
#     guess=int(input("enter the guess number: "))
#     if(guess==number):
#         print("You guessed correctly")
#         break
#     elif(guess < number):
#         print("You're Low")
#     else:
#         print("You're High")
# my_dict={'key1':'value1','key2':'value2','key3':'value3'}
# for i in my_dict:
#     print(i,my_dict[i])

# my_tup=(1,2,3,4)
# l=["sanoop","shashank"]



# names = []
# scores = []

# for name,score in zip(names,scores):
#     print(name,score)



# #def funName(param):
# #   statement

# def power(*args):
#     return base ** exp

# power(5,8,4)
# power(5)

# #*args

# def avr(*args):
#     return sum(args)/len(args)

# avr(1,2,3,4)

# # lambda x : x+y
# double = lambda x : x*2

# print(double(5))

# def double(val):
#     return val *2 
#*kwargs


#write a simple prg to check prime

#count vowels and consonants
# text=input("Enter the string here: ").lower()
# l=text.split()
# consonant_count=0
# vowel_count=0
# for i in l:
#     for j in i:
#         if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
#             vowel_count+=1
#         else:
#             consonant_count+=1
# print(vowel_count)
# print(consonant_count)
data=[
    {"name":"Alice","age":30},
    {"name":"Bob","age":25},
    {"name":"Eve","age":22}
]
sorted_data=sorted(data,key=lambda x:x['age'])
print(sorted_data)