import time
import random


def blockers(constantblock):
    if "1" not in count:
        intheway = ['a fearsome Fer-De-Lance, coiled and ready to strike '
                    'has slithered \n out of the foliage', 'a snarling Jaguar '
                    'threatening to pounce \n has padded out of the '
                    'underbrush', 'the ghost of Pacal himself, the legendary '
                    'Mayan King of Palenque, '
                    '\n appears in a cloud of vapours ']
        pathblocker = random.choice(intheway)
        print("but", pathblocker, "to block your path.")
        count.append("1")
        time.sleep(2)
        constantblock.append(pathblocker)
    else:
        print("but", constantblock[0], "to block your path.")
        time.sleep(2)


def print_pause(message):
    print(message)
    time.sleep(2)


def wrong_choice():
    if "Pacal" in constantblock[0]:
        print_pause("The ghost of Pacal looms above you for a moment, \n"
                    "and then gobbles your eternal soul.")
        print_pause("You have lost the game, and your soul.")
        play_again()
    elif "Fer" in constantblock[0]:
        print_pause("The deadly snake strikes quickly from its coiled "
                    "position, \n firmly attaching itself to your face.")
        print_pause("Unfortunately, you have joined the ranks "
                    "of the faceless.")
        print_pause("You have lost the game, and your face.")
        play_again()
    elif "Jaguar" in constantblock[0]:
        print_pause("The Jaguar springs towards you and ravages "
                    "your soft fleshy body, \n leaving nothing for the birds.")
        print_pause("Unfortunately, you are nowhere to be found.")
        print_pause("You have lost the game, and your existence.")
        play_again()


def intro():
    print_pause("You emerge from the thick oppressive jungle into "
                "a clearing \n to see the ancient "
                "ruins of Palenque towering in front of you.")
    print_pause("For a moment you are in awe, and feel a shimmering "
                "upon the air \n that whispers of hidden legends and "
                "centuries-old blood sacrifices.")
    print_pause("To your left is the path to the famed "
                "Temple of Inscriptions,")
    blockers(constantblock)
    print_pause("To your right is the path to the Temple of the Jaguar. "
                "\n You wonder what your archeology "
                "professor, Sherbert Mandrill, would say now.")
    if "flute" in inventory:
        print_pause("You get a sudden urge to play your new found flute.")
        play_flute()


def proper_input(adventurer, firstoption, secondoption):
    while True:
        response = input(adventurer).lower()
        if firstoption in response:
            break
        elif secondoption in response:
            break
        else:
            print_pause("Have you had tequila for breakfast again "
                        "Adventurer?, \n"
                        "That response is neither option I have offered.")
    return response


def get_flute():
    response = proper_input("Would you like to pick up the flute?: ",
                            "yes", "no")
    if "yes" in response:
        print_pause("You pick up the small wooden flute, "
                    "and head back to the entrance.")
        inventory.append("flute")
        intro()
    elif "no" in response:
        print_pause("You head back to the entrance empty handed, "
                    "and wonder how you will get to \n"
                    "the Temple of Inscriptions. Your lack of "
                    "musicality is most disappointing.")
        intro()
        get_input()


def play_flute():
    response = proper_input("Would you like to play your flute?: ",
                            "yes", "no")
    if "yes" in response:
        if "Pacal" in constantblock[0]:
            print_pause("You start to play the flute and like magic, "
                        "the ghost of Pacal")
            print_pause("does a fancy dance and dissolves into the "
                        "vapours of the jungle.")
            temple_inscriptions()
        elif "Fer" in constantblock[0]:
            print_pause("You start to play the flute and like magic "
                        "the Fer-de-Lance")
            print_pause("does a slithery dance and slithers off with "
                        "your underpants.")
            print_pause("You truly understand what it means to be a "
                        "jungle commando.")
            temple_inscriptions()
        elif "Jaguar" in constantblock[0]:
            print_pause("You start to play the flute and like magic "
                        "the Jaguar")
            print_pause("does a freaky little shimmy and shakes his "
                        "tail off into the vines.")
            temple_inscriptions()
    elif "no" in response:
        wrong_choice()


def get_input():
    response = proper_input("Please indicate which way you would like to go.",
                            "left", "right")
    if "left" in response:
        if "flute" in inventory:
            temple_inscriptions()
        else:
            wrong_choice()
    if "right" in response:
        temple_jaguar()


def temple_jaguar():
    print_pause("You stride toward the Temple of the Jaguar and "
                "are surprised to see you are alone.")
    print_pause("The temple looms impressively at the far end of "
                "the courtyard with the Jaguar \n"
                "throne carved deep within the bas relief.")
    if "flute" in inventory:
        "After seeing nothing else to do here, you head back to the entrance."
    else:
        print_pause("You notice there is a small wooden flute "
                    "discarded on the ground.")
        get_flute()


def temple_inscriptions():
    print_pause("You finally head down the path of the "
                "Temple of Inscriptions.")
    print_pause("As you reach the momentous temple you pause "
                "for a moment to take \n"
                "in the majesty of one of the finest structures in the ruins.")
    print_pause("You see your hat you forgot on a nearby bench "
                "the day before \n"
                "and quickly pick it up.")
    print_pause("You will now not receive the sunburn of your "
                "life in future digs.")
    print_pause("You have won the game, and the fight against "
                "crispy noggins everywhere. ")
    play_again()


def play_again():
    response = proper_input("Would you like to play again?: ", "yes", "no")
    if "yes" in response:
        inventory.clear()
        count.clear()
        constantblock.clear()
        play_game()
    if "no" in response:
        print_pause("Thanks for adventuring through the jungle with us!")
        print_pause("Don't forget to tip your programmers!")
        print_pause("Mention your quest when swimming in the cenote "
                    "for a discount on two day old tortillas.")


def play_game():
    intro()
    get_input()


inventory = []
count = []
constantblock = []
play_game()
