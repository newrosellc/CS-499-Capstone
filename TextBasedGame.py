"""Amber Rose"""

'''Title function, created via outside source:
https://patorjk.com/software/taag/#p=display&f=Cards&t=Puppeteer'''


def title():
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


'''Function for what to say as you enter a room'''


def enter_room():
    global prev_room
    global current_room
    if prev_room != current_room:
        print('\n"You are in the ' + Color.BOLD + Color.YELLOW + current_room + Color.END, end='."\n\n')
        if 'item' in in_room[current_room] and in_room[current_room]['item'][0] != '':
            room_item = in_room[current_room]['item'][0]
            print(in_room[current_room]['text'])
            print((in_room[current_room]['added_text'].format(room_item)))
        else:
            print((in_room[current_room]['text']))
        prev_room = current_room


'''Showing the instructions for the user'''


def show_instructions():
    print('\n' + ('-' * 60))
    print('Please enter which direction you would like to go.\nFrom this room, you may enter ', end='')
    global current_room
    bold = [Color.BOLD + Color.DARKCYAN + '"' + y + '"' + Color.END for y in rooms_directions[current_room]]
    print(*bold, sep=' or ', end='.\n\n')
    if 'item' in in_room[current_room]:
        if in_room[current_room]['item'][0] != '':
            print('There\'s an item in this room you can get by entering ' + Color.BOLD + Color.GREEN +
                  '"Get Item"' + Color.END + '.')
    print('You may also check your inventory with ' + Color.BOLD + Color.GREEN + '"Inventory"' + Color.END +
          '\nor enter ' + Color.BOLD + Color.BLUE + '"Quit"' + Color.END + ' to quit the game.')
    print('-' * 60)


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


'''Boss battle trigger function that depends on which items are in the inventory'''


