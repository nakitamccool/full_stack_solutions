class Bird(object):
    """
    Bird Class
    """

    def __init__(self, kind, call):
        """
        Set the bird kind and it's call
        """
        self._kind = kind
        self._call = call

    def do_call(self):
        """
        Print out the bird kind and the call
        """
        print("A %s goes %s" % (self._kind, self._call))

owl = Bird('Owl', 'Twit Twoo!')
print(owl._kind)


class Parrot(Bird):
    """
    Parrot class
    """

    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.learned_phrases = list()

    def learn_phrase(self, phrase):
        """
        Teach the parrot a new phrase
        """
        self.learned_phrases.append(phrase)

    def do_call(self):
        Bird.do_call(self)
        print('\n'.join(self.learned_phrases))

polly = Parrot()
polly.learn_phrase("I'm a pretty Polly")
polly.learn_phrase("Who's a pretty boy, then?")
polly.do_call()
