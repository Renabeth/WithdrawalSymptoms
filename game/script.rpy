# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Evelyn",color="#b0d5f5")
define v = Character("Valerie", color="#a881f7")
define vq = Character("???", color="#a881f7")
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
image eve tired = im.Scale("images/eve tired.png", 500, 1100)
image eve vomit = im.Scale("images/eve vomit.png", 500, 1100)
image eve crying = im.Scale("images/eve crying.png", 500, 1100)


image val normal = im.Scale("images/val normal.png", 500, 1100)
image val normal 75 = im.Scale("images/val normal 75.png", 500, 1100)
image val normal 25 = im.Scale("images/val normal 25.png", 500, 1100)
image val angry = im.Scale("images/val angry.png", 500, 1100)
image val annoyed = im.Scale("images/val annoyed.png", 500, 1100)
image val crying = im.Scale("images/val crying.png", 500, 1100)
image val depressed = im.Scale("images/val depressed.png", 500, 1100)
image val happy = im.Scale("images/val happy.png", 500, 1100)
image val smug = im.Scale("images/val smug.png", 500, 1100)

image kit normal = im.Scale("images/kit normal.png", 650, 930)
image kit concerned = im.Scale("images/kit concerned.png", 650, 930)
image kit vomit = im.Scale("images/kit vomit.png", 650, 930)





#Booleans
default inspect_mode = False
default screen_tooltip = ""
default came_from_music = False
default came_from_cant_feel_anymore = False
default came_from_drugs = False
default came_from_cemetery_1 = False
default came_from_offer_kit_drugs = False
default came_from_answer_phone = False
default came_from_val_discovery = False
default came_from_sesbian_lex = False
default came_from_music_alt = False
default came_from_true_ending = False
default came_from_good_ending = False
default came_from_suicide_ending = False
default came_from_delusion_ending = False
default came_from_bad_touch = False
default came_from_cemetery_1_alt = False
default came_from_get_even_higher = False





# Custom Transitions
#used for WAKING UP
define fuzzy_transition = ImageDissolve( 
    "images/fuzzy_transition.jpg",2.0,        
    ramplen=128
)

define fuzzy_transition_fast = ImageDissolve( 
    "images/fuzzy_transition.jpg",1.0,        
    ramplen=128
)

#used for ENTERING HALLUCINATIONS
define spiral_transition = ImageDissolve( 
    "images/spiral_transition.jpg",2.2,        
    ramplen=128,
    
)

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
Withdrawal Symptoms features themes of:

• Drug addiction and substance abuse
• Toxic relationships
• Hallucinations
• Death and Grieving
• Infidelity & Sexual Assault
• Suicide

