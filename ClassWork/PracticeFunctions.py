def our_story(noun, verb, adjective):
    story = f'Once upon a time in a small, {adjective} village, there lived a curious {noun} named Sammy. \nSammy was tired of endlessly {verb} and decided to embark on a new adventure. \nHe wanted to become a programming Python!'
    print(story)


noun = input('Write a noun: ')
verb = input('Write a verb: ')
adjective = input('Write a adjective: ')

our_story(noun, verb, adjective)
