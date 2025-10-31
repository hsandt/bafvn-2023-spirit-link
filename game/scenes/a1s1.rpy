label a1s1:

    # Renpy needs to be told to stop Main Menu BGM (Title Theme)
    stop music fadeout 2.0

    call start_cinematic from _call_start_cinematic

    pause 1.0

    image act_title = Text("{color=[gui.idle_color]}{size=80}Act 1 - The Summer Fair{/size}{/color}")

    show act_title:
        yalign 0.5
        xalign 0.5
    with dissolve

    pause 2.0

    hide act_title with dissolve

    call end_cinematic from _call_end_cinematic

    "How far would you go to achieve your dreams?"
    "This was a question Professor Mara once posed to me as a naive, first year."
    "At the time, I said “I’d do anything”. Now, I am reconsidering."

    call start_cinematic from _call_start_cinematic_1

    scene bg university_outside with fade
    play music mystery

    # uncomment when asset is ready
    # play music chill

    show charlet exhausted at character_warp_to("middle_left")

    call end_cinematic from _call_end_cinematic_1

    charlet "Great Garuda, why did they have to choose {i}today{/i} to hold this event?"

    #sunlight effect? flash?

    "Today is unmercifully hot. Humidity has made the air oppressive and the colorful umbrellas above me,
    dyed in the traditional patterns of the Mawi tribe, did little to protect from the heat."
    "I dab at the sweat on my brow, lamenting the loss of the expensive powder I applied that morning."

    charlet sad "Great. So much for best impressions."

    #maybe show a mirror

    "A glance in the mirror reveals uneven patches of skin and smeared rouge. I swipe at it hastily, hoping no one noticed."
    "No one did. Of course not. Tucked in between the history and literature department’s booths, my own remains woefully forgotten."

    show charlet exhausted zorder 1

    "Bored and sweaty, I amuse myself by looking around."

    jump .look_choice

label .look_choice:
    while not (has_looked_at_crowd and has_looked_at_booth):
        if has_looked_at_crowd or has_looked_at_booth:
            "I look around a bit more."

        menu:
            "I look at the crowd." if not has_looked_at_crowd:
                call .look_at_crowd from _call_a1s1_look_at_crowd

            "I observe the booths." if not has_looked_at_booth:
                call .look_at_booth from _call_a1s1_look_at_booth

    jump .after_look

label .look_at_crowd:
    #bg focus on crowd (new bg or zoom in?)

    hide charlet with character_dissolve

    "A throng of curious viewers fills Panha-Kam University’s courtyard, lured by the colorful booths lining the square."
    "Each department has brought their best, each aiming to net themselves a rich sponsor.
    Colorful signboards cry out the merits of their research."

    "The fair is a vibrant tapestry of agendas and ambitions. Representatives from all industries,
    from hunter’s and merchant’s guilds to investors, mingled with students and curious onlookers."

    show charlet exhausted at character_warp_to("middle_left") zorder 1
    with character_dissolve

    $ has_looked_at_crowd = True
    return

label .look_at_booth:
    #bg focus on booth

    hide charlet with character_dissolve

    "A crowd catches my eye. The engineering and alchemy departments, of course."
    "Their towering displays command attention and their signs boast of life-changing advances in magitech,
    drawing representatives from the railroad and mining companies like flies to honey."

    "As I watch, a man in a suit examines the engineering team’s latest invention:
    a long-barreled rifle more accurate than the last, capable of shooting a bird at 50 paces."

    # Show above companion
    show charlet scared at character_warp_to("middle_left") zorder 1

    "I cringe as he peers down its nozzle."

    show makara neutral at companion_warp_to("middle_right")

    makara "Fear not. I can smell the weapon is unloaded. Although it is true that humans should be more cautious. Especially with such weak senses."

    show charlet neutral

    "Makara is right. Though it has been only two days since the attack in Alcatra, the event’s security is concerningly lax."
    "Here were some of Enon’s most brilliant minds and richest merchants, all conveniently gathered in one place. A perfect target."

    "The possibility of vigilantes and would-be terrorists hiding in the crowd leaves my heart in my throat."
    "I scan the crowd, my eyes lingering on the scattered men dressed in the brown and green of the hunter’s guild."
    "Their gestures are friendly, but their eyes are sharp, and their stances suggest an air of purpose. Friend or foe?"

    show charlet intrigued

    "In a sea of strangers, it is impossible to know. The Island Liberation Front, or {i}ILF{/i}, had thousands of followers. Any one here could be a member."
    "And while the ILF was, generally, peaceful in their efforts to advocate for recognition of Mocau-Laedan as a sovereign nation,
    the recent attacks have cast doubt on the organization."
    "Were the attacks really just the work of independent rebels? Or was the ILF just trying to save face?"

    show charlet neutral

    "I force levity into my voice."

    charlet smile "Well, at least I have you, {i}oh mighty Makara{/i}, to save me in spite of my poor, human senses."

    makara "Indeed. With me here, you need not fear anything."

    show charlet smile

    "A big boast from a little dragon.\n"
    extend "Nonetheless, the words give me some comfort."

    hide makara with character_dissolve
    show charlet exhausted

    $ has_looked_at_booth = True
    return