def boss_battle():
    weapon = inventory['Weapon']
    ammo = inventory['Ammo']
    aid = inventory['Aid']
    rings = inventory['Tools']
    global you_won
    print('"You enter the ' + Color.BOLD + Color.YELLOW + 'Foyer' + Color.END + ', searching for '
          'anything of use, but soon realize that the front door is cracked open. '
          '\nSuddenly, you hear a creak in the floorboards behind you. You turn around and see the ' + Color.BOLD
          + Color.PURPLE + 'Puppeteer' + Color.END + '\ncreeping behind you with the same menacing smile plastered '
          'across its face as before. With an unnatural\namount of force, the '
          + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ' shoves you, sending you flying through the '
          'front door, down the porch\nstairs, and crashing down onto the rocky ground outside.'
          ' Disoriented, you shakily rise to\nyour feet and prepare to fight for your life."')

    print('\n' + ('v' * 110) + '\n')
    input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

    if len(weapon) == 0 or len(ammo) == 0 or len(aid) == 0 or len(rings) < 5:
        if len(rings) < 5:
            print('\n"You\'re barely able to gather your bearings before an ungodly energy takes over your body.\n'
                  'Each iron rod left embedded into your flesh pulls aggressively at your tendons. You\nfeel yourself'
                  ' lifted from the soil, your entire weight pulling down against the hooks,\nscraping bone and muscle'
                  ' against iron. You are powerless. An unknown force holds you up,\nlike a macabre marionette, and'
                  ' all you can do is cry. As you dangle, the ' + Color.BOLD + Color.PURPLE + 'Puppeteer'
                  + Color.END + ' approaches\nyou with its menacing smile. It get closer, looking you over, and you '
                  'notice a sort of giddy\nexcitement in its eyes, as if it\'s just received a new toy. The '
                  'creature turns away from you,\nand you suddenly drop to the ground with a thud. As the creature'
                  ' walks away, you drag along\nbehind it, powerless; pulled like a doll through the mud."')
        elif len(aid) == 0:
            print('\n"The ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ' creeps down the stairs toward'
                  ' you. It raises an arm\nand beckons the sky above you, as if grabbing at something. When nothing '
                  'happens,\nits once giddy expression melts away into a dark, twisted scowl. You realize the creature'
                  '\nwas reaching for your phantom bindings. Since you were able to free yourself,\nthe creature '
                  'no longer has an easy way to control you. The creature, now enraged,\nstarts toward you. Your '
                  'heart begins to race, and you raise your arms to fight,\nbut just as quickly as you\'d gotten up,'
                  ' you collapse, and all fades to black. It appears\nyou\'ve lost too much blood to maintain '
                  'consciousness. You wade in and out,\nas you\'re dragged through the forest. When you finally'
                  ' reawaken, you find yourself\nhanging from fresh hooks in your flesh. The '
                  + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END +
                  ' approaches you with\nits menacing smile and that sort of giddy excitement in its eyes again.\n'
                  'The creature has found a new toy: you, its macabre marionette."')
        elif len(weapon) == 0:
            print('\n"The ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ' creeps down the stairs toward'
                  ' you. It raises an arm\nand beckons the sky above you, as if grabbing at something. When nothing '
                  'happens,\nits once giddy expression melts away into a dark, twisted scowl. You realize the creature'
                  '\nwas reaching for your phantom bindings. Since you were able to free yourself,\nthe creature '
                  'no longer has an easy way to control you. The creature, now enraged,\nstarts toward you. Your '
                  'heart begins to race, and you raise your arms to fight,\nbut you realize you hands won\'t be enough'
                  ' to defend yourself against the ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + '.\nYou '
                  'make a run towards the treeline, praying you\'ll be able to escape, or at least that you\'ll\nfind a'
                  ' tree branch thick enough to knock the creature down, but before you know it,\nthe creature smacks'
                  ' you across the ground, sending you flying into a tree, knocking you\nunconscious... You awaken to'
                  ' find yourself hanging from fresh hooks in your flesh. The ' + Color.BOLD + Color.PURPLE +
                  'Puppeteer' + Color.END + '\napproaches you with its menacing smile and that sort of giddy excitement'
                  ' in its eyes again.\nThe creature has found a new toy: you, its macabre marionette."')
        else:
            print('\n"The ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ' creeps down the stairs toward'
                  ' you. It raises an arm\nand beckons the sky above you, as if grabbing at something. When nothing '
                  'happens,\nits once giddy expression melts away into a dark, twisted scowl. You realize the creature'
                  '\nwas reaching for your phantom bindings. Since you were able to free yourself,\nthe creature '
                  'no longer has an easy way to control you. The creature, now enraged,\nstarts toward you. Your '
                  'heart begins to race, and you raise the shotgun and aim it directly\ninto the face of the creature.'
                  ' *click*...*click*,*click*,*click*... Your heart sinks.\nYou realize that you never found any ammo '
                  'for the shotgun. You swing the shotgun at the creature,\nstriking it, but the creature is hardly'
                  ' phased by the blow at all. In fact, the creature only seems\nangrier. You make a run towards the '
                  'treeline, praying you\'ll be able to escape, but before you\nknow it, the creature smacks'
                  ' you across the ground, sending you flying into a tree, knocking you\nunconscious... You awaken to'
                  ' find yourself hanging from fresh hooks in your flesh. The ' + Color.BOLD + Color.PURPLE +
                  'Puppeteer' + Color.END + '\napproaches you with its menacing smile and that sort of giddy excitement'
                  ' in its eyes again.\nThe creature has found a new toy: you, its macabre marionette."')
        return
    else:
        print('"The ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ' creeps down the stairs toward'
              ' you. It raises an arm\nand beckons the sky above you, as if grabbing at something. When nothing '
              'happens,\nits once giddy expression melts away into a dark, twisted scowl. You realize the creature'
              '\nwas reaching for your phantom bindings. Since you were able to free yourself,\nthe creature '
              'no longer has an easy way to control you. The creature, now enraged,\nstarts toward you. Your '
              'heart begins to race, and you raise the shotgun and aim it directly\ninto the face of the creature. '
              + Color.BOLD + Color.RED + '*BOOM*' + Color.END + '. The shotgun explodes with sound and light as\nyou '
              'fire one shot and then another into the ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END +
              '. The creature squeals and shrieks,\nas you reload and fire two more rounds. Your wounds ache under the'
              ' force of the recoil,\nbut you don\'t stop firing until the ammo box is empty.'
              ' Only then do you allow yourself\na moment to breath. From a distance, you cautiously '
              'gaze upon the creature. The once menacing\nbeast is now but a crumpled version of itself. Moments ago, '
              'it smiled as it fought\nfor control over your body; now it lay lifelessly, like the doll it '
              'always wanted."')

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
            'Shotgun Ammo',
            'Ammo',
            '\n"You lift the box of ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ', noting the weight and '
            'relieved\nit isn\'t empty. The box is missing a few shots from it, but it should\nbe enough to take down'
            ' the ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ', with a functioning shotgun."'
        ],
        'text': '"You open the small ceiling hatch of the attic and climb the pull down\nstairs'
                ' that present themselves. The attic appears to be meant for\nmaintenance, rather than storage,'
                ' so you\'re not able to find much\nas you step through a thick fog of dust and cellulose."',
        'added_text': '"You notice a dusty box, hiding beside the opening to the attic,'
                      '\nthat you believe reads "' + Color.BOLD + Color.GREEN + '{}' + Color.END + '"."'
    },
    'Children\'s Bedroom': {
        'item': [
            'Hammer',
            'Tools',
            '\n"You reach down and grab the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '. It\'s clean, as if'
            ' new. At least\nit wasn\'t used on the children... You doubt it\'ll be a good enough weapon\nagainst the '
            + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ', but maybe you can use it to remove a shackle.'
            ' You\npull your left ankle in and hold an edge of the iron against the floor,\nsteadying it '
            'to get a clean shot. You swing the hammer down onto the ring\nand pain shoots up your leg. The recoil '
            'of each strike twists the iron\nbracelet against bone. The pain is excruciating, but it\'s too late to '
            'stop now.\nThe bottom most edge of the ring if already nearly flattened. You moan\nin pain until one '
            'final strike weakens the iron enough that you\'re able\nto split the rod and pull the loop from your leg.'
            ' You drop the once clean\ntool down onto the once clean floor, now covered in your own blood,'
            ' and,\nalthough it could be used again, you decide the pain was far too\ngreat to relive. You limp'
            ' towards the door, hoping you don\'t\nbleed out before you\'re able to escape."'
        ],
        'text': '"Compared to the rest of the house, this room is surprisingly spotless.\nThe room clearly'
                ' belonged to two children, as toys adorn the shelves.\nThe room looks tidy,'
                ' but played in. A bunk-bed on the far end of the room\nstands quietly,'
                ' with the blankets on each bed carefully slipped down,\nas if the children were'
                ' taken gently from their beds while they slumbered.\nThe stillness is almost '
                + Color.BOLD + 'more' + Color.END + ' unnerving than the chaos outside of this room."',
        'added_text': '"One thing stands out though. You notice, peering out from beneath the\nbottom bunk,'
                      ' a ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ' resting, out of place.'
                      ' There\'s something especially\nsinister about how it hides in wait..."'
    },
    'Main Bedroom': {
        'item': [
            'Rusted Cutting Pliers',
            'Tools',
            '\n"You pick up the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '. They\'re very rusted,\nbut you hope'
            ' they hold together long enough to cut at least\none of your cuffs. You elect the back of the neck,'
            ' hoping it\'ll\nbe the least painful method to remove something in a place\nso difficult to reach.'
            ' Your theory is thankfully correct, as you\nendure minimal injury cutting the iron link. The most painful'
            ' part\nwas removing the warped metal from the thick muscle that lines\nyour neck. Painful, yes, but '
            'necessary. You move to use the pliers\non the next ring, but realize the previous task had ruined\nthe '
            'rusty blades, damaging them beyond repair."'
        ],
        'text': '"You enter what appears to be the master bedroom where a man\nand a woman shared a bed.'
                ' The smell of decay churns your gut as you\nlook around, spotting blood on every surface, even the'
                ' attic door\nto your north. From the looks of the blood soaking the room'
                ', the wife\nwas attacked in bed and dragged into the bathroom. Checking the walk-in\ncloset,'
                ' you find her final resting place... or places. You find her\ncut to pieces, limbs hanging from the '
                'closet railings with puddles\nof coagulated blood pooled on the floor beneath them."',
        'added_text': '"Walking from the closet, you notice a pair of ' + Color.BOLD + Color.GREEN + '{}' + Color.END +
                      '\nresting on the bed\'s right side table, accompanied by many\nof the wife\'s fingers and toes."'
    },
    'Bathroom': {
        'item': [
            'Rusted Hack Saw',
            'Tools',
            '\n"You pick up the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ' and get to work on your shackles.\n'
            'You start on the ring that threads your right shin. As you saw\nat the ring, you feel the vibration '
            'rattling against your bones.\nYou grip the ring tighter, hoping to absorb the vibration as you\n'
            'saw harder. The iron ring chips away at the saw\'s rusted teeth, but you\nmanage to cut through the iron '
            'before the saw snaps, rendering it\nuseless. You pull the ring from its roots, a painful, but manageable '
            '\nexperience, and exhale a breath of silent victory."'
        ],
        'text': '"You walk into the bathroom to find, unironically, a blood bath.\nEvery inch of the bathroom '
                'is covered in blood, the source of which\nis likely connected to the crop of mutilated limbs '
                'protruding\nout of the deep sea of blood, like icebergs, in the bathtub."',
        'added_text': '"On the counter beside the sink, you spot a ' + Color.BOLD + Color.GREEN + '{}' + Color.END +
                      ',\nlikely the tool of choice used for the aforementioned\ndismemberment."'
    },
    'Back Entryway': {
        'text': '"You look around at the home you\'ve taken refuge in. The smell of death\nlooms thick within air. '
                'Bloodied boot prints trail from room to room,\nand bloodied hand prints '
                'decorate the walls. All around you sits\nthe signs of a massacre. There is a door on each '
                'side of you, and down\nthe hall, you can see a dining table and the front door on its far side."'
    },
    'Dining Room': {
        'item': [
            'Rusted Kitchen Shears',
            'Tools',
            '\n"You grab the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ' and position them around\nthe '
            'iron ring that curves out from your right wrist. Although\nthe shears weren\'t made to cut through metal,'
            ' the fact that\nthe link was forged so crudely works in your favor. The shears\nbend and twist the metal'
            ' until ultimately snapping the link.\nUnfortunately, the process bends and snaps the shears as well,'
            '\nbreaking them for good."'
        ],
        'text': '"On the dining table there is a rancid feast. A decaying roast\nsits at the table\'s center,'
                ' surrounded by flies and maggot infested\nside dishes. Four plates surround the spread, donned with'
                ' uneaten,\nmolded food, but upon closer inspection, you notice that the plates\ndid not'
                ' in fact go untouched. The food was not eaten, but appears to\nhave been ' + Color.BOLD + 'played'
                + Color.END + ' in? It\'s as if the family was sat at the table together,\nand ' + Color.BOLD +
                'pretended' + Color.END + ' to eat, as if controlled by someone playing with\ndolls in a dollhouse."',
        'added_text': '"Beside the infested roast lies a pair of ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '."'
    },
    'Foyer': {
        'text': ''
    },
    'Washroom': {
        'item': [
            'Rusted Garden Shears',
            'Tools',
            '\n"You grab the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ' and retract their arms,'
            ' making them\neasier to handle. You slip the blades into the hoop that threads your\nleft wrist.'
            ' Awkwardly, you position the arms of the shears, pointing them\naway from you. You try to squeeze '
            'the arms together, but the ring\nmerely rolls between the blades, causing it to twist within your muscles.'
            '\nYou writhe in pain, but reestablish your grasp, making sure your next cut is\nmore secure than the last.'
            ' You try to cut your shackle once more with one\nfinal squeeze, and manage to snap the iron...'
            ' as well as the shears\nthemselves. I guess the shears couldn\'t hold up to their deterioration."'
        ],
        'text': '"You enter the small washroom, and the smell of death chokes you.\nYou see '
                'a little boy\'s arm hanging from the opening of the dryer\nand the top of a little girl\'s'
                ' head peaking out from the open\nwasher. You suspect there is more to be seen inside'
                ', but decide\nyou\'d rather not know. Instead you check behind the toilet\n'
                'and around the utility sink for anything that could help you."',
        'added_text': '"On the long, steel counter top beside the utility sink\nyou find '
                      + Color.BOLD + Color.GREEN + '{}' + Color.END + ', covered in blood."'
    },
    'Kitchen': {
        'item': [
            'First Aid Kit',
            'Aid',
            '\n"You find a ' + Color.BOLD + Color.GREEN + '{}' + Color.END + '! Thankfully, there are plenty of '
            'bandages\nand antiseptic to treat the wounds from the accident, as well as\nthe gaping wounds made by the '
            + Color.BOLD + Color.PURPLE + 'Puppeteer\'s' + Color.END + ' barbaric attempts\nat surgical implantation. '
            'Patching up all of your wounds, especially\nas you remove your bindings, should ensure that you stay'
            ' steady\nlong enough to defeat the ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + '."'
        ],
        'text': '"You enter the kitchen, wafting through the flies that leap from\nthe fridge and counter tops in'
                ' surprise. On the stove, you find pots\nof molding food, filled with maggots. The largest pot is'
                ' filled with,\nwhat seem to be, human hearts. Your suspicions are quickly confirmed\nas you glance'
                ' over to the other human entrails rotting in the sink."',
        'added_text': '"You notice bloody gauze below the drawers on the left side of the\noven. '
                      'It lies, unrolled next to a bloody hand print that streaks away,\nback '
                      'out of the kitchen to another room. Clearly, someone was caught\nbefore they'
                      ' could patch themselves up. Hopefully, that means\nthere might still'
                      ' be a ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ' nearby."'
    },
    'Living Room': {
        'item': [
            'Shotgun',
            'Weapon',
            '\n"You pick up the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ', resting near the feet '
            'of the dead man,\nslumped and decaying, in his armchair. Although there are clear\nsigns of rust '
            'beginning to eat at the metal, the gun still seems\nto work just fine. Too bad there isn\'t any ammo'
            ' left inside.\nCombined with ammo, this would probably be an adequate weapon to\ntake down the '
            + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + '."'
        ],
        'text': '"Looking around, you\'re sure the room was once a comfortable,\n'
                'love-filled space for the small family. Now, the room hosts\nonly the chilling, final resting place '
                'of their patriarch.\nUpon inspecting the bloody prints left by his boots, you get a\n'
                'glimpse into his final moments. You see that he walked in and out\nof each room, likely attacking and'
                ' disposing of each family member,\nbefore sitting in his armchair, here, shotgun propped between his'
                '\nlegs, and firing a shot directly into his skull. You question what\nkind of sick person could kill'
                ' their entire family like that...\nthen you notice the iron rings embedded into his arms and legs..."',
        'added_text': '"You spot, in a puddle of blood at the foot of the armchair,\n'
                      'the ' + Color.BOLD + Color.GREEN + '{}' + Color.END + ', lying coldly in mourning."'
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

'''Title'''

title()

input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

print('\n' + ('v' * 110) + '\n')


'''Intro'''

print(Color.BOLD + Color.PURPLE + '"Puppeteer"\n' + Color.END)
print('    "Head throbbing and vision blurry, you awaken on the ground in the middle of a dark forest.\n'
      'As you blink yourself awake, you notice your vehicle, totaled, a few yards from where you lay.\n'
      'You spot bloody drag marks in the dirt leading to you from your car. Did someone remove you\nfrom the wreckage? '
      'As you struggle to stand, you realize that there are metal rings, amateurishly\ncrafted out of car scraps,'
      ' embedded into your wrists, shins, and one into the back of your neck.\nThey appear to be tethered to'
      ' wires that somehow disappear upward into the sky, connected to something\ndark and otherworldly.'
      ' You look like some sort of grotesque puppet. Before you get the chance\nto pull at your abhorrent bindings, '
      'a long, twisted creature with a menacing smile\nemerges from the woods to continue working on you.'
      ' Without thinking, you jump to your feet,\nwounds searing with pain, and run for your life. '
      'You don\'t dare to look back, certain that if you were\nto stumble, the creature, your twisted '
      + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + ', would overtake you in matter of '
      'moments.\nYou spot the lights of a home in the distance, and with your last burst of energy,'
      '\nyou manage to reach the home, slam through the back door, and lock the door behind you."\n')

input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

print(('v' * 110) + '\n')

print(Color.BOLD + Color.RED + '                                      "This is'
      ' your final refuge."\n\n' + Color.END + Color.BOLD + '"You must find a way to remove all five of your shackles, patch up your bleeding wounds,'
      ' and find a weapon\n to defend yourself if you\'re to have any hope of escaping here '
      'with control over your own life."\n' + Color.END)

print('\n' + ('v' * 110))

input(Color.BOLD + Color.CYAN + 'Press Enter to Continue' + Color.END + '\n')

'''While playing loop that cycles between checking room location, showing the instructions,
awaiting and verifying user input, then either moving rooms, checking the inventory, getting an item,
quitting the game, or triggering the boss battle, unless the input is invalid. To break the loop
the user either wins or loses the game, or quits manually.'''

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
            print('\n' + ('v' * 110) + '\n')
            print(Color.BOLD + Color.GREEN + (' ' * 27) + '"YOU WIN!"' + Color.END)
            print(Color.BOLD + Color.GREEN + (' ' * 20) + '"Thank you for playing:"\n\n' + Color.END)
            title()
            print('\n' + ('v' * 110) + '\n')
            break
        else:
            print('\n' + ('v' * 110) + '\n')
            print(Color.BOLD + Color.RED + (' ' * 50) + '"YOU ARE DEAD"' + Color.END)
            print('\n' + ('v' * 110) + '\n')
            break
print('\nThanks for playing ' + Color.BOLD + Color.PURPLE + 'Puppeteer' + Color.END + '.')
