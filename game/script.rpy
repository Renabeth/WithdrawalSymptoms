# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn",color="#b0d5f5")
define v = Character("Valerie", color="#a881f7")
define k = Character("Kit", color="#ff7033")

define eh = Character("Evelyn?",color="#b0d5f5")
define vh = Character("Valerie?", color="#a881f7")
define kh = Character("Kit?", color="#ff7033")

image eve normal = im.Scale("images/eve normal.png", 500, 1100) # only need to define these once per character portrait
image eve annoyed = im.Scale("images/eve annoyed.png", 500, 1100)
image eve angry = im.Scale("images/eve angry.png", 500, 1100)
image eve high = im.Scale("images/eve high.png", 500, 1100)
image eve horny = im.Scale("images/eve horny.png", 500, 1100)
image eve mental breakdown = im.Scale("images/eve mental breakdown.png", 550, 1100)
image eve smirk = im.Scale("images/eve smirk.png", 500, 1100)
image eve sobbing = im.Scale("images/eve sobbing.png", 500, 1100)
image eve tear up = im.Scale("images/eve tear up.png", 500, 1100)
image eve tired = im.Scale("images/eve vomit.png", 500, 1100)

image val normal = im.Scale("images/val normal.png", 550, 1100)
image val angry = im.Scale("images/val angry.png", 550, 1100)
image val annoyed = im.Scale("images/val annoyed.png", 550, 1100)
image val crying = im.Scale("images/val crying.png", 550, 1100)
image val depressed = im.Scale("images/val depressed.png", 550, 1100)
image val happy = im.Scale("images/val happy.png", 550, 1100)
image val smug = im.Scale("images/val smug.png", 550, 1100)





default inspect_mode = False
default screen_tooltip = ""
default came_from_music = False

screen bedroom_inspect():

    # Do not use modal True: it blocks normal dialogue clicks.
    add "bg room"

    textbutton ("Inspect On" if inspect_mode else "Inspect Off"):
        xpos 1700
        ypos 1000
        action ToggleVariable("inspect_mode")

    if inspect_mode:
        imagebutton auto "bg room_bed_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "My bed")
            unhovered SetVariable("screen_tooltip", "")
            action Call("inspect_bed")

    if screen_tooltip:
        text screen_tooltip:
            xpos 20
            ypos 930

    
    #$ achievement.grant("first_achievement")
    #$ renpy.notify("Achievement Unlocked: First Achievement!")


screen content_warning():

    tag menu

    add Solid("#000")

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 1000

        vbox:
            spacing 50

            text "Content Warning" size 60 xalign 0.5

            text """
Withdrawal Symptoms has themes of:

• Drug addiction and substance abuse
• Toxic relationships
• Hallucinations
• Death and Grieving
• Suicide

If you're ok with that we hope you enjoy the game :)
""" xalign 0.5 text_align 0.5

            textbutton "Continue":
                xalign 0.5
                action Return()

# The game starts here.
# labels act as bookmarks or chapter titles that assign a name to a specific point in your game's script
label start:



    #Prologue will go here
    #scene bg cemetary
    call screen content_warning with fade

    scene bg room with fade
    #show screen bedroom_inspect #Put this in scenes that you can inspect

    "dialogue here {glitch=5.0}{color=#bababa}{b}██████{/b}{/color}{/glitch}"


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # This shows a character sprite. A placeholder is used, but you can

    # music - loops | sound - plays once
   

    # Scene 1 - Game Starts Here 
    show eve normal at left
    
    #show val normal at right

    play sound "audio/sfx_knocking.mp3" volume 1.0 #kit knocking
    e "uggghhh..."
    play sound "audio/sfx_knocking.mp3" volume 1.0
    e "hhhhhhhhhhhhhhhhhhhhhhhhhh,,,"
    e "Not again..."
    e "What time even is it?"
    play sound "audio/sfx_knocking.mp3" volume 1.0
    #hide screen bedroom_inspect #will need to hide inspect during choices, re-enable after
    #FIRST CHOICE
    menu:
        "Ughhh"
        "Stay in bed":
            jump stay_in_bed
            

        "Answer the door":
            jump answer_door


    # hide screen bedroom_inspect
    return


label inspect_bed:
    "That's my bed. What do you mean there's nowhere to sit?"
    return
         
    
