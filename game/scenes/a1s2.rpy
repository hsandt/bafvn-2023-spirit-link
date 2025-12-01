label a1s2:
    # "Act 1: Scene 2 - Attack"
    jump .raegan_arrives

label .raegan_arrives:

    show charlet neutral at character_move_to("left")
    show pichit neutral at character_move_to("middle", 0.75)
    pause 0.2
    show raegan neutral at character_warp_to("right")

    "The stranger is tall and elegantly dressed in a three-piece suit, despite the heat.
    He should be drenched in sweat."
    "Instead, his collar and cuffs are clean and neat as though freshly laundered.
    Even his hair is impeccable. Meanwhile, my own hair feels matted and itchy."

    show pichit smile

    voice "audio/voice/pichit_1201b.opus"
    pichit "Oh, you’re back."

    # Forgot to add "pichit" 2 lines below at first, so "He said..." wasn't exported in dialogue.tab
    # and we had to insert this line later in the spreadsheet, so exceptionally we use suffixes
    # "-1" and "-2" since we don't want to offset all the voiced line numbers after that

    voice "audio/voice/pichit_1202-1b.opus"
    pichit "Charlet, I’d like to introduce you to Mr. Raegan Vanich! He is the third child of Lord Vanich, founder of Vanich Corporation."

    # Waiting for asset
    # voice "audio/voice/pichit_1202-2b.opus"
    pichit "He said he was interested in sponsoring the expedition!"

    voice "audio/voice/pichit_1203a.opus"
    pichit "Raegan, this is Dr. Charlet Kasamsun, the brains behind the expedition."

    voice "audio/voice/raegan_1201a.opus"
    raegan "A pleasure to meet you, Charlet. I’ve heard wonderful things about your plans."

    "Just like Pichit, I switch to speaking Enonian."

    show charlet smile
    voice "audio/voice/charlet_1201a.opus"
    charlet "Likewise, Mr. Vanich. Vanich Industries has done so many amazing things, it is a great honor to meet you."

    show raegan smile
    voice "audio/voice/raegan_1202a.opus"
    raegan "Just Raegan, please. Should all go well, I imagine we will be working very closely together."

    show charlet neutral

    "His smile is dangerously charming and I find myself flustered by my own reaction to it."

    show charlet smile
    voice "audio/voice/charlet_1202a.opus"
    charlet "Raegan, then."

    jump .raegan_conversation

label .raegan_conversation:

    # Setup statements: when adding a debug scene hub, create some flag "debug_jump"
    # and if true, execute them
    #
    # scene bg university_outside
    # show charlet smile at character_warp_to("left")

    call start_cinematic from _call_start_cinematic_3

    show raegan smile zorder 1 at character_move_to("middle")

    # Currently, chaining transforms with comma `,` will not play them in parallel,
    # so we need to play both in sequence with pause
    # (or in parallel but that’d need a dedicated transform)
    # See https://github.com/renpy/renpy/issues/6681
    # show pichit neutral at character_move_to("right"), darker

    show pichit neutral at character_move_to("right")

    # Wait for previous animation to finish
    pause 1.0

    # Quick fix: if player skipped, force finish previous animation now
    # as darker will interrupt it immediately
    show pichit neutral at character_move_to("right", 0.0)

    show pichit at darker

    call end_cinematic from _call_end_cinematic_3

    voice "audio/voice/raegan_1203a.opus"
    raegan "It’s always a pleasure to meet someone who can appreciate the Island’s unique charm. What drove your interest?"

    voice "audio/voice/charlet_1203a.opus"
    charlet "My ancestors came from the Island. Studying at the academia made me realize just how little we, in Enon, know about Moacu-Laedan."

    voice "audio/voice/charlet_1204c.opus"
    charlet "It is my hope that this expedition will help build a bridge between our people and promote appreciation of spirits."

    show raegan neutral

    voice "audio/voice/raegan_1204a.opus"
    raegan "Indeed… Pichit mentioned your goal was to catalogue folktales from the Island? Have you ever heard any tales of Lalahon?"

    show charlet intrigued

    "My eyes widen. That Raegan has heard of Lalahon at all, is surprising."
    "Stories about Lalahon are rare and their contents contradictory. The few I’ve heard have been told to me by my grandfather."

    "According to his tales, Lalahon is either a benevolent goddess born from the ashes of great god Bathala’s heart, or an evil beast that killed Bathala and used his fire to destroy the forests."
    "Which version of the tale was true, has been the subject of many debates between the two of us. Only one thing was certain: Lalahon was powerful."

    voice "audio/voice/charlet_1205a.opus"
    charlet "Only a couple passed down from my grandfather. Much of her history appears lost."

    voice "audio/voice/charlet_1206a.opus"
    charlet "I hope that this expedition will allow many more of these tales to be collected and preserved for future generations."

    show charlet smile

    voice "audio/voice/charlet_1207a.opus"
    charlet "Who knows, maybe we’ll even discover the secret behind the mist that covered the Island!"

    show raegan smile

    voice "audio/voice/raegan_1205a.opus"
    raegan "A worthy endeavor for sure. I look forward to hearing more of your goals and the tourism business proposition."

    voice "audio/voice/charlet_1208a.opus"
    charlet "Of course. I have a schedule here, would you like to set up a time to meet?"

    jump .smoke

