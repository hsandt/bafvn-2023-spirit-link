label a1s1:

    # Renpy needs to be told to stop Main Menu BGM (Title Theme)
    stop music fadeout 2.0

    # TO REVISE: find a better act name
    "Act 1 - The summer fair" with dissolve

    # TODO komehara: add location to explain player we are on Enon

    pause 2.0

    "How far would you go to achieve your dreams?"
    # if "to pose a question" very formal? OK in this context?
    # here, "as a green" clear here that it applies to "me" and not "Professor Mara", but is it grammatically correct?
    "This was a question Professor Mara once posed to me as a naive, first year."
    "At the time, I said ‘I'd do anything’. Now, I was reconsidering."

    $ quick_menu = False

    scene bg university_outside with fade
    play music mystery

    # uncomment when asset is ready
    # play music chill

    show charlet exhausted at character_warp_to("middle_left")

    $ quick_menu = True

    charlet "Great Garuda, why did they have to choose {i}today{/i} to hold this event?"

    #sunlight effect? flash?

    "Today was unmercifully hot. Humidity had made the air oppressive and the colorful umbrellas above me,
    dyed in the traditional patterns of the Mawi tribe, did little to protect from the heat."
    "I dabbed at the sweat on my brow, lamenting the loss of the expensive powder I had applied that morning."

    charlet sad "Great. So much for best impressions."

    #maybe show a mirror

    "A glance in the mirror revealed uneven patches of skin and smeared rouge. I swiped at it hastily, hoping no one noticed."
    "No one did. Of course not. Tucked in between the history and literature department's booths, my own remains woefully forgotten."

    show charlet exhausted

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

    # FIXME: Panha-Kam vs Alcatra University
    "A throng of curious viewers fills Panha-Kam's courtyard, lured by the colorful booths lining the square."
    "Each department has brought their best, each aiming to net themselves a rich sponsor.
    Colorful signboards cry out the merits of their research."

    "The fair is a vibrant tapestry of agendas and ambitions. Representatives from all industries,
    from hunter’s and merchant guilds to investors, mingled with students and curious onlookers."

    $ has_looked_at_crowd = True
    return

label .look_at_booth:
    #bg focus on booth

    hide charlet with character_dissolve

    "A crowd catches my eye. The engineering and alchemy departments, of course."
    "Their towering displays command attention and their signs boast of life-changing advances in magitech,
    drawing representatives from the railroad and mining companies like flies to honey."

    # Understanding issue: faster *and* at 50 paces, or faster *when* at 50 paces? Did range improve from last model?
    "As I watch, a man in a suit examines the engineering team’s latest invention:
    a long-barreled rifle more accurate than the last, capable of shooting a bird faster than 50 paces."

    # Show above companion
    show charlet scared at character_warp_to("middle_left") zorder 1

    "I cringe as he peers down its nozzle."

    show makara neutral at companion_warp_to("middle_right")

    makara "Fear not. I can smell the weapon is unloaded. Although it is true that humans should be more cautious. Especially with such weak senses."

    show charlet neutral

    "Makara is right. Though it has been only two days since the attack in Alcatra, the event's security is concerningly lax."
    "Here were some of Enon's most brilliant minds and richest merchants, all conveniently gathered in one place. A perfect target."

    "The thought left me tense. The possibility of vigilantes and would-be terrorists hiding in the crowd left my heart in my throat."
    "I scan the crowd, my eyes lingering on the scattered men dressed in the brown and green of the hunter’s guild."
    "Their expressions are friendly, but their eyes are sharp, and their stances suggest an air of purpose. Friend or foe?"

    show charlet intrigued

    # TODO komehara: explain ILF
    "In a sea of strangers, it is impossible to know. The ILF had thousands of followers. Any one here could be a member."
    "And while the ILF was, generally, peaceful in their efforts to advocate for recognition of Mocau-Laedan as a sovereign nation,
    the recent attacks had cast doubt on the organization."
    "Were the attacks really just the work of independent rebels? Or was the ILF just trying to save face?"

    show charlet neutral

    "I force levity into my voice."

    charlet smile "Well, at least I have you, {i}oh mighty Makara{/i}, to save me in spite of my poor, human senses."

    makara "Indeed. With me here, you need not fear anything."

    show charlet smile

    "A big boast from a little dragon.\n"
    extend "Nonetheless, the words gave me some comfort."

    show charlet neutral
    hide makara with character_dissolve

    $ has_looked_at_booth = True
    return