label stay_in_bed:
    # Scene - Eve doesn't answer door talks with Val in bed
    show screen bedroom_inspect

    "Ughh,, I'm too hungover for this"
    "It'll probably stop."
    "Eventually."
    stop music fadeout 1.0
    "I roll onto my side and look at Val."
    "Looks like she's still passed out. Lucky bitch."
    "I can barely hear her breathing. It's kinda cute, in a way."
    v "*yawwwn* Good morning baby."
    v "...Who's banging?"
    e "I dunno, someone with no decency"
    v "Prolly the neighbor, doesn't she know we're trying to sleep?"
    e "I know, what kind of person bangs on someone's door so early?"
    "I glance over at our alarm clock."
    "It's 3PM."
    "I look back at Val, she's looking at me with her puppy dog eyes."
    v "Bedhead really suits you, y'know?"
    e "Yeah it matches how little I take care of the rest of my body."
    "Val pouts."
    v "You know that's not what I mean."
    e "Well I think your bedhead doesn't suit you." #this part may change
    e "It looks much better than the rest of you, stands out."
    "God I'm such a dick."
    v "Well I guess if we're up anyways we should do something"
    e "Yeah, guess so."
    


    
    menu:
        v "What do you wanna do?"
        "Do drugs":
            jump mem_hallucination_1
        
        "Fuck":
            jump sesbian_lex

        "Answer the door":
            jump answer_door_alt # Talk with Kit (alternate)


    # TODO: add walking sound effects
label answer_door:

    # Scene - answer the door
    "Alriiiight I'm coming!"
    play sound "audio/sfx_knocking.mp3" volume 1.0 #kit knocking
    "I struggle to sit up, hangover's a total bitch."
    "I rest my hand on the bed-"
    e "AGH- fuck"
    "A sharp pain runs up my arm, wakes me right up."
    "I look down at my hand, a used needle is stuck right in the middle of my palm."
    "I rip it out, hurts like a bitch."
    "Blood drips down my hand onto the bedsheet. Luckily it's so gross already, you can barely notice it."
    "Can't believe I forgot to throw out the needles from last night. That's what I get for leaving shit around."
    show val normal at right
    v "hmmnmmm?"
    "Shit, I woke her up."
    e "Sorry, just stabbed myself. Go back to bed."
    play sound "audio/sfx_knocking.mp3" volume 1.0 #kit knocking
    "Right, forgot about that."
    "I toss the needle into my disgusting mess of a floor and start stumbling towards the doorway."
    hide val normal
    #play music "audio/sfx_floor_creak.mp3" volume 0.3
    e "Alright, alright I'm here. Stop the banging for god's sake."
    #stop music fadeout 1.0
    "I open the door, the sunlight from the hallway balcony is so bright it immediately blinds me."
    "I slam my eyes shut to keep the light out."
    "Before i can even get a word out her voice pierces my ears."
    k"EEEEEEEEEEEEEEEEEEEEEEEEEVVVEEEEEEEEEEE!!!!!!!!♡"
    "Oh god."
    "I don't even get a chance to react before I can feel her wrap her arms tight around me."
    "I finally open my eyes to be greeted with her all too happy grinning face."
    e "I've told you it's Evely-"
    k "AWWWW,, but Eve is just SUCH a cute nickname!♡"
    e "-and can you please stop yelling. Val is asleep."
    e "If you wanna talk move it into the hallway..."
    e "..without me."
    "I slam the door shut. Back in (fix later)"
    "Her incessant shouting manages to reach me even through the cheap, busted up, plywood door."
    k "OKAY WELL, I’M GONNA BRING BY SOME FRUIT LATER!!! SEE YOU THEN!!! *♡*"
    e "God damn it."
    k "ALSO MY MOM SAYS YOU CAN HAVE ANOTHER MONTHS EXTENSION ON YOUR RENT!!!*♡*"
    "I wander back to bed and slam my face into my pillow. Thankfully no needles this time."
    show val happy at right
    v "mmm? Good morning baby."
    show eve smirk at left
    e "Hey, Kit came by."
    v "Ughh, did you cover for me?"
    e "...in a way"
    v "Whatever, as long as she's gone."
    e "Yeah totally... except she's coming back in a little bit to bring us more fruit"
    v "Noooooooo… shiiiit."
    e "It couldn't have been that bad."
    v "You literally don't get it."
    v "Last time she asked if she could borrow my vibrator."
    v "In front of all my coworkers."
    v "I wanted to kill myself."
    v "Frankly I still might, we have a razor somewhere in this shithole I'm sure."
    v "Look for it for me. I'll start drowning myself in the sink in the meantime."
    e "I think there might be too many mold infested dishes in there, you probably have a better chance of dying from disease than any attempt at drowning."
    v "Welp, there goes that plan."
    "Valerie lays down next to me in a huff, she's so light I can barely feel her hit the bed."
    play sound "audio/sfx_stomach_growl.mp3" volume 0.5
    "Well I guess I'm not much better, wish we had money for takeout."
    "Wish we had money at all."
    v "Guess suicide's off the menu, you have any better plans for the day?"



    menu:
        "Sit around and do nothing":
            "nothing"
            $ came_from_music = False

        "Fuck":
            jump sesbian_lex
        "Listen to some music":
            $ came_from_music = True
            e "This silence is killing me, I'm gonna put on an album."
            "I start rummaging through the pile of garbage next to the CD player."
            v "Pick something that isn't total trash please."
            e "Got it, so none of your CDs?"
            "Val roles her eyes at me, fair."
            menu:
                "deaftunes - throughout the fern":
                    $ persistent.heard_deaftunes = True
                    "yap about deaftunes"

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    jump mem_hallucination_2

                "The Reused - Drawing":
                    $ persistent.heard_reused = True
                    "yap about the reused"

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    jump mem_hallucination_2

                "Mindless Self Benevolence - or":
                    $ persistent.heard_reused = True
                    e "Here we go."
                    show or-album-cover at truecenter
                    show val annoyed at right
                    v "Ugh. Really? This shitty band again?"
                    e "This shit fucks and you can't deny it."
                    e "I've heard you sing Medication around the apartment before."
                    v "Don't they literally say slurs in like half of their songs?"
                    e "Listen I'm not saying the damn slurs."
                    v "You still shouldn't support them."
                    e "I don't know if this four dollar thrift store CD qualifies as supporting them."
                    e "Now shut it and vibe."
                    hide or-album-cover
                    "I sit back and relax on the bed while the sounds of the album fill the apartment."
                    "The noises of the roads outside bleed through the walls and muddle with the melodies of the music."
                    "God, this brings back memories."
                    "We've been dating for almost 2 years now."
                    "Ugh, feels like I'm back there."
                    show eve tired at left
                    "My vision starts to blur and the walls are... wrong."
                    "I try blinking to clear my eyes but it only gets worse."
                    "My ears start to ring with familiar voices."

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    jump mem_hallucination_2

                "Samsara - In Vitro":
                    $ persistent.heard_samsara = True
                    "yap about samsara"

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    jump mem_hallucination_2
    #end scene
    return