label .smoke:

    # Start flash
    # Dict transition plays while further statements are applied, allowing us to show the flash
    # without delay while also updating character expressions and hiding UI
    show overlay flash zorder 2 with { "master": Dissolve(0.15) }

    # Start showing smoke as soon as possible to give it some time to appear (but not enough, would need prewarm,
    # see more below)
    #
    # Normally we should `show fx smoke onlayer fx` with `fx` added to custom config.layers
    # but this currently doesn’t work, see https://lemmasoft.renai.us/forums/viewtopic.php?p=574874#p574874
    # so we must use a trick from https://lemmasoft.renai.us/forums/viewtopic.php?p=571461
    # to show particles on a separate screen
    #
    # Other known issues:
    # - first batch of particles sometimes appears in wave and then disappears, despite `start` parameter
    # - no way to prewarm particles, so they take time to appear on screen
    #   see https://lemmasoft.renai.us/forums/viewtopic.php?t=70172
    show screen smoke

    call start_cinematic from _call_start_cinematic_4

    show charlet intrigued
    show raegan surprised
    show pichit intrigued at reset_brightness

    play sound audio.sfx.smoke

    # Hold flash
    pause 0.25

    # End flash
    hide overlay with Dissolve(0.15)

    call end_cinematic from _call_end_cinematic_4

    "Before Raegan can respond, a bright flash blinds us. The air grows thick with the scent of smoke."
    "Coughs sound out in the alleys as confusion spreads among the crowd. People cover their mouths and noses, or those of the children they accompany."
    "Some start running toward the exit while others take refuge in the main building."
    "I look for the origin of the smoke. It seems to pour out from Dr. Barouche’s alchemy station."

    show charlet at darker
    show raegan anxious

    voice "audio/voice/raegan_1206a.opus"
    raegan "My pardons, Pichit… Do you know what’s happening?"

    show pichit smile

    "Pichit smiles, nonchalantly waving a hand to dismiss the commotion, but I can see tension in his shoulders."

    voice "audio/voice/pichit_1204b.opus"
    pichit "Some demonstrations must have malfunctioned. I’m sure it’s nothing to be concerned about, sir."

    show pichit neutral
    show raegan thinking
    show charlet at reset_brightness

    voice "audio/voice/charlet_vocalize_thinking.opus"
    charlet "…"

    show bg at invert(0.2)
    show charlet at invert(0.2)
    show pichit at invert(0.2)
    show raegan at invert(0.2)

    pause 0.35

    show bg at reset_invert(0.2)
    show charlet at reset_invert(0.2)
    show pichit at reset_invert(0.2)
    show raegan at reset_invert(0.2)

    pause 0.1

    show pichit at darker
    show raegan at darker

    show makara neutral at companion_warp_to("far_left"), flip

    pause 0.5

    show charlet anxious
    voice "audio/voice/makara_1201a.opus"
    makara "I sense ill intent lurking amidst this smoke. We had better quickly leave this place."

    show charlet serious

    voice "audio/voice/charlet_1209a.opus"
    charlet "{i}Understood.{/i}"

    hide makara with character_dissolve

    show raegan at reset_brightness
    show pichit at reset_brightness

    voice "audio/voice/charlet_1210a.opus"
    charlet "Everyone, I think we should go. It doesn’t feel safe here."

    voice "audio/voice/raegan_1207a.opus"
    raegan "Yes, that’s probably best."

    call start_cinematic from _call_start_cinematic_5

    show charlet at character_exit_to_left_easeout(1.5)
    show raegan at character_exit_to_left_easeout(1.7)
    show pichit at character_exit_to_left_easeout(2.0)

    pause 0.25

    stop music fadeout 1.0

    jump .assassin_appears

