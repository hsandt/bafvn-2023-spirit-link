label a1s2:
    "Act 1: Scene 2 - Gathering Attack"
    jump .assassin_appears

label .assassin_appears:
    scene bg university_outside

    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("middle")
    show pichit neutral at character_warp_to("right"), darker

    raegan "It's always a pleasure to meet someone who can appreciate the island's unique charm. What drove your interest?"

    charlet "My ascendants came from the island. Studying at the academia made me realize just how little we, in Enon, know about Moacu."

    # TODO Seri: fill discussion on future work, adding details about it (collecting old tales, relationship with spirits)
    charlet "I am hoping this work will help build bridges between our peoples."

    show charlet intrigued
    show raegan intrigued
    show pichit intrigued at reset_brightness

    "Before Raegan can respond, a commotion behind him made all three of us turn."
    "Smoke seems to pour out of a few stands to the west; confused mumblings rise from the nearby crowd."

    raegan "My pardons, Pichit, was this planned as part of the event?"

    show pichit smile

    "Pichit smiles lazily, waving a hand to dismiss the commotion."

    pichit "Some demonstrations must have malfunctioned, it's nothing to be concerned about, sir."

    scene bg smoke with Dissolve(0.25)
    show phrarat neutral at character_warp_to("middle")

    stop music fadeout 1.0
    pause 0.5

    "No sooner have the words left Pichit’s mouth that a man covered in red emerges from the dispersing smoke. A knife flashes on his waist."

    "He tears a piece of his fabric scarf, wads it up into his hand..."

    play sound audio.sfx.fire

    "... and makes it burn."

    scene bg university_inside with Dissolve(0.25)
    show charlet scared at character_warp_to("far_left", 0.5)
    show raegan surprised at character_warp_to("middle_left", 0.5)
    show pichit surprised at character_warp_to("middle_right", 0.5)
    show phrarat neutral at character_warp_to("far_right")

    pause 0.5

    charlet "A vigilante?!"

    "The man grits his teeth before launching the fire projectile with inhuman speed directly at Raegan."

    show phrarat determined at bump_left
    pause 0.1
    show pichit battle serious at character_move_to("middle", 0.25)
    pause 0.25
    play sound audio.sfx.throw
    pause 0.5

    "Before Raegan or I could react, Pichit's sword thrusts forward, protecting Raegan from the projectile and sending it falling to the pavement."

    "Pichit spun suddenly, with no trace of his earlier, easy humor left on his face."

    show pichit shout

    pichit "Get inside, now!"

    # Needs timed menu, will do later if we still want this

    # "What do I do?!? If I leave, Pichit might be killed, but if Raegan, our only potential investor was hurt, the entire deal would fall through. I decide to…"

    # menu:
    #     "Stay.":
    #         "I can’t let Pichit face the assassin alone. Makara is strong. I can do this."

    #     "Go.":
    #         "Pichit can handle himself. I need to have faith in him and ensure Raegan gets away. I could always contact someone using a telepathy spell if needed."

    # "The choice is stolen from me just as I finally make up my mind."

    "Vanich grabs my arm, hauling me backward into a nearby storage room."

    show charlet at character_exit_to_left(0.5)
    show raegan at character_exit_to_left(0.8)
    show pichit battle serious at character_move_to("left")
    show phrarat at character_move_to("right")

    pause 1.0

    phrarat "Don’t get in my way, I have no quarrel with you."

    pichit "Who are you?"

    phrarat "I’m your savior."

    jump .fight1

