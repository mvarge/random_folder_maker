import os
import random
from words import words


class Tree(object):

    def __init__(self, nodes=1, max_depth=1, files=0):
        self.nodes = xrange(nodes)
        self.max_depth = max_depth
        self.files = files

    def depth(self):
        return random.randint(0, self.max_depth)

    def word(self):
        '''Generate an word and guarantees that it don't clashes
        with any other existent directory.
        
        LBYL approach.
        '''
        word = fake_word()
        if word not in os.listdir(os.getcwd()):
            return word
        else:
            return "{0}_{1}".format(word, fake_word())

    def gen_tree(self, root="root"):
        parent = os.path.join(os.getcwd(), root)
        os.makedirs(parent)
        os.chdir(parent)
        for node in self.nodes:
            word = self.word()
            os.makedirs(word)
            os.chdir(os.path.join(parent, word))
            depth = self.depth()
            while depth:
                for f in xrange(random.randint(0, self.files)):
                    filename = "{0}.txt".format(self.word())
                    open(filename, 'a').close()
                folder = self.word()
                os.makedirs(folder)
                os.chdir(os.path.join(os.getcwd(), folder))
                depth -= 1
            os.chdir(parent)

def fake_word():
    return random.choice(words)

if __name__ == "__main__":
    from helper import parse
    args = parse()
    t = Tree(args.folders, args.depth, args.files)
    t.gen_tree(args.name)
