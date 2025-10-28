label a1s3:
    scene bg university_inside with wipeleft_medium
    show pichit battle grimace at character_enter_from_right_to_easein("far_left", 0.3)
    pause 0.6

    pichit "Urg!"

    show fan neutral at companion_warp_to("middle_left")

    "Fortunately, Fan created soft beech bark behind my back to cushion the impact, so I didn’t break anything."

    fan "This reminds me of your childhood… I would always protect you from bad falls when you were playing outdoors."

    show pichit battle anxious

    pichit "Aha… Yeah… Thanks for having my back."

    hide fan with character_dissolve

    $ should_show_side_image = True
    # technically we should show telepathy shared but we don't have such a variant,
    # so let's just show scared without blue effect
    charlet scared "Pichit! Are you alright?"

    show pichit battle serious

    pichit "{i}Yeah… I’m fine.{/i}"

    show pichit battle anxious

    show phrarat determined at character_enter_from_right_to_easein("right")

    pichit "{i}I… managed to get him into the building.{/i}"
    pichit "{i}What should I do now?{/i}"

    charlet telepathy "Just keep fighting to drive him into a corner. When he starts using intense fire, it will trigger the sprinkler system and you’ll be able to get the edge."

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

#     pichit "{i}Okay, Charlet, tell me about…{/i}"

#     call .unused_analyze_one_element

#     # Insert some fight here…

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
#     "Clothes have traditional Moacu patterns, but are written roughly."
#     "Ink mixed with blood. Shows pride but also anger and hastiness. He doesn’t care about his environment enough."
#     "Pichit could take advantage of this, or try to slow him down."
#     $ has_analyzed_assassin_weapon = True
#     return

# label .unused_analyze_stone:
#     "Normally people and esp. Moacu natives wear one color, symbolic of their aptitude for an art. A few experts master and show two colors."
#     "In his case, the creature is clearly Green and handles cloth creation and patterns."
#     "So Red Fire must be produced by a stone, maybe stolen from the previous attack."

#     "He seems to be mastering Fire because his attacks are quite eruptive and uncontrolled. Pichit could take advantage of this."
#     "His spirit also seems exhausted, weaving cloth over and over again as it’s burning. Maybe it will reach its limit soon…"
#     $ has_analyzed_assassin_stone = True
#     return

label .fight2:
    # setup for debug warp
    # scene bg university_inside
    # show pichit battle serious at character_warp_to("middle_left")
    # show phrarat determined at character_warp_to("middle_right")

    "While I distract him with my sword, I let Fan grow vines from the plant with striking red leaves behind him."

    show pen neutral at companion_warp_to("right")

    pen "I’ll cover your back!"

    "This time, his spirit takes control of the scarf, splitting it into multiple, thinner strips to intercept the vines."

    show phrarat smile

    phrarat "Humph. You thought that would work twice?"

    hide pen with character_dissolve
    show phrarat determined

    "He touches the scarf at the intersection of the strips with his free hand to kindle it. The fire quickly spreads in all directions, before reaching the vines."

    "They emit a purple smoke as they are consumed by the flames."

    phrarat "Already gone? Looks like interior plants won’t help you much."

    "The assassin deals a strong blow, making me lose my balance. He lowers his body and takes a stance I recognize from earlier."

    phrarat shout "Phoenix…"

    phrarat surprised "Ugh… !"

    "The fighter interrupts his move, grabbing his chest and coughing."

    phrarat "What did you… ?"

    pichit "It is not wise to burn plants without knowing what they’re made of. With the amount of toxic particles you’ve inhaled, you won’t be able to breathe normally for a while."

    "The vigilante goes down on bended knee, panting faster and faster. Drops of sweat start trickling from his forehead."

    pichit battle anxious "This is over. But I know your cause is a noble one… So please, let me help you…"

    phrarat "No…"

    phrarat shout "It won’t end here!!"

    show pichit battle serious

    "My opponent gathers his last ounce of strength to stand up. He talks with difficulty."

    # Voice acting: talk while panting and pausing, doing efforts to finish sentence
    phrarat "My family has been working with toxic dyes for years! You think a little poison is gonna stop me?!"

    "This time, he tears off not only his scarf, but also his tunic and hood before setting them on fire. A blazing whirl surrounds him."

    show pichit battle grimace

    show pichit at character_move_to_easein("far_left", 0.3)

    "I leap back to avoid being engulfed by the flames."

    show pichit battle anxious

    phrarat "If I can’t make it out alive… at least I’ll bring you down with this whole place! With Vanich!"

    show pen neutral at companion_warp_to("middle")

    pen "Phrarat, wait… !"
    pen "Your body won’t stand it if you use all of the gem’s power at once!"

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

    # Safety on skip: terminate previous animation
    show pen:
        rotate 0
        xpos 0.2
        ypos 0.6

    "I catch it mid-air to prevent it from crashing on the ground."

    pichit "Hey! Are you alright?"

    pen "…"
    pen "It’s too late… I can’t stop him now."

    play sound audio.sfx.impact_glass

    "The flames spread in the greenhouse, burning half of the plants. Fan muster its energy to protect me, and the other spirit, from the destructive force."

    "The blaze then spirals toward the ceiling. The glass panels break under the heat, leaving nothing but glittering dust suspended in the air."

    "The heat eventually reaches the fire sprinklers, causing their bubbles to break."

    jump .sprinkler

