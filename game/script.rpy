# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn",color="#b0d5f5")
define v = Character("Valerie", color="#a881f7")
define k = Character("Kit", color="#ff7033")
define l = Character("Landlord")

screen bedroom():
    add "bg room"
    modal True

    imagebutton auto "bg room_bed_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "My bed")
        unhovered SetVariable("screen_tooltip","")
        action Jump ("bed")



# The game starts here.
# labels act as bookmarks or chapter titles that assign a name to a specific point in your game's script
label start:

    scene bg room

    label room:
        call screen bedroom

    label bed:
        "That's my bed. What do you mean there's no where to sit?"
        # jump room


    # Code for glitched/blocked out text
    "dialogue here {glitch=5.0}{color=#bababa}{b}██████{/b}{/color}{/glitch}"

    $ achievement.grant("first_achievement")
    "You unlocked an achievement!"
    


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # music - loops | sound - plays once

    show eileen happy at left

   

    # Scene 1 - Game Starts Here 
    # TODO: First cemetery scene will go here


    play music "audio/sfx_knocking.mp3" volume 0.2 #kit knocking
    e "uggghhh..."
    e "hhhhhhhhhhhhhhhhhhhhhhhhhh,,,"
    e "Not again..."
    e "What time even is it?"

    #FIRST CHOICE
    menu:
        "Stay in bed":
            jump stay_in_bed
            

        "Answer the door":
            jump answer_door


         
    
label stay_in_bed:
    # Scene - Eve doesn't answer door talks with Val in bed

    "Ughh,, I'm too hungover for this"
    "It'll probably stop."
    "Eventually."
    "Looks like Val is still passed out. Lucky bitch."
    "I can barely hear her breathing, it's cute in a way."
    v "*yawwwn* Good morning baby."
    v "...who's banging?"
    e "I dunno some dipshit."
    v "Prolly the neighbor, doesn't she know we're trying to sleep?"
    e "I know, what kind of person bangs on someone's door so early?"
    "I glance over at our alarm clock."
    "It's 3PM."
    
    menu:
        "Do drugs":
            jump mem_hallucination_1
        
        "Fuck":
            jump sesbian_lex

        "Answer the door":
            jump answer_door_alt # Talk with Kit (alternate)


    # TODO: add walking sound effects
label answer_door:
    # Scene - Eve gets out of bed and answers the door
    stop music fadeout 1.0
    # temporarily removed dialogue here

    menu:
        "Sit around and do nothing":
            "nothing"
        "Fuck":
            jump sesbian_lex
        "Listen to some music": #Eve & Val get high as they listen to music. All music choices lead to the mem_hallucination 2.
            menu:
                "deaftunes - throughout the fern": #needs to be persistant 
                    "yap about deaftunes"
                    jump mem_hallucination_2
                "The Reused - Drawing":
                    "yap about the reused"
                    jump mem_hallucination_2
                "Samsara - In Vitro":
                    "yap about samsara"
                    jump mem_hallucination_2

    #end scene
    return

label mem_hallucination_1:
    "Scene - memory hallucination 1"
    # "Landlord knocks on door"
    # Are you high? (choices - yes, no, do you really care)
    # eventually jump to mem hallucination 2
    # TODO: Only jump to landlord scene if choices are stay in bed > drugs
    jump landlord_knocks

label mem_hallucination_2:
    "Scene - memory hallucination 2. Evelyn Remembers her and Valerie having an argument about their drug usage and Val being vindictive and pushing the blame on her"
    # Evelyn Remembers her and Valerie having an argument about their drug usage and Val being vindictive and pushing the blame on her
    jump cemetery_scene_1

label mem_hallucination_3:
    "Scene - memory hallucination 3. Evelyn Remembers a doctors appointment where a doctor berates her and Valerie for their excessive drug usage"
    jump cemetery_scene_2


label mem_hallucination_4:
    "Scene - memory hallucination 4. Evelyn Remembers having sex with Valerie and making her take drugs until she overdoses"

label sex_hallucination_1:
    "Scene - sex hallucination 1"

label sex_hallucination_2:
    "Scene - sex hallucination 2"
    # Eve takes drugs while jerking off the Valerie, causes hallucinations to get worse/more violent/aggresive

    menu:
        "I can't deal with this right now": # Leads to infidelity ending
            ""
            jump infidelity_ending
        "I don't want to stop. I want to touch her.": # Leads to bad touch ending
            ""
            jump bad_touch_ending


