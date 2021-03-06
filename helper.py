import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--folders", help="Number of parent folders.", 
            type=int, default=10)
    parser.add_argument("-d", "--depth", help="Max depth of sub folders. The ammount will \
            be randomly chosen.", type=int, default=10)
    parser.add_argument("-n", "--name", help="Name of parent dir. (Default = 'root')",
            default="root") 
    parser.add_argument("-f", "--files", help="File numbers to create, if any.",
            default=0, type=int) 
    return parser.parse_args()