label answer_door_alt:
    # Scene - If Eve intially doesn't answer the door
    
    # Potentially alternate paths to infidelity, good, and suicide endings

    e "Honestly that knocking is pissing me off."

label drugs:
    #Scene - Eve does drugs
    e "Drugs. I wanna do drugs."


label mem_hallucination_1:
    "Scene - memory hallucination 1"
    # "Landlord knocks on door"
    # Are you high? (choices - yes, no, do you really care)
    # eventually jump to mem hallucination 2
    # TODO: Only jump to landlord scene if choices are stay in bed > drugs
    jump landlord_knocks

label mem_hallucination_2:
    scene bg room with pixellate
    show val angry at right
    show eve angry at left
    vh "I just wish you would dress better, we're going out for fucks sake."
    eh "What the hell's the matter with how I dress?"
    vh "You look homeless, your top is full of holes and covered in shit."
    eh "Oh what so I dont always look perfect like-"
    show val depressed at right
    vh "Don't."
    eh "Why not?"
    eh "You always bring her up."
    vh "Evelyn, I'm still grieving."
    eh "It doesn't sound like grieving when you compare me to her every time I do something wrong."
    show eve normal at left
    eh "She wouldn't smoke in the apartment. She would clean up after we eat."
    eh "Well maybe I do smoke inside."
    eh "Maybe I don't clean up after you."
    eh "..."
    eh "Whatever, I'm gonna get high."
    show val annoyed at right
    vh "No. No the fuck you aren't."
    vh "We have somewhere to be jackass."
    vh "You can't just spend all your time getting high, dressing like a slob and getting nothing done."
    vh "I mean, it's no wonder i'm the only one here who can hold down a goddamn job."
    show eve angry at left
    "I stood up in a rage"
    eh "Well it's not my fault that you're so used to having a girlfriend who looks perfect all the fucking time for you."
    show val crying at right
    eh "If you want someone as perfect as her, why don't you go and dig {glitch=5.0}{color=#bababa}{b}█████{/b}{/color}{/glitch} out of her grave and date her instead."
    "Valerie's tears had already hit the floor by the time my sentence had stopped."
    show eve normal at left
    eh "Shit- I didn't mean that- I'm sorry-"
    vh "Well at least {glitch=5.0}{color=#bababa}{b}█████{/b}{/color}{/glitch} acted like she loved me instead of just saying it."

    if came_from_music:
        $ came_from_music = True 
        jump after_music
    
    return


    # Evelyn Remembers her and Valerie having an argument about their drug usage and Val being vindictive and pushing the blame on her
    #jump cemetery_scene_1

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


label after_music:
    "Scene - Eve starts crying listening to music after hallucination 2"
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
label sesbian_lex:
    # "Scene - Eve has 'sex' with Vallerie"
    #jump mem_hallucination_1
    e "God, I wanna fuck." 


        


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


transform credits_scroll:
    ypos 1.2                   
    linear 15.0 ypos 0.30       

    #return

screen credits():

    add Solid("#000")

    vbox:
        
        #at credits_scroll
        xalign 0.5
        spacing 30

        text "Withdrawal Symptoms" size 60 xalign 0.5

        null height 100

        text "Writing\nAubrey" xalign 0.5
        text " Art\nCeci" xalign 0.5
        text "Programming\n      Serena" xalign 0.5
        text "Music\nJoe" xalign 0.5

        null height 50

        text "Thank you for playing!" size 60 xalign 0.5

label credits:

    scene black with fade
    show screen credits

    $ renpy.pause(10.0, hard=True)

    hide screen credits with fade

    return