import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folders", help="Number of parent folders.", 
            type=int, default=10)
    parser.add_argument("-d", "--depth", help="Max depth of sub folders. The ammount will \
            be randomly chosen.", type=int, default=10)
    parser.add_argument("-n", "--name", help="Name of parent dir. (Default = 'root')",
            default="root") 
    return parser.parse_args()