label .assassin_appears:

    scene bg smoke with Dissolve(0.7)
    pause 0.25
    show phrarat silhouette at character_warp_to("middle") with Dissolve(1.0)
    pause 0.5

    # Quick flash transition
    show screen white_overlay with Dissolve(0.15)

    # when using screen smoke trick, we need to hide it manually even when changing scene
    hide screen smoke

    scene bg university_outside_with_characters_for_zoom at camera_zoom_in_from_far(1.0/5, 1.0, 0.4)

    show fx_speed_lines_forward:
        xalign 0.5 yalign 0.5
    # replacing fire with slashes again
    # show fx_fire_forward:
    #     xalign 0.5 yanchor 0.0 ypos 0.7

    play sound audio.sfx.slash1

    hide screen white_overlay with Dissolve(0.15)

    # Make sure to wait at least camera_zoom_in_from_far duration - hide screen transition above
    # (0.4-0.15=0.25), or the new effect will stop the zoom in
    # shader progression
    pause 0.5
    # Force reset in case player skipped pause above, to avoid getting stuck in the middle of
    # zoom in effect
    show bg at reset
    show bg at sepia(0.1)
    show fx_speed_lines_forward at sepia(0.1)
    # replacing fire with slashes again
    # show fx_fire_forward at sepia(0.1)

    # change BG and show Pichit in fighting stance blocking the fire
    # more cinematic: show the fire being blocked, then reveal it was Pichit

    call end_cinematic from _call_end_cinematic_5

    "As we’re moving away, a red shape emerges from the smoke."

    scene bg university_outside with bg_dissolve

    play sound audio.sfx.impact_catch

    "I realize belatedly that Pichit has shoved me to the floor."

    call start_cinematic from _call_start_cinematic_6
    pause 1.0
    play music premonition
    show phrarat determined at character_warp_to("middle")
    pause 1.0
    call end_cinematic from _call_end_cinematic_6

    "I look up, shocked to find Raegan half-sprawled over the table of my booth, a dark figure standing over him."
    "A glowing shield is the only barrier between his chest and his assailant’s knife. As I suspected, the red gem on Raegan’s collar is not just decorative like mine."

    show phrarat shout

    phrarat "That damn gemstone… !"

    show phrarat determined

    $ should_show_side_image = True
    show charlet scared
    voice "audio/voice/charlet_1211a.opus"
    charlet "{i}He speaks Laedani… A separatist vigilante?!{/i}"
    $ should_show_side_image = False

    # TODO impact SFX and hit FX

    show pichit battle shout:
        alpha 0.0
        xpos 0.2
        ypos 1.0
        parallel:
            linear 0.2 alpha 1.0
        parallel:
            linear 0.2 xpos 0.5
    show phrarat surprised at character_move_to("middle_right", 0.2)

    "Before I can react, Pichit tackles him."

    # Dictionary transition trick to play dissolve in parallel with next vpunch
    hide pichit
    hide phrarat
    with { "master": Dissolve(0.25) }

    show bg with vpunch

    "The two men go rolling, the pamphlets I had printed falling with them."

    # show charlet on top since she’s shorter and on the edge
    show raegan surprised at character_warp_to("left")
    show charlet scared at character_warp_to("far_left")

    "For a moment, there is only a mad tangle of limbs. Then Pichit goes flying."

    show phrarat determined at character_enter_from_right_to_easein("far_right", 0.5)
    show pichit battle serious at character_warp_to("middle", 0.4)

    "As he stands up before the assassin, he holds a sword in his hand. I vaguely recognize it as a replica from the history booth."

    "The assassin, now holding a crimson scarf, tears a part of it with his knife and balls it up."

    "As the ball spontaneously ignites, he throws the fiery projectile at us. I brace myself…"

    play sound audio.sfx.throw_fireball
    pause 0.2

    show pichit at character_move_to_easein("middle_left", 0.2)
    pause 0.2

    "… But I’m not hurt. A wooden shield looms above me."

    show pichit battle shout

    voice "audio/voice/pichit_1205a.opus"
    pichit "Don’t just sit there! Get inside! Now!"

    show pichit battle serious

    #TODO Sword SFX and FX

    show pichit at character_move_to_easein("middle", 0.2)

    "Pichit’s blade thrusts forward with surprising skill. Swaths of red cloth flutter to the ground."

    #TODO Sword SFX and FX

    call .pichit_phrarat_cross_blades(0.2) from _call_a1s2_pichit_phrarat_cross_blades

    "The assassin, enraged, lunges. Blade meets blade. The two seem evenly matched."

    "I look around for help, but people are even more panicked than before. Even the hunters are running away from the battle scene."

    "I can’t blame them: they are trained to kill animals, not humans."

    show pichit battle shout

    voice "audio/voice/pichit_1206b.opus"
    pichit "What are you doing here? Go!"

    show pichit battle serious

    show charlet shout
    voice "audio/voice/charlet_1212a.opus"
    charlet "But you–"

    show raegan anxious
    show charlet anxious

    "Vanich grabs my arm, hauling me backward."

    voice "audio/voice/raegan_1208a.opus"
    raegan "We need to get away, now."

    show charlet serious

    "My gaze flicks between Pichit and Vanich. Then I nod."

    show charlet shout
    voice "audio/voice/charlet_1213a.opus"
    charlet "I know somewhere we’ll be safe!"

    show charlet serious

    show charlet at character_exit_to_left(0.5)
    show raegan at character_exit_to_left(0.8)

    play sound audio.sfx.running2

    stop music fadeout 2.0

    "We run, dashing between confused onlookers and oblivious attendees still staring at the smoke billowing from the alchemy stands."

    pause 0.2

    # TODO: Let player choose whether to follow Pichit or Charlet’s PoV (at first), in case they want to directly
    # dive into the battle
    # Eventually though, just before Charlet calls Pichit, we’ll force PoV to Charlet and Raegan since
    # player must make a choice to reveal Makara or not

    jump .refuging_in_building