label .fight1:

    "{i}I don't know what he's talking about, but he seems pretty determined to finish Raegan. I won't let him!{/i}"

    play music battle
    pause 1.7

    show phrarat determined at character_move_to("middle_right", 0.1)
    pause 0.05
    show pichit at character_move_to("far_left", 0.1)
    play sound audio.sfx.scarf

    "The assassin uses his scarf as a whip and swings it toward my face. I dance backward to dodge..."

    play sound audio.sfx.slash_impact3
    pause 0.15

    show pichit at character_move_to_easein_elastic("middle_left", 0.4)
    show phrarat at bump_left(0.05, 0.1)

    pause 0.25

    show phrarat at character_move_to("middle_right", 0.25)
    show bg at hpunch_powerful

    "... and slash back with a stroke of my blade, but my opponent blocks it."
    "We keep crossing each other's blade."

    $ count = 2

    while count > 0:

        show pichit at character_move_to_easein("left", 0.25)
        show phrarat at character_move_to_easein("right", 0.25)

        pause 0.15
        play sound audio.sfx.slash_impact3
        pause 0.10

        show pichit at character_move_to_easein_elastic("middle_left", 0.25)
        show phrarat at character_move_to_easein_elastic("middle_right", 0.25)
        show bg at hpunch_powerful
        pause 0.5

        $ count -= 1

    "Our two blades lock."

    play sound audio.sfx.scarf
    pause 0.5
    play sound audio.sfx.catch
    pause 0.1
    show phrarat at bump_left(0.05, 0.1)
    show pichit at fall_left

    "The Assassin wraps his whip around my leg, pulls it to make me lose my balance and tackles me to the ground."

    "If only I could get rid of that whip! Come to think of it, how hadn’t it burned to ash already?"

    # TODO - reformat below

    "Pichit continued to attack to no avail."

    "There, I spied it. A small spirit hidden in the assassin’s headdress. It was reconstructing the cloth faster than it burned."
    "Recalling my lessons with my father I  reached out into the ether, calling for Pichit."
    "Please. Please let him hear it. Then. There it was. A snap!"

    charlet "On his shoulder! There’s a spirit on his shoulder. It is keeping the scarf from burning up!"

    "Pichit looked surprised but responded with perfect fluidity. It was obvious from his movements he had done this before."

    pichit "Of course! Fan, a little help please!"

    show fan neutral at companion_warp_to("left")

    "A large bark shield wove itself into existence around Pichit’s arm."

    phrarat "Neat parlor trick. Too bad your shield will burn to ash long before Vanich has a chance to escape."

    scene bg black with CropMove(0.5, "wipeleft")
    scene bg university_inside with wipeleft

    show charlet neutral at character_warp_to("left")

    # TODO: simplify top rafters
    "Through a haze of smoke the assassin fixates his gaze on us. Spinning back, I notice Raegan is missing."
    "A sound pulls my gaze upwards. There. he somehow made his way up onto one of the top rafters."
    "I never imagined he was so nimble, I thought a little hysterically. He looks down on me."

    show raegan neutral at character_warp_to("right")
    # show raegan smile at character_warp_to("right")

    "There’s sprinklers in this building."

    "Brilliant, it seemed he was indeed a genius after all. It would be a pleasure to work with him if we survived this."
    "Reaching out to the connection, I tell Pichit the plan, who starts backing up toward the warehouse entrance."

    scene bg university_inside
    show pichit neutral at character_warp_to("left")
    show phrarat neutral at character_warp_to("right")
    # show phrarat angry at character_warp_to("right")

    phrarat "Cowering away as usual Pichit Sirawa!"

    pichit "You! H-How do you know my name?"

    phrarat "I know the names of all my family. Especially cowards who betray our heritage for the likes of Vanich enterprises."

    "The assassin flicks his wrist. A rope binds Pichit’s shield, burning it to ash. rope twirls around Pichit’s wooden shield, searing it to pieces."
    "Your guide’s spirit is quick enough to blast vines through the ground, blocking the Assassin’s path and allowing Pichit to inch closer to the building."

    pichit "Ironic coming from someone who keeps burning his own tribal cloth. What would your ancestors say?"

    phrarat "A small price to pay. Their corruption must stop. They are raping our land, stealing our gemstones, murdering our spirits for their own gain."

    "The Assassin strikes at the vines. Instead of cleaving through them, more, grow back in their place."

    pichit "For someone so concerned with our native culture, I’m surprised you don’t even recognize what type kind of vines these are."

    "Perpetua plants. A smart move. The vines would regenerate faster than he could do damage. Now it was just a matter of how much energy the assassin’s spirit  had left."

    "A snap sounded in my mind. Professor Mara’s voice stirred to life. Finally, using my abilities, I snap both Pichit and Mara together into one connection."

    mara "Charlet, are you still at the fair? Security has been sent in, they’re demanding to know if Raegan Vanich is safe."

    "A groaning Pichit answers."

    pichit "For the moment."

    charlet "We have a plan-"

    mara "There’s no time! Goto the basement. There should be a console there that will lock you in a safe room."

    "Good enough. breaking the connection I head upstairs towards Raegan who's too busy studying the switch, flipping it back and forth."

    scene bg university_inside
    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("right")

    raegan "There’s no electricity. It’s got to be in the basement."

    charlet "There’s no time to explain. Here, take it."

    "Grabbing a gemstone from my back pocket I shove it into Raegan’s hands."

    charlet "It’ll protect you and let me communicate with you. I’ll turn the sprinklers on once he’s inside and you get the power on!"

    "To his credit the Raegan sighs but does as he is told, loping down the stairs and toward the secure room."
    "Once the door slams behind him, I reestablish a connection with Pichit."

    "I try to analyze the opponent."

    call .analyze_one_element from _call_a1s2_analyze_one_element

    scene bg university_inside
    show pichit neutral at character_warp_to("left")
    show phrarat neutral at character_warp_to("right")

    pichit "Why Vanich? There are men out there that are far worse. He at least acts humanely."

    phrarat "You really think so? You think there’s profit in waiting for spirits to die? Don’t tell me you really believe they offer their gemstones willingly? No!"
    phrarat "He takes them by force just like the rest. He just hides it better than the others."

    # show phrarat angry

    phrarat "Pen, now."

    "The telepathic connection with Pichit goes numb for a moment before the entryway erupts, caving in, my guide along with it, caked in dirt."

    pichit "That worked faster than expected."

    "Smoke begins to ooze into the warehouse, Pichit wouldn’t see an attack coming before it was too late!"
    "I call upon Makara for assistance but he refused, the smoke would only render him useless."

    phrarat "No more plants, no more chances. Choose: move or die."

    "Before I’m able to get a good look, a sword skewers out of the shadows and toward Pichit, who barely dodges it but is sent careening into one of the exhibits. A glass case full of exquisite vases."

    "I try to analyze the opponent once more."

    call .analyze_one_element from _call_a1s2_analyze_one_element_1

    scene bg university_inside
    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("right")

    "In addition, Lobbyist notices a fire sprinkler inside the building. MC transmits the info and tell Guide to lure him inside the building."

    jump .fight2

