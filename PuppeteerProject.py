"""Amber Rose"""

'''Function for what to say as you enter a room'''


def enter_room():
    global prev_room
    global current_room
    if prev_room != current_room:
        print('\n"You are in the ' + Color.BOLD + Color.YELLOW + current_room + Color.END, end='."\n\n')
        if 'item' in in_room[current_room] and in_room[current_room]['item'] != '':
            room_item = in_room[current_room]['item'][0]
            print(in_room[current_room]['text'])
            print((in_room[current_room]['added_text'].format(room_item)))
        else:
            print((in_room[current_room]['text']))
        prev_room = current_room


'''Showing the instructions for the user'''


def show_instructions():
    print('\nPlease enter which direction you would like to go.\nFrom this room, you may enter ', end='')
    global current_room
    bold = [Color.BOLD + Color.DARKCYAN + '"' + y + '"' + Color.END for y in rooms_directions[current_room]]
    print(*bold, sep=' or ', end='.\n\n')
    if 'item' in in_room[current_room]:
        if in_room[current_room]['item'] != '':
            print('There\'s an item in this room you can get by entering ' + Color.BOLD + Color.GREEN +
                  '"Get Item"' + Color.END + '.')
    print('You may also check your inventory with ' + Color.BOLD + Color.GREEN + '"Inventory"' + Color.END +
          '\nor enter ' + Color.BOLD + Color.BLUE + '"Quit"' + Color.END + ' to quit the game.\n')


'''Moving through rooms function'''


def move_room(direction):
    global current_room
    current_room = rooms_directions[current_room][direction]


'''Function to add an item to the inventory'''


def add_item():
    global current_room
    if 'item' in in_room[current_room]:
        item = in_room[current_room]['item'][0]
        item_type = in_room[current_room]['item'][1]
        item_text = in_room[current_room]['item'][2]
        if item != '':
            inventory[item_type].append(item)
            print(item_text.format(item))
            in_room[current_room]['item'][0] = ''
        else:
            print('\n"There doesn\'t seem to be any items of use in this room."')
    else:
        print('\n"There doesn\'t seem to be any items of use in this room."')


'''Function for checking the inventory'''