label .refuging_in_building:

    call start_cinematic from _call_start_cinematic_7

    scene bg university_inside with wiperight_medium
    show charlet serious at character_warp_to("middle_left")
    show raegan anxious at character_warp_to("middle_right")

    pause 0.5

    call end_cinematic from _call_end_cinematic_7

    "Now safe behind the university’s wards, the realization of what happened hits me."

    show charlet scared

    voice "audio/voice/charlet_1214a.opus"
    charlet "Did… did he just try to kill us?!"

    voice "audio/voice/raegan_1209a.opus"
    raegan "Not us. Me."

    show charlet intrigued

    play music mystery

    voice "audio/voice/charlet_1215a.opus"
    charlet "Why would he be trying to kill you?"

    show raegan sad

    voice "audio/voice/raegan_1210a.opus"
    raegan "A man in my position makes many enemies, Dr. Kasamsun. And there are even more who would kill me just to spite my father."

    "Raegan’s expression is dark and his gaze worried. His eyes scan the room, lingering on the boxes stacked against the wall."

    "I realize that the gemstone on his collar is cracked. The protective shield he used earlier must have been single-use."

    # Waiting for asset
    # voice "audio/voice/raegan_1211a.opus"
    raegan "Are we safe here?"

    voice "audio/voice/charlet_1216a.opus"
    charlet "As safe as can be. The university’s wards won’t allow non-staff into the store rooms. You wouldn’t have been able to get in without me."

    "Or my keystone rather. Setting up wards to recognize specific people was impossible."

    show raegan thinking

    # Waiting for asset
    # voice "audio/voice/raegan_1212a.opus"
    raegan "We should contact the security."

    voice "audio/voice/charlet_1217a.opus"
    charlet "I’m on it."

label .telecall:

    call start_cinematic from _call_start_cinematic_8
    show makara neutral at companion_warp_to("left"), flip
    show charlet telepathy with character_dissolve
    call end_cinematic from _call_end_cinematic_8

    "I summon Makara and focus, using its telepathic power to reach out to Jamil, the head of security."
    "Our conversation is brief and to the point. Unsurprisingly given the chaos, he is being inundated with telecalls."

    call start_cinematic from _call_start_cinematic_9
    hide makara
    show charlet neutral
    with character_dissolve
    call end_cinematic from _call_end_cinematic_9

    voice "audio/voice/charlet_1218a.opus"
    charlet "I got someone. They’ll send a squad to Pichit’s location as soon as they can."

    voice "audio/voice/charlet_1219a.opus"
    charlet "There have been several outbreaks of fire in the university’s district, so most firefighters and security guards have their hands full."

    show raegan anxious

    voice "audio/voice/raegan_1213a.opus"
    raegan "A coordinated attack… Let’s hope that Pichit will withstand that fight until then…"

    window hide
    pause 0.5
    show raegan neutral
    pause 0.5
    window show

    voice "audio/voice/raegan_1214a.opus"
    raegan "By the way, Charlet… How did you contact them?"

    voice "audio/voice/charlet_1220b.opus"
    charlet "Uh?"

    voice "audio/voice/raegan_1215a.opus"
    raegan "I haven’t seen you touch your gemstone device at all. Is it a new model that doesn’t need physical interactions?"

    show charlet scared

    voice "audio/voice/charlet_1221a.opus"
    charlet "{i}Oh no! I was so worried about Pichit that I totally forgot to hide my power!{/i}"

    show charlet neutral

    voice "audio/voice/charlet_1222a.opus"
    charlet "{i}Well, I can probably tell him about my spirit now. After all, he already knows that I am a descendant of the Islanders.{/i}"

    voice "audio/voice/charlet_1223a.opus"
    charlet "Oh, that’s…"

    show makara neutral at companion_warp_to("left"), flip

    voice "audio/voice/makara_1202a.opus"
    makara "Charlet, wait. We don’t know if we can trust that man yet. It may be unwise to reveal too much about you before you know him better."

    voice "audio/voice/charlet_1224a.opus"
    charlet "{i}But he’s going to travel with us on the expedition. He’s bound to notice your existence sooner or later.{/i}"

    voice "audio/voice/makara_1203a.opus"
    makara "I see. Then, I leave the final choice to you."

    hide makara with character_dissolve

    voice "audio/voice/charlet_1225a.opus"
    charlet "{i}Alright. Should I introduce Raegan to Makara?{/i}"

    menu:
        "I mention the presence of Makara, although invisible.":
            call .choice_telecall_1_mention_makara from _call_a1s2_choice_telecall_1_mention_makara

        "I don’t mention Makara and pretend to use a telestone.":
            call .choice_telecall_2_pretend_telestone from _call_a1s2_choice_telecall_2_pretend_telestone

    jump .charlet_calls_pichit

label .choice_telecall_1_mention_makara:

    show charlet smile

    voice "audio/voice/charlet_1226b.opus"
    charlet "No, no, that’s just an armband with a decorative jewel. I don’t need it to telecall people. I have much better."

    show makara neutral at companion_warp_to("left"), flip

    # visually, Charlet presents Makara with her arm bent in V with open hand like someone on an ad poster
    "I designate Makara with my open hand."

    voice "audio/voice/charlet_1227a.opus"
    charlet "Here! My spirit companion. You see, my family has preserved the tradition of spirit binding for generations."

    show raegan intrigued

    voice "audio/voice/raegan_vocalize_silence_thinking_a.opus"
    "Raegan cannot hide his perplexity."

    voice "audio/voice/charlet_1228a.opus"
    charlet "You can’t see my spirit, right?"

    voice "audio/voice/charlet_1229a.opus"
    charlet "Don’t worry, Enonians are simply born spirit-blind. Even I had to do a special training on Moacu-Laedan so I could perceive them."

    show charlet serious
    show raegan neutral

    voice "audio/voice/charlet_1230a.opus"
    charlet "Anyway, Makara allows me to reach other people’s minds."

    $ has_mentioned_makara_to_raegan = True
    return

