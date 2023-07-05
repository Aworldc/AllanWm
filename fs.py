# Some absolute JShead wants the nodejs fs api in python
# It's so much more convenient

def readFileSync(path):
    with open(path, 'r') as file:
        data = file.read()
    return data
