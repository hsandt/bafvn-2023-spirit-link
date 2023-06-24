label a1s1:

    # Renpy needs to be told to stop Main Menu BGM (Title Theme)
    stop music fadeout 2.0

    # TO REVISE: find a better act name
    "Act 1 - The summer fair" with dissolve

    pause 2.0

    "How far would you go to achieve your dreams?"
    # if "to pose a question" very formal? OK in this context?
    # here, "as a green" clear here that it applies to "me" and not "Professor Mara", but is it grammatically correct?
    "This was a question Professor Mara once posed to me as a green, first year."
    "At the time, I said ‘I'd do anything’. Now standing under the scorching, summer sun, I was reconsidering."

    scene bg university_outside with fade

    # uncomment when asset is ready
    # play music chill

    show charlet neutral at character_left
    charlet "Great Garuda, why did they have to choose {i}today{/i} to hold this event?"

    #sunlight effect? flash?

    hide charlet

    "Today was unmercifully hot. Humidity had made the air oppressive and the colorful umbrellas above me,
    dyed in the traditional patterns of the Mawi tribe, did little to protect from the heat."
    "I dabbed at the sweat on my brow, lamenting the loss of the expensive powder I had applied that morning."

    show charlet neutral at character_left
    charlet "Great. So much for best impressions."

    hide charlet

    #maybe show a mirror

    "A glance in the mirror revealed uneven patches of skin and smeared rouge. I swiped at it hastily, hoping no one noticed."
    "No one did. Of course not. Tucked in between the history and literature department's booths, my booth remains woefully forgotten."
    "Bored and sweaty I amuse myself by looking around. I..."

    jump .look_choice

label .look_choice:
    while not (has_looked_at_crowd and has_looked_at_booth):
        menu:
            "Look at the crowd." if not has_looked_at_crowd:
                call .look_at_crowd from _call_a1s1_look_at_crowd

            "Observe the booths." if not has_looked_at_booth:
                call .look_at_booth from _call_a1s1_look_at_booth

    jump .after_look

label .look_at_crowd:
    #bg focus on crowd (new bg or zoom in?)

    "A throng of curious passerbys fills Panha-Kam's courtyard, lured by the colorful booths lining the square."
    "Each department has brought their best each aiming to net themselves a rich, sponsor.
    Colorful signboards cry out the merits of their research."
    "The fair is a vibrant tapestry of agendas and ambitions. Representatives from all industries,
    from hunters’ and merchant guilds to investors, mingle with students and curious onlookers."

    $ has_looked_at_crowd = True
    return

label .look_at_booth:
    #bg focus on booth

    "A crowd catches my eye. The engineering and alchemy departments, of course."
    "Their towering displays command attention and their signs boast of life-changing advances in magitech,
    drawing representatives from the railroad and mining companies like flies to honey."
    # Understanding issue: faster *and* at 50 paces, or faster *when* at 50 paces? Did range improve from last model?
    "As I watch, a man in a suit examines the engineering team’s latest invention:
    a long-barreled rifle more accurate than the last, capable of shooting a bird faster at 50 paces."
    "I cringe as he peers down its nozzle."


    show makara neutral at character_right

    makara "Do not worry. Demonstration weapons are generally unloaded. Although it is true that humans should be more careful at these times."

    "My companion is right. Though it has been only two days since the attack in Alcatra, the event's security is concerningly lax."
    # When I read this first, I thought she was talking about people protecting the fair. After reading more below and checking the exact definition of
    # "vigilantes" I now see the double side of this. But I wonder how other people see it. It may sound like "a justice defender" or "a rebel" depending
    # on the point of view, which may or may not be frightening for a mere citizen. On the other side, maybe "terrorist" would be too strong?
    "The possibility of vigilantes hiding in the crowd, makes me tense."
    "My eyes scan the crowd and lingers on the men scattered throughout amongst them in the brown and green of the hunter’s guild."
    "Their expressions are friendly, but their eyes are sharp, and their stance gives off an air of purpose."
    "Friend or foe? In a sea of strangers it is impossible to know."

    "I force levity into my voice."

    charlet "Well, at least I have you, oh mighty Makara, to save me in spite of my poor, human senses."

    makara "Indeed. With me here, you need not fear anything."
    hide makara neutral
    hide charlet

    "A big boast from a little dragon, but the words gave me some comfort."

    # Flow issue: need transition?
    "While the ILF was, for the most part, peaceful in their efforts to advocate for recognition of Mocau-Laedan as a sovereign nation,
    the recent, vigilante attacks had cast doubt on the organization."
    "However much they might claim no association with the rebels, their track record didn't look good."

    $ has_looked_at_booth = True
    return

