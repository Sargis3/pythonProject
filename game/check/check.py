

# def request_question():
#     answer = input()
#     return answer
#
#
# def answer_of_bot(user_answer):
#     if user_answer == "hi":
#         return "hi"
#     elif user_answer == "how are you":
#         return "fine , how are you"
#     elif user_answer == "how ord are you ?":
#         return "I am a robot , i have not a age"
#
#
# def main_logic_of_bot():
#     print(answer_of_bot(request_question))
#     print(answer_of_bot(request_question))
#     print(answer_of_bot(request_question))
#     print(answer_of_bot(request_question))
#
#
# print(main_logic_of_bot())

#
# def request_question():
#     answer = input("eli harcer kan?")
#     return answer
#
#
# def answer_of_bot(user_answer):
#     if user_answer == "hi":
#         return "hi"
#     elif user_answer == "vonces":
#         return "vat , du?"
#     elif user_answer == "qani tarekanes":
#         return "debil es robotem tariq chunem"
#     elif user_answer == "Manuky debila?":
#         pass
#     else:
#         print("iharke")
#
#
# def main_logic_of_bot():
#     while True:
#         question = request_question()
#         print(answer_of_bot(question))
#         if question == "break":
#             print("breaking while loop")
#             break
#
#
# print(main_logic_of_bot())


# class MyType:
#     value = "value"
#     description = "description"
#     abc = 15678
#
#
# my_type = MyType()
# my_type1 = MyType()
# print(my_type.value)
# print(my_type.description)
# print(my_type.abc)
# print(MyType.abc + 1000000)
# class Car:

#     def __init__(self, name, door_quantity, chairs_quantity, wheels_quantity, max_speed):
#         self.name = name
#         self.door = door_quantity
#         self.chairs = chairs_quantity
#         self.wheels = wheels_quantity
#         self.max_speed = max_speed
#
#     def run(self, name):
#         if name:
#             print("the device is on")
#         else:
#             print("the device is off")
#         return self.name + " is running"
#
#
# bmw = Car("BMW", 2, 5, 4, 240)
# audi = Car("AUDI", 2, 5, 4, 241)
#
# if bmw.max_speed > audi.max_speed:
#     print("bmw is faster")
# else:
#     print("audi is faster")
#
#
# def some_name(x, y):
#     return x + y
#
#
# print(some_name(1, 2))
# print(bmw.run(name=""))
# print(audi.run(name=""))
#
#

#
# class GuestRoom:
#
#     def __init__(self, name, flowers, chair, table):
#         self.name = name
#         # self.TV = TV
#         self.Flowers = flowers
#         self.chair = chair
#         self.table = table
#
#
# guestroom = GuestRoom("flowers", "chair", "table")
#
#
# print(guestroom.Flowers)
# print(guestroom.chair)
# print(guestroom.table)
#
#


class Home:

    def __init__(self, door, window, flowers, tv, computer, bed):
        self.door = door
        self.window = window
        self.flowers = flowers
        self.tv = tv
        self.computer = computer
        self.bed = bed


class GuestRoom(Home):

    def abc(self):
        return self.door


guestroom = GuestRoom("door", "window", "flowers", "tv", "computer", "bed")

print(guestroom.window)
print(guestroom.flowers)
print(guestroom.tv)

print("---------------------------------------------------------------")


class Room(Home):

    def bcd(self):
        return self.door


room = Room("door", "window", "flowers", "tv", "computer", "bed")

print(room.door)
print(room.window)
print(room.flowers)
print(room.computer)
print(room.bed)

print("---------------------------------------------------------------")


class Room2(Home):

    def bcd(self):
        return self.door


room2 = Room2("door", "window", "flowers", "tv", "computer", "bed")

print(room2.door)
print(room2.window)
print(room2.flowers)
print(room2.computer)
print(room2.bed)



#ctrl alt l