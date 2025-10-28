label a1s3:
    scene bg university_inside with wipeleft_medium
    show pichit battle grimace at character_enter_from_right_to_easein("far_left", 0.3)
    pause 0.6

    pichit "Urg!"

    show fan neutral at companion_warp_to("middle_left")

    "Fortunately, Fan created soft beech bark behind my back to cushion the impact, so I didn't break anything."

    fan "This reminds me of your childhood... I would always protect you from bad falls when you were playing outdoors."

    show pichit battle anxious

    pichit "Aha... Yeah... Thanks for having my back."

    hide fan with character_dissolve

    $ should_show_side_image = True
    # technically we should show telepathy shared but we don't have such a variant,
    # so let's just show scared without blue effect
    charlet scared "Pichit! Are you alright?"

    show pichit battle serious

    pichit "{i}Yeah... I'm fine.{/i}"

    show pichit battle anxious

    show phrarat determined at character_enter_from_right_to_easein("right")

    pichit "{i}I... managed to get him into the building.{/i}"
    pichit "{i}What should I do now?{/i}"

    charlet telepathy "Just keep fighting to drive him into a corner. When he starts using intense fire, it will trigger the sprinkler system and you'll be able to get the edge."

    # Cut for now to get started with Raise your Voice jam 2025
    # charlet telepathy "I will help you as much as I can with my remote vision. Just tell me what you need to know."

    # Known issue: a weird bug causes Pichit to quickly move to the left before moving
    show pichit at character_move_to_easein("left", 0.5, 0.05)

    show pichit battle serious

    pichit "{i}Understood.{/i}"

    $ should_show_side_image = False

    call start_cinematic

    # Known issue: a weird bug causes Phrarat to insta move right to prepare attack,
    # instead of tweening
    call a1s2.pichit_phrarat_cross_blades

    call end_cinematic

    jump .fight2

# label .unused_pichit_asks_for_analyzes:

#     show pichit at character_move_to_easein("middle_left", 0.5)
#     show phrarat at character_move_to_easein("middle_right", 0.5)

#     pichit "{i}Okay, Charlet, tell me about...{/i}"

#     call .unused_analyze_one_element

#     # Insert some fight here...

#     "I try to analyze the opponent once more."

#     call .unused_analyze_one_element

#     jump .fight2

# label .unused_analyze_one_element:
#     menu:
#         "his weapons" if not has_analyzed_assassin_weapon:
#             call .unused_analyze_weapon
#         "his gemstone" if not has_analyzed_assassin_stone:
#             call .unused_analyze_stone

#     return

# label .unused_analyze_weapon:
#     # TODO: new text
#     "Clothes have traditional patterns of Moacu, but are written roughly."
#     "Ink mixed with blood. Shows pride but also anger and hastiness. He doesn't care about his environment enough."
#     "Pichit could take advantage of this, or try to slow him down."
#     $ has_analyzed_assassin_weapon = True
#     return

# label .unused_analyze_stone:
#     "Normally people and esp. Moacu natives wear one color, symbolic of their aptitude for an art. A few experts master and show two colors."
#     "In his case, the creature is clearly Green and handles cloth creation and patterns."
#     "So Red Fire must be produced by a stone, maybe stolen from the previous attack."

#     "He seems to be mastering Fire because his attacks are quite eruptive and uncontrolled. Pichit could take advantage of this."
#     "His spirit also seems exhausted, weaving cloth over and over again as it's burning. Maybe it will reach its limit soon..."
#     $ has_analyzed_assassin_stone = True
#     return

label .fight2:
    # setup for debug warp
    # scene bg university_inside
    # show pichit battle serious at character_warp_to("middle_left")
    # show phrarat determined at character_warp_to("middle_right")

    "While I distract him with my sword, I let Fan can grow vines from the plant with striking red leaves behind him."

    show pen neutral at companion_warp_to("right")

    pen "I'll cover your back!"

    "This time, his spirit takes control of the scarf, splitting it into multiple, thinner strips to intercept the vines."

    "It acted even faster than usual, but it's clear that this quick action spent a lot of its energy."

    show phrarat smile

    phrarat "Humph. You thought that would work twice?"

    hide pen with character_dissolve
    show phrarat determined

    "He touches the scarf at the intersection of the strips with his free hand to kindle it. The fire quickly spreads in all directions, before reaching the vines."

    "They emit a purple smoke as they are consumed by the flames."

    phrarat "Already gone? Looks like interior plants won't help you much."

    "The assassin deals a strong blow, making me lose my balance. He lowers his body and takes a stance I recognize from earlier."

    phrarat shout "Phoenix..."

    phrarat surprised "Ugh... !"

    "The fighter interrupts his move, grabbing his chest and coughing."

    phrarat "What did you... ?"

    pichit "It is not wise to burn plants without knowing what they're made of. With the amount of toxic particles you've inhalted, your body won't stand for long."

    pichit "First, your vision will become blurry. Then, you will lose control of your muscles. And your spirit doesn't have enough strength left to protect you."

    "The vigilante goes down on bended knee, panting faster and faster. Drops of sweat start trickling from his forehead."

    pichit battle anxious "This is over. But I know your cause is a noble one... So please, let me help you..."

    phrarat "No..."

    phrarat shout "It won't end here!!"

    show pichit battle serious

    "My opponent gathers his last ounce of strength to stand up."

    "This time, he tears off not only his scarf, but also his tunic and hood before setting them on fire. A blazing whirl surrounds him."

    show pichit battle grimace

    show pichit at character_move_to_easein("far_left", 0.3)

    "I leap back to avoid being engulfed by the flames."

    show pichit battle anxious

    phrarat "If I can't make it out alive... at least I'll bring you down with this whole place! With Vanich!"

    show pen neutral at companion_warp_to("middle")

    pen "Phrarat, wait... !"
    pen "Your body won't stand it if you use all of the gem's power at once!"

    phrarat "Graaah!!"

    "The assassin ignores his companion, intensifying the whirl of fire, which gains in radius and height."

    "It ends up hitting the spirit, who was flying too close, projecting it backward."

    show pen:
        parallel:
            linear 0.3 rotate -360
        parallel:
            easein 0.3 xpos 0.2
        parallel:
            easeout 0.3 ypos 0.6

    pen "Aw!!"

    "I catch it mid-air to prevent it from crashing on the ground."

    pichit "Hey! Are you alright?"

    pen "..."
    pen "It's too late... I can't stop him now."

    play sound audio.sfx.impact_glass

    "The assassin's flames spiral toward the ceiling. The glass panels break under the heat, leaving nothing but glittering dust suspended in the air."

    "The heat eventually reaches the fire sprinklers, causing their bubbles to break."

    jump .sprinkler