label .after_look:

    #breeze effect and maybe stomach growling sound effect?

    # maybe add a highlight of some sort of dessert like a call out a box in the middle of the screen?

    pause 1.0

    # Show above companion
    show charlet exhausted at character_warp_to("middle_left") zorder 1

    "Coconut oil and burnt sugar. My stomach rumbles at the scent of ume cakes in the air. I wish I had time to eat breakfast that morning, but I'd been too busy setting up the booth."

    show charlet intrigued

    charlet "Maybe I should have focused my studies on food instead of folklore. At least I’d have an excuse to eat."

    show makara neutral at companion_warp_to("middle_right")

    # FIXME logic: if she changed field of studies, she would also have a different advisor

    makara "And what? Bribed your advisor with cake? I could hardly see that working. With how much time she spends reading, one would think she lived off prose and not portions."

    charlet "Hey, Professor Mara isn’t that bad! Even she eats. Sometimes..."

    # show coffee or a view of the professor buried in books?

    charlet "Okay. You're right. But maybe I should have brought something edible."

    hide makara neutral with character_dissolve

    pause 0.5

    "This event was my chance. I had to secure a sponsor."
    "Otherwise, my dreams of preserving the island's rich culture will dissipate like the mists that once shrouded Moacu-Laedan some 250 years ago."

    "The booth's pamphlets, with their colorful photographs showcasing the island’s rich history, seemed to mock me.
    I had spent months researching the island and stayed up all night printing pamphlets."
    "But for what? To hand out six to a handful of students who took them out of pity?"

    #stomach growling noise again

    charlet "... maybe I should just grab lunch. It doesn’t look like anyone is coming anytime soon."
    "Just as I prepare to leave, a voice stops me."

    # Show above companion
    show pichit smile at character_warp_to("right") zorder 1

    pichit "Oi! Charlet! Hey!"

    show pichit at character_move_to("middle_right")

    "It was Pichit wearing his signature, broad grin. He was a born and bred native of Moacu-Laedan, though he had moved to the continent for school."

    # FIXME: Panha-Kam vs Alcatra University
    "Bayani, another alumni from Alcatra University, had introduced him to me as a potential guide for my expedition two months ago."

    "He is also accompanied by a spirit."

    # Move characters to far sides to leave space for spirits
    show charlet at character_move_to("left")
    show pichit at character_move_to("right")

    show makara neutral at companion_warp_to("middle_left"), flip
    show fan neutral at companion_warp_to("middle_right")

    makara "We meet again, my fellow. How do you feel today?"

    fan "The flowers here are healthy despite the sun of summer... The gardeners must be playing close attention."

    makara "... I will take this as your greetings."

    "I'm glad that only both of us can see and hear our spirits. Especially as I see a man I don't know in the back."

    hide makara
    hide fan
    with character_dissolve

    show charlet at character_move_to("left")

    charlet "Hey Pichit. Who is the gentleman with you?"

    show pichit neutral at character_move_to("middle")
    show raegan neutral at character_warp_to("right")

    "Behind him is a stranger, tall and elegantly dressed in a three-piece suit, despite the heat. He should have been drenched in sweat."
    "Instead his collar and cuffs were clean and neat as though freshly laundered.
    Even his hair was impeccable. Meanwhile, my own hair felt matted and itchy."

    pichit smile "Charlet, I'd like to introduce you to Mr. Raegan Vanich! He is the third son of Lord Vanich, founder of the Vanich Trading Company."
    "He said he was interested in sponsoring the expedition!"

    pichit "Raegan, this is Dr. Charlet Kasamsun, the brains behind the expedition."

    raegan "A pleasure to meet you, Charlet. I've heard wonderful things about your plans."

    charlet smile "Likewise, Mr. Vanich. The Vanich Trading Company has done so many amazing things, it is a great honor to meet you."

    raegan smile "Just Raegan, please. Should all go well, I imagine we will be working very closely together."

    "His smile is dangerously charming and I find myself flustered by my own reaction to it."

    charlet "Raegan, then."

    #more scene tbd

    # Commented out for playtesting
    # "3. As MC and Raegan begin making arrangements to meet up, the group the area begins to fill with smoke"

    jump a1s2