label .after_look:

    #breeze effect and maybe stomach growling sound effect?

    # maybe add a highlight of some sort of dessert like a call out a box in the middle of the screen?

    pause 1.0

    "Coconut oil and burnt sugar. My stomach rumbles at the scent of ume cakes in the air. I wish I had time to eat breakfast that morning, but had been too busy setting up the booth."

    show charlet neutral at character_left

    charlet "Maybe I should have focused my studies on food instead of folklore. At least then I’d have an excuse to eat."

    show makara neutral at character_right

    makara "And what? Bribed your advisor with cake? I could hardly see that working. With how much time she spends reading, one would think she lived off prose and not portions."

    charlet "Hey, Professor Mara isn’t that bad! Even she eats. Sometimes..."

    # show coffee or a view of the professor buried in books?

    charlet "Okay. You're right. But maybe I should have brought something edible. It doesn’t look like anyone is coming anytime soon."

    hide makara neutral

    "This event was my chance. I had to secure a sponsor."
    "Otherwise, my dreams of preserving the island's rich culture will dissipate like the mists that once shrouded Moacu-Laedan some 250 years ago."

    # odd transition, may need transitional sentence
    "The booth, pamphlets with their colorful photographs showcasing the island’s rich history seemed to mock me.
    I had spent months researching the island and stayed up all night printing pamphlets."
    "But for what? To hand out six to a handful of students who took them out of pity?"

    #stomach growling noise again

    charlet "...maybe I should just grab lunch."
    "Just as I make to leave, a voice stops me."

    show pichit neutral at character_right
    # When asset is ready, replace with:
    # show pichit happy at character_right

    pichit "Oi! Charlet! Hey!"

    "It was Pichit wearing his signature, broad grin. He was a born and bred native of Mocau-Laedan, though he had moved to the continent for school."

    "Bayani, another alumni from Alcatra University, had introduced him to me as a potential guide for my expedition two months ago."

    "He is also accompanied by a spirit."

    # Move characters to far sides to leave space for spirits
    show charlet at character_far_left
    show pichit at character_far_right

    show makara neutral at companion_middle_left, flip
    show fan neutral at companion_middle_right

    makara "We meet again, my fellow. How do you feel today?"

    fan "The flowers here are healthy despite the sun of summer... The gardeners must be playing close attention."

    makara "... I will take this as your greetings."

    "I'm glad that only both of us can see and hear our spirits. Especially as I see a man I don't know in the back."

    hide makara
    hide fan

    charlet "Hey Pichit. Who is the gentleman with you?"

    # When asset is ready, replace with:
    show pichit neutral at character_middle
    # show pichit happy at character_right
    show raegan neutral at character_right

    "Behind him is a stranger, tall and elegantly dressed in a three-piece suit, despite the heat. He should have been drenched in sweat."
    "Instead his collar and cuffs were clean and neat as though freshly laundered.
    Even his hair was impeccable. Meanwhile, my own hair felt matted and itchy."

    pichit "Charlet, I'd like to introduce you to Mr. Raegan Vanich! He is the third son of Lord Vanich, founder of the Vanich Trading Company."
    "He said he was interested in sponsoring the expedition!"

    pichit "Raegan, this is Dr. Charlet Kasamsun, the brains of behind the expedition."

    raegan "A pleasure to meet you, Charlet. I've heard wonderful things about your plans."

    charlet "Likewise, Mr. Vanich. The Vanich company has done so many amazing things, it is a great honor to meet you."

    raegan "Just Raegan, please. Should all go well, I imagine we will be working very closely together."

    "His smile is dangerously charming and I find myself flustered by my own reaction to it."

    charlet "Raegan, then."

    #more scene tbd

    # End of playtesting

    pause 1.0

    "This is the end of the playtesting section. Thank you for playing!"

    # Commented out for playtesting
    # "3. As MC and Raegan begin making arrangements to meet up, the group the area begins to fill with smoke"

    # jump a1s2