label .sprinkler:
    call start_cinematic

    stop music fadeout 2.0
    play sound audio.sfx.shower2
    pause 1.0
    show phrarat surprised
    pause 1.0

    call end_cinematic

    "Sparkles of water coat everything in the greenhouse. Soon, even the assassin’s desperate flames are extinguished."

    show phrarat anxious

    "He looks up, searching for the source of the sudden indoor rain and sees the sprinklers. He falls to his knees."

    show pen:
        ease 1.0 xpos 0.5

    "His spirit joins him."

    pen "Phrarat…"

    call start_cinematic

    hide pen with character_dissolve
    pause 0.2
    show pichit at character_move_to_ease("middle_left", 1.2)
    pause 1.0

    call end_cinematic

    play music mystery

    show phrarat determined

    phrarat "How ironic that I was stopped by that safety system."

    show phrarat neutral

    phrarat "After Enon brought advanced industry to Moacu-Laedan, traditional cloth making stopped being profitable and my father had to close the family business."

    phrarat "He joined one of Vanich’s factories in search for a more stable source of income."

    show phrarat determined

    phrarat "Then, they let him burn alive during a night overtime because they weren’t willing to spend money on safety in a poorer district like ours."

    pichit "…"

    call start_cinematic

    play sound audio.sfx.running2
    pause 1.0

    call end_cinematic

    "Hooves and shuffling boots resound at the entrance to the greenhouse."

    "The assassin is soon surrounded by a dozen security guards, armed with tonfas and muskets."

    guard "Drop your weapons!"

    show phrarat determined

    show screen smoke

    "The criminal grabs a circular pouch from his belt and slams it onto the ground. A cloud of smoke covers the room."

    "Fearing another surprise attack, I brace myself, but nothing happens."

    hide phrarat
    hide screen smoke
    with bg_dissolve

    show pichit battle serious

    "By the time the smoke clears, he and his spirit are gone. The confused guards look around for the culprit, but he is nowhere on this floor."

    show pichit battle anxious

    "I hear a voice from above."

    # Voice acting: post-process: shout from far, echo
    phrarat "You really think the Vanich son is better than his father? That he’ll help you for the sake of Moacu-Laedan?"

    show pichit battle serious

    "I look upward, just like the guards now scattered across the greenhouse’s alleys."

    "The assassin is standing on the roof frame, now completely devoid of glass. He looks down at me one last time, before running away on the tangle of beams."

    guard "Go after him! Quick!"

    play sound audio.sfx.running2

    "Most of the guards leave the building to chase after him. Only a few remain to check on me and patrol the area in case new attackers appear."

    "However, they spot no other signs of danger. It seems that the man in red – Phrarat – was an independent actor indeed."

    jump .aftermath

