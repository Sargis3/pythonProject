class Questions:
    def __init__(self, quest_list):
        self.__quest_list = quest_list

    def question_list(self):
        return self.__quest_list


obj = Questions(["5*5", "7+7", "5*3+4", "8-6"])
for i in range(0, len(obj.question_list())):
    print(obj.question_list()[i])