label .after_look:

    #breeze effect and maybe stomach growling sound effect?

    # maybe add a highlight of some sort of dessert like a call out a box in the middle of the screen?

    window hide
    pause 1.0
    window show

    "Coconut oil and burnt sugar. My stomach rumbles at the scent of ume cakes in the air. I wish I had time to eat breakfast that morning, but I’d been too busy setting up the booth."

    show charlet sad

    charlet "I wish I had brought some traditional dishes from Moacu. That would be on topic, and I’d have an excuse to eat."

    show makara neutral at companion_warp_to("middle_right")

    makara "An interesting idea. Whom would you ask to cook them?"

    charlet "Sorry? I can handle a few son-in-law eggs on my own."

    makara "Yet, I do remember that your experiments from last year did not lead to the expected color. While I do not eat human food, my keen sense of smell suggested that–"

    charlet "Okay, okay. I’ll just ask Aunt Urai next time."

    "Talking so much with Makara in a public space would usually grant me funny looks from Enonians, who cannot see or hear spirits."
    "But the only people here are my booth neighbors, who are well-versed in Islander culture. They won't blame me for this."
    "Besides, the blue jewel that adorns my armband looks like a telestone on purpose: it makes people think that I'm remotely talking to someone. Good to live in the modern age."

    hide makara with character_dissolve

    pause 0.5

    "Anyway, this event is my chance. I have to secure a sponsor."
    "Otherwise, my dreams of preserving the Island’s rich culture will dissipate like the mists that once shrouded Moacu-Laedan some 250 years ago."

    "The booth’s pamphlets, with their colorful photographs showcasing the Island’s rich history, seem to mock me.
    I have spent months researching the Island and stayed up all night printing pamphlets."
    "But for what? To hand out six to a handful of students who took them out of pity?"

    #stomach growling noise again

    charlet "… Maybe I should just grab lunch. It doesn’t look like anyone is coming anytime soon."
    "Just as I prepare to leave, a voice stops me."

    jump .pichit_arrives

label .pichit_arrives:

    # Show above companion
    # KNOWN ISSUE: ideally Pichit would be looking left but because he wasn't drawn with flipping in mind,
    # he looks a bit odd when flipped, so we keep him looking to the right even if it's weird that he's
    # not looking at Charlet
    show pichit smile at character_warp_to("right") zorder 1

    pichit "Oi! Charlet! Hey!"

    show pichit at character_move_to("middle_right")

    "It is Pichit wearing his signature, broad grin. He was a born and bred native of Moacu-Laedan, though he moved to the continent for school."

    "Bayani, another alumni from Panha-Kam University, introduced him to me as a potential guide for my expedition two months ago."

    show charlet smile

    charlet "Hey, Pichit! Thanks for coming today."

    "He is also accompanied by a spirit."

    call start_cinematic from _call_start_cinematic_2

    # Move characters to far sides to leave space for spirits
    show charlet at character_move_to("left", 0.5)
    show pichit at character_move_to("right", 0.5)
    pause 0.5

    show makara neutral at companion_warp_to("middle_left"), flip
    show fan neutral at companion_warp_to("right", _xpos_offset=-0.03)

    pause 0.5

    call end_cinematic from _call_end_cinematic_2

    makara "We meet again, my fellow. How do you feel today?"

    window hide
    pause 1.0
    window show

    fan "The flowers here are healthy despite the summer sun… The gardeners must be paying close attention."

    makara "… I suppose this means you are fine."

    window hide
    pause 0.2
    window show

    "Fan is Pichit’s forest spirit. Like many companions, it has a very different personality than its human counterpart. But it does share his love of nature."

    "I let our spirits hold their whimsical conversation while I chitchat with Pichit in Laedani. My northern accent gradually transitions to southern as I mimic Pichit to put him at ease."

    window hide
    pause 0.5
    window show

    "As we talk about the fair's organization, a man I don’t know approaches from behind Pichit."

    hide makara
    hide fan
    with character_dissolve

    jump a1s2
