import os
import random
from words import words


class Tree(object):

    def __init__(self, nodes=1, max_depth=1):
        self.nodes = xrange(nodes)
        self.max_depth = max_depth

    def depth(self):
        return random.randint(0, self.max_depth)

    def gen_tree(self):
        os.makedirs("fake_tree")
        parent = os.path.join(os.getcwd(), "fake_tree")
        os.chdir(parent)
        for node in self.nodes:
            word = fake_word()
            os.makedirs(word)
            os.chdir(os.path.join(parent, word))
            depth = self.depth()
            while depth:
                folder = fake_word()
                os.makedirs(folder)
                os.chdir(os.path.join(os.getcwd(), folder))
                depth -= 1
            os.chdir(parent)

def fake_word():
    return random.choice(words)

if __name__ == "__main__":
    t = Tree(10, 10)
    t.gen_tree()
