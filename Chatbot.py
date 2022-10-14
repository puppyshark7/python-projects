# import
import random

#backgrond introduction
print('Have you ever wanted to "talk" or chat with a computer?  If so, you can talk with a computer right now.')
print()

# chatbot introduction
print('Hello. This is Aden 9. I am a chatbot.')
print('I like animals and I like to talk about food.')
name = input('What is your name?: ')
print('Hello,', name,'. Nice to meet you.')

# get year information
year = input('I am not very good at dates. What is the year?: ')
print('Yes, I think that is correct. Thanks!')

# ask user to guess age
myage = random.randint(10,20)
ageguess = input('Can you guess my age? - enter a number 10 - 20: ')
while not (ageguess==myage):
    if ageguess <myage:
        print('Too low. Try a higher number.')
    else:
        print('Too high. Try a lower number.')
    ageguess = input('Can you guess my age? - enter a number 10 - 20: ')
print('Yes you are correct. I am', myage,'.')

# do math to calaulate when chatbot will be 100
myage = int(myage)
nyears = 100 - myage
print('I will be 100 in', nyears, 'years.')
print('That will be the year', int(year) + nyears,'.')

# food conversation
print('I love chocolate.')
food = input('How about you? What is your favorite food?: ')
print('I like', food, 'too.')
question = 'How often do you eat ' + food + '?: '
howoften = input(question)
print('Interesting. I wonder if that is good for your health.')

# animal conversation
animal = input('My favorite animal is a panda. What is yours?: ')
print(animal,'! I do not like them.')
print('I wonder if a', animal, 'likes to eat ', food, '?')

# conversation about feelings
feeling = input('How are you feeling: ')
print('Why are you feeling', feeling,'.')
reason = input('Please tell me: ')
print('I understand. Thanks for sharing.')

# goodbye
print('It has been a long day')
print('I am too tired to talk. We can chat again later.')
print('Goodbye', name, 'I liked chatting with you')