label .choice_telecall_2_pretend_telestone:

    voice "audio/voice/charlet_1231a.opus"
    charlet "Yes, it’s a new kind of stone gear that connects directly to my brainwaves."

    show raegan surprised

    voice "audio/voice/raegan_1216a.opus"
    raegan "Really? That’s impressive! Why didn’t my technology watch group notify me of this? Can I have a look at it?"

    show raegan neutral

    show charlet scared at character_move_to_easein("left", 0.3)

    "As Raegan tries to touch my armband, I instinctively withdraw it out of his reach."

    voice "audio/voice/charlet_1232a.opus"
    charlet "Sorry, it’s… a prototype from the university’s lab. They lent it to me."

    voice "audio/voice/charlet_1233a.opus"
    charlet "They’re still experimenting with it, but it’s not ready for production, so they prefer keeping it private for now."

    show raegan sad
    show charlet neutral

    voice "audio/voice/raegan_1217a.opus"
    raegan "Oh, I… I understand. Please pardon my intrusion."

    show raegan neutral
    show charlet smile

    voice "audio/voice/charlet_1234a.opus"
    charlet "It’s alright."

    return

label .charlet_calls_pichit:

    window hide
    pause 1.0
    window show

    show charlet neutral

    voice "audio/voice/charlet_vocalize_thinking.opus"
    charlet "…"

    voice "audio/voice/charlet_1235a.opus"
    charlet "I’m worried for Pichit. I’ll go check on him."

    call start_cinematic from _call_start_cinematic_10
    stop music fadeout 1.0

    show charlet telepathy with character_dissolve
    pause 0.5

    # BETTER FX: zoom on Charlet’s head and dissolve to Pichit, ARMS manga transition style

    scene bg university_outside with wipeleft_medium

    jump .fight_intro

# BATTLE WITH PICHIT
label .fight_intro:

    # Place fights at zorder >= 1 so we can easily draw spirit sprites behind them later
    # Place assassin a bit above since Pichit’s left arm looks more in the background
    show pichit battle serious zorder 1 at character_warp_to("left")
    show phrarat determined zorder 2 at character_warp_to("right")

    pause 1.0

    call end_cinematic from _call_end_cinematic_10

    show phrarat shout
    phrarat "Don’t get in my way! My quarrel is not with you!"

    show phrarat determined
    show pichit battle shout

    voice "audio/voice/pichit_1207b.opus"
    pichit "Who are you? Why are you attacking us?"

    show pichit battle serious
    show phrarat smile

    "The assassin scoffs at me."

    # Voice acting: voice the scoff "Humph!" at the beginning of this line
    phrarat "Can’t you guess? You’re from Moacu-Laedan, right?"

    show phrarat determined

    phrarat "Haven’t you seen what Vanich did to our nation?"

    voice "audio/voice/pichit_1208a.opus"
    pichit "I know… But Raegan’s different. He’s trying to improve our relationship with Enon and the rest of the mainlanders."

    phrarat "Ha! You really think he’ll be satisfied just building bridges?"
    phrarat "He’ll want more and more… Until he completely consumes our homeland."

    voice "audio/voice/pichit_1209b.opus"
    pichit "Maybe… But for now, I have to count on him to make things better."

    phrarat "Then I have no choice but to crush you too."

    jump .fight1