label .aftermath:

    scene bg black with wipeleft_fast
    pause 0.5
    scene bg university_inside with wipeleft_fast

    show pichit exhausted at character_warp_to("middle")

    "The guards accompany us to the infirmary. A nurse comes to administer me first aid."

    # TODO: reconstruct Pichit non-battle pose with grimace sprite from normal pose + battle grimace

    pichit "Ouch!"

    # TODO: describe cuts and injuries during the fight

    "My wound stings as she rubs a swab on it. Multiple cuts and small burns cover my body and my clothes. My muscles still ache from the past fight."

    "Even then, I haven’t suffered any major damage. I thank Fan for his support."

    show charlet anxious at character_enter_from_left_to_easein("left", 0.5)
    pause 0.2

    charlet "Pichit! Are you alright?"

    show pichit smile

    pichit "Yeah… Thanks for helping me get through this."

    show charlet neutral
    show pichit neutral

    show raegan intrigued at character_enter_from_right_to_easein("right", 0.5)

    "Raegan also enters the infirmary, but he has difficulties getting past the guards, who keep checking that Vanich’s son is unharmed."

    "After assuring them that he’s fine, he finally joins us."

    show raegan smile

    raegan "Thank you for protecting me, both of you."

    pichit "Sure… You’re welcome."

    pichit "{i}I hope… it was worth it…{/i}"

    show raegan neutral

    raegan "I will report this incident to my company. We don’t know when there will be new attacks, so I will ask for a closer protection for myself – and the expedition."

    raegan "The militia should also come back later to ask you for more information. The more they know, the faster they’ll be able to identify the culprit."

    raegan "Enon keeps a registry of all the islanders who moved to the continent, so it should be a matter of time."

    # TODO: did you hear anything about him? Name or family situation? => player choice
    # in this case it's better NOT to have Raegan listen to the father story, so Pichit can hide information or not
    # on purpose, depending on trust

    raegan "But for now, you two should rest."

    charlet "You’re right. We’ll meet again later."
    pichit "I don’t need to be asked twice!"

    show charlet at character_exit_to_right_easeout
    show pichit at character_exit_to_right_easeout

    show raegan thinking at character_move_to_easein("middle")

    stop music fadeout 5.0

    raegan "…"
    raegan "Looks like it won’t be that easy…"

    jump .prologue_ending

    return

label .prologue_ending:

    # adapt cinematic effect from jam ending in a1s2

    call start_cinematic

    pause 1.0

    play music to_be_continued noloop

    show bg at sepia
    show raegan at sepia

    pause 2.8

    scene bg black with Dissolve(1.0)

    pause 1.78

    image end_text1 = Text("Spirit Link - Prologue", textalign=0.5, slow_cps=20)

    show end_text1 with dissolve:
        xalign 0.5
        yalign 0.5
        yoffset -30

    pause 2.29

    image end_text2 = Text("End", textalign=0.5, slow_cps=10)

    show end_text2 with dissolve:
        xalign 0.5
        yalign 0.5
        yoffset 30

    pause 2.45

    hide end_text1
    hide end_text2
    with dissolve

    pause 10.7

    stop music fadeout 8.0

    pause 5.0

    return


label .unused_museum:
    "A dagger skewers out of the shadows and toward me. I barely dodge it and I’m sent careening into one of the exhibits. A glass case full of exquisite vases."

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

    "A smirk widens across the Assassin’s face and the showman pulls the trigger, but nothing happens."
    "The Assassin begins to laugh, turning away from the man who’s still fiddling with the rifle."

    phrarat "The idiot can’t even shoot his rifle. Proof that even the universe wants me to succeed."

    "After knocking the gun around enough times, the rifle erupts, knocking the man back into concrete and distracting the Assassin long enough to allow me to strike."

label .unused_alternative_tired_pen:
    "The Assassin bares his teeth and with a sudden screech of his shoes, rolls upward, snatching his spirit into his arms and landing on his feet."
    "Immediately he brings his dagger close, cutting another piece of his scarf, putting it to the spirits mouth."

    phrarat "Please, make more, I need another whip."

    "The spirit doesn’t move, doesn’t start weaving, it’s too tired from constantly weaving pattern after pattern for its master to use."
    "Assured that there’s no fight left in the spirit, I finally let the vines fall to the ground for good this time."

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
