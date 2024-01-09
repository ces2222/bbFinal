import os


class MyFirstProcess:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Hello, I am {}.".format(self.name))