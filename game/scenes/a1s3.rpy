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

    call start_cinematic
    show pichit battle anxious
    show phrarat determined at character_enter_from_right_to_easein("right")
    pause 1.0
    call end_cinematic

    pichit "{i}And, erm... I got him into the building.{/i}"
    pichit "{i}What should I do now?{/i}"

    charlet telepathy "Just keep fighting until he uses too much fire and triggers the sprinkler system."

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

label .fight2:
    # setup for debug warp
    # scene bg university_inside
    # show pichit battle serious at character_warp_to("middle_left")
    # show phrarat determined at character_warp_to("middle_right")

    "I get back into the fight."

    "This time, the numerous shrubs and trees displayed in the greenhouse allow me to vary my moves: cutting leaves for offense, proliferating roots for defense…"

    "Unfortunately, plants under glass are not as robust and their roots are not as deep. The assassin quickly dispatches my attack with a combination of slashes and fire projectiles."

    show screen smoke

    "One spark hits the Aquilaria tree at the center of the installation. It catches fire and immediately starts spreading white smoke."

    show phrarat surprised at character_move_to_easein("right", 0.3)

    phrarat "… !!"

    stop music fadeout 2.0

    show phrarat neutral

    "The assassin suddenly stops attacking, his angry expression replaced with sadness."

    show pichit anxious

    pichit "{i}Why the sudden change of attitude? Is it my chance to counter attack? No, wait. I recognize this scent…{/i}"

    hide screen smoke with bg_dissolve

    "We both wait for the smoke to disappear, then resume fighting."

    call start_cinematic

    play music battle
    # perfect timing for blades to cross on a beat
    pause 0.94

    show pichit battle serious
    show phrarat determined

    call a1s2.pichit_phrarat_cross_blades

    call end_cinematic

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

    pichit "It's not recommended to burn plants without knowing what they’re made of."
    pichit "With the amount of toxic particles you’ve inhaled, you won’t be able to breathe normally for a while."

    "The vigilante goes down on bended knee, panting faster and faster. Drops of sweat start trickling from his forehead."

    pichit "This is over."

    window hide
    pause 1.0
    window show

    # Voice acting: talk while panting and pausing, doing efforts to finish sentence
    phrarat "… Is that so? Then why don’t you finish me then?"

    show pichit battle anxious

    pichit "… Earlier, when that tree burnt… I recognized the scent of oud incense. The one we use to honor the deceased."

    pichit "You stopped fighting because you remembered someone dear who passed away, didn’t you?"

    phrarat "…"

    # Voice acting: talk while panting and pausing, doing efforts to finish sentence
    phrarat "I… don’t need your pity."

    show pichit battle serious
    show phrarat determined

    "My opponent gathers his last ounce of strength to stand up."

    pichit "Stop. You’ll just waste what’s left of your life force."

    show phrarat shout

    phrarat "My family has been working with toxic dyes for years! You think a little poison is gonna stop me?!"

    show pen neutral at companion_warp_to("far_right"), flip

    phrarat "Pen! I need more cloth!"

    show phrarat determined

    pen "…"

    "His spirit looks exhausted. Was it the relentless weaving that drained its energy, or did the poison affect it via the assassin's body?"

    hide pen with character_dissolve

    phrarat "Tsk… I have no choice then."

    "In the blink of an eye, he sets his own tunic on fire, along with what remains of his scarf. A blazing whirl surrounds him."

    show phrarat shout

    phrarat "Dragon Tornado!!"

    show pichit battle grimace

    show pichit at character_move_to_easein("far_left", 0.3)

    "I leap back to avoid being engulfed by the flames."

    show pichit battle anxious

    phrarat "If I can’t make it out alive… at least I’ll bring you down with this whole place! With Vanich!"

    show pen neutral at companion_warp_to("middle")

    pen "Phrarat, wait… !"
    pen "Your body won’t stand it if you use all of the gem’s power at once!"

    phrarat "Graaah!!"

    "The assassin ignores his companion and makes the whirlwind accelerate. It flows higher and farther."

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

    "Fortunately, they spot no other signs of danger."

    jump .aftermath

