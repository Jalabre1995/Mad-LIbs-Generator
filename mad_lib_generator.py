# Mad libs Random Story Generator
#In order to deal with the random numbers, I will import the randint from the random library
from random import randint
import copy
story = (
    "One day my {} blank freind and I decided to go to the {} game in {}. " +
    "We really wanted to see the {} play the {}. " +
    "But we managed to find a great price for the {} game on {}. " +
    "Hey at least its a {} day out in {} . " 
)

#Create a dictionay to loop up words by type
word_dict = {
    'adjective': ['greed', 'mad', 'sad', 'grubby', 'abrasive', 'rich', 'harsh', 'tasty'],
    'city name': ['Hartford', 'Boston', 'New York', 'Cleveland', 'Miami', 'Oregon'],
    'noun': ['people', 'map', 'music','dog', 'hamster', 'ball', 'hotdog', 'salad'],
    'action verb': ['run', 'fall', 'carry', 'watch', 'swim','jump', 'bounce'],
    'sports noun': ['ball', 'mit','puck','uniform', 'helmet', ],
    'place': ['park', 'desert', 'forest', 'store', 'restaurant', 'waterfall']
}

#Create a function that is going to select a random word
def get_word(type, local_dict):
    #Create a varibale called words and have it equal to the local_dict from the parameters and have it hve a key called type sp it will selct if its a adjective, verb, noun etc.
    words = local_dict[type]
    cnt = len(words) - 1
    #Create the index that we are going to use
    index = randint(0,cnt)
    #Return  local_dict and its going to select the type 
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('place', local_dict),
        get_word('adjective', local_dict),
        get_word('action verb', local_dict)
    )

print("STORY 1: ")
print(create_story())