label .fight1:

    call start_cinematic from _call_start_cinematic_11

    play music battle
    pause 1.7

    call .phrarat_whip_dodged_duck from _call_a1s2_phrarat_whip_dodged_duck

    call end_cinematic from _call_end_cinematic_11

    show pichit battle anxious

    "The assassin ignites his scarf and swings it like a whip towards my head. I duck in time to dodge it, but I can feel the surrounding heat on my face."

    show pichit battle serious

    call .phrarat_blade_dodged_backward from _call_a1s2_phrarat_blade_dodged_backward

    "Another sword strike. I dance out of reach, narrowly losing a finger."

    voice "audio/voice/pichit_1210b.opus"
    pichit "{i}It looks like all the sword dance lessons my mother forced me to learn are finally paying off…{/i}"

    call start_cinematic from _call_start_cinematic_12

    # TODO: change animation calls to match text
    call .phrarat_whip_catch from _call_a1s2_phrarat_whip_catch
    pause 0.25
    call .pichit_cut_catching_whip from _call_a1s2_pichit_cut_catching_whip
    pause 0.25

    call .pichit_phrarat_cross_blades(0.0) from _call_a1s2_pichit_phrarat_cross_blades_1

    call end_cinematic from _call_end_cinematic_12

    "A jab. Another twist. I rush forward, slashing forward with my blade."

    show pichit battle anxious

    "He blocks it and puts me on the defensive. Sweat beads on my forehead as I strain to keep away while stopping his attempts to run past me toward Raegan."

    show phrarat shout

    phrarat "Traitor! You dishonor our people by siding with the likes of him! Have you no pride?!"

    show pichit battle serious
    show phrarat anxious

    "I vault over a booth, kicking at its legs. It sags, the canopy falling to obstruct the assassin."

    show phrarat shout

    phrarat "Stop this! Just let me get rid of that worm and I’ll leave you be!"

    show phrarat determined

    voice "audio/voice/pichit_1211b.opus"
    pichit "Sorry, but Raegan is our last hope to lead Vanich Industries toward the right path."

    show phrarat shout

    phrarat "You really think that? He’ll be just like his father! Just like everyone else!"

    show phrarat determined

    "The sword gives me better reach, but this close, the advantage is lost. With his dagger, my assailant chains quick strikes that force me backward."
    "As our blades clash, I inch closer to the fountain at the center of the university yard."

    call start_cinematic from _call_start_cinematic_13

    call .pichit_phrarat_cross_blades(-0.1, 2) from _call_a1s2_pichit_phrarat_cross_blades_2
    call .pichit_phrarat_cross_blades(-0.2, 1) from _call_a1s2_pichit_phrarat_cross_blades_3

    call end_cinematic from _call_end_cinematic_13

    "Our blades lock. A stalemate. I feel myself tiring. At this rate, I’ll die."

    show fan neutral at companion_warp_to("far_left"), flip

    voice "audio/voice/fan_1102a.opus"
    fan "To your right…"

    "I jump back just in time to dodge his blade. Without Fan’s warning, I would have been badly hurt."
    "The assassin’s wrist flicks forward."

    call start_cinematic from _call_start_cinematic_14

    show pichit battle serious
    hide fan with character_dissolve

    call .phrarat_whip_catch from _call_a1s2_phrarat_whip_catch_1
    pause 0.5

    call end_cinematic from _call_end_cinematic_14

    show pichit battle grimace

    "His burning scarf wraps like a whip around my left leg. Agony paralyzes me."

    play sound audio.sfx.scarf
    show phrarat at bump_right(0.05, 0.1)
    show pichit at fall_left
    pause 0.2
    play sound audio.sfx.hit
    pause 0.3

    "He pulls the whip back to make me lose my balance. My back slams into a nearby crate, the wind knocked out of me."

    voice "audio/voice/pichit_1212a.opus"
    pichit "{i}That damn whip. If only I could get rid of it!{/i}"

    voice "audio/voice/pichit_1213a.opus"
    pichit "{i}How come it hasn’t already been consumed by the flames? How much fabric does this guy have?!{/i}"

    "My thoughts scatter as the assassin lunges at me. He raises his dagger, ready to stab me in the chest."

    show pichit battle shout

    voice "audio/voice/pichit_1214b.opus"
    pichit "Fan, now!"

    play sound audio.sfx.summon
    show fan neutral at companion_warp_to("far_left", _ypos_offset=0.25), flip
    pause 0.5

    play sound audio.sfx.block_shield2
    "A large bark shield materializes around my arm, just in time to protect me from the assault."

    show pichit battle serious

    phrarat "So, you finally showed your spirit."

    show phrarat shout

    phrarat "But you betray our heritage by using your power for the likes of Vanich!"

    show phrarat determined

    voice "audio/voice/pichit_1215a.opus"
    pichit "Ironic coming from someone who keeps burning his own tribal cloth. What would your ancestors say?"

    phrarat "A small price to pay. Their corruption must stop. They have invaded our land, and now they are exploiting spirits to claim their powers for themselves."

    show pichit battle anxious

    "The assassin wraps his burning scarf around my shield. The scent of burnt wood fills the air. It won’t take long before it burns to ashes."

    show pichit battle grimace
    hide fan with character_dissolve

    phrarat "Your dry wood stands no chance against my flames. Let’s put an end to this."

    call start_cinematic from _call_start_cinematic_15

    show pichit battle serious

    # TODO: FX vines
    play sound audio.sfx.vines
    pause 0.2

    show phrarat surprised at character_move_to_easein_elastic("middle")
    pause 0.5

    call end_cinematic from _call_end_cinematic_15

    phrarat "What?!"

    call start_cinematic from _call_start_cinematic_16

    show fan neutral at companion_warp_to("right"), reset_flip
    pause 0.5

    call end_cinematic from _call_end_cinematic_16

    show pichit battle shout

    voice "audio/voice/pichit_1216a.opus"
    pichit "Good job, Fan!"

    show pichit battle serious

    voice "audio/voice/pichit_1217a.opus"
    pichit "You really thought I was just losing ground all that time, uh?"

    voice "audio/voice/pichit_1218a.opus"
    pichit "Never cared having a break for a minute to appreciate nature surrounding you?"

    "As we moved along the university courtyard, cobblestones made way for grass, filled with bushes and decorative flowers. A nearby fountain keeps them hydrated."

    "While the assassin was busy burning my shield, Fan blasted numerous vines from this fertile soil to block the assassin’s limbs."

    # Note that it was a backward fall so this will make Pichit stand up but also move forward (right) a little
    show pichit at reset_fall(0.2)

    "I stand up, throwing away the remains of my carbonized shield. Now, I have the upper hand."

    # Force reset in case player skipped pause above, to avoid getting stuck in the middle of translation
    show pichit at reset_fall

    show phrarat anxious

    phrarat "More plants, really? I’ll just burn them like the rest…"

    "With a snap of fingers, he sparks fire at the vines restraining him. But they refuse to yield."

    show phrarat shout

    phrarat "Why are they resisting?!"

    show phrarat anxious

    voice "audio/voice/pichit_1219b.opus"
    pichit "Can’t recognize the perpetuas that grow in our homeland? Sturdy and quick to absorb water, they will resist your fire for a while."

    hide fan with character_dissolve

    voice "audio/voice/pichit_1220a.opus"
    pichit "{i}Now’s my chance!{/i}"

    call start_cinematic from _call_start_cinematic_17

    show pichit at character_move_to_easein("middle_left", 0.2, _xpos_offset=-0.05)
    pause 0.3
    show pichit at character_move_to_easein("left", 0.2, _xpos_offset=-0.05)

    call end_cinematic from _call_end_cinematic_17

    "I step forward to strike my opponent, but he uses his whip to keep me at bay."

    voice "audio/voice/pichit_1221a.opus"
    pichit "{i}I can’t get too close…{/i}"

    "He can still wield that scarf with mere movements of the wrist, and my vines are not strong enough to paralyze his every articulation."

    voice "audio/voice/pichit_1222a.opus"
    pichit "{i}How should I approach him? If only I knew the source of his power…{/i}"

    $ should_show_side_image = True
    show charlet telepathy
    voice "audio/voice/charlet_1236a.opus"
    charlet "Pichit! Can you hear me?"

    show pichit battle anxious

    "I startle at her voice echoing in my head. It’s not the first time we try telepathy with Charlet, but it always makes an impression."

    show pichit battle serious

    show charlet telepathy
    voice "audio/voice/charlet_1237a.opus"
    charlet "I see it! His spirit is on his left shoulder!"

    # FX: special shader or blue layer to show the spirit as a faint shimmer, then reveal it fully thanks to Charlet’s vision power

    "My eyes narrow, seeking the faint shimmer of a spirit in hiding."

    show pen neutral at companion_warp_to("middle", _xpos_offset=0.1)

    "Then I see it. I mistook it for the heat!"

    "It’s producing red cloth from its own body and weaving it at the same time, at a faster pace than the assassin burns it."

    show pichit battle anxious

    voice "audio/voice/pichit_1223c.opus"
    pichit "{i}Wait a minute. If his spirit’s power is related to cloth, where does his fire come from?{/i}"

    show phrarat shout

    phrarat "Graaah!!"

    "My thoughts are interrupted once more. Unable to burn the vines, the assassin takes his dagger with his free hand and starts cutting the vines."

    show phrarat determined
    show pichit battle serious

    "I reinforce my connection with Fan to spawn new ones faster than he can cut them. But even aided by the natural flora behind me, I can feel Fan struggling to keep up."

    voice "audio/voice/pichit_1224b.opus"
    pichit "{i}I need to finish this quickly!{/i}"

    show fan neutral at companion_warp_to("far_right")

    voice "audio/voice/pichit_1225a.opus"
    pichit "{i}Fan! Focus on his shoulder!{/i}"

    # FX: vines

    "My spirit readily complies, vines whipping forward towards the assassin."

    show pichit battle anxious

    "But it isn’t enough. The flames are too hot. The tendrils curl into ash too quickly…"

    hide fan with character_dissolve

    voice "audio/voice/pichit_1226a.opus"
    pichit "{i}Charlet, I can’t reach it!{/i}"

    $ should_show_side_image = True

    show charlet telepathy
    voice "audio/voice/charlet_1238a.opus"
    charlet "Try to lure him to the greenhouse! It has fire sprinklers!"

    voice "audio/voice/pichit_1227b.opus"
    pichit "{i}I see… It won’t be that easy to lead such an aggressive guy, though.{/i}"

    show charlet telepathy
    voice "audio/voice/charlet_1239a.opus"
    charlet "I’m sorry… I wish I could help you with my spirit, but my mastery of water isn’t that good…"

    show pichit battle serious
    voice "audio/voice/pichit_1228a.opus"
    pichit "{i}It’s okay… I’ll find a way.{/i}"

    $ should_show_side_image = False

    show pichit battle serious

    window hide
    pause 0.5
    window show

    phrarat "So, you finally noticed my spirit, uh? It took you time…"

    show phrarat smile

    phrarat "Maybe you forgot your ancestral values after living with those Enonians for too long?"

    show phrarat shout

    phrarat "Even lowering yourself to attacking someone else’s spirit!"

    show phrarat determined

    voice "audio/voice/pichit_1229a.opus"
    pichit "What are you talking about? We’re in the middle of a fight, and {i}you{/i} attacked us!"

    voice "audio/voice/pichit_1230a.opus"
    pichit "Besides, who’s betraying our traditions? Your fire comes from a gemstone, right?"

    phrarat "…"

    phrarat "A necessary evil to put an end to this madness."

    show phrarat shout

    phrarat "Pen!"

    show phrarat determined

    "My opponent’s spirit flies away from his shoulder to get closer to the ground I’m growing the vines from."

    "This time, it spins thick threads, moving from place to place among the plants like a spider. It’s so fast that my eyes can barely follow."

    "The small garden is soon covered by a web of viscous fibers, trapping the perpetua sprouts inside."

    show phrarat smile

    "With no new vines coming at him, it’s not long before the assassin gets rid of the last remnants of them."

    show pichit battle anxious

    show pichit at character_exit_to_left_easeout(0.45)

    "As I sense my demise is close, I run toward the greenhouse."

    show phrarat determined

    phrarat "You’re not my target, but you may lead me to Vanich…"
    phrarat "… and you’re too dangerous to be left alone."

    show phrarat shout
    phrarat "Pen!"

    "I turn my head back to my opponent. His spirit spins a thread and throws it forward. It wraps around a lamp post on my right, and its other end around the assassin’s arm."

    hide phrarat
    hide pen
    with character_dissolve

    "The spirit rewinds the thread as fast as it spun it, launching its companion at high speed toward my position."

    show pichit battle grimace at character_warp_to("left")

    voice "audio/voice/pichit_1231c.opus"
    pichit "Uh-oh…"

    "Keeping the momentum of his thrust, the assassin takes an offensive stance."

    show phrarat shout zorder 2 at character_enter_from_right_to_easein("middle", 0.3)

    phrarat "Phoenix Dance!"

    # CG: Phoenix Dance

    "He twirls around, his blazing dagger in one hand and a solidified scarf in the other."

    "I get hit with full force."

    show pichit at character_exit_to_left(0.3)

    jump a1s3


