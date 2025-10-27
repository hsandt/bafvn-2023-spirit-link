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

    charlet telepathy "Just keep fighting. As soon as he starts using intense fire, it will trigger the sprinkler system and you'll be able to get the edge."

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

    show pichit at character_move_to_easein("left", 0.5)
    show phrarat at character_move_to_easein("right", 0.5)

    call end_cinematic

    jump .fight2

# label .unused_pichit_asks_for_analyzes:

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
    scene bg university_inside
    show pichit battle serious at character_warp_to("left")
    show phrarat determined at character_warp_to("right")

    # show phrarat sad
    # TODO: pen sad
    show pen neutral at companion_warp_to("far_right")

    play sound audio.sfx.impact_glass

    "A dagger skewers out of the shadows and toward me. I barely dodge it and I'm sent careening into one of the exhibits. A glass case full of exquisite vases."

    phrarat "What a waste."

    # This raises guide's sympathy
    "Entirely focused on the shattered remains of the exhibit, vases shattered, dirt and seeds that had been hidden in the vases scattered across the floor. Such history, wasted."

    "Without hesitation, the Assassin flips his dagger and sends it hurling for my head."
    "I expected it, using the dirt and seeds on the floor, I spring forth spiked vines that envelop the dagger, only for them to smash whatever is left of the exhibit vases in the process."

    hide pen

    phrarat "You destroy our culture without hesitation."

    "Before I can respond, the man from the military booth emerges from the open doorway behind the Assassin. His rifle aimed for the Assassin’s head."

    man_with_rifle "Freeze!!!"

    "A smirk widens across the Assassin's face and the showman pulls the trigger, but nothing happens."
    "The Assassin begins to laugh, turning away from the man who’s still fiddling with the rifle."

    phrarat "The idiot can't even shoot his rifle. Proof that even the universe wants me to succeed."

    "After knocking the gun around  enough times, the rifle erupts, knocking the man back into concrete and distracting the Assassin long enough to allow me to strike."
    "Bringing the vines upward from the discarded dagger, I slash them across the Assassins arm who stumbles to the ground almost immediately, his spirit tossed off his shoulder in the process."

    pichit "Poison in the spikes."

    "The Assassin grips at the ground, trying to grapple his way toward his Spirit only who isn’t even moving from where it landed. It’s panting relentlessly, trying to catch its breath."

    pichit "This is over. I know your cause is a noble one, please, let me help you. I can explain everything to you."

    "The Assassin bares his teeth and with a sudden screech of his shoes, rolls upward, snatching his spirit into his arms and landing on his feet."
    "Immediately he brings his dagger close, cutting another piece of his scarf, putting it to the spirits mouth."

    phrarat "Please, make more, I need another whip."

    "The spirit doesn’t move, doesn’t start weaving, it’s too tired from constantly weaving pattern after pattern for its master to use."
    "Assured that there’s no fight left in the spirit, I finally lets the vines fall to the ground for good this time."

    # show phrarat angry

    "No, no, please, we need to burn it! All of it!!!"

    "The Assassin lights a solitary flame in his hand and shakily brings it to his scarf. He’s going to ignite his actual scarf, and use that as his last ditch effort."
    "Fortunately I feel Raegan’s presence as he finally links up with my gemstone."

    scene bg university_inside
    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("right")

    raegan "I do hope I’m not late, the power should be back on."

    charlet "Great."

    # Back to Charlet PoV
    "I pull the lever, opening the sprinklers."

    stop music fadeout 2.0
    play sound audio.sfx.shower2
    pause 2.0

    "Sparkles of water coat everything in the warehouse, including the Assassin's flame which sputters out in his hand."

    "He looks up, searching for the source of the sudden indoor rain and sees the lever I just pulled. He falls to his knees."

    scene bg university_inside
    show pichit battle serious at character_warp_to("left")
    show charlet neutral at character_warp_to("middle")
    show phrarat neutral at character_warp_to("far_right")

    phrarat "Of course, the host to Makara is the one who stops me."

    "How did he know Makara, the spirit wasn’t even visible!?!? I don’t know but there is a pure and unadulterated hatred simmering in his eyes."

    stop sound fadeout 2.0

    charlet "What does that matter?"

    "The Assassin ignores my question but doesn’t break eye contact."

    play music mystery

    phrarat "How ironic, of course they decided to put a sprinkler in here instead of over there."

    pichit "Over where?"

    phrarat "Vanich enterprises let my father burn alive in a factory because they weren’t willing to spend the money in a poorer district to ensure it was well protected."

    "I don't know what to say to that, Pichit doesn’t know what to say to that and Raegan is dead silent over the shared link."
    "The sounds of hooves and shuffling boots, sound at the entrance to the warehouse where the Military showman must have slinked off to."
    "The Assassin hears it too and in an instant, procures a circular pouch from his belt, slamming it onto the ground below, by the time the smoke clears, he and his Spirit are gone."

    hide phrarat

    # End of playtesting

    pause 1.0

    "This is the end of the playtesting section. Thank you for playing!"

    return
    # jump a1s3