label .sprinkler:
    stop music fadeout 2.0
    play sound audio.sfx.shower2
    pause 2.0

    "Sparkles of water coat everything in the greenhouse. Soon, even the assassin's desperate flames are extinguished."

    "He looks up, searching for the source of the sudden indoor rain and sees the sprinklers. He falls to his knees."

    show pichit battle anxious at character_move_to_easein("middle", 0.5)
    show charlet anxious zorder 1 at character_enter_from_left_to_easein("left", 0.5)
    show raegan anxious at character_enter_from_left_to_easein("far_left", 0.5)

    "After I confirm the situation with Charlet, she joins me in case I need support until the militia arrives."

    "Raegan stays a bit behind, in case the assassin still has cards in his hands."

    charlet "Pichit!"

    # phrarat "Of course, the host to Makara is the one who stops me."

    # "How did he know Makara, the spirit wasn’t even visible!?!? I don’t know but there is a pure and unadulterated hatred simmering in his eyes."

    # stop sound fadeout 2.0

    # charlet "What does that matter?"

    # "The Assassin ignores my question but doesn’t break eye contact."

    play music mystery

    phrarat "How ironic that this was what stopped me."

    phrarat "Vanich Industries let my father burn alive in a factory because they weren’t willing to spend money on safety in a poorer district like ours."

    "I don't know what to say to that, Pichit doesn’t know what to say to that and Raegan is dead silent over the shared link."

    "The sounds of hooves and shuffling boots, sound at the entrance to the warehouse where the Military showman must have slinked off to."

    "The Assassin hears it too and in an instant, procures a circular pouch from his belt, slamming it onto the ground below, by the time the smoke clears, he and his Spirit are gone."

    hide phrarat

label .unused_museum:
    "A dagger skewers out of the shadows and toward me. I barely dodge it and I'm sent careening into one of the exhibits. A glass case full of exquisite vases."

    phrarat "What a waste."

    # This raises guide's sympathy
    "Entirely focused on the shattered remains of the exhibit, vases shattered, dirt and seeds that had been hidden in the vases scattered across the floor. Such history, wasted."

    "Without hesitation, the Assassin flips his dagger and sends it hurling for my head."
    "I expected it, using the dirt and seeds on the floor, I spring forth spiked vines that envelop the dagger, only for them to smash whatever is left of the exhibit vases in the process."

    hide pen

    phrarat "You destroy our culture without hesitation."

label .unused_man_with_rifle:
    "Before I can respond, the man from the military booth emerges from the open doorway behind the Assassin. His rifle aimed for the Assassin’s head."

    man_with_rifle "Freeze!!!"

    "A smirk widens across the Assassin's face and the showman pulls the trigger, but nothing happens."
    "The Assassin begins to laugh, turning away from the man who’s still fiddling with the rifle."

    phrarat "The idiot can't even shoot his rifle. Proof that even the universe wants me to succeed."

    "After knocking the gun around enough times, the rifle erupts, knocking the man back into concrete and distracting the Assassin long enough to allow me to strike."

label .unused_alternative_tired_pen:
    "The Assassin bares his teeth and with a sudden screech of his shoes, rolls upward, snatching his spirit into his arms and landing on his feet."
    "Immediately he brings his dagger close, cutting another piece of his scarf, putting it to the spirits mouth."

    phrarat "Please, make more, I need another whip."

    "The spirit doesn’t move, doesn’t start weaving, it’s too tired from constantly weaving pattern after pattern for its master to use."
    "Assured that there’s no fight left in the spirit, I finally lets the vines fall to the ground for good this time."

    # show phrarat angry

    "No, no, please, we need to burn it! All of it!!!"

    "The Assassin lights a solitary flame in his hand and shakily brings it to his scarf. He’s going to ignite his actual scarf, and use that as his last ditch effort."

label .unused_alternative_sprinkler_start:

    "Fortunately I feel Raegan’s presence as he finally links up with my gemstone."

    scene bg university_inside
    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("right")

    raegan "I do hope I’m not late, the power should be back on."

    charlet "Great."

    # Back to Charlet PoV
    "I pull the lever, opening the sprinklers."

    # End of playtesting

    pause 1.0

    "This is the end of the playtesting section. Thank you for playing!"

    return
    # jump a1s3