If you're ok with that we hope you enjoy the game :)
""" xalign 0.5 text_align 0.5

            textbutton "Continue":
                xalign 0.5
                action Return()

# The game starts here.
# labels act as bookmarks or chapter titles that assign a name to a specific point in your game's script
label start:

    stop music fadeout 1.0
    call screen content_warning with fade

    #Prologue
    scene bg cemetery with fade
    show eve normal at left
    play music "audio/sfx_night_ambience.mp3"
    "It's chilly."
    "Figures. I pick the one night where the weather decides to be a pain in the ass."
    "The fog and flickering streetlamps aren't doing this place any favors either. I can barely make out the tombstones."
    scene bg cemetery with dissolve
    show eve normal at left
    "I don't even know why I came out here."
    "Pretty sure no one buried here gives a rats ass about me."
    "At least the fog will hide the smoke so I don't get kicked out."
    "*flick* *flick*"
    "God damn it."
    "*flick*"
    "Shit, lighter's busted."
    "I do not have it in me right now to walk back home."
    "I look back up and across the field of foggy graves I see a girl standing over a grave."
    "Weirdly enough she isn't looking down and bawling her eyes out."
    "Instead, she's looking at me."
    "Now she's walking towards me."
    show val normal at right
    "I didn't take anything that strong today, I swear."
    "I don't need some freaky ghost shit happening right now either."
    "She stops and looks at me, her eyes are bloodshot. Probably not from the same reason mine are."
    vq "Need a light?"
    e "Aren't you supposed to be like, mourning your mom or whatever?"
    show val annoyed at right
    vq "My girlfriend, {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch}."
    vq "She would've told me to stop staring and help you out."
    show val normal at right
    e "Well that's very kind of her, it's not often I get to smoke with a ghost."
    "She stares at me for a second, then pulls out a tiny purple lighter and-"
    vq "I don't usually see many druggies in this cemetery, certainly none as approachable as you."
    e "Guess I'm special."
    e "You want some?"
    show val annoyed at right
    vq "No thanks, I don't like the taste of nicotine."
    e "I wouldn't be too worried about that, got something much tastier in these."
    v "Name's Valerie by the way."
    show val happy at right
    show eve smirk at left
    e "Cute name, if anyone hung out with me they'd probably call me Evelyn."
    v "So Evelyn, how often do you aimlessly wander around cemeteries?"
    e "Usually whenever I'm on the hunt for grieving widows to pick up."
    show val normal at right
    "She winces a little, yeah probably a shitty line to pull on the chick visiting her dead girlfriend."
    "Dumbass."
    v "For the record if you're trying to pick up chicks then the cemetery probably isn't your best bet."
    e "And yet you're still talking to me."
    "She pauses for a moment."
    v "Hey so, you got a phone?"
    "I watch her reach into her pocket and pull out a crumpled up receipt for flowers."
    "She scribbles her number on it and hands it to me."
    show val happy at right
    v "You seem cool, keep in contact."
    e "First time I've gotten a girl's number in a cemetery."
    v "You were the one trying pick up lines on grieving widows."
    e "Guess so..."
    "She practically runs away before I can respond."
    hide val happy
    show eve normal at left
    "Weird, I'll probably never see her again anyways so whatever."
    stop music fadeout 1.0

    scene bg room with fade
    #show screen bedroom_inspect #Put this in scenes that you can inspect

    #"dialogue here {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch}"


    show eve tired at left
    
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
        "Ughhh,,,"
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
    #show screen bedroom_inspect
    play sound "audio/sfx_knocking.mp3" volume 0.8
    show eve normal at left
    "Ughh,, I'm too hungover for this."
    "It'll probably stop."
    play sound "audio/sfx_knocking.mp3" volume 0.8
    "Eventually."
    "I roll onto my side and look at Val."
    "Looks like she's still passed out. Lucky bitch."
    "I can barely hear her breathing. It's kinda cute, in a way."
    show val smug at right
    v "*yawwwn* Good morning baby."
    v "...Who's banging?"
    e "I dunno, someone with no decency."
    v "Prolly the neighbor, doesn't she know we're trying to sleep?"
    e "I know, what kind of person bangs on someone's door so early?"
    "I glance over at our alarm clock."
    show eve annoyed at left
    "It's 3PM."
    "I look back at Val, she's looking at me with her puppy dog eyes."
    v "Bedhead really suits you, y'know?"
    show eve smirk at left
    e "Yeah it matches how little I take care of the rest of my body."
    "Val pouts."
    show val annoyed at right
    v "You know that's not what I mean."
    e "Well I think your bedhead doesn't suit you." #this part may change
    e "It looks much better than the rest of you, stands out."
    "God I'm such a dick."
    v "Well I guess if we're up anyways we should do something."
    e "Yeah, guess so."
    


    
    menu:
        v "What do you wanna do?"
        "Drugs":
            play music "audio/music_track_1.mp3"
            $ came_from_drugs = True
            show eve smirk at left
            show val smug at right
            e "Drugs. I wanna do drugs."
            show val normal at right
            v "Already? We just woke up."
            e "I think we're both too sober and we should fix that."
            v "Yeah okay, you get them though I'm still sleepy."
            e "Yes ma'am."
            "I crawl out of our bed and walk over to the light switch."
            show eve normal at left
            "I flick it on."
            show val annoyed at right
            v "Aughhhh,,, too bright,,,, shut it offfff."
            "She hides her head under the blanket."
            e "Sorry, sorry."
            "Guess I gotta rummage through our shit in the dark."
            show bg drugs with dissolve
            "I wander over to the one table in our room and grab a random pill bottle."
            "Good enough."
            "I flop back into our bed and open the bottle, taking two pills myself and leaving the rest up to Val."
            show bg pillow with dissolve
            show val happy at right
            v "Thank you baby."
            show eve high at left
            e "Shhhhh, just take your pillssss."
            "I lay there on the bed staring at the ceiling."
            "I feel Val's weight next to me as I start to feel the high."
            "I close my eyes and feel it wash over me, but just as I do I hear a familiar voice."
            "I open my eyes, but my vision is burry now."
            "I hear two voices, they slowly start to become clearer."
            #hide eve normal
            stop music fadeout 1.0
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
    play music "audio/music_track_1.mp3" fadein 0.3
    "I rest my hand on the bed, the mattress sags into the floor"
    "A sharp pain runs up my arm, wakes me right up."
    "I look down at my hand, a used needle is stuck right in the middle of my palm."
    "I rip it out, it's painful. Hope I don't catch something."
    "Blood drips down my hand onto the bedsheet. Luckily it's so gross already, you can barely notice it."
    "Can't believe I forgot to throw out the needles from last night.” 
    “That's what I get for leaving shit around."
    show val normal at right
    v "hmmnmmm?"
    "Shit, I woke her up."
    e "Sorry, stabbed myself. Go back to bed."
    play sound "audio/sfx_knocking.mp3" volume 1.0 #kit knocking
    "Right, forgot about that."
    "I toss the needle into my disgusting mess of a floor and start stumbling towards the doorway."
    hide val normal
    #play music "audio/sfx_floor_creak.mp3" volume 0.3
    e "Alright, alright I'm here. Stop the banging for god's sake."
    #stop music fadeout 1.0
    "I open the door, the sunlight from the hallway balcony is so bright it immediately blinds me."
    "I slam my eyes shut to keep the light out."
    "Before I can even get a word out her voice pierces my ears."
    k"EEEEEEEEEEEEEEEEEEEEEEEEEVVVEEEEEEEEEEE!!!!!!!!♡"
    "Oh god."
    "I don't even get a chance to react before I can feel her wrap her arms tight around me."
    "I finally open my eyes to be greeted with her all too happy grinning face."
    e "I've told you it's Evelyn."
    k "AWWWW,, but Eve is just SUCH a cute nickname!♡"
    e "and can you please stop yelling. Val is asleep."
    e "If you wanna talk move it into the hallway..."
    e "..without me."
    "I slam the door shut."
    "Her incessant shouting manages to reach me even through the cheap, busted up, plywood door."
    k "OKAY WELL, I'M GONNA BRING BY SOME FRUIT LATER!!! SEE YOU THEN!!! *♡*"
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
    e "Yeah totally... "
    e "except she's coming back in a little bit to bring us more fruit."
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
    "My stomache growls, guess I'm not much better. Wish we had money for takeout."
    "Wish we had money at all."
    stop music fadeout 1.0



    menu:
        v "Guess suicide's off the menu, you have any better plans for the day?"
        "Sit around and do nothing":
            #TODO: Need to add scene
            "nothing"
            #$ came_from_music = False

        "Fuck":
            jump sesbian_lex
        "Listen to some music":
            $ came_from_music = True
            play music "audio/music_track_3.mp3"
            show eve normal at left
            e "This silence is killing me, I'm gonna put on an album."
            "I start rummaging through the pile of garbage next to the CD player."
            v "Pick something that isn't total trash please."
            e "Got it, so none of your CDs?"
            "Val roles her eyes at me, fair."
            menu:
                "Deaftunes - Throughout the Fern":
                    $ persistent.heard_deaftunes = True
                    "Here's a classic."
                    #show drawing-album-cover at truecenter
                    show val happy at right
                    v "I thought you weren't gonna put on my CDs?"
                    show eve smirk at left
                    e "Had a change of heart"
                    e "plus Vhulva is a great song."
                    v "It's an {b}AMAZING{/b} song."
                    v "You can't {b}JUST{/b} appreciate the classics though. Ramone, the first song on NX is iconic."
                    e "Yeah yeah whatever you say dweeb."
                    "She's making a mocking face at me."
                    #hide drawing-album-cover
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
                    stop music fadeout 1.0
                    jump mem_hallucination_2

                "The Reused - Drawing":
                    $ persistent.heard_reused = True
                    "Oh yeah here we go"
                    show drawing-album-cover at truecenter
                    show val smug at right
                    v "Y'know I actually kinda prefer their older stuff."
                    show eve smirk at left
                    e "I mean don't get me wrong, I enjoy their self titled-"
                    e "but this album is nonstop hits"
                    e "and definitely underrated."
                    v "I mean it's got some good tracks, but The Smell of Paint is so iconic."
                    v "No track here has this much staying power."
                    e "Whatever you say poser."
                    hide drawing-album-cover
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
                    stop music fadeout 1.0
                    jump mem_hallucination_2

                "Mindless Self Benevolence - or":
                    $ persistent.heard_reused = True

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    e "Here we go."
                    show or-album-cover at truecenter
                    show val annoyed at right
                    v "Ugh. Really? This shitty band again?"
                    show eve smirk at right
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

                    
                    stop music fadeout 1.0
                    jump mem_hallucination_2

                "Samsara - In Vitro":
                    $ persistent.heard_samsara = True

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    e "Here's something."
                    "I pick up the Samsara CD. Val loves this band."
                    show val happy at right
                    v "I thought you weren't gonna put on my CDs?"
                    e "Had a change of heart."
                    show val smirk at left
                    e "PLus their music is nostalgic to me."
                    v "You're so old. My mom would play this in the car when I was a kid."
                    e "Well clearly you have a young and hip mom."
                    v "Or you're just old."
                    e "We're practically the same age."
                    v "I was literally 14 when you graduated high school."
                    show eve annoyed at left
                    e "Ugh gross don't say that or else I'm picking another CD."
                    show eve smirk at left
                    e "And besides, I didn't graduate high school."
                    show val annoyed at right
                    v "And what an invigorating life you lead now."
                    e "I know, I'm amazing."
                    e "Now zip it and listen to your mommy's music taste."
                    "I sit back and relax on the bed while the sounds of the album fill the apartment."
                    "The noises of the roads outside bleed through the walls and muddle with the melodies of the music."
                    "God, this brings back memories."
                    "We've been dating for almost 2 years now."
                    "Ugh, feels like I'm back there."
                    show eve tired at left
                    "My vision starts to blur and the walls are... wrong."
                    "I try blinking to clear my eyes but it only gets worse."
                    "My ears start to ring with familiar voices."
                    stop music fadeout 1.0
                    jump mem_hallucination_2
   
    #end scene
    return


label answer_door_alt:
    # Scene - If Eve intially doesn't answer the door
    
    # Potentially alternate paths to infidelity, good, and suicide endings
    play music "audio/music_track_1.mp3" fadein 0.3
    e "Honestly that knocking is pissing me off."
    play sound "audio/sfx_knocking.mp3" volume 1.0 #kit knocking
    "Guess I'll go see what she wants now."
    hide val annoyed
    "I stumble towards the door, the faint memory is still racking my brain."
    "I reach the door and shout through the crack."
    show eve angry at left
    e "Kit we're kinda busy right now! Could you like, piss off."
    show kit normal at right
    k "AWWWW but i brought over fruit!!!!!!!! ☆♡"
    k "C'MONNN EVEEE just let me innnnnn,, you'll LOVE these fruitss!!!**"
    e "If I come out there will you shut up."
    k "Mhm mhm sure yes totally~"
    "She's not gonna shut up either way."
    "But I don't want her to bother Val while she comes down."
    show bg hallway with dissolve
    "I open the door and walk outside, closing it behind me."
    k "Oh WOW, your apartment looks kinda gross Eve..."
    k "How do you live like that?"
    k "You NEED to let me come over and deep clean your place sometime."
    e "That's not happening."
    k "OH! I almost forgot!"
    "She places a heavy basket of fruit into my hands."
    k "Grew these myself!! Hehe. ♡~"
    "She looks way too proud of herself, gross."
    k "Oh my gosh Eve-"
    e "Evelyn."
    k "Eve your eyes are so red, are you high?"
    e "Not yet."

    menu:
        "Offer kit drugs":
            jump offer_kit_drugs
        "They're all for me":
            jump take_drugs_alone


label kit_at_door:
    #Scene - Kit at the door after the player decides to do drugs
    play music "audio/music_track_3.mp3"
    scene black with fuzzy_transition
    scene bg room with fuzzy_transition
    show eve high at left
    "The high is finally starting to wear off."
    show eve annoyed at left
    play sound "audio/sfx_knocking.mp3" volume 1.0 #kit knocking
    "Oh good, the banging is back."
    "Guess I'll go see what she wants now."
    "I stumble towards the door, the faint memory is still racking my brain."
    "I reach the door and shout through the crack."
    show eve angry at left
    e "Kit we're kinda busy right now! Could you like, piss off."
    show kit normal at right
    k "AWWWW but i brought over fruit!!!!!!!! ☆♡"
    k "C'MONNN EVEEE just let me innnnnn,, you'll LOVE these fruitss!!!**"
    show eve annoyed at left
    e "If I come out there will you shut up."
    k "Mhm mhm sure yes totally~"
    "She's not gonna shut up either way."
    show eve normal at left
    "But I don't want her to bother Val while she comes down."
    "I open the door and walk outside, closing it behind me."
    show bg hallway with dissolve
    show kit concerned at right
    k "Oh WOW, your apartment looks kinda gross Eve..."
    k "How do you live like that?"
    show kit normal at right
    k "You NEED to let me come over and deep clean your place sometime."
    e "That's not happening."
    k "OH! I almost forgot!"
    show eve annoyed at left
    "She places a heavy basket of fruit into my hands."
    k "Grew these myself!! Hehe. ♡~"
    "She looks way too proud of herself, gross."
    k "Oh my gosh Eve-"
    e "Evelyn."
    

    menu:
        k "Eve your eyes are so red, are you high?"
        "Yes":
            show eve smirk at left
            k "OH! I was right!"
            e "Yeah."
            k "Cool!"
            k "My mom doesn't let me do drugs."
            e "Sucks for you I guess."
        "No":
            show eve smirk at left
            k "Oh! Silly me, it's rude to assume."
            e "I lied, I am high."
            k "OH! Wait so I was right!"
            e "No, I lied again."
            "Kit pouts from my teasing."
            e "Ok I lied, I wasn't lying, I really am high."
        "Do you really care?":
            show eve smirk at left
            k "Hmmmm, not really."
            e "Cool."
            k "Y'know my mom doesn't let me do drugs."
            e "I don't care."
    
    show eve annoyed at left
    e "So... I'm gonna go back inside."
    k "OKAY!! Hope you enjoy the fruit!!!!!!!"
    "I slam the door on her."
    hide kit normal
    show bg room with dissolve
    show val smug at right
    v "What was that about?"
    e "Fruit."
    show eve normal at left
    menu:
        "That gave me such a headache, I gotta do something to relax."
        "Get even higher":
            $ came_from_get_even_higher = True
            "Not being sober will help this."
            "I go grab whatever from the table and lay in bed with Val."
            e "Hey let's get high some more."
            "I don't even wait for her response before putting an acid tab on my tongue and waiting for it to kick in."
            show eve high at left
            "When it does I feel the walls close in a little and the familiar voices start to come back into earshot."
            stop music fadeout 0.3
            jump mem_hallucination_2

        "Listen to some music":
            $ came_from_music_alt = True
            e "This silence is killing me, I'm gonna put on an album."
            "I start rummaging through the pile of garbage next to the CD player."
            v "Pick something that isn't total trash please."
            e "Got it, so none of your CDs?"
            "Val roles her eyes at me, fair."
            menu:
                "deaftunes - throughout the fern":
                    $ persistent.heard_deaftunes = True
                    "Here's a classic."
                    #show drawing-album-cover at truecenter
                    v "I thought you weren't gonna put on my CDs?"
                    e "Had a change of heart"
                    e "plus Vhulva is a great song."
                    v "It's an {b}AMAZING{/b} song."
                    v "You can't {b}JUST{/b} appreciate the classics though. Ramone, the first song on NX is iconic."
                    e "Yeah yeah whatever you say dweeb."
                    "She's making a mocking face at me."
                    #hide drawing-album-cover
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
                    stop music fadeout 0.3
                    jump mem_hallucination_2

                "The Reused - Drawing":
                    $ persistent.heard_reused = True
                    "Oh yeah here we go"
                    show drawing-album-cover at truecenter
                    v "Y'know I actually kinda prefer their older stuff."
                    e "I mean don't get me wrong, I enjoy their self titled-"
                    e "but this album is nonstop hits-"
                    e "and definitely underrated."
                    v "I mean it's got some good tracks, but The Smell of Paint is so iconic."
                    v "No track here has this much staying power."
                    e "Whatever you say poser."
                    hide drawing-album-cover
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
                    stop music fadeout 0.3
                    jump mem_hallucination_2

                "Mindless Self Benevolence - or":
                    $ persistent.heard_reused = True

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

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

                    
                    stop music fadeout 0.3
                    jump mem_hallucination_2

                "Samsara - In Vitro":
                    $ persistent.heard_samsara = True

                    if (persistent.heard_deaftunes
                        and persistent.heard_reused
                        and persistent.heard_samsara):
                        $ achievement.grant("oldhead")
                        $ renpy.notify("Achievement Unlocked: Oldhead")

                    e "Here's something."
                    "I pick up the Samsara CD. Val loves this band."
                    v "I thought you weren't gonna put on my CDs?"
                    e "Had a change of heart."
                    e "PLus their music is nostalgic to me."
                    v "You're so old. My mom would play this in the car when I was a kid."
                    e "Well clearly you have a young and hip mom."
                    v "Or you're just old."
                    e "We're practically the same age."
                    v "Girl I was literally 14 when you graduated high school."
                    e "Ugh gross don't say that or else I'm picking another CD."
                    e "And besides, I didn't graduate high school."
                    v "And what an invigorating life you lead now."
                    e "I know, I'm amazing."
                    e "Now zip it and listen to your mommy's music taste."
                    "I sit back and relax on the bed while the sounds of the album fill the apartment."
                    "The noises of the roads outside bleed through the walls and muddle with the melodies of the music."
                    "God, this brings back memories."
                    "We've been dating for almost 2 years now."
                    "Ugh, feels like I'm back there."
                    show eve tired at left
                    "My vision starts to blur and the walls are... wrong."
                    "I try blinking to clear my eyes but it only gets worse."
                    "My ears start to ring with familiar voices."
                    stop music fadeout 0.3
                    jump mem_hallucination_2
            # listen to music 
            #jump after_music_alt

label get_even_higher_cont:
    scene bg black with fuzzy_transition
    scene bg room with fuzzy_transition
    show eve normal at left
    #play music "audio/music_track_3.mp3" fadein 0.3
    "I start to come back down."
    "I look over at Valerie, I'm full of anger thinking about that argument."
    e "Val."
    show val normal at right
    v "Hm?"
    show eve angry at left
    e "I'm so pissed."
    v "What, why?"

    menu:
        "Try to patch things up":
            jump cemetery_scene_1
        "Confront her on the argument":
            #play music "audio/music_track_2"
            "Why do you always do that?"
            v "Do what?"
            e "You always bring her up whenever we fight."
            e "Like she's your guardian angel, I just-"
            e "it makes me feel so fucking pathetic."
            e "I hate it."
            v "Baby, this seems like it's a lot for you, I think we should just talk this out."
            menu:
                v "Let me take you somewhere"
                "Hear her out":
                    jump cemetery_scene_1_alt
                "Fuck her til she knows I was right":
                    ""
                "Get so high you leave this world":
                    play music "audio/music_hallucination.mp3"
                    e "No."
                    v "Baby-"
                    "I ignore her."
                    "Fuck this."
                    "I don't need to take this shit from her."
                    "I'm too sober to deal with this"
                    "I rummage around the apartment and eat a half finished edible, a mushroom and some random pill before laying down on the floor."
                    menu:
                        "Valerie is wrong.":
                            "She's wrong."
                            menu:
                                "I know Valerie is wrong.":
                                    "She's always wrong."
                                    menu:
                                        "I know more than Valerie.":
                                            "I'm always right."
                                            menu:
                                                "I know what Valerie really wants.":
                                                    "Evelyn is always right."
                                                    menu:
                                                        "I know Valerie":
                                                            jump delusion_ending_drugs


            


label offer_kit_drugs:
    scene bg hallway
    show eve smirk at left
    show kit normal at right
    #TODO: kits room background
    $ came_from_offer_kit_drugs = True
    play music "audio/music_track_3.mp3"
    e "You wanna join me?"
    k "I dunnoooo, my mom does't really want me doing drugs."
    e "Aww c'mon, they're just like the plants you grow it's nothing unnatural."
    k "I meannn, I GUESS if it's plant based I can try."
    k "Should I come inside?"
    show eve normal at left
    e "No. It's gross in there."
    k "Awwwwwwwwwww, c'mon let me clean it up just a LITTLE."
    e "Nope, off limits."
    k "Okayyy FINE, my apartment then!!!!!"
    "She grabs my wrist tightly and drags me over to her apartment."
    "I break free for a second to lock my door."
    show bg room kit with dissolve
    "The second we enter her apartment I'm blinded by bright colors and plants everywhere."
    "We sit down on her floor."
    k "SOOO what drugs are we doing!! hehe"
    show eve annoyed at left
    e "You are {i}very{/i} enthusiastic."
    k "Well I'm all excited now!!!"
    e "Alright, alright."
    "I pull out a baggie of mushrooms from my pocket, Kit lights up at the sight."
    k "MUSHROOMS!!♡♡"
    e "Shhh, not so damn loud, jesus."
    k "Oh! Right,, we gotta be... secretive..."
    show eve angry at left
    e "No you dipshit you're just gonna make me deaf."
    "Kit and I each take some."
    show eve high at left
    "Me a lot more than her."
    k "Welp, down the hatch! ⋆°✩"
    "We lay back and relax, I let my eyes rest as everything feels nice."
    "I hear some voices I recognize and I open my eyes."
    "No one's there but the walls feel weird, and the voices start getting louder."
    jump mem_hallucination_2

label answer_phone:
    scene black with fuzzy_transition
    scene bg room kit with fuzzy_transition
    #"Scene - Eve answers Val's phone"
    "I feel myself returning to reality."
    "I look over at Kit who's also starting to come down."
    "The argument is still ringing through my head."
    "She was such a bitch that night. Wouldn't leave me the hell alone."
    play music "audio/music_track_1.mp3"
    show kit normal at right
    show eve normal at left
    k "EVE! That felt so good OMG. Do you have any more??"
    show eve high at left
    e "Yeah, it feels good, and no, I don't."
    show eve normal at left
    "I probably do have more at the apartment but I'm not telling her that."
    "Suddenly I feel a persistent buzz in my pocket."
    "I reach in there and pull out a phone."
    "It's not mine though, it's Valerie's. I must've accidentally taken it this morning."
    show eve annoyed at left
    "Shit, she's getting a call."
    "It's one of her friends, I shouldn't answer."
    "I'll just text back for her."
    "\"Hey sorry, can't answer rn im with my girlfriend\""
    "It buzzes again immediately."
    "\"kk! we just havent called in awhile so i wanted to hear your voice! call me l8r\""
    k "OH HEY! Isn't that Valerie's phone?"
    k "I'd recognize her SUPER cute phone case anywhere! ✩~"
    

    menu:
        k "Why do you have her phone?"
        "Explain why you have the phone":
            e "Oh uh, I think I grabbed it by accident this morning."
            k "Oh! Okay!"
            k "How's Val been?? I haven't seen her in FOREVER."
            k "Is she avoiding me? I haven't even seen her at her job."
            e "She's fine, she just quit her job is all."
            k "OH? Why?"
            show eve normal at left
            e "They weren't paying her enough, had to uh look elsewhere."
            k "Where's she working now?"
            e "She's still looking okay."
            
            menu:
                k "Well how has your relationship been~~"
                "Confide in her":
                    $ came_from_answer_phone = True
                    e "To be honest, it's been... a little rocky."
                    k "Oh! Spill the beans girl I can give advice!"
                    "Ugh, she's way too excited about this."
                    "I should just back out, or lie."
                    e "Truth is, I've been... remembering things."
                    k "Mhm mhm??"
                    e "Fights. Old fights we've had."
                    k "Oh."
                    "She looks like she's regretting being so excited now that it's serious."
                    show eve crying at left
                    e "Val has always been so damn critical of me, always criticizing the way I live my life."
                    e "Comparing me to her ex-girlfriend, like she loves her more than me."
                    k "Oh Eve, that's terrible."
                    e "Thank you. It's good to have someone be on my goddamn side for once."
                    e "There was this one time with this doctor..."
                    e "I can just barely remember it."
                    e "It was like..."
                    jump mem_hallucination_3
                

                    #"I storm back to the apartment and lay on my bed next to Val." #TODO: idk why this is here
        "Flirt with Kit to get her off your back":
            e "Oh, y'know.."
            e "Hey Kit?"
            k "Yeah?"
            e "Anyone every tell you that you are very pretty?"
            k "Oh um, yeah sometimes,,"
            e "Well, I think you are {i}very{/i} pretty."
            "I crawl over to her and put my hand on her chin."
            k "EVE!!"
            e "Yeah?"
            "She's blushing."
            k "E-EVE w-what about valerie?!"
            Eve "Shhhh, it's fine trust me, she's into it when I do this"
            Kit "I-I- I dunno if I'm comfortable Eve,,"
            Eve "Hey, heyy it's fine."
            "I run my hand along her side, I watch her react to it."
            "I lean in and kiss her."
            "She doesn't pull away."
            menu:
                "Fuck Kit.":
                    play music "audio/music_track_2.mp3"
                    k "Eeeveee,, mnmmnmnn.."
                    e "c'monn~"
                    "I kiss her deep again."
                    "I grab her hand, she doesn't fight back."
                    "I put her hand under my top and on my chest."
                    e "Do you like my little tits"
                    "She's nodding her head and whimpering."
                    "Wow, she's even more subby than me. It's so cute."
                    k "Eve... a-are you sure?"
                    e "Hmm?"
                    k "Are you sure Valerie is okay with us..."
                    menu:
                        "Lie.":
                            jump infidelity_ending





label kit_comes_over:
    #"Scene - kit comes over to eves apartment"
    scene black with fuzzy_transition
    scene bg room kit with fuzzy_transition
    play music "audio/music_track_3.mp3"
    e "And... yeah..."
    k "Eve... I think she was just worried about you."
    e "N-no she.. she just wants to make me like her stupid ex."
    k "Eve I think you're just uncomfortable with her loving both of you."
    k "It seems like you're just pushing her away."

    menu:
        "Why don't we go back to your apartment and talk it out with her, okay?"
        "Bring Kit back to your apartment":
            jump val_discovery
        "I know Valerie better than her":
            e "Fuck off, you both just wanna turn meinto her stupid perfect ex."
            e "You're even worse than her, you think you know her."
            k "Eve I-"
            e "THAT'S NOT MY FUCKING NAME"
            menu:
                "I know Valerie.":
                    jump delusion_ending_kit



label val_discovery:
   
    #Scene - Eve and Kit discover Val is dead
    scene bg room
    $ came_from_val_discovery = True
    play music "audio/music_track_1.mp3"
    e "Fine."
    "I stand up and walk with Kit back over to our apartment."
    "I feel uneasy about this but I can't place why."
    "I unlock the door and walk in, Kit follows behind me."
    e "Yeah so, here's where we live."
    e "Sorry if it smells like shit we don't have guests over."
    e "Baby! I'm home!"
    show val normal at right #change expression later
    v "Oh hey! What's Kit doing here?"
    e "Oh y'know she-"
    k "OH!! Eve! I think she's sleeping!"
    e "What?"
    e "No she's right here."
    stop music fadeout 0.3
    "Just as I finish my thought I look up at Kit-"
    "and she's vomitting."
    k "Oh my god..."
    k "sh-she's-"
    k "Dead."
    e "Um no Kit, she's right here."
    show val normal 75 at right with fuzzy_transition
    "I look over at Val but something's very wrong."
    "She isn't focused in my vision anymore." 
    show val normal 25 at right with fuzzy_transition
    "Even her voice is starting to sound off."
    play music "audio/music_track_hallucination.mp3"
    "I feel my heartbeat start to well up in my chest."
    "It's pumping hard and I start panicking."
    v "{glitch=5.0}{color=#bababa}{b}babyyyyyyyyyyyyy, are you okay?{/b}{/color}{/glitch}"
    hide val normal 25
    "No, no no no no no-"
    e "NO!"
    scene bg pillow with dissolve
    "I look back over at Kit but something is different."
    "I see her now."
    "Valerie."
    scene bg dead val with fuzzy_transition_fast
    "A wave panic fills my entire body."
    "I rush over to the table start grabbing various pill bottles and start downing them."
    "Kit tackles me to the ground before I can finish the bottle."
    k "Eve! Eve!!"
    "I writhe in her grasp until I feel the walls start to get blurry again as I start to remember."
    jump mem_hallucination_4

label aftermath:
    play music "audio/music_track_title"
    "As I come back down from everything I'm not in my apartment anymore."
    "I'm outside on the balcony as the police are rummaging through my apartment."
    "Valerie is gone."
    "And I didn't even get to say goodbye."
    "The next few weeks were a blur."
    "I wasn't arrested on the grounds of I wasn't mentally stable enough to have known what I was doing."
    "I don't really think that was true but..."
    "They put me in mandated therapy for it"
    "Kit and her mom, who was our landlord, took me in."
    "I'm sure they love having a 25 year old drug addict on their couch."
    "Well, Kit's couch"
    "Her mom doesn't stick around much except to make sure I haven't relapsed and killed her daughter."
    "I still feel numb, like none of this is real."

    menu:
        "Heal.":
            jump good_ending

label take_drugs_alone: #TODO: scene not finished
    "follows they're all for me choice"

label mem_hallucination_1:
    #"Scene - memory hallucination 1"
    #NOTE: Note to self, do this if a new scene is using the same background as the previous screen, otherwise transition graphic wont display properly
    play music "audio/music_hallucination.mp3"
    scene black with spiral_transition
    scene bg room with spiral_transition
    show eve normal at left
    eh "Hey, I think im gonna get high again, wanna take some with me~"
    show val normal at right
    vh "Evelyn, you know I don't like to do anything more than, like, drinking,,"
    eh "Heyy c'mon, just a little, ok?~"
    eh "It's just a little pill it won't hurt."
    show val annoyed at right
    vh "Are you sure? I just, I don't want to get sucked into doing this kinda stuff."
    eh "What, like me?"
    "I giggled, playing it off in a joking tone but it did kinda hurt to hear her say that."
    "Painting me like I was pressuring her."
    show eve smirk at left
    eh "I'll take one with you if that makes you feel better."
    "She glanced away, clearly reluctant."
    vh "Alright fine, but only if you we do it together."
    "But she agreed anyway."
    eh "Ready?"
    "She nodded her head."
    "We both downed the pill, she made sure to wash hers down with water."
    show val normal at right
    vh "I guess that wasn't so bad."
    eh "See? What did I tell you?"
    stop music fadeout 1.0

    if came_from_drugs:
        $ came_from_drugs = True 
        jump kit_at_door

    if came_from_sesbian_lex:
        $ came_from_sesbian_lex = True
        jump after_sex_high
    
    return


label mem_hallucination_2:
    play music "audio/music_hallucination.mp3"
    scene black with spiral_transition
    scene bg room with spiral_transition
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
    show eve annoyed at left
    eh "Whatever, I'm gonna get high."
    show val angry at right
    vh "No. No the fuck you aren't."
    vh "We have somewhere to be jackass."
    vh "You can't just spend all your time getting high, dressing like a slob and getting nothing done."
    vh "I mean, it's no wonder i'm the only one here who can hold down a goddamn job."
    show eve angry at left
    "I stood up in a rage."
    eh "Well it's not my fault that you're so used to having a girlfriend who looks perfect all the fucking time for you."
    show val crying at right
    eh "If you want someone as perfect as her, why don't you go and dig {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch} out of her grave and date her instead."
    "Valerie's tears had already hit the floor by the time my sentence had stopped."
    show eve normal at left
    eh "Shit- I didn't mean that- I'm sorry-"
    vh "Well at least {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch} acted like she loved me instead of just saying it."
    stop music fadeout 1.0
    if came_from_music:
        $ came_from_music = True 
        jump after_music

    if came_from_music_alt:
        $ came_from_music_alt = True 
        jump after_music_alt

    if came_from_offer_kit_drugs:
        $ came_from_offer_kit_drugs = True 
        jump answer_phone

    if came_from_get_even_higher:
        $ came_from_get_even_higher = True 
        jump get_even_higher_cont
    
    return


    # Evelyn Remembers her and Valerie having an argument about their drug usage and Val being vindictive and pushing the blame on her
    #jump cemetery_scene_1

label mem_hallucination_3:
    play music "audio/music_hallucination.mp3"
    #"Scene - memory hallucination 3. Evelyn Remembers a doctors appointment where a doctor berates her and Valerie for their excessive drug usage"
    scene black with spiral_transition
    scene bg doctor with spiral_transition
    "Doctor?" "Mixing substances, not sleeping, not eating regularly. These are very dangerous patterns of behavior. this isn't something I can just ignore."
    show eve normal at left
    eh "I can ignore it fine enough."
    "Doctor?" "This hasn't gotten any better since your last physical, Evelyn. I'm worried about you doing this to yourself."
    eh "You aren't really worried, you're just paid to tell me that bull."
    "Doctor?" "I can't imagine you aren't a little worried, you came here for your appointment after all."
    eh "No, she made me come here."
    show val normal at right
    vh "Baby, I'm worried about you."
    show eve angry at left
    eh "Don't pretend like I'm the only one getting fucked up every night."
    show val angry at right
    vh "Okay, yeah. I'm not innocent. But at least I'm trying to get us some help."
    show val annoyed at right
    vh "Evelyn, you're destroying your life, our life."
    "I shoot daggers at her. I can't hide how annoyed I am she's airing our shit out."
    show val normal at right
    vh "I want us to have a real life, I hate seeing you laying in bed all day."
    vh "I'm still trying, I still go to work, I have friends outside. I'm still doing things."
    eh "Yeah, doesn't stop you from using all that job money to pay for us to get high when you come home."
    show val depressed at right
    vh "That's not fair."
    eh "You think having a job makes you better?"
    vh "I never said I was better, but I can't even get you to leave the house most of the time."
    eh "You buy us food and spend the rest on the shit we use to get high."
    show val angry at right
    vh "You woudn't eat if I didn't buy us food, you'd starve to death drugged out on the floor."
    eh "Always trying to pretend like you don't want to be high right next to me."
    eh "{i}\"We could stop at any time\"{/i} right?"
    show val normal at right
    vh "If you would just try, maybe we could."
    vh "Don't make me complacent in you falling apart, dumbass."
    "I can hear that hack doctor talking, I barely process any words they're saying."
    "Doctor?" "Evelyn, what concerns me most is that this pattern can become fatal."
    eh "Whatever. It's my life not yours, just leave it alone."
    show val depressed at right
    vh "Sweetie, please."
    vh "I don't want to lose you too."
    "I stood up to leave."
    "Doctor?" "This is not something to dismiss, Evelyn. I may have to send you to a psychiatric center if this behavior remains consistent."
    eh "That's total bullshit."
    "I feel Val weakly grab onto my hand as I try to leave."
    vh "Baby, it might be for the best. If we both go."
    vh "You're right, I don't think I'm inncoent in this either so... please."
    eh "I'm not taking any more of this shit."
    vh "Evelyn please, I can't just sit by and watch you kill yourself like this."
    eh "You don't get to decide that for me."
    show eve normal at left
    eh "So what if I OD? You already lost one girlfriend. You can handle it again."
    eh "I'm just the imperfect girlfriend, right?"
    eh "Nothing like her."
    show val crying at right
    "Val looks like she's on the brink of tears."
    vh "Don't talk about her like that."
    "I can't stand it when she looks at me like that. Like I hurt her. Like it's my fault."
    vh "Please… I'm just trying to get you to be better to yourself."
    eh "So I can be more like {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch}, right?"
    "She hides her face in her hands. It doesn't matter. I can tell she's crying anyways."
    vh "*sniff* You think I could go through at again?"
    eh "I think you'd survive, yeah."
    vh "That's not the same thing and you know it."
    stop music fadeout 1.0

    if came_from_cant_feel_anymore:
        $ came_from_cant_feel_anymore = True
        jump after_hallucination_panic
    
    if came_from_cemetery_1:
        $ came_from_cemetery_1 = True
        jump try_to_remember

    if came_from_cemetery_1_alt:
        $ came_from_cemetery_1 = True
        jump try_to_remember

    if came_from_answer_phone:
        $ came_from_answer_phone = True
        jump kit_comes_over

    return
    #jump cemetery_scene_2


label mem_hallucination_4:
    play music "audio/music_hallucination.mp3"
    #"Scene - memory hallucination 4. Evelyn Remembers having sex with Valerie and making her take drugs until she overdoses."
    "I can finally remember it, my heart feels like it's going to rip out of my chest, and I'm covered in vomit."
    "And just like that I'm back there. in that moment. I'm laying down, and she's on top of me."
    scene black with spiral_transition
    scene doctor with spiral_transition
    # another scene trans here
    vh "Baby, are you sure?"
    eh "It'll be okay I promise."
    vh "It's just, it's a lot more than we usually do..."
    eh "C'mon we've been alright so far, haven't we?"
    eh "A little more won't hurt. I'll do it with you okay, it'll be less scary that way."
    "I don't even remember what we took that night, but it was excessive, way too excessive."
    "I think she was bleeding from all the needles."
    eh "Hey,, hey, hey,, Val g-get on top of me,, it feels good like thatttt,,"
    vh "y-yeah okay, b-baby I don't feel good."
    eh "It's fine it's finee, it's o-ok if you have to vomit on me it's kind of hot,,"
    "I remember her on top of me, I wasn't exactly sober myself so it's all a bit of a haze."
    "But I remember she was twitching, I could feel her hands shake as she held on to me."
    "She was looking down at me, her face was all kinds of blue. I was jerking off looking up at her, but she just didn't look right."
    vh "Baby I, I feel-"
    vh "*blech*"
    "She vomited all over me, I don't even think I stopped touching myself until she fell limp on top of me."
    "Then I panicked."
    eh "V-val, Valerie? A-are you okay??"
    "I felt her convulsing on top of me."
    "The amount of substances in me at the time definitely didn't help."
    "I shoved her off of me."
    eh "Fuck, fuck fuck,,fuck fuckfuck fuck fuck fuck {b}FUCK.{/b}"
    "I stood up, threw the blanket over her body."
    eh "Fuckfuckfuckfuck it's all my fault, it's all my fault."
    eh "I fell to my knees after that."
    eh "N-no nonono she's ok, y-yeah she's ok, she's just taking a nap."
    eh "Y-yeah heh, heheheh, s-she's okay s-she's just um tired and sleeping t-that's okay."
    eh "I-I think I'll just-"
    eh "and then I passed out."
    "I don't know if it was from the shock or all the drugs in my system but when I woke up..."
    "Valerie was there like she always was."
    "I spotted a body pillow on the bed that I hadn't noticed before."
    "I just assumed she bought it. But I guess, it was just as she was."
    stop music fadeout 1.0
    if came_from_val_discovery:
        $ came_from_val_discovery = True
        jump aftermath




    return


label after_music:
    scene bg room with fuzzy_transition
    # "Scene - Eve starts crying listening to music after hallucination 2"
    play music "audio/music_track_2.mp3" fadein 0.3
    "The voices fade as I finally start to feel normal again."
    "My eyes open to the sight of a familiar stained wet gross ceiling."
    "My skull is banging like a drum."
    v "Baby are you ok?"
    "I look over at her, I'm still pissed."
    "I want to yell at her, tell her how much she hurts me."
    "Let her see what it's like to be compared to a corpse in a ditch who can do no wrong."
    "I can feel the rage bubbling up again, pulsing through my skin wanting to rip through it and break out."
    "She puts her hand on my shoulder, my mind is so blinded by emotion I can't even feel it, and the pounding in my skull is only getting worse."
    "BANG. BANG. BANG."
    "If I can't get all of this anger out in one way or another, then I'm going to god damn explode."

    menu:
        v "Baby I'm worried, can I help?"    
        "Try to talk to your girlfriend":
            #Leads to mem hallucination 4 and good ending
            "Eve tries to talk it out with Val but she starts subconciously blocking out what Valerie says until running out in a panic where she runs into kit bringing over some fruits"
        "Fuck the feelings away": #TODO scene not finished
            jump sex_hallucination_2
            ""
        "Get so fucked up you don't feel anymore":
            $ came_from_cant_feel_anymore = True 
            "I can't hold it in anymore, I have to get rid of these disgusting feelings." 
            "Before they become me or I become dead."
            "When I look at her all I can think about is how much I know she hates me."
            "And how I might hate her more."
            "I need to get up."
            "As I try to move I collapse backwards onto the ground."
            "I stand up too fast, I feel so lightheaded I might pass out."
            "My eyes dart around the room to look for something to numb the pain."
            "I spot an acid tab sitting on some random pile of shit on the floor."
            "Just as quickly as I notice it I shove it into my mouth."
            "Before I knew it I'm on the ground."
            "Looking up. The apartment is wrong again."
            "And I can hear the voices coming back."
            jump mem_hallucination_3


label after_music_alt:
    scene black with fuzzy_transition
    scene bg room with fuzzy_transition
    play music "audio/music_track_3.mp3" fadein 0.3
    "The voices fade as I finally start to feel normal again."
    "My eyes open to the sight of a familiar stained wet gross ceiling."
    "My skull is banging like a drum."
    v "Hey cutie, are you okay?"
    "I look over at her. I'm still pissed, I feel a bit bad despite that."
    "I want her to yell back at me, hurt me like I hurt her."
    "She puts her hand on my shoulder, my mind is so overwhelmed with emotions I can't even feel her."
    "It's making me so dizzy, I just want to get these feelings out."
    
    menu:
        v "Baby I'm worried, are you feeling alright?"
        "Try to patch things up":
            jump cemetery_scene_1
            
        "Confront her on the argument":
            "Why do you always do that?"
            v "Do what?"
            e "You always bring her up whenever we fight."
            e "Like she's your guardian angel, I just-"
            e "it makes me feel so fucking pathetic."
            e "I hate it."
            v "Baby, this seems like it's a lot for you, I think we should just talk this out."
            menu:
                v "Let me take you somewhere"
                "Hear her out":
                    jump cemetery_scene_1_alt
                "Fuck her til she knows I was right":
                    ""
                "Get so high you leave this world":
                    e "No."
                    v "Baby-"
                    "I ignore her."
                    "Fuck this."
                    "I don't need to take this shit from her."
                    "I'm too sober to deal with this"
                    "I rummage around the apartment and eat a half finished edible, a mushroom and some random pill before laying down on the floor."
                    menu:
                        "Valerie is wrong.":
                            "She's wrong."
                            menu:
                                "I know Valerie is wrong.":
                                    "She's always wrong."
                                    menu:
                                        "I know more than Valerie.":
                                            "I'm always right."
                                            menu:
                                                "I know what Valerie really wants.":
                                                    "Evelyn is always right."
                                                    menu:
                                                        "I know Valerie":
                                                            jump delusion_ending_drugs
            



label after_hallucination_panic: #TODO not finished
    scene bg room with fuzzy_transition
    "Scene after mem hal 3"


label cemetery_scene_1:
    # "Scene - Eve and Hallucination Valerie make up and go to the cemetery" (try to patch things up)
    # TODO: Make this cemetery BG
    $ came_from_cemetery_1 = True
    scene bg room
    show eve normal at left
    show val normal at right
    play music "audio/music_track_1.mp3" fadein 0.3
    e "Agh, I'm sorry, I just, I keep remembering shit."
    e "Stupid fucking arguments we've had."
    e "I just- I hate when I get like that. I just, I hate it so much when you talk about her."
    e "I get so angry when you talk about her."
    e "Even if she's the entire reason we met."
    e "I hate it so fucking much."
    show val depressed at right
    v "Maybe, we could visit her."
    show eve annoyed at left
    e "What? Why?"
    v "It might be good for the both of us, don't you think?"
    e "I- I guess."
    e "Sure."
    "I take one more look at Val and walk towards the door."
    show val normal at right
    show bg outside cem day with fade
    "I have fond memories of the cemetery, even if {i}she{/i} is buried there"
    "I walk with Val to the cemetery, it's always weird walking around in the daylight."
    "We always get shifty looks from everyone."
    "I guess probably because I look like shit."
    "Or maybe they just hate to see two girls together."
    show bg cemetery with dissolve
    "We get to the cemetery quick enough, Val takes us over to her grave."
    show val smug at right
    show eve normal at left
    v "Hey, {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch}."
    e "God I hate that name so much."
    v "I'm back, I brought Evelyn this time."
    v "I know you two never met, but she's helping me heal."
    show val depressed at right
    v "She was there for me when you..."
    show val crying at right
    "Valerie is crying. I want to comfort her but, I'm so uncomfortably angry that I can't."
    "I just stand there, looking down at her."
    "Crying."
    "But she stands back up."
    show val normal at right
    v "Sorry *sniffle* about that."
    "And she wipes her tears off her face."
    v "Let's uh, go stand under the tree, okay?"
    show bg tree with dissolve
    "We go and walk over to the lone tree among the graves, we sit down underneath it."
    v "Do you know why we came here?"
    e "So you could talk about your dead ex-girlfriend?"
    v "No, so that I could talk to you."
    v "Sweetie, I care a lot about you and, I know it hurts sometimes and..."
    "She's going off on a rant again but.."
    "this time I don't feel as pushed away by it."
    v "I just, really want you to get better, I care about you and…"
    v "I don't want you to destroy your life or worse."
    v "I- I don't want you to overdose."
    v "I don't want to lose you, too."
    v "Can you please try to remember..."
    "Fine, just this once. For her."
    "I lay back against the tree, I feel the wind on my face and I try to focus and remember, remember why she's so worried."
    jump mem_hallucination_3

label cemetery_scene_1_alt:
    #Hear her out and go to the cemetery
    #TODO background and sprites
    $ came_from_cemetery_1_alt = True
    play music "audio/music_track_1.mp3" fadein 0.3
    e "Yeah, okay... where?"
    v "We're going to visit her."
    e "What? Why?"
    v "It might be good for the both of us."
    v "Don't you think?"
    e "I-I guess."
    e "Sure."
    "I take one more look at Val and walk towards the door."
    show bg outside cem day with fade
    "I have fond memories of the cemetery, even if {i}she{/i} is buried there"
    "I walk with Val to the cemetery, it's always weird walking around in the daylight."
    "We always get shifty looks from everyone."
    "I guess probably because I look like shit."
    "Or maybe they just hate to see two girls together."
    show bg cemetery with dissolve
    "We get to the cemetery quick enough, Val takes us over to her grave."
    v "Hey, {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch}."
    e "God I hate that name so much."
    v "I'm back, I brought Evelyn this time."
    v "I know you two never met, but she's helping me heal."
    v "She was there for me when you..."
    "Valerie is crying. I want to comfort her but, I'm so uncomfortably angry that I can't."
    "I just stand there, looking down at her."
    "Crying."
    "But she stands back up."
    v "Sorry *sniffle* about that."
    "And she wipes her tears off her face."
    v "Let's uh, go stand under the tree, okay?"
    show bg tree with dissolve
    "We go and walk over to the lone tree among the graves, we sit down underneath it."
    v "Do you know why we came here?"
    e "So you could talk about your dead ex-girlfriend?"
    v "No, so that I could talk to you."
    v "Sweetie, I care a lot about you and, I know it hurts sometimes and..."
    "She's going off on a rant again but.."
    "this time I don't feel as pushed away by it."
    v "I just, really want you to get better, I care about you and…"
    v "I don't want you to destroy your life or worse."
    v "I- I don't want you to overdose."
    v "I don't want to lose you, too."
    v "Can you please try to remember..."
    "Fine, just this once. For her."
    "I lay back against the tree, I feel the wind on my face and I try to focus and remember, remember why she's so worried."
    jump mem_hallucination_3

label cemetery_scene_2:
    #Eve arrives at the cemetery with Val's body
    play music "audio/sfx_night_ambience.mp3"
    e "We're here. It's chilly again."
    e "Figures. I'd pick a night where the weather decides to remind me of you."
    e "Feels like just yesterday you were here mourning… her."
    e "I'm so sorry that you have to join her."
    e "I hope she treats you better up there than I could down here."
    e "heheh..."
    "I dragged her over by the only tree in the cemetery."
    e "This seems like a nice palce, right? Nice and in the shade."
    "I jammed the shovel into the ground and began digging."
    "I dug and dug until the hole was deep enough."
    e "I'm sorry I couldn't get a coffin for you, those are really expensive."
    e "You deserve better."
    e "I hope the bag keeps you safe at least."
    "I push her into the hole."
    "I wince as I hear her slam against the ground."
    "Goodbye. Lover."
    "I buried Val in that pit."
    "Once I had filled it back up I rummaged around the cemetery for rocks to create a makeshift gravestone."
    "I carved her name into one of the rocks."
    "Finally, I put a flower I snagged onto her grave."
    e "I'll miss you."
    e "Forever."
    jump true_ending
    



label try_to_remember:
    #"Scene - try hard to remember" (eve realizes val is dead)
    #NOTE: This part got really long and nested but making it different labels wouldve been clunky so whatever
    scene bg cemetery with fuzzy_transition
    "I remembered it."
    #play music "music_track_1.mp3"
    "She took me there, to the doctor."
    "Because..."

    menu:
        "Apologize to her":
            "She cared about me."
            "She just, she just wanted me to get better."
            "I start to cry."
            "For once, I'm not overwhelmed by anger."
            "I just let my feelings out."
            "But once I was finished I heard her voice."
            v "Do you remember?"
            "I nod my head."
            v "Baby, I'm just, so glad. Glad you know that I cared about you."
            v "I cared about you so much."
            menu:
                v "Baby, look at me."
                "Look at her":
                    show eve normal at left
                    show val normal at right
                    v "See how much I cared about you."
                    "I look up at her."
                    show val normal 75 at right with fuzzy_transition
                    "But she's wrong."
                    play music "audio/music_track_3.mp3" fadein 0.3
                    "She looks... wrong."
                    "She isn't focused in my vision anymore." 
                    show val normal 25 at right with fuzzy_transition
                    "Even her voice is starting to sound off."
                    "I feel my heartbeat start to well up in my chest."
                    "It's pumping hard and I start panicking."
                    v "{glitch=5.0}{color=#bababa}{b}babyyyyyyyyyyyyy, are you okay?...{/b}{/color}{/glitch}"
                    hide val normal 25 with fuzzy_transition
                    "No, no no no no no-"
                    e "NO!"
                    "I scream at full volume."
                    "Everyone's staring at me. They're all staring."
                    show bg outside cem day with dissolve
                    "I sprint back home, back to my apartment, to our apartment."
                    "The scenery speeds besides me as I stumble and run and trip all the way back home."
                    scene bg hallway with dissolve
                    "I slam against the door and frantically reach into my pockets trying to feel for my keys."
                    scene bg pillow with dissolve
                    "I finally find them and jam the key in the lock."
                    "I run into the apartment."
                    menu:
                        "See her.":
                            "Finally, I see her."
                            scene bg dead val with fuzzy_transition
                            #play music "audio/music_panic.mp3" fadein 0.3
                            "I didn't see her before..."
                            "...but I see her now."
                            "A wave of nausea hits me. I feel it well up in my throat."
                            "I can't stop myself from vomiting into my hand at the sight of it."
                            "I'm so dizzy."
                            "I can't stand up straight." #hehe straight
                            "I walk over to the bed and look down at it."
                            e "Valerie."
                            "I'm crying again."
                            

                            menu:
                                "Her body is laying there."
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "vomit.":
                                    "I throw up again, all over my hand and on her."
                                    "I'm so nauseous I can't even think."
                                    "My whole body is shaking violently."
                                    "It feels like static."
                                    menu:
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                        "persist.":
                                            "I can't give up."
                                            "She wouldn't want me to."
                                            "She would want me to be strong."
                                            "For her."
                                            menu:
                                                "KILL YOURSELF":
                                                    jump suicide_ending
                                                "KILL YOURSELF":
                                                    jump suicide_ending
                                                "Get high until you can't think.":
                                                    "I can only be so strong."
                                                    e "I'm sorry baby, I just, I can't deal with this."
                                                    e "Please understand."
                                                    "I grab whatever I can find on the floor and take it."
                                                    "I don't care anymore, I just can't be sober right now."
                                                    "I fall to the floor and let my mind get hazy."
                                                    menu:
                                                        "KILL YOURSELF":
                                                            jump suicide_ending
                                                        "Get help.":
                                                            scene bg hallway with fuzzy_transition
                                                            "I finally manage to get myself under control, I stumble my way out of our apartment."
                                                            "My apartment."
                                                            "I ran into Kit shortly after."
                                                            "She took me back into her apartment, she could see how messed up I was."
                                                            "I told her about Valerie, how she died and how I'd be hiding it."
                                                            "I don't remember what I said exactly, that whole night is still a haze."
                                                            "I'm glad I confided in her that night, I think it might've been what I needed to not do something rash."
                                                            "I stayed over at Kit's for a couple nights."
                                                            "I wasn't ready to go back to that apartment yet."
                                                            "But one night, I finally built up the courage."
                                                            "Out of everything, I remember that perfectly."
                                                            menu:
                                                                "Mourn.":
                                                                    stop music fadeout 0.3 
                                                                    #play music "audio/music_title.mp3" fadein 0.3 
                                                                    "I stand in front of the door to my apartment."
                                                                    "I can feel myself shaking, I'm still not sure if I have the strength to face her."
                                                                    "I made sure Kit didn't come with me. She doesn't need to see Val like this."
                                                                    "She should remember her as she was."
                                                                    "I take a deep breath and walk into the apartment."
                                                                    scene bg drugs with dissolve
                                                                    "It's just how I left it."
                                                                    scene bg dead val with dissolve
                                                                    "She's just how I left her."
                                                                    e "H-hey baby, miss me? I'm sorry. For everything."
                                                                    "I can already feel the tears welling up and running down my face."
                                                                    "This has been trapped inside me for so long."
                                                                    "I can't hold it in."
                                                                    "I sat on the floor next to her sobbing for at least an hour."
                                                                    "Eventually, I muster the strength to get up."
                                                                    e "I'm, uh, I'm gonna give you a proper resting place."
                                                                    e "You shouldn't be stuck in this shitty old apartment all the time."
                                                                    e "My voice is still shaking, I've never felt emotions so overwhelming."
                                                                    e "I know the perfect place."
                                                                    e "I'm sure you remember it as fondly as I do."
                                                                    "I go and rummage through our apartment, I find an old bag we used to move our mattress one time."
                                                                    e "Should be big enough."
                                                                    "I carefully place her inside it."
                                                                    scene bg bed with dissolve
                                                                    e "You look so peaceful."
                                                                    "I zip up her bag and I drag her out of the aprtment."
                                                                    scene bg hallway with dissolve
                                                                    e "Heheh, I brought a shovel for the occasion."
                                                                    e "I hope you're proud of me, I even picked up a job to get the money for it."
                                                                    "I'm still crying."
                                                                    "Hey so, sorry if this hurts, we don't have any elevators so uhh... down the stairs we go."
                                                                    "I dragged her all the way down the stairs and onto the sidewalk."
                                                                    scene bg cemetery with fade
                                                                    e "Y'know I bet I look hella suspicious doing this."
                                                                    e "A crazy girl with a shovel and a body bag talking to herself while she walks."
                                                                    e "I'm not talking to myself though, you're here."
                                                                    e "Right, Val?"
                                                                    "I keep dragging her down the sidewalk."
                                                                    e "We're uh, we're getting close. I bet you can already tell where we're going, right?"
                                                                    e "You were always perceptive like that."
                                                                    e "Not me though, just look at how long it took for me to notice that you…"
                                                                    e "I'll try to quit."
                                                                    e "I know you would've wanted me to."
                                                                    e "I can't promise I won't slip up, but I'll try."
                                                                    jump cemetery_scene_2







                                                        "KILL YOURSELF":
                                                            jump suicide_ending
                                                "KILL YOURSELF":
                                                    jump suicide_ending
                                                "KILL YOURSELF":
                                                    jump suicide_ending

                                                
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                        "KILL YOURSELF":
                                            jump suicide_ending
                                    
                                        
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "KILL YOURSELF":
                                    jump suicide_ending
                                "KILL YOURSELF":
                                    jump suicide_ending







        "She's still wrong":
            "She thinks she's better than me." 
            "She thinks I can't take care of myself."
            "She thinks I'm {i}so{/i} fucking pathetic."
            "I bet she wishes I would just turn into {glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch}"
            "So she could see her again."
            "So she could touch her again."
            "So she could get rid of me."
            "You fucking disgust me."
            v "Sweetie?"
            e "I'm right... you don't even care about me."
            e "You just want me to become her."
            e "Well too bad."
            e "I decide who I become."
            v "Evelyn-"
            "Before she could even start to spit her bullshit argument at me I ran away."
            "I ran back to our apartment."
            "I climbed up the stairs and blindly sprinted towards our door."
            "Until I slammed into something huge and fell down."
            k "EVE?"
            "I look up and see Kit standing in front of me."
            k "OH MY GOSH!! I’m so so sorry, let me help you up!"
            "She grabs my arm and roughly pulls me back up, it hurts a little."
            e "It's fine."
            k "What happened??? You look so panicked!"
            e "It's fine."
            k "Are you sure??"
            e "I said it's fine. Val was just being a bitch."
            k "Oh no... What did she do?"
            e "She thinks she knows better than me."
            e "All she does is nag and yell at me for minding my own goddamn fucking business."
            e "So what if I wanna get a little high some of the time?"
            e "She doesn't have to drag me to some stupid hack doctor about it."
            e "And all this stupid bullshit."
            e "\"Baby, get a job \"{glitch=5.0}{color=#bababa}{b}████{/b}{/color}{/glitch} wouldn't have left the food out.\""
            e "I've heard enough about her stupid fucking ex, I hope she stays dead in that hole."
            k "EVE!"
            "She grabs me on the shoulder and shakes me a little."
            k "I think maybe Valerie has a point. You don't seem healthy."
            e "Oh so you know better than me too."
            k "I just think that both you and Valerie would be happier if you took some steps to get better habits."
            e "Oh so now you think you know Valerie better than I do?!"
            k "Eve, that's not what I meant."

            menu:
                "I know Valerie better than her.":
                    "Fuck off, you both just wanna turn me into her stupid perfect ex."
                    k "Eve, I-"
                    e "THAT'S NOT MY FUCKING NAME."
                    menu:
                        "I know Valerie.":
                            jump delusion_ending_kit

                                                               
                        


#The "sex" scene
label sesbian_lex:
    play music "audio/music_track_2.mp3"
    $ came_from_sesbian_lex = True
    # "Scene - Eve has 'sex' with Vallerie"
    #jump mem_hallucination_1
    e "God, I wanna fuck."
    v "Yeah?"
    e "Yeah."
    v "Okay, but you know the rules."
    e "yes ma'am... no touching and do what you say." 
    v "That's a good girl."
    v "Now strip and lay on the bed."
    "I already know the drill, i peel off each article of my clothing while she watches me."
    "I lay down onto our gross messy bed, all our pillows and shit piled around me."
    "I look up and meet her gaze, she's staring down at me with daggers in her eyes."
    "It's so fucking hot."
    v "You can start stroking now. Stroke your tiny little dick for me."
    "Fuck, she's so attractive when she's like this."
    "I can already feel my heart pounding out of my chest as I touch myself for her."
    v "You're such a pathetic little whore, you'll do anything just to get off won't you?"
    e "Mmnnmgmmhn, yeah..."
    v "Good, then I want you to take a little something for me, okay?"
    e "Okayyyyyy~~"
    "I feel something in my hand, I don't even look at it before I put it in my mouth."
    v "Yeah, get all fucked up for me, okay?"
    e "mhmmm~~"
    "It hits me faster than I expect, I start to feel more out of it as I keep jerking off to her."
    v "Go on. Keep stroking."
    v "You're so pathetic"
    v "Just laying there jerking off to me."
    v "It's adorable."
    "I wimper and writhe under her as I touch myself."
    "The high is making me feel funny."
    "I start jerking faster."
    v "Hey hey slow down."
    e "Mmmnmnmnn I-I'm closeee."
    v "No no, hold it in."
    v "Quickshot."
    v "You don't get to cum."
    v "Not after what you've done."
    v "You're disgusting and pathetic and you don't deserve to feel that kind of pleasure."
    "I stop touching myself and just writhe in the discomfort of being almost there."
    v "Isn't that right?"
    v "Just sit in it. No release."
    v "Good girl."
    "As I lay there beneath her, breathinng heavily, I start to hear voices."
    "My vision starts to get fuzzy."
    "I close my eyes a little but the voices get louder..."
    "and when I open them..."
    jump mem_hallucination_1

    


label after_sex_high:
    stop music fadeout 0.3
    scene black with fuzzy_transition
    scene bg room with fuzzy_transition
    "The voices fade away"
    "My vision returns to normal."
    "I'm still pent up, on the edge."
    "Val is sitting on the bed next to me."
    v "Hey baby, feeling better?"
    e "Ahh, still feeling... pent up."

    menu:
        v "Ah okay, anything you want to do to distract yourself?"
        "Get higher to calm down":
            "I start to come back down, I don't think that helped."
            "I feel even more emotional than before."
            "I look over at Valerie"
            menu:
                "I'm still pissed about that night."
                "Confront her on the argument":
                    "Why do you always do that?"
                    v "Do what?"
                    e "You always bring her up whenever we fight."
                    e "Like she's your guardian angel, I just-"
                    e "it makes me feel so fucking pathetic."
                    e "I hate it."
                    v "Baby, this seems like it's a lot for you, I think we should just talk this out."
                    
                    menu:
                        v "Let me take you somewhere."
                        "Hear her out":
                            jump cemetery_scene_1_alt
                        "Fuck her til she knows I was right":
                            "" #TODO not finished
                        "Get so high you leave this world":
                            e "No."
                            v "Baby-"
                            "I ignore her."
                            "Fuck this."
                            "I don't need to take this shit from her."
                            "I'm too sober to deal with this"
                            "I rummage around the apartment and eat a half finished edible, a mushroom and some random pill before laying down on the floor."
                            menu:
                                "Valerie is wrong.":
                                    "She's wrong."
                                    menu:
                                        "I know Valerie is wrong.":
                                            "She's always wrong."
                                            menu:
                                                "I know more than Valerie.":
                                                    "I'm always right."
                                                    menu:
                                                        "I know what Valerie really wants.":
                                                            "Evelyn is always right."
                                                            menu:
                                                                "I know Valerie":
                                                                    jump delusion_ending_drugs



                

                    
        #TODO: not finished
        "Fuck Again":
            ""
        "Get some air":
            ""

        



label suicide_ending:
    #"Scene - Suicide Ending"
    stop music fadeout 0.3
    play music "audio/music_dramatic.mp3" fadein 0.3
    scene bg dead val
    "I can't do this."
    "She can't be."
    "She can't be."
    "I can't live without her."
    "I panic."
    "I reach for the closest bottle of pills and down them all."
    "It only takes a couple of seconds until I convulse and fall to the floor."
    "I feel my mind getting hazier.."
    "my body feels separate from me.."
    "and in these last couple seconds I just think to myself... "
    "you know, in most peoples final moments I'm sure they think about all the people that will miss them,"
    "all the things they didn't get to do,"
    "their regrets,"
    "their finaly words,"
    "but I don't have any of that."
    "And all I can think about is how excited I am to see you again."
    "Valerie."
    stop music fadeout 0.3
    $ achievement.grant("suicide_ending")
    $ renpy.notify("Achievement Unlocked: I'll be with you soon")
    jump credits_suicide
    

label bad_touch_ending:
    stop music fadeout 0.3
    #$ came_from_bad_touch True
    "I can't restrain myself any longer."
    "The sight of her naked body just keeps teasing me."
    "I'm so goddamn pent up I just-"
    "I need to touch her"
    "to relieve myself"
    "to let me finish"
    "I sit up in a flash and reach towards Valerie."
    "I go to put my hands on her wrists but she's gone"
    "and I never saw her again after that."
    "..."
    "..."
    "I'm so fucking selfish."


    $ achievement.grant("bad_touch_ending")
    $ renpy.notify("Achievement Unlocked: Crossed the line")
    jump credits_bad_touch

    

label infidelity_ending:
    stop music fadeout 0.3
    e "It's fine."
    "I push her to the ground."
    e "Take off your clothes."
    "She pulls her overalls without even so much as a second thought"
    e "Val said it's fine."
    "I grab her hips."
    e "Val is out of town."
    "I pull off my own pants."
    e "She doesn't need to know."
    "I grab her dick."
    e "Val thinks it's hot."
    "I start crying."
    e "Val is dead."
    e "Val broke up with me."
    e "Val loved her more than me."
    e "Kit."
    e "Put it in me. Now."
    
    $ achievement.grant("infidelity_ending")
    $ renpy.notify("Achievement Unlocked: Not love")
    jump credits_infidelity


label delusion_ending_kit:
    stop music fadeout 0.3
    #"Evelyn never learns of Valerie's death and impersonates her / mentally becomes 'her'"
    play music "audio/music_dramatic.mp3"
    "I push her out of the way and run into my apartment."
    "She doesn't know anything."
    "I'm right."
    "I'M RIGHT."
    "Evelyn's right."
    "She's always right."
    "Isn't that right?"
    menu:
        "Valerie.":
            $ achievement.grant("delusion_ending")
            $ renpy.notify("Achievement Unlocked: As if nothing happened")
            jump credits_delusion
    
    $ achievement.grant("delusion_ending")
    $ renpy.notify("Achievement Unlocked: As if nothing happened")

label delusion_ending_drugs:
    stop music fadeout 0.3
    play music "audio/music_dramatic.mp3"
    menu:
        "I am"
        "Valerie":
            $ achievement.grant("delusion_ending")
            $ renpy.notify("Achievement Unlocked: As if nothing happened")
            jump credits_delusion




label good_ending:
    stop music fadeout 0.3
    "But the therapy helps."
    "And Kit has become someone I can rely on."
    "So even if she's gone I hope Valerie watches over me as I try to heal."
    "Even if that's selfish of me."

    $ achievement.grant("good_ending")
    $ renpy.notify("Achievement Unlocked: Heal.")
    jump credits_good_ending

label true_ending:
    stop music fadeout 0.3
    $ came_from_true_ending = True
    #"Scene - True ending."
    #"Eve confides in Kit that Valerie is dead"
    scene black
    "After that I just, kept living my life."
    "So much time passed, so much time without"
    "her."
    "Valerie."
    "But today's been three years since she died."
    scene bg val buried timeskip with dissolve 
    "And here I am, back at the cemetery."
    "I sit on the floor next to her."
    play music "audio/sfx_day_ambience.mp3"
    e "Hey baby, I missed you."
    e "Sorry I haven't visited in awhile. I just, got kinda busy."
    e "I met this girl..."
    e "I was out at a bar with Kit."
    e "I know, still weird that we're friends."
    e "I think you of all people know how much she drove me up the wall."
    e "But, she's been there for me."
    e "She made me hear about this stupid book the other day, you might've liked it."
    e "Reminds me of those weird homoerotic anime scenes you would show me."
    e "It was called like, Warmed Competitors, or something dumb like that."
    e "Whatever that's off-topic."
    e "So yeah, I met this girl, I think you would've liked her."
    e "She listens to the same music you would, and she um"
    e "she helped me from relapsing the other day."
    e "Yeah..."
    e "Maybe I'll bring her around here sometime."
    e "I haven't told her about you yet, sorry."
    e "I'm just a little worried, y'know?"
    e "Cuz of how I was."
    e "I just hope she's better at dealing with this kind of thing than me."
    e "I still miss you."
    e "Every day."
    "It hasn't really gotten easier but I have people to support me through it."
    e "I love you, Valerie."
    stop music fadeout 0.3

    $ achievement.grant("true_ending")
    $ renpy.notify("Achievement Unlocked: Valerie.")
    jump credits_true_ending

transform credits_scroll:
    ypos 1080                  
    linear 120.0 ypos -5000       

    #return

#credits screens
screen credits_delusion():

    add "images/bg room.png" 

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 30

        #add Transform("images/logo.png", zoom=0.7, xalign=0.5)
        add "images/title_screen_logo.png" xalign 0.5
        text "A Game By Studio GKG" size 40 xalign 0.5

        null height 50

        #text "Writing\nAubrey \"Aubsickle\" Morra" xalign 0.5
        text "Writing" size 40 xalign 0.5
        text "Aubrey \"Aubsickle\" Morra" size 32 xalign 0.5
        text "\n"
        text "Programming" size 40 xalign 0.5
        text "Serena \"Renabetha\" D'Avanzo" size 32 xalign 0.5
        text "\n"
        text "3D Environments & Character Art" size 40 xalign 0.5
        text "Skye \"Ghost Fetus\" Peterson" size 32 xalign 0.5
        text "\n"
        text "Music" size 40 xalign 0.5
        text "Joe \"joe_con7\" Connors" size 32 xalign 0.5
        #text "3D Environments & Character Art\nSkye \"Ghost Fetus\" Peterson" xalign 0.5
        #text "Programming\nSerena \"Renabetha\" D'Avanzo" xalign 0.5
        #text "Music\nJoe \"joe_con7\" Connors" xalign 0.5
        text "\n"
        text "Logo & GUI Design" size 40 xalign 0.5
        text "Aubsickle" size 32 xalign 0.5
        text "\n"
        text "Voice Acting" size 40 xalign 0.5
        text "Evelyn - Aubsickle" size 32 xalign 0.5
        text "Valerie - Renabetha" size 32 xalign 0.5
        text "Kit - Beatrice \"Rubea\""size 32 xalign 0.5
        text "\n"
        text "Additional Help From" size 40 xalign 0.5
        text "Coding With Be and E" size 32 xalign 0.5
        text "Kia Azad" size 32 xalign 0.5
        text "Wattson" size 32 xalign 0.5
        text "\n"
        text "SFX from Pixabay.com" size 40 xalign 0.5
        text "\n"
        text "Speical Thanks" size 40 xalign 0.5
        text "You!!!" size 32 xalign 0.5

        null height 200

        text "Thank you for playing!" size 60 xalign 0.5

        null height 1000

screen credits_true_ending():

    add "images/bg cemetery.png" 

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 30

        #add Transform("images/logo.png", zoom=0.7, xalign=0.5)
        add "images/title_screen_logo.png" xalign 0.5
        text "A Game By Studio GKG" size 40 xalign 0.5

        null height 50

        #text "Writing\nAubrey \"Aubsickle\" Morra" xalign 0.5
        text "Writing" size 40 xalign 0.5
        text "Aubrey \"Aubsickle\" Morra" size 32 xalign 0.5
        text "\n"
        text "Programming" size 40 xalign 0.5
        text "Serena \"Renabetha\" D'Avanzo" size 32 xalign 0.5
        text "\n"
        text "3D Environments & Character Art" size 40 xalign 0.5
        text "Skye \"Ghost Fetus\" Peterson" size 32 xalign 0.5
        text "\n"
        text "Music" size 40 xalign 0.5
        text "Joe \"joe_con7\" Connors" size 32 xalign 0.5
        #text "3D Environments & Character Art\nSkye \"Ghost Fetus\" Peterson" xalign 0.5
        #text "Programming\nSerena \"Renabetha\" D'Avanzo" xalign 0.5
        #text "Music\nJoe \"joe_con7\" Connors" xalign 0.5
        text "\n"
        text "Logo & GUI Design" size 40 xalign 0.5
        text "Aubsickle" size 32 xalign 0.5
        text "\n"
        text "Voice Acting" size 40 xalign 0.5
        text "Evelyn - Aubsickle" size 32 xalign 0.5
        text "Valerie - Renabetha" size 32 xalign 0.5
        text "Kit - Beatrice \"Rubea\""size 32 xalign 0.5
        text "\n"
        text "Additional Help From" size 40 xalign 0.5
        text "Coding With Be and E" size 32 xalign 0.5
        text "Kia Azad" size 32 xalign 0.5
        text "Wattson" size 32 xalign 0.5
        text "\n"
        text "SFX from Pixabay.com" size 40 xalign 0.5
        text "\n"
        text "Speical Thanks" size 40 xalign 0.5
        text "You!!!" size 32 xalign 0.5

        null height 200

        text "Thank you for playing!" size 60 xalign 0.5

        null height 1000

screen credits_good_ending():

    add "images/bg hallway.png" 

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 30

        #add Transform("images/logo.png", zoom=0.7, xalign=0.5)
        add "images/title_screen_logo.png" xalign 0.5
        text "A Game By Studio GKG" size 40 xalign 0.5

        null height 50

        #text "Writing\nAubrey \"Aubsickle\" Morra" xalign 0.5
        text "Writing" size 40 xalign 0.5
        text "Aubrey \"Aubsickle\" Morra" size 32 xalign 0.5
        text "\n"
        text "Programming" size 40 xalign 0.5
        text "Serena \"Renabetha\" D'Avanzo" size 32 xalign 0.5
        text "\n"
        text "3D Environments & Character Art" size 40 xalign 0.5
        text "Skye \"Ghost Fetus\" Peterson" size 32 xalign 0.5
        text "\n"
        text "Music" size 40 xalign 0.5
        text "Joe \"joe_con7\" Connors" size 32 xalign 0.5
        text "\n"
        text "Logo & GUI Design" size 40 xalign 0.5
        text "Aubsickle" size 32 xalign 0.5
        text "\n"
        text "Voice Acting" size 40 xalign 0.5
        text "Evelyn - Aubsickle" size 32 xalign 0.5
        text "Valerie - Renabetha" size 32 xalign 0.5
        text "Kit - Beatrice \"Rubea\""size 32 xalign 0.5
        text "\n"
        text "Additional Help From" size 40 xalign 0.5
        text "Coding With Be and E" size 32 xalign 0.5
        text "Kia Azad" size 32 xalign 0.5
        text "Wattson" size 32 xalign 0.5
        text "\n"
        text "SFX from Pixabay.com" size 40 xalign 0.5
        text "\n"
        text "Speical Thanks" size 40 xalign 0.5
        text "You!!!" size 32 xalign 0.5

        null height 200

        text "Thank you for playing!" size 60 xalign 0.5

        null height 1000

screen credits_suicide():

    add "images/bg room.png" 

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 30

        #add Transform("images/logo.png", zoom=0.7, xalign=0.5)
        add "images/title_screen_logo.png" xalign 0.5
        text "A Game By Studio GKG" size 40 xalign 0.5

        null height 50

        #text "Writing\nAubrey \"Aubsickle\" Morra" xalign 0.5
        text "Writing" size 40 xalign 0.5
        text "Aubrey \"Aubsickle\" Morra" size 32 xalign 0.5
        text "\n"
        text "Programming" size 40 xalign 0.5
        text "Serena \"Renabetha\" D'Avanzo" size 32 xalign 0.5
        text "\n"
        text "3D Environments & Character Art" size 40 xalign 0.5
        text "Skye \"Ghost Fetus\" Peterson" size 32 xalign 0.5
        text "\n"
        text "Music" size 40 xalign 0.5
        text "Joe \"joe_con7\" Connors" size 32 xalign 0.5
        text "\n"
        text "Logo & GUI Design" size 40 xalign 0.5
        text "Aubsickle" size 32 xalign 0.5
        text "\n"
        text "Voice Acting" size 40 xalign 0.5
        text "Evelyn - Aubsickle" size 32 xalign 0.5
        text "Valerie - Renabetha" size 32 xalign 0.5
        text "Kit - Beatrice \"Rubea\""size 32 xalign 0.5
        text "\n"
        text "Additional Help From" size 40 xalign 0.5
        text "Coding With Be and E" size 32 xalign 0.5
        text "Kia Azad" size 32 xalign 0.5
        text "Wattson" size 32 xalign 0.5
        text "\n"
        text "SFX from Pixabay.com" size 40 xalign 0.5
        text "\n"
        text "Speical Thanks" size 40 xalign 0.5
        text "You!!!" size 32 xalign 0.5

        null height 200

        text "Thank you for playing!" size 60 xalign 0.5

        null height 1000


screen credits_infidelity():


    add "images/bg drugs.png" 

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 30

        #add Transform("images/logo.png", zoom=0.7, xalign=0.5)
        add "images/title_screen_logo.png" xalign 0.5
        text "A Game By Studio GKG" size 40 xalign 0.5

        null height 50

        #text "Writing\nAubrey \"Aubsickle\" Morra" xalign 0.5
        text "Writing" size 40 xalign 0.5
        text "Aubrey \"Aubsickle\" Morra" size 32 xalign 0.5
        text "\n"
        text "Programming" size 40 xalign 0.5
        text "Serena \"Renabetha\" D'Avanzo" size 32 xalign 0.5
        text "\n"
        text "3D Environments & Character Art" size 40 xalign 0.5
        text "Skye \"Ghost Fetus\" Peterson" size 32 xalign 0.5
        text "\n"
        text "Music" size 40 xalign 0.5
        text "Joe \"joe_con7\" Connors" size 32 xalign 0.5
        text "\n"
        text "Logo & GUI Design" size 40 xalign 0.5
        text "Aubsickle" size 32 xalign 0.5
        text "\n"
        text "Voice Acting" size 40 xalign 0.5
        text "Evelyn - Aubsickle" size 32 xalign 0.5
        text "Valerie - Renabetha" size 32 xalign 0.5
        text "Kit - Beatrice \"Rubea\""size 32 xalign 0.5
        text "\n"
        text "Additional Help From" size 40 xalign 0.5
        text "Coding With Be and E" size 32 xalign 0.5
        text "Kia Azad" size 32 xalign 0.5
        text "Wattson" size 32 xalign 0.5
        text "\n"
        text "SFX from Pixabay.com" size 40 xalign 0.5
        text "\n"
        text "Speical Thanks" size 40 xalign 0.5
        text "You!!!" size 32 xalign 0.5

        null height 200

        text "Thank you for playing!" size 60 xalign 0.5

        null height 1000

screen credits_bad_touch():

    add "images/bg bed.png" 

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 30

        #add Transform("images/logo.png", zoom=0.7, xalign=0.5)
        add "images/title_screen_logo.png" xalign 0.5
        text "A Game By Studio GKG" size 40 xalign 0.5

        null height 50

        #text "Writing\nAubrey \"Aubsickle\" Morra" xalign 0.5
        text "Writing" size 40 xalign 0.5
        text "Aubrey \"Aubsickle\" Morra" size 32 xalign 0.5
        text "\n"
        text "Programming" size 40 xalign 0.5
        text "Serena \"Renabetha\" D'Avanzo" size 32 xalign 0.5
        text "\n"
        text "3D Environments & Character Art" size 40 xalign 0.5
        text "Skye \"Ghost Fetus\" Peterson" size 32 xalign 0.5
        text "\n"
        text "Music" size 40 xalign 0.5
        text "Joe \"joe_con7\" Connors" size 32 xalign 0.5
        text "\n"
        text "Logo & GUI Design" size 40 xalign 0.5
        text "Aubsickle" size 32 xalign 0.5
        text "\n"
        text "Voice Acting" size 40 xalign 0.5
        text "Evelyn - Aubsickle" size 32 xalign 0.5
        text "Valerie - Renabetha" size 32 xalign 0.5
        text "Kit - Beatrice \"Rubea\""size 32 xalign 0.5
        text "\n"
        text "Additional Help From" size 40 xalign 0.5
        text "Coding With Be and E" size 32 xalign 0.5
        text "Kia Azad" size 32 xalign 0.5
        text "Wattson" size 32 xalign 0.5
        text "\n"
        text "SFX from Pixabay.com" size 40 xalign 0.5
        text "\n"
        text "Speical Thanks" size 40 xalign 0.5
        text "You!!!" size 32 xalign 0.5

        null height 200

        text "Thank you for playing!" size 60 xalign 0.5

        null height 1000
#credits labels
label credits_delusion:

    show screen credits_delusion
    play sound "audio/voicemail_delusion.mp3" 
 
    #scroll time 60ish seconds
    #scene bg pills with fade

    $ renpy.pause(70.0, hard=True)

    #hide screen credits with fade

    return

label credits_true_ending:

    show screen credits_true_ending
    play sound "audio/voicemail_true_ending.mp3" 
 

    $ renpy.pause(70.0, hard=True)

    #hide screen credits with fade

    return

label credits_good_ending:

    show screen credits_good_ending
    play sound "audio/voicemail_good_ending.mp3" 
 

    $ renpy.pause(70.0, hard=True)

    #hide screen credits with fade

    return 


label credits_suicide:

    show screen credits_suicide
    play sound "audio/voicemail_suicide.mp3" 
 

    $ renpy.pause(70.0, hard=True)

    #hide screen credits with fade

    return 

label credits_infidelity:

    show screen credits_infidelity
    play sound "audio/voicemail_infidelity.mp3" 
 

    $ renpy.pause(70.0, hard=True)

    #hide screen credits with fade

    return 

label credits_bad_touch:

    show screen credits_bad_touch
    play sound "audio/voicemail_bad_touch.mp3" 
 

    $ renpy.pause(70.0, hard=True)

    #hide screen credits with fade

    return 