label .aftermath:

    scene bg black with wipeleft_fast
    pause 0.5
    scene bg university_inside with wipeleft_fast

    show pichit exhausted zorder 1 at character_warp_to("middle")

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

    raegan "Thank you for protecting me."

    pichit "Sure… You’re welcome."

    pichit "{i}I hope it will be worth it…{/i}"

    # Raegan talks about the importance of reports and unintentionally reveals his role as lobbyist

    show raegan neutral

    raegan "I will report the attack to my company. I will try to convince them to assign us bodyguards so I can still join the expedition safely."

    raegan "Normally, the militia should come back later to ask you for your testimony."
    raegan "I know that Enon keeps a registry of all the Islanders who moved to the continent, as well as suspected ILF supporters."
    raegan thinking "So, by crosschecking it with your description of the assassin, they may be able to identify him."

    show pichit intrigued

    "I'm amazed by how much Raegan knows about administrative and criminal matters.
    Then again, he was the target, so it's not surprising that he would closely study the actions of any potential opponents."

    show pichit neutral

    raegan "That said, I can accelerate the process by passing on any relevant piece of information directly to the authorities, thanks to my extended network."

    show charlet at darker

    raegan "Pichit, did you notice anything during your fight that could help the investigation?"

    pichit "{i}Hm... That cloaked man – Phrarat, as I heard from his spirit – trusted in me by revealing his deep, personal motivations.{/i}"
    pichit "{i}Should I keep them for myself, or report them to gain Raegan's trust and maximize our chance of survivals during the expedition?{/i}"

    while not (has_told_thats_all or has_told_nothing):
        if has_told_assassin_family_story or has_told_trivia:
            show pichit neutral
            raegan neutral "Anything else?"

        menu:
            "I tell Raegan about the assassin's name and father." if not has_told_assassin_family_story:
                pichit "I heard his spirit call him 'Phrarat'. It could be his nickname, though."
                "I explain why Phrarat's family business closed and how his father died in one of Vanich's factories."
                raegan sad "I see... An unfortunate accident."
                raegan thinking "This will however prove precious information in identifying the culprit."
                $ has_told_assassin_family_story = True
            "I tell Raegan about his spirit." if not has_told_assassin_spirit_appearance:
                pichit "He was accompanied by a flying spirit. It looked like a silkmoth with a cat head, and its body was covered with green and yellow stripes."
                raegan thinking "Interesting... Most guards will be unable to see it, but some Islanders may accept to help us identify it in the crowd."
                raegan neutral "Most of them just want to live peacefully in Enon, after all."
                $ has_told_assassin_spirit_appearance = True
            "I tell Raegan some unusable trivia." if not has_told_trivia:
                pichit smile "Ah, yes! He kept shouting the names of his attacks before using them!"
                pichit intrigued "I'm not sure why he'd do that. I mean, shouldn't that help me dodge them?"
                raegan surprised "I... see..."
                $ has_told_trivia = True
            "I tell Raegan I haven't noticed anything else." if not has_told_thats_all and (has_told_assassin_family_story or has_told_trivia):
                pichit "No, that was all."
                raegan "I see. Thank you."
                $ has_told_thats_all = True
            "I tell Raegan that I haven't noticed anything particular." if not has_told_nothing and not (has_told_assassin_family_story or has_told_trivia):
                pichit intrigued "Not really. I admit I was really focused on surviving all that time."
                raegan "Understandable."
                $ has_told_nothing = True

    window hide
    show pichit neutral
    show charlet at reset_brightness
    pause 0.5
    window show

    raegan "Well, I need to go back to my headquarters now. You two should rest."

    pichit "I don’t need to be asked twice!"
    charlet "Same for me. We’ll meet again later."

    call start_cinematic

    show charlet at character_exit_to_left_easeout(1.0)
    show pichit at character_exit_to_left_easeout(1.5)
    pause 1.5
    # Known issue: small bug on move start
    show raegan at character_move_to_easein("middle")
    pause 1.0
    show raegan thinking

    call end_cinematic

    stop music fadeout 5.0

    raegan "…"
    raegan "Looks like it won’t be that easy…"

    jump .prologue_ending

    return

label .prologue_ending:

    # adapt cinematic effect from jam ending in a1s2

    call start_cinematic

    pause 1.0

    play music premonition

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