def check_inventory():
    print(Color.BOLD + Color.GREEN + '\n\nINVENTORY' + Color.END)
    print('-' * 100)
    missing_item = 0
    for item_type, item in inventory.items():
        if len(item) > 0:
            print(item_type + ': ', end='')
            print(*item, sep=', ')
        else:
            if missing_item == 0:
                missing_item += 1
    print('You\'ve removed ' + Color.BOLD + Color.RED + '{} out of 5'.format(len(inventory['Tools'])) +
          Color.END + ' of your rings.')
    if missing_item > 0 or len(inventory['Tools']) < 5:
        print('You haven\'t found all of the items needed to survive.')
    else:
        print('You\'ve found all of the items needed to survive! Time to face the ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + '...')
    print('-' * 100)


'''Boss battle trigger function'''


def boss_battle():
    weapon = inventory['Weapon']
    ammo = inventory['Ammo']
    aid = inventory['Aid']
    rings = inventory['Tools']
    global you_won
    print('"You enter the foyer, then realize the front door is cracked open. You hear a creak behind you and see '
          'the\n' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ' creeping behind you with the '
          'same menacing smile as before. With an unnatural amount of force,\nthe ' + Color.BOLD + Color.PURPLE +
          'Puppeteer' + Color.END + ' shoves you, sending you flying through the front door and crashing onto\nthe'
          ' rocky ground outside. Disoriented, you rise to your feet and prepare to fight for you life."')

    if len(weapon) == 0 or len(ammo) == 0 or len(aid) == 0 or len(rings) < 5:
        if len(rings) < 5:
            print('\n"puppet ending"')
        elif len(aid) == 0:
            print('\n"bled out"')
        elif len(weapon) == 0:
            print('\n"no weapon"')
        else:
            print('\n"*click*, *click*, no ammo"')
        return
    else:
        you_won += 1


'''Function to quit the game'''


def quitting():
    global current_room
    global prev_room
    in_exit = 0
    while in_exit == 0:
        current_room = 'Quit'
        print('\nIf you\'re sure you\'d like to quit, enter ' + Color.BOLD + Color.BLUE +
              '"Quit"' + Color.END + ' again, otherwise enter ' + Color.BOLD + Color.YELLOW + '"Go Back"' +
              Color.END + '.\n')
        answer = input().title()
        if answer == 'Quit':
            break
        elif answer == 'Go Back':
            current_room = prev_room
            print('\n"You are back in the ' + Color.BOLD + Color.YELLOW + current_room + Color.END, end='."\n')
            if 'item' in in_room[current_room]:
                item = in_room[current_room]['item'][0]
                print((in_room[current_room]['text'].format(item)))
            else:
                print((in_room[current_room]['text']))
                break
        else:
            print('\nI\'m sorry, that isn\'t a valid input.')


'''Colors and bold text options from external source: 
https://stackoverflow.com/questions/8924173/how-can-i-print-bold-text-in-python'''


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


'''Dictionary of the directions to move to each room'''
rooms_directions = {
    'Attic': {
        'South': 'Main Bedroom'
    },
    'Children\'s Bedroom': {
        'South': 'Back Entryway'
    },
    'Main Bedroom': {
        'North': 'Attic',
        'East': 'Bathroom',
        'South': 'Dining Room'
    },
    'Bathroom': {
        'West': 'Main Bedroom'
    },
    'Back Entryway': {
        'North': 'Children\'s Bedroom',
        'East': 'Dining Room',
        'South': 'Washroom'
    },
    'Dining Room': {
        'North': 'Main Bedroom',
        'West': 'Back Entryway',
        'East': 'Foyer',
        'South': 'Kitchen'
    },
    'Foyer': {
        'West': 'Dining Room',
        'South': 'Living Room'
    },
    'Washroom': {
        'North': 'Back Entryway'
    },
    'Kitchen': {
        'North': 'Dining Room',
        'East': 'Living Room'
    },
    'Living Room': {
        'North': 'Foyer',
        'West': 'Kitchen'
    }
}

'''Dictionary of what is found and said in each room'''
in_room = {
    'Attic': {
        'item': [
            'Shotgun Bullets',
            'Ammo',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"attic text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Children\'s Bedroom': {
        'item': [
            'Hammer',
            'Tools',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"child text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Main Bedroom': {
        'item': [
            'Rusted Cutting Pliers',
            'Tools',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"main text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Bathroom': {
        'item': [
            'Rusted Hack Saw',
            'Tools',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"bathroom text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Back Entryway': {
        'text': '"basic room text"'
    },
    'Dining Room': {
        'item': [
            'Rusted Kitchen Shears',
            'Tools',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"dining text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Foyer': {
        'text': '"basic room text."'
    },
    'Washroom': {
        'item': [
            'Rusted Garden Shears',
            'Tools',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"washroom text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Kitchen': {
        'item': [
            'First Aid',
            'Aid',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"kitchen text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Living Room': {
        'item': [
            'Shotgun',
            'Weapon',
            '\n"item text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
        ],
        'text': '"basic room text"',
        'added_text': '"living text ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    }
}

'''Dictionary to insert inventory items and differentiates their uses'''
inventory = {
    'Weapon': [],
    'Ammo': [],
    'Aid': [],
    'Tools': []
}

'''Variables'''

playing = 0
prev_room = ''
current_room = 'Back Entryway'
bold_list = []
you_won = 0

'''Title, created via outside source:
https://patorjk.com/software/taag/#p=display&f=Cards&t=Puppeteer'''

print(Color.PURPLE + r'''
 ██▓███   █    ██  ██▓███   ██▓███  ▓█████▄▄▄█████▓▓█████ ▓█████  ██▀███  
▓██░  ██▒ ██  ▓██▒▓██░  ██▒▓██░  ██▒▓█   ▀▓  ██▒ ▓▒▓█   ▀ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▓██  ▒██░▓██░ ██▓▒▓██░ ██▓▒▒███  ▒ ▓██░ ▒░▒███   ▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▓▓█  ░██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░▒▒█████▓ ▒██▒ ░  ░▒██▒ ░  ░░▒████▒ ▒██▒ ░ ░▒████▒░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░▒▓▒░ ░  ░░░ ▒░ ░ ▒ ░░   ░░ ▒░ ░░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░     ░░▒░ ░ ░ ░▒ ░     ░▒ ░      ░ ░  ░   ░     ░ ░  ░ ░ ░  ░  ░▒ ░ ▒░
░░        ░░░ ░ ░ ░░       ░░          ░    ░         ░      ░     ░░   ░ 
            ░                          ░  ░           ░  ░   ░  ░   ░     
''' + Color.END)

input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

print('\n' + ('v' * 110) + '\n')


'''Intro'''

print(Color.BOLD + Color.PURPLE + '"Puppeteer"\n' + Color.END)
print('"Head throbbing and vision blurry, you awaken on the ground in the middle of a dark forest.\n'
      'As you blink yourself awake, you notice your vehicle crashed a few yards from where you lay.\n'
      'You notice drag marks leading from you open door to where you are. Someone removed you from your car?\n'
      'As you struggle to stand, you realize that, embedded into your wrists, kneecaps,\n'
      'and the back of your neck are metal rings attached to wires that seem to disappear upward into the sky.\n'
      'You look like some sort of grotesque puppet. Before you get the chance to pull at your abhorrent binding,\n'
      'a long, twisted creature with a menacing smile emerges from the woods to continue working on you.\n'
      'Without thinking, you jump to your feet, wounds searing with pain, and run for your life.\n'
      'You don\'t look back, but you can tell that if you were to slow down, the creature would have you once again.\n'
      'You spot the lights of a home in the distance, and with your last burst of energy,'
      '\nyou manage to reach the home, burst through the back door, and shut and lock it behind you.\n')

input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

print(('v' * 110) + '\n')

print(Color.BOLD + Color.RED + '         "This is your final refuge."\n\n' + Color.END + Color.BOLD +
      '"You must find a way to remove all five of your shackles, patch up your bleeding wounds, and find a weapon\n'
      'to defend yourself if you\'re to have any hope of escaping here with control over your own life."\n' + Color.END)

input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

print('\n' + ('v' * 110))

'''While playing loop'''

while playing == 0:
    enter_room()

    show_instructions()

    user_input = input().title()

    if user_input == 'Quit':
        quitting()
        if current_room == 'Quit':
            break
    elif user_input == 'Get Item':
        add_item()
    elif user_input == "Inventory":
        check_inventory()
        continue
    elif user_input in rooms_directions[current_room]:
        move_room(user_input)
    else:
        print('\nI\'m sorry, that isn\'t a valid input')
        continue

    if current_room == 'Foyer':
        print('\n' + ('v' * 110) + '\n')
        boss_battle()
        if you_won > 0:
            print(Color.BOLD + Color.YELLOW + '\n"YOU WIN"' + Color.END)
            print('\n' + ('v' * 110) + '\n')
            break
        else:
            print(Color.BOLD + Color.RED + '\n"YOU ARE DEAD"' + Color.END)
            print('\n' + ('v' * 110) + '\n')
            break
print('\nThanks for playing.')