label .fight2:
    scene bg university_inside
    show pichit neutral at character_warp_to("left")
    show phrarat neutral at character_warp_to("right")

    # show phrarat sad
    # TODO: pen sad
    show pen neutral at companion_warp_to("far_right")

    phrarat "What a waste."

    # This raises guide's sympathy
    "Entirely focused on the shattered remains of the exhibit, vases shattered, dirt and seeds that had been hidden in the vases scattered across the floor. Such history, wasted."

    "Without hesitation, the Assassin flips his dagger and sends it hurling for Pichit’s head."
    "Pichit expected it, using the dirt and seeds on the floor, he springs forth spiked vines that envelop the dagger, only for them to smash whatever is left of the exhibit vases in the process."

    hide pen

    phrarat "You destroy our culture without hesitation."

    "Before Pichit can respond, the man from the military booth emerges from the open doorway behind the Assassin. his rifle aimed for the Assassin’s head."

    man_with_rifle "Freeze!!!"

    "A smirk widens across the Assassin's face and the showman pulls the trigger, but nothing happens."
    "The Assassin begins to laugh, turning away from the man who’s still fiddling with the rifle."

    phrarat "The idiot can't even shoot his rifle. Proof that even the universe wants me to succeed."

    "After knocking the gun around  enough times, the rifle erupts, knocking the man back into concrete and distracting the Assassin long enough for Pichit to strike."
    "Bringing the vines upward from the discarded dagger, Pichit slashes them across the Assassins arm who stumbles to the ground almost immediately, his spirit tossed off his shoulder in the process."

    pichit "Poison in the spikes."

    "The Assassin grips at the ground, trying to grapple his way toward his Spirit only who isn’t even moving from where it landed. It’s panting relentlessly, trying to catch its breath."

    pichit "This is over. I know your cause is a noble one, please, let me help you."

    "The Assassin bares his teeth as a response and with a sudden screech of his shoes, rolls upward, snatching his spirit into his arms and landing on his feet."
    "Immediately he brings his dagger close, cutting another piece of his scarf, putting it to the spirits mouth."

    phrarat "Please, make more, I need another whip."

    "The spirit doesn’t move, doesn’t start weaving, it’s too tired from constantly weaving pattern after pattern for its master to use."
    "Pichit, assured that there’s no fight left in the spirit, finally lets the vines fall to the ground for good this time."

    # show phrarat angry

    "No, no, please, we need to burn it! All of it!!!"

    "The Assassin lights a solitary flame in his hand and shakily brings it to his scarf. He’s going to ignite his actual scarf, and use that as his last ditch effort."
    "Fortunately I feel Raegan’s presence as he finally links up with my gemstone."

    scene bg university_inside
    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("right")

    raegan "I do hope I’m not late, the power should be back on."

    charlet "Great."

    "I pull the lever, opening the sprinklers and sending sparkles of water to coat everything in the warehouse, including the Assassin's flame which sputters out in his hand."
    "He looks up, searching for the source of the sudden indoor rain and sees the lever I just pulled. He falls to his knees."

    scene bg university_inside
    show pichit neutral at character_warp_to("left")
    show charlet neutral at character_warp_to("middle")
    show phrarat neutral at character_warp_to("far_right")

    phrarat "Of course, the host to Makara is the one who stops me."

    "How did he know Makara, the spirit wasn’t even visible!?!? I don’t know but there is a pure and unadulterated hatred simmering in his eyes."

    charlet "What does that matter?"

    "The Assassin ignores my question but doesn’t break eye contact."

    phrarat "How ironic, of course they decided to put a sprinkler in here instead of over there."

    pichit "Over where?"

    phrarat "Vanich enterprises let my father burn alive in a factory because they weren’t willing to spend the money in a poorer district to ensureit was well protected."

    "I don't know what to say to that, Pichit doesn’t know what to say to that and Raegan is dead silent over the shared link."
    "The sounds of hooves and shuffling boots, sound at the entrance to the warehouse where the Military showman must have slinked off to."
    "The Assassin hears it too and in an instant, procures a circular pouch from his belt, slamming it onto the ground below, by the time the smoke clears, he and his Spirit are gone."

    hide phrarat

    # End of playtesting

    pause 1.0

    "This is the end of the playtesting section. Thank you for playing!"

    return
    # jump a1s3

label .analyze_one_element:
    menu:
        "Analyze weapon" if not has_analyzed_assassin_weapon:
            call .analyze_weapon from _call_a1s2_analyze_weapon
        "Analyze stone" if not has_analyzed_assassin_stone:
            call .analyze_stone from _call_a1s2_analyze_stone

    return

label .analyze_weapon:
    # TODO: new text
    "Clothes have traditional patterns of Moacu, but are written roughly."
    "Ink mixed with blood. Shows pride but also anger and hastiness. He doesn't care about his environment enough."
    "Guide could take advantage of this, or try to slow him down."
    $ has_analyzed_assassin_weapon = True
    return

label .analyze_stone:
    "Normally people and esp. Moacu natives are specialized in one color. A few experts master two colors."
    "In his case, the creature (that she can see) is clearly Green and handles cloth creation and patterns."
    "So Red Fire must be produced by the stone, maybe stolen from the previous attack."

    "He seems to be mastering Fire less and attacks are quite brutal and uncontrolled. Guide could take advantage of this."

    "Creature seems exhausted, maybe by the usage of Fire on top of its works. Maybe he can't create more cloth during fight and is limited?"
    $ has_analyzed_assassin_stone = True
    return
