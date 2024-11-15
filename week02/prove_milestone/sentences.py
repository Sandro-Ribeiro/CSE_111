import random

def get_determiner(quantity):
    """
    Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
        
    # Randomly choose and return a determiner.
    determiner = random.choice(words)
    return determiner

def get_noun(quantity):
    """
    Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                  "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", 
                 "dogs", "girls", "men", "rabbits", "women"]
        
    noun = random.choice(words)
    return noun

def get_verb(quantity, tense, noun):
    """
    Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs
    calssified for noun:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """

    if tense == "past" and quantity == 1:
        words ={
            "bird": ["drank", "ate", "grew", "thought", "ran", "slept", "walked"],
            "boy": ["drank", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "car": ["ran"],
            "cat": ["drank", "ate", "grew", "thought", "ran", "slept", "walked"],
            "child": ["drank", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "dog": ["drank", "ate", "ran", "slept", "laughed", "walked"],
            "girl": ["drank", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "man": ["drank", "ate", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "rabbit": ["drank", "ate", "ran", "slept", "walked"],
            "woman": ["drank", "ate", "thought", "ran", "slept", "talked", "walked", "wrote"]
        }
    if tense == "past" and quantity != 1:
        words ={
            "birds": ["drank", "ate", "grew", "thought", "ran", "slept", "walked"],
            "boys": ["drank", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "cars": ["ran"],
            "cats": ["drank", "ate", "grew", "thought", "ran", "slept", "walked"],
            "children": ["drank", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "dogs": ["drank", "ate", "ran", "slept", "laughed", "walked"],
            "girls": ["drank", "ate", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "men": ["drank", "ate", "thought", "ran", "slept", "talked", "walked", "wrote"],
            "rabbits": ["drank", "ate", "ran", "slept", "walked"],
            "women": ["drank", "ate", "thought", "ran", "slept", "talked", "walked", "wrote"]
        }
    elif tense == "present" and quantity == 1:
        words= {
            "bird": ["drinks", "eats", "grows", "thinks", "runs", "sleeps", "walks"],
            "boy": ["drinks", "eats", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
            "car": ["runs"],
            "cat": ["drinks", "eats", "grows", "thinks", "runs", "sleeps", "walks"],
            "child": ["drinks", "eats", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
            "dog": ["drinks", "eats", "runs", "sleeps", "laughs", "walks"],
            "girl": ["drinks", "eats", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
            "man": ["drinks", "eats", "thinks", "runs", "sleeps", "talks", "walks", "writes"],
            "rabbit": ["drinks", "eats", "runs", "sleeps", "walks"],
            "woman": ["drinks", "eats", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        }
    elif tense == "present" and quantity != 1:
        words = {
            "birds": ["drink", "eat", "grow", "think", "run", "sleep", "walk"],
            "boys": ["drink", "eat", "laugh", "think", "run", "sleep", "talk", "walk", "write"],
            "cars": ["run"],
            "cats": ["drink", "eat", "grow", "think", "run", "sleep", "walk"],
            "children": ["drink", "eat", "laugh", "think", "run", "sleep", "talk", "walk", "write"],
            "dogs": ["drink", "eat", "run", "sleep", "laugh", "walk"],
            "girls": ["drink", "eat", "laugh", "think", "run", "sleep", "talk", "walk", "write"],
            "men": ["drink", "eat", "think", "run", "sleep", "talk", "walk", "write"],
            "rabbits": ["drink", "eat", "run", "sleep", "walk"],
            "women": ["drink", "eat", "think", "run", "sleep", "talk", "walk", "write"]
        }
    elif tense == "future" and quantity == 1:
        words = {
            "bird": ["will drink", "will eat", "will grow", "will think", "will run", "will sleep", "will walk"],
            "boy": ["will drink", "will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "car": ["will run"],
            "cat": ["will drink", "will eat", "will grow", "will think", "will run", "will sleep", "will walk"],
            "child": ["will drink", "will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "dog": ["will drink", "will eat", "will run", "will sleep", "will laugh", "will walk"],
            "girl": ["will drink", "will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "man": ["will drink", "will eat", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "rabbit": ["will drink", "will eat", "will run", "will sleep", "will walk"],
            "woman": ["will drink", "will eat", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        }
    elif tense == "future" and quantity != 1:
        words = {
            "birds": ["will drink", "will eat", "will grow", "will think", "will run", "will sleep", "will walk"],
            "boys": ["will drink", "will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "cars": ["will run"],
            "cats": ["will drink", "will eat", "will grow", "will think", "will run", "will sleep", "will walk"],
            "children": ["will drink", "will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "dogs": ["will drink", "will eat", "will run", "will sleep", "will laugh", "will walk"],
            "girls": ["will drink", "will eat", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "men": ["will drink", "will eat", "will think", "will run", "will sleep", "will talk", "will walk", "will write"],
            "rabbits": ["will drink", "will eat", "will run", "will sleep", "will walk"],
            "women": ["will drink", "will eat", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        }


    verb = random.choice(words[noun])
    return verb

def get_preposition(determiner):
    """
    Return a randomly chosen preposition
    from this dictionary of prepositions classified according 
    to the determiner:
       "a": ["About", "Across", "After", "At", "By", "For", "From", "To"],
        "one": ["About", "After", "By", "For", "To"],
        "the": ["Above", "Around", "Behind", "Below", "Beyond", "In", "Into", 
                "Near", "Of", "On", "Onto", "Over", "Under", "With"],
        "some": ["Across", "Along", "Around", "Behind", "Below", "From", 
                "Near", "Off", "Out", "Past", "With", "Without"],
        "many": ["Across", "Around", "Behind", "Below", "Over", "Under", "With"]
    Return: a randomly chosen preposition.
    """

    words = {
        "a": ["About", "Across", "After", "At", "By", "For", "From", "To"],
        "one": ["About", "After", "By", "For", "To"],
        "the": ["Above", "Around", "Behind", "Below", "Beyond", "In", "Into", 
                "Near", "Of", "On", "Onto", "Over", "Under", "With"],
        "some": ["Across", "Along", "Around", "Behind", "Below", "From", 
                "Near", "Off", "Out", "Past", "With", "Without"],
        "many": ["Across", "Around", "Behind", "Below", "Over", "Under", "With"]
    }

    preposition = random.choice(words[determiner])
    return preposition


def get_prepositional_phrase(quantity, determiner):
    """
    Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition(determiner).capitalize()
    determiner =  get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun},"

    return prepositional_phrase

def get_adjective():
    """
    Return a randomly chosen an adjective from this list 
    of adjectives:
        "happy", "sad", "bright", "dark", "tall", "short", 
        "small", "big", "fast", "slow", "kind", "rude", 
        "heavy", "light", "old", "young", "colorful", 
        "noisy", "quiet", "beautiful", "ugly"
    """

    words = [
        "happy", "sad", "bright", "dark", "tall", "short", 
        "small", "big", "fast", "slow", "kind", "rude", 
        "heavy", "light", "old", "young", "colorful", 
        "plain", "noisy", "quiet", "clever", "brave", 
        "foolish", "beautiful", "ugly"
    ]

    adjective = random.choice(words)
    return adjective

def get_adverb():
    """
    Return a randomly chosen an adverb from a dictionary
    of classified adverbs:
        "manner": ["quickly", "slowly", "happily", "sadly", "brightly",
                "silently", "loudly", "gracefully", "awkwardly", 
                "gently", "firmly", "courageously", "foolishly", 
                "beautifully", "badly", "carefully", "carelessly", 
                "easily"],
        "time": ["often", "rarely", "always", "sometimes", "never", 
                "completely"],
        "place": ["here", "there", "everywhere"],
        "frequency": ["always", "sometimes", "never"],
        "intensity": ["completely", "very", "extremely"]
    """

    words = {
        "manner": ["quickly", "slowly", "happily", "sadly", "brightly",
                "silently", "loudly", "gracefully", "awkwardly", 
                "gently", "firmly", "courageously", "foolishly", 
                "beautifully", "badly", "carefully", "carelessly", 
                "easily"],
        "time": ["often", "rarely", "always", "sometimes", "never", 
                 "completely"],
        "place": ["here", "there", "everywhere"],
        "frequency": ["always", "sometimes", "never"],
        "intensity": ["completely", "very", "extremely"]
    }

    classification = random.choice(list(words.keys()))
    adverb = random.choice(words[classification])
    return classification, adverb   

def make_sentence(quantity, tense):
    """
    Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adjective = get_adjective()
    verb = get_verb(quantity, tense, noun)
    classification, adverb = get_adverb()
    prepositional_phrase = get_prepositional_phrase(quantity, determiner)
    
    if classification == "manner" or classification == "place" or classification == "intensity":
        print( prepositional_phrase + f" {determiner} {adjective} {noun} {verb} {adverb}")
    elif classification == "time":
        print( f"{adverb}, " + prepositional_phrase + f" {determiner} {adjective} {noun} {verb}")
    elif classification == "frequency":
        print( prepositional_phrase + f" {determiner} {adjective} {noun} {adverb} {verb}")

def main():

    dados = [
        [1, "past"],
        [1, "present"],
        [1, "future"],
        [2, "past"],
        [2, "present"],
        [2, "future"]
    ]
    
    for dado in dados:
        make_sentence(dado[0], dado[1])

    
main()