# Reusable battle sequences

# UNUSED
label .phrarat_whip_dodged_backward:
    show phrarat at character_move_to("middle_right", 0.1)
    pause 0.05
    show pichit at character_move_to("far_left", 0.1)
    play sound audio.sfx.scarf
    # interrupt scarf sound before hit for dodge sound (also covers scarf wipe in the air)
    pause 0.45
    play sound audio.sfx.swift_move1

    return

label .phrarat_whip_dodged_duck:
    show phrarat at character_move_to("middle_right", 0.1)
    pause 0.05
    show pichit at bump_down(abs_yoffset=100)
    play sound audio.sfx.scarf
    # interrupt scarf sound before hit for dodge sound (also covers scarf wipe in the air)
    pause 0.45
    play sound audio.sfx.swift_move1

    return

label .phrarat_blade_dodged_backward:
    show phrarat at character_move_to("middle_right", 0.1)
    play sound audio.sfx.slash3
    pause 0.2
    play sfx1 audio.sfx.swift_move1
    show pichit at character_move_to("far_left", 0.1)

    return

# UNUSED
label .pichit_slash_blocked:
    play sound audio.sfx.slash_impact3
    pause 0.15

    show pichit at character_move_to_easein_elastic("middle_left", 0.4)
    show phrarat at bump_left(0.05, 0.1)

    pause 0.25

    show phrarat at character_move_to("middle_right", 0.25)
    show bg at hpunch_powerful

    return

