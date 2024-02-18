import random

names = ['Johny', 'Arnold', 'Emma', 'Robert', 'Daniel', 'Chris', 'Leonardo', 'Tom', 'Charles', 'Cameron',
         'Kate', 'Natalie', 'Angelina', 'Scarlet', 'Adam', 'Anne', 'Ben', 'Owen', 'Sandra', 'Jennifer', 'Taylor']
cities = ['New York', 'Amsterdam', 'London', 'Chicago', 'Tokyo', 'Berlin', 'Paris', 'Barcelona', 'Dubai', 'Istanbul',
          'Los Angeles', 'Rome', 'Singapore', 'Prague', 'Madrid', 'Las Vegas', 'Sydney', 'San Francisco', 'Brazil']
verbs = ['swim in', 'walk on', 'eat', 'sleep on', 'dance with', 'write', 'listen to', 'jump off', 'dream of', 'take',
         'install', 'learn about', 'build', 'fit', 'understand', 'pack', 'train', 'keep', 'paint', 'cook', 'slide', 'buy',
         'share']
nouns = ['information', 'phone', 'sock', 'bed', 'banana', 'headphones', 'cat', 'picture', 'heart', 'magazine', 'steak',
         'agency', 'food', 'shirt', 'drama', 'relation', 'world', 'profession', 'grandmother', 'child', 'hat', 'desk']
adjectives = ['civil', 'beautiful', 'large', 'red', 'colorful', 'united', 'soft', 'golden', 'delicious', 'bald',
              'plain',
              'chubby', 'clean', 'fancy', 'attractive', 'hot', 'skinny', 'kind', 'grumpy', 'polite', 'fluffy']
adverbs = ['slowly', 'coldly', 'sadly', 'sincerely', 'loudly', 'quickly', 'calmly', 'truly', 'gently', 'perfectly',
           'happily',
           'softly', 'carefully', 'bravely', 'angrily', 'easily', 'cheerfully', 'eagerly']
places = ['downstairs', 'outside', 'on the beach', 'in the bookstore', 'on the bed', 'in the shower', 'on the sofa',
          'in school', 'in the park', 'in the cinema', 'around the block', 'in the sea', 'in the hotel room',
          'over there']


def random_sentence():
    print('Your first sentence/s is/are:\n--------------')
    while True:
        sentences_count = random.choice(range(1, 5))
        subject_count = random.randint(1, 2)
        for current_sentence in range(sentences_count):
            name1 = random.choice(names)
            name2 = random.choice(names)
            city = random.choice(cities)
            verb = random.choice(verbs)
            noun = random.choice(nouns)
            adjective = random.choice(adjectives)
            adverb = random.choice(adverbs)
            place = random.choice(places)
            if subject_count == 1:
                verb_list = verb.split()
                if len(verb_list) == 2:
                    verb_, preposition = verb_list[0], verb_list[1]
                    print(f"{name1} from {city} {adverb} {verb_+'s '+ preposition} {'the ' +adjective} {noun} {place}!")
                else:
                    print(f"{name1} from {city} {adverb} {verb}s {'the ' +adjective} {noun} {place}!")
            else:
                print(f"{name1} and {name2} from {city} {adverb} {verb} {'the ' +adjective} {noun} {place}!")
        answer = input("Click [Enter] for more or [S] to stop the program: ")
        if answer.lower() == 's':
            break
        else:
            print('-------------------')


random_sentence()
