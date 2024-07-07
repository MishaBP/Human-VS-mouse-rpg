from random import randint


class Person():
    x = 0
    y = 0
    hp = 100
    apple = 0
    bonus = 0
    damage = (randint(1, 20) + bonus)

    def dinner(self):
        self.hp += 10
        self.apple -= 1


class Enemy:
    hp = randint(0, 100)
    damage = randint(1, 20)


#    def __init__(self):
#       self.reset()
#    def reset(self):
#        hp = randint(0,100)
#        damage = randint(1,20)
#Human = Person(0,0,100)

hostile = Enemy()
Human = Person()


def main():
    while (Human.hp > 0):
        dirr = input("Where? UP/Down/Right/Left/search?")
        if dirr == ("up" or "Up"):
            Human.y += 1
        elif dirr == ("down" or "Down"):
            Human.y -= 1
        elif (dirr == ("Right" or "right")):
            Human.x += 1
        elif (dirr == ("Lefr" or "left")):
            Human.x -= 1
        elif (dirr == "hp"):
            print(Human.hp)
        elif (dirr == "eat apple"):
            if Human.apple > 0:
                Person.dinner(Human)
            else:
                print("you dont have an apple ));")
        elif (dirr == "search"):
            searchresult = randint(0, 100)
            if (searchresult < 20):
                print("your fount nothing")
            elif (searchresult > 20 and searchresult < 60):
                print("your found an apple")
                Human.apple += 1
            else:
                print("you were attacked a mouse! Awwws")
                fight()
        else:
            print("Затычка");
        print("Y", "X", "HP", "APPLE")
        print(Human.y, Human.x, Human.hp, Human.apple)
    if (Human.hp == 0 or Human.hp < 0):
        print("you are dead")


def hostilehit():
    Human.hp -= hostile.damage
    print("Mouse hit yOU" + " " + str(hostile.damage))


def humanhit():
    hostile.hp -= Human.damage
    print("You hit mouse" + " " + str(Human.damage))


def hostilereset():
    hostile.hp = randint(0, 100)
    hostile.damage = randint(1, 20)


def fight():
    while ((Human.hp > 0) and (hostile.hp > 0)):
        print("Y", "X", "HP", "APPLE")
        print(Human.y, Human.x, Human.hp, Human.apple)
        print("Mouse HP")
        print(hostile.hp)
        hostilehit()
        dirr = input("fight or leave ")
        if adirr == "fight" or dirr == "":
            humanhit()
    print("you are winn + Bonus apple and damage")
    Human.bonus += 1
    Human.apple += 1
    hostilereset()
    main()


if __name__ == '__main__':
    main()
