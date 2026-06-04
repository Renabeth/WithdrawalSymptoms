# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn",color="#b0d5f5")
define v = Character("Valerie", color="#a881f7")
define k = Character("Kit", color="#ff7033")
define l = Character("Landlord")



# The game starts here.
# labels act as bookmarks or chapter titles that assign a name to a specific point in your game's script
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at left

    # music - loops | sound - plays once
    "Scene 1"
    play music "audio/sfx_knocking.mp3" volume 0.3
    e "uggghhh..."
    e "hhhhhhhhhhhhhhhhhhhhhhhhhh,,,"
    e "Not again..."
    e "What time even is it?"
    # e "What should I do?"

    menu:
        "Stay in bed":
            jump stay_in_bed
            

        "Answer the door":
            e "Alriiiight I'm coming."
            

    "I struggle to sit up, but I finally get out of my rickety ass bed and start walking to the door."
    e "FUCK."
    "Shit, I forgot to throw out the needles from last night."
    v "mmmnmmm?"
    e "Sorry, stabbed myself. Go back to bed."
    "Right, almost forgot about that."
    "I toss the needle into the disgusting mess of a floor and make my way to the door."
    e "Alright, alright I'm here. Stop the banging for God's sake."
    stop music fadeout 1.0 
    "I open the door, and an intense beam of light temporarily blinds me."
    "Before I can even get a word out, her voice pierces my ears."
    # e "You've created a new Ren'Py game."
    show eileen happy at right with fade

    # v "Once you add a story, pictures, and music, you can release it to the world!"


    # This ends the game.

    return

label stay_in_bed:
    "Despite the obnoxious banging, I can't muster the strength to answer the door. I'm too hungover for this."
    "It'll probably stop."
    "Eventually."
    stop music fadeout 1.0
    # v "What do you want to do?"
    
    menu:
        "Drugs":
            "drugs are cool"
            jump memory_hallucination_1
        
        "Fuck":
            "hell yeah"

        "Talk with Kit (alt)":
            "yadayada"


label memory_hallucination_1:
    "Scene - memory hallucination 1"



label good_ending:
    

label suicide_ending:
    

label bad_touch_ending:
    

label infidelity_ending:
    