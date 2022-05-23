from game.quest.quest import *


class Answers:
    def __init__(self, quest_list):
        self.__answer_list = quest_list

    def answer_list(self):
        return self.__answer_list


obj = Answers([25, 30, 45, 10])
for i in range(0, len(obj.answer_list())):
    print(obj.answer_list()[i])
