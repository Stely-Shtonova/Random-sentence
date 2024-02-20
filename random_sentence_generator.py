import random

# creating the lists the computer will choose from
names = ['Johny', 'Arnold', 'Emma', 'Robert', 'Daniel', 'Chris', 'Leonardo', 'Tom', 'Charles', 'Cameron',
         'Kate', 'Natalie', 'Angelina', 'Scarlet', 'Adam', 'Anne', 'Ben', 'Owen', 'Sandra', 'Jennifer', 'Taylor']
places = ['New York', 'Amsterdam', 'London', 'Chicago', 'Tokyo', 'Berlin', 'Paris', 'Barcelona', 'Dubai', 'Istanbul',
          'Los Angeles', 'Rome', 'Singapore', 'Prague', 'Madrid', 'Las Vegas', 'Sydney', 'San Francisco', 'Brazil']
verbs = ['swim in', 'walk on', 'eat', 'sleep on', 'dance with', 'write to', 'listen to', 'jump off', 'dream of', 'take',
         'install', 'learn about', 'build', 'fit in', 'understand', 'know about', 'keep', 'paint', 'prepare',
         'talk about', 'pay for', 'share', 'sing to', 'hug', 'love', 'like', 'adore', 'hate', '', 'want', 'use', 'call',
         'think about', 'clean']
nouns = ['information', 'phone', 'sock', 'pizza', 'banana', 'headphones', 'cat', 'picture', 'heart', 'magazine',
         'steak', 'agency', 'food', 'shirt', 'drama', 'student', 'world', 'professor', 'grandmother', 'child', 'hat',
         'desk', 'horse', 'tomatoes', 'finger', 'family', 'history', 'system', 'music', 'movie', 'woman', 'payment',
         'pie', 'tea', 'coffee']
adjectives = ['civil', 'beautiful', 'large', 'red', 'colorful', 'united', 'soft', 'golden', 'delicious', 'bald',
              'cute', 'chubby', 'clean', 'fancy', 'attractive', 'hot', 'skinny', 'kind', 'grumpy', 'polite', 'long',
              'angry', 'rude']
adverbs = ['slowly', 'coldly', 'sadly', 'sincerely', 'loudly', 'quickly', 'calmly', 'truly', 'gently', 'perfectly',
           'happily', 'softly', 'carefully', 'bravely', 'angrily', 'easily', 'cheerfully', 'eagerly', 'surprisingly']


def random_sentence():
    print('Your first sentence/s is/are:\n--------------')
    while True:
        # letting the computer choose the count of iterations/sentences
        sentences_count = random.randint(1, 3)
        for current_sentence in range(sentences_count):
            # chooses number of subjects and the type of the sentence
            type_of_sentence = random.choice(['question', 'simple'])
            subject_count = random.randint(1, 2)
            if subject_count == 1:
                name1 = random.choice(names)
            else:
                name1 = random.choice(names)
                name2 = random.choice(names)
            # the computer chooses a random word from each of the sequences
            verb = random.choice(verbs)
            noun = random.choice(nouns)
            adjective = random.choice(adjectives)
            adverb = random.choice(adverbs)
            place = random.choice(places)
            # checks if the sentence is a question and prints it
            if type_of_sentence == 'question':
                question_word = random.choice(['Who', 'Why', 'When', 'How'])
                details = random.choice(['often', 'many times', 'long'])
                # checking if the subject is only one -> checks/fixes grammar
                if subject_count == 1:
                    if question_word != 'How':
                        print(f"{question_word} does {name1} {verb} the {noun}?")
                    else:
                        print(f"{question_word} {details} does {name1} {verb} the {noun}?")
                else:
                    if question_word != 'How':
                        print(f"{question_word} do {name1} and {name2} {verb} the {noun}?")
                    else:
                        print(f"{question_word} {details} do {name1} and {name2} {verb} the {noun}?")
            else:
                # checking if the subject is only one -> checks/fixes grammar
                if subject_count == 1:
                    verb_list = verb.split()
                    if len(verb_list) == 2:
                        verb_, preposition = verb_list[0], verb_list[1]
                        print(
                            f"{name1} {adverb} {verb_ + 's ' + preposition} {'the ' + adjective} {noun} in {place}.")
                    else:
                        print(f"{name1} {adverb} {verb}s {'the ' + adjective} {noun} in {place}.")
                else:
                    print(f"{name1} and {name2} {adverb} {verb} {'the ' + adjective} {noun} in {place}.")
        # prompting the user for directions
        answer = input("Click [Enter] for more or [S] to stop the program: ")
        if answer.lower() == 's':
            break
        else:
            print('-------------------')


random_sentence()