label landlord_knocks:
    "Scene - Landlord knocks on the door"
    l "are you high?"

    # all choices here lead to the same outcome
    menu:
        "Yes":
            ""
        "No":
            ""
        "Do you really care?":
            ""
        
    "some dialogue here"
    jump mem_hallucination_2


label cemetery_scene_1:
    "Scene - Eve and Hallucination Valerie make up and go to the cemetery"
    # choices - try to patch things up / panic???

    menu:
        "Try to patch things up":
            "Eve and Hallucination Valerie make up and go to the cemetery. Valerie goads Eve into remembering"
            jump mem_hallucination_3
        "??? panic??":
            "route not finished yet"

label cemetery_scene_2:
    "Scene - Choices for True ending/Suicide/Delusion ending. Happens after mem hallucination 3"

    menu:
        "Apologize to her":
            # True ending path
            menu:
                "Look at her":
                    ""
                    menu:
                        "See her.":
                            "Eve notices Valerie isnt visually clear (hallucinations) is rotting (hallucination of body)"
                            "Eve runs back to the apartment with Valerie's hallucination screaming at her"
                            "Evelyn discovers Valerie is dead"
                            menu:
                                "KILL YOURSELF":
                                    "suicide ending path"
                                    jump suicide_ending
                                "Vomit":
                                    "Evelyn vomits again"
                                    menu:
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                        "Persist.":
                                            "Evelyn freezes in shock"
                                            menu:
                                                "KILL YOURSELF":
                                                    jump suicide_ending
                                                "Get high until you can't think":
                                                    "Do drugs (jump mem_hallucination_4)"
                                                    # TODO might write mem_hallucination_4 dialogue here to make things simpler
                                                    menu:
                                                        "KILL YOURSELF":
                                                            jump suicide_ending
                                                        "Get help":
                                                            jump true_ending
        "She's still wrong":
            "Path to Delusion Ending"
            jump delusion_ending



                                  
                               
                                
                    
                    

                        



#The "sex" scene
# TODO: This label may be unnecessary 
label sesbian_lex:
    "Scene - Eve has 'sex' with Vallerie"
    jump mem_hallucination_1

label answer_door_alt:
    # Scene - If Eve intially doesn't answer the door
    stop music fadeout 1.0
    
    # Potentially alternate paths to infidelity, good, and suicide endings

    # May not need this
    # k "What are your plans for today?"

    #menu:
        #"Sit around and do nothing":
            #""
        #"Fuck":
            #jump sesbian_lex
        #"Listen to some music":
            #""
    
    #jump mem_hallucination_4
        

label post_music:
    # Scene - Eve starts crying listening to music after hallucination 2
    # e "I can't stop crying"

    menu:
        "Try to talk to your girlfriend":
            #Leads to mem hallucination 4 and good ending
            "Eve tries to talk it out with Val but she starts subconciously blocking out what Valerie says until running out in a panic where she runs into kit bringing over some fruits"
        "Fuck the feelings away":
            jump sex_hallucination_2
            ""
        "Get so fucked up you don't feel anymore":
            "" 


label suicide_ending:
    "Scene - Suicide Ending"
    

label bad_touch_ending:
    # Choices here always result in bad touch
    menu:
        "Stoke.":
            ""
        "Touch her.":
            ""
        
    #Continue having "sex"
    menu:
        "Stoke.":
            ""
        "Touch her.":
            ""

    #Continue having "sex" (again)
    menu:
        "Touch her.":
            "Evelyn tries to touch Valerie while they are having sex and her hallucination disappears"

    

label infidelity_ending:
    "Eve runs into Kit and is pent-up sexually"
    menu:
        "Fuck Kit": # locks into infedility
            "Kit refuses and mentions Valerie"
            menu:
                "Lie":
                    "Eve fucks Kit while crying and making excuses about Valerie (Infidelity Ending)"
        "Try to talk to her": #Re-routes you to Delusion depending on choices
            "Eve tries to explain her and Valerie's issues"
            menu:
                # TODO: This option should only appear if you pick "Try to talk to her" (other routes that lead to delusion can't reroute to infidelity. I'm tired and my brain hurts gn)
                "Fuck Kit": # back to infidelity 
                    ""
                "Confide in her": # Delusion endning
                    "Kit says that Eve is in the wrong"
                    jump delusion_ending


label delusion_ending:
    "Evelyn never learns of Valerie's death and impersonates her / mentally becomes 'her'"

label good_ending:

label true_ending:
    "Scene - True ending."
    "Eve confides in Kit that Valerie is dead"
    menu:
        "Mourn.":
            "Eve buries Valerie"


# This ends the game.

    #return