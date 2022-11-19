import random


# Dokończyć tworzenie nicku (randomowy już jest) import modułu
# Energy bar < Globalna, zapytać
# poprawić błędy językowe


# def title_screen():
#     print('-' * 15, 'Welcome', '-' * 15)
#     print('This is RPG game called "Game"\n'
#           'Your options: \n'
#           '--new game--\n'
#           '--quit--')
#     userinput = input()
#     while True:
#         if userinput == 'quit':
#             quit()
#         elif userinput == 'new game':


# def nickname():


def startgame():
    print('You are somewhere in city, you dont know where you are \n'
          'Who you should talk to and then suddenly\n'
          'You hear a scream in a basement behind you \n'
          'You seems to know this voice, but you cant \n'
          'remember from\n'
          'What you want to do?\n'
          '---tavern, basement, blacksmith---')
    while True:
        userinput = input('>')
        if userinput == 'tavern':
            tavern()  # jest
        elif userinput == 'basement':
            basement()  # jest
        elif userinput == 'blacksmith':
            blacksmith()  # jest
        else:
            print('valid option, try again')


def tavern():
    print('The only thing in your mind is a scream from women\n'
          'Why didnt you help her?')
    print('Now you have to decide, what you want to do\n'
          '---blacksmith, basement, sleep---')

    while True:
        userinput = input('>')
        if userinput == 'basement':
            basement()
        elif userinput == 'blacksmith':
            blacksmith()
        elif userinput == 'sleep':
            print('you feel way better now\n whats next?\n'
                  '---blacksmith, basement, sleep---')
            user = input()
            if user == 'blacksmith':
                blacksmith()
            elif user == 'basement':
                basement()
            else:
                print('try again')
        else:
            print('Valid move...')


def blacksmith():
    print('I think this women needs help\n'
          'what are we going to do here?\n'
          '---basement, tavern, buyeq---')

    while True:
        userinput = input()
        if userinput == 'basement':
            basement()
        elif userinput == 'tavern':
            tavern()
        elif userinput == 'buyeq':
            buyeq()  # jest
        else:
            print('Come on, focus...')


def buyeq():
    print('Hello there, what do you want to buy?\n'
          'map - 70g\n'
          '---buymap, back---')
    while True:
        userinput = input()
        if userinput == 'buymap':
            if inventory['money'][0] >= 70:
                inventory['inne'][0].append('map')
                print('Congratulation, you have bought a map')
                print(inventory)
                blacksmith()
            else:
                print('you dont have enough money!')
        else:
            print('hm?')
            blacksmith()


def basement():
    print('What you can see here is something on left and darkness\n'
          'whats next?\n'
          '---left, up, blacksmith, tavern, rynek---')
    while True:
        userinput = input()
        if userinput == 'left':
            print('inside pile of hay you have found a knife')
            inventory['weapon'].append('knife')
            print(inventory)
        elif userinput == 'up':
            skeleton()
        elif userinput == 'tavern':
            tavern()
        elif userinput == 'blacksmith':
            blacksmith()
        elif userinput == 'rynek':
            if inventory['inne'][0] == 'map':
                print('with this map you can travel \n'
                      'wherever you want \n'
                      'good luck traveler')
                quit()
            else:
                print('I think you need a map to move from this city')
        else:
            print('Try again')


def skeleton():
    print('You see a giant skeleton. Its going toward someone.\n'
          'Behind skeleton is probably women, who was screaming before\n'
          '---south, fight---')
    while True:
        userinput = input()
        if userinput == 'fight':
            fight()
        elif userinput == 'south':
            basement()
        else:
            print('Try again')


def fight():
    print('you decided to fight with skeleton. Let the battle begin!')
    monster_atk = random.randint(1, 10)
    player_atk = random.randint(5, 10)
    while True:
        userinput = input(">")
        if userinput == 'fight':
            if monster_atk > player_atk:
                print('you have died.')
                quit()
            else:
                print('you have won the fight')
                princess()
        else:
            print('theres nothing you can do')


def princess():
    print('Women is half alive and she begs you\n'
          'not to kill her. As close you get\n'
          'as more terrified you are\n'
          'as a reward she gives you 50g')
    inventory['money'][0] = 70
    print(inventory)
    print('whats next?\n'
          '---south,---')
    while True:
        userinput = input(">")
        if userinput == 'south':
            fight_two()
        else:
            print('try again!')


def fight_two():
    print('You see another skeleton going towards you and a women\n'
          'what now?\n'
          '---fight---')
    monster_atk = random.randint(1, 10)
    player_atk = random.randint(9, 10)
    while True:
        userinput = input(">")
        if userinput == 'fight':
            if monster_atk > player_atk:
                print('you have died.')
                False
            else:
                print('you have won the fight')
                basement_new()
        else:
            print('theres nothing you can do')


def basement_new():
    print('What you can see here is something on left and darkness\n'
          'whats next?\n'
          '---left, up, blacksmith, tavern, rynek---')
    while True:
        userinput = input()
        if userinput == 'left':
            print('All you see is emptiness')
        elif userinput == 'up':
            skeleton()
        elif userinput == 'tavern':
            tavern()
        elif userinput == 'blacksmith':
            blacksmith()
        elif userinput == 'rynek':
            if 'map' not in inventory['inne']:
                print('I think you need a map to move from this city')
            else:
                print('with this map you can travel \n'
                      'wherever you want \n'
                      'good luck traveler')
                quit()
        else:
            print('Try again')


inventory = {'weapon': [],
             'money': [20],
             'inne': []
             }

startgame()