label .phrarat_whip_catch:
    show phrarat at bump_left
    play sound audio.sfx.scarf
    pause 0.25
    show pichit at bump_left
    play sound audio.sfx.impact_catch

    return

label .pichit_cut_catching_whip:
    show pichit at bump_left
    play sound audio.sfx.slash2
    pause 0.5
    play sound audio.sfx.slash3
    # use different channel to play next sound overlapping the end of the previous one
    $ renpy.music.play(audio.sfx.swift_move2, channel="sfx1", loop=False)

    show phrarat at character_move_to("right", 0.1)

    return

label .pichit_phrarat_cross_blades(_xpos_offset=0.0, sfx_variant_number=1):
    show pichit at character_move_to_easein("left", 0.25, _xpos_offset)
    show phrarat at character_move_to_easein("right", 0.25, _xpos_offset)

    pause 0.15

    call .play_blade_clash_sfx_variant(sfx_variant_number) from _call_a1s2_play_blade_clash_sfx_variant

    # Hotfix to adjust timing, as SFX variant impact part is not playing at the same time
    if sfx_variant_number == 1:
        pause 0.2
    else:
        pause 0.05

    show pichit at character_move_to_easein_elastic("middle_left", 0.25, _xpos_offset)
    show phrarat at character_move_to_easein_elastic("middle_right", 0.25, _xpos_offset)
    show bg at hpunch_powerful
    pause 0.5

    return

label .play_blade_clash_sfx_random_variant:
    $ sfx_variant_number = renpy.random.randint(1, 2)
    call .play_blade_clash_sfx_variant(sfx_variant_number) from _call_a1s2_play_blade_clash_sfx_variant_1

    return

label .play_blade_clash_sfx_variant(variant_number):
    if variant_number == 1:
        $ sfx_variant = audio.sfx.blade_clash1
    else:
        $ sfx_variant = audio.sfx.blade_clash2
    play sound sfx_variant

    return
