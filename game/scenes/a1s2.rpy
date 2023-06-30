label a1s2:
    # "Act 1: Scene 2 - Attack"
    jump .assassin_appears

label .assassin_appears:
    scene bg university_outside

    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("middle")
    show pichit neutral at character_warp_to("right"), darker

    raegan "It's always a pleasure to meet someone who can appreciate the island's unique charm. What drove your interest?"
    show raegan intrigued

    charlet "My ancestors came from the island. Studying at the academia made me realize just how little we, in Enon, know about Moacu. It is my hope that this expedition will help build a bridge between our people and promote appreciation of spirits."

    raegan "Indeed... Pichit mentioned your goal was to catalogue folktales from the island? Did you ever hear any of tales of Lalahon?"

    show charlet intrigued

    "My eyes widened. That Raegan had heard of Lalahon at all, was surprising. Stories about Lalahon were rare and their contents contraditory. The few that I had heard had been told to me by my grandfather."

    "According to grandfather's tales, Lalahon was either a benevolent goddess born from the ashes of the great, god Bathala's heart, or an evil beast that had killed Bathala and used his fire to destroy the forests."
    "Which version of the tale was true, had been the subject of many debates between the two of us. Only one thing was certain: Lalahon was powerful."

    charlet "Only a couple passed down from my grandfather. Much of her history appears lost. I hope that this expedition will allow many more of these tales to be collected and preserved for future generations."
    charlet "Who knows, maybe we'll even discover the secret behind the mist that covered the island!"

    raegan "A worthy endeavour for sure. I look forward to hearing more of your goals and the tourism business proposition."

    charlet "Of course. I have may schedule here would you like to set up time to meet?"

    show pichit intrigued at reset_brightness

    play sound audio.sfx.smoke

    "Before Raegan could respond, a bright flash blinded us. Confused cries sounded out in the crowd and the air grew thick with the scent of smoke."
    "I turned west, watching as smoke poured out from the direction of the alchemy station. Had one of the displays malfunctioned?"

    raegan "My pardons, Pichit... Was a this part of the event?"

    show pichit smile

    "Pichit smiled, nonchalantly waving a hand to dismiss the commotion, but I could see from the tension in his shoulders he was perturbed."

    pichit "Some demonstrations must have malfunctioned. I'm sure it's nothing to be concerned about, sir."

    raegan "Are you sure, that-"

    # no smoke asset yet, so just reuse outside
    # scene bg smoke with bg_dissolve
    scene bg university_outside with bg_dissolve
    show phrarat neutral at character_warp_to("middle")

    stop music fadeout 1.0
    pause 0.5

    "A sudden impact steals the rest of his words. A swath of red cuts through the smoke too quick to catch. Belatedly I realize that Pichit has shoved me to the floor."

    scene bg university_outside with bg_dissolve
    show charlet scared at character_warp_to("far_left")
    show raegan surprised at character_warp_to("middle_left")
    show pichit surprised at character_warp_to("middle_right")
    show phrarat neutral at character_warp_to("far_right")

    "I look up, shocked to find Raegan half-sprawled over the table of my booth, a dark figure standing over him. A glowing shield is the only barrier between his chest and his assailant's knife."

    "A vigilante?!?"

# TODO impact SFX and hit FX

    "Before I can react, Pichit tackles him. The two men go rolling, the pamphlet's I had printed falling with them."

    play sound audio.sfx.throw_fireball
    show phrarat determined at bump_left
    pause 0.1
    show pichit battle serious at character_move_to("middle", 0.25)
    pause 0.25
    play sound audio.sfx.slash1
    pause 0.5

    "For a moment, there is only a mad tangle of limbs. Then Pichit goes flying. The assailant, stands, his knife replaced by a scarf."
    "The incongruity of me strikes me. Why is he balling up a scarf?"

    "..Then my question is answered. Flames ignite. The simple scarf transformed into a firey projectile. I brace myself..."

    pause 0.5

    "...Only to find myself safe. A wooden shield looms above me."

    show pichit battle shout

    pichit "Don't just sit there! Get inside now!"

    "As the shield dematerializes I see Pichit, standing before the assassin. A sword is in his hand. Vaguely I recognize it as a replica from the history booth."

#TODO Sword SFX and FX

    "Pichit's blade thrusts forward with surprising skill. Swaths of red cloth flutter to the ground."

    #TODO Sword SFX and FX

    "The assassin, enraged, lunges. Blade meets blade. The two seem near evenly matched, but I can see Pichit tiring."

    #TODO Sword SFX and FX 3x

    show pichit battle shout

    pichit "What are you doing here? Go!"

    #TODO Sword SFX

    "What do I do?!? What do I do?!?"

    "If I leave now, what if Pichit dies? Even with his spirit beast, how could a tour guide face off against an assassin?"

    "But what was the alternative? If Raegan was hurt, or Garuda-help us, died, what would happen to us?"

    "The proverbial death of both our careers would be the best case scenario. At worse we'd be pegged as accomplices and cast in prison, proof or no proof."
    "Panic left me paralyzed. But I had to move. Time was ticking."
    "Taking in a shaky breath I..."

    menu choice1:
        " Decided to stay.":
            "I can’t let Pichit face the assassin alone. Makara is strong. I can do this!"
            jump a1s1run


        "Go.":
            "Pichit can handle himself. I need to have faith in him and ensure Raegan's safety. Then I could contact someone via telestone."
            jump a1s1run



label a1s1run:

    "The choice is stolen from me just as I make up my mind."

    "Vanich grabs my arm, hauling me backwards."

    raegan "We need to get away, now."

    "My gaze flicks between Pichit and Vanich. Then I nod."

    charlet "Into the school! I know somewhere we'll be safe!"

    show charlet at character_exit_to_left(0.5)
    show raegan at character_exit_to_left(0.8)

    play sound audio.sfx.running2

    "We run, dashing between confused onlookers and oblivious attendees still staring at the smoke billowing from the alchemy stands. Distantly, I hear Dr. Barouche's booming voice claiming a mechanical failure."

    pause 0.5

    scene bg university_inside with bg_dissolve
    show charlet scared at character_warp_to("far_left", 0.5)
    show raegan surprised at character_warp_to("middle_left", 0.5)

    pause 0.5

    "Now safe behind the unversity's wards, the realization of what happened hits me."

    charlet "D-did...did he just try to kill us?!"

    raegan "Not us. Me."

    charlet "Why would he be trying to kill you"

    raegan "A man in my position makes many enemies, Dr. Kasamsun. And there are even more that would kill me just to spite my father."

    "Raegan's expression is dark and his gaze worried. His eyes scan the room, lingering on the boxes stacked against the wall."

    raegan "Are we safe here?"

    charlet "As safe as can be. The university's wards won't allow non-staff into the store rooms. You wouldn't have been able to get in without me."

    "Or my keystone rather. Setting up wards to recognize specific people was impossible."

    raegan "We should contact someone. Do you have a telestone? Can you reach the guard?"

    "I shook my head. The telestone I had was a prototype, courtesy of the charms department. The range was a few hundred meters at best."

    charlet "No. But there should be guards someone where on campus."

    "Focusing, I tried to reach out to Jamil, the head of security. Our conversation was brief and to the point. Unsurprisingly given the chaos, he was being inundated with telecalls."

    charlet "I got someone. They'll be there as soon as they can. Everything will be okay."

    "Or so I hoped. It could be minutes or hours before they came. Worry for Pichit left me deaf to Raegan's reply. Though it was risky, I couldn't help but activate the telestone again, this time reaching out for Pichit..."

    scene bg black with wipeleft_fast
    pause 0.1
    scene bg university_outside with wipeleft_fast

# TODO Switch to Pichit POV, fade screen, maybe new BG angle or zoom in?

# BATTLE WITH PICHIT

    show pichit battle serious at character_warp_to("left")
    show phrarat neutral at character_warp_to("right")

    pause 1.0

    phrarat "Don't get in my way! My quarrel is not with you!"

    pichit "Who are you? Why are you attacking us?"

    phrarat "A hero here to save you from {i}them{/i}."

    "{i}I don't know what he's talking about, but he seems pretty determined to finish Raegan. I won't let him!{/i}"

    pichit "Fan! Block him!"

    jump .fight1

label .fight1:

    play music battle
    pause 1.7
    show phrarat determined at character_move_to("middle_right", 0.1)
    pause 0.05
    show pichit at character_move_to("far_left", 0.1)
    play sound audio.sfx.scarf

    call .phrarat_whip_dodged from _call_a1s1run_phrarat_whip_dodged

    "The assassin lunges at me. His makeswift whip swings towards my face, the heat of leaving my skin hot."

    call .pichit_slash_blocked from _call_a1s1run_pichit_slash_blocked

    "Thankfully, Fan blocks the worst of it. Another strike. I dance out of reach, narrowly losing a finger."

    "{i}It looks like all the sword dance lessons my mother forced me to learn are finally paying off...{/i}"

    # TODO: change animation calls to match text
    call .phrarat_whip_catch from _call_a1s1run_phrarat_whip_catch
    pause 0.25
    call .pichit_cut_catching_whip from _call_a1s1run_pichit_cut_catching_whip
    pause 0.25

    call .pichit_phrarat_cross_blades(0.0) from _call_a1s1run_pichit_phrarat_cross_blades

    "A jab. Another twist. I rush forward, slashing forward with my blade."
    "He blocks it and puts me on the defensive. Sweat beads on my forehead as I strain to keep away while stopping his attempts to run."

    phrarat "Traitor! You dishonor our people by siding with the likes of him! Have you no pride?"

    pichit "I don't know what you're talking about!"

    "I vault over a booth, kicking at its legs. It sags, the canopy falling to obstruct the assassin."

    phrarat "Stop this! Just let me get rid of that worm and I'll leave you be!"

    "The sword gives me better reach, but this close the advantage is lost. He slices forward with his dagger. Quick strikes that force me backward."
    "As our blades clash I inch closer to the fountain and the biology team's plant display. The Fan more has to work with, the better."

    call .pichit_phrarat_cross_blades(-0.1, 2) from _call_a1s1run_pichit_phrarat_cross_blades_1
    call .pichit_phrarat_cross_blades(-0.2, 1) from _call_a1s1run_pichit_phrarat_cross_blades_2

    "Our blades lock. A stalemate. I feel my self tiring. At this rate I'll die."

#todo show fan
    fan "To your right!"

    "I jump back. A blade slices down. It narrowly misses me. Without Fan's warning I would have died."

    "{i}Fan! Shield!{/i} I cry as the assassin wrist flicks forward."

    call .phrarat_whip_catch from _call_a1s1run_phrarat_whip_catch_1
    pause 0.5

    "Too late. A length of flame wraps around my left leg. Agony paralyzes me."

    play sound audio.sfx.scarf
    show phrarat at bump_right(0.05, 0.1)
    show pichit at fall_left
    pause 0.2
    play sound audio.sfx.hit
    pause 0.3

    "Only a second. It is enough. My feet fly out from beneath me. My back slams into a nearby crate, the wind knocked out of me."

    "{i}That damn whip. If only I could get rid of it!{/i}."

    "{i}...Wait a minute, why hadn’t it burned to ash already? How much fabric did this guy have?!?{/i}"

    "My thoughts scatter as the assassin lunges at me, whip at ready. I recognize the stance."

    pichit "Fan, now!"

    show fan neutral at companion_warp_to("left")

    "A large bark shield weaves halts materializes in time to stop this newest volley."

    phrarat "Neat parlor trick! Too bad it'll be gone before long! How many strikes would it take? Three?"

    "I grit my teeth. He's right. Even aided by the natural flora behind me, I can feel Fan struggling to keep up."
    "As though sensing my weakness, the assassin abandons his dagger for the whip. The scent of burnt wood fills the air."

    charlet telepathy "Pichit! Can you hear me?"

    "I start at her voice. I had forgotten the telestone. Stupid! So stupid! I should have called for help! Too late now."

    charlet telepathy "Look at his shoulder! There’s a spirit on his shoulder!"

    "My eyes narrowed, seeking the faint shimmer of a spirit in hiding. There I saw it! I had mistaken it for the heat!"

    "{i}Fan! Focus on his shoulder{/i} My spirit readily complies, vines whipping forward towards the assassin."

    "It isn't enough. The flames are too hot. The tendrils curl into ash too quickly. What do I do?"

    charlet telepathy "Get him inside! Let the sprinklers can take care of the fire!"

    "An idea pops into my head. A crazy idea. The type of idea that would have Charlet yelling and my mother tanning my hide."

    "I do it anyway. Allowing my exhaustion to show, I ask Fan to make another attempt. As the asssasin blocks it, I begin to cough and sway."

    "The assassin is on me in moments. The flat of his dagger presses into my throat, close enough I know the simplest movement will slice my skin to ribbons."

    "I swallow, suddenly realizing just how big a risk I am taking."

    pichit "You win! I give up! He's in the school! In the faculty room!"

    phrarat "How do you know that?"

    pichit "My friend. She told me!"

    "The assassin eyes narrow with suspicion. My heart races in my throat as the seconds pass. Then the pressure of the knife eases."

    phrarat "Thank you...friend."

    "Then the assassin turns, disappearing neatly into the crowd."

    # pichit telepathy "He's coming your way. Get ready!"


# CHARLET POV SWITCH

    scene bg black with wipeleft_fast
    pause 0.5
    scene bg university_inside with wipeleft_fast
    show charlet scared at character_warp_to("far_left", 0.5)
    show raegan surprised at character_warp_to("middle_left", 0.5)
    show pichit surprised at character_warp_to("middle_right", 0.5)

    pause 0.5

    "I wait, heart in my throat as Pichit's voice fades. It feels like an eternity before I hear Pichit skids into the store room."

    charlet "Pichit! You're alright!"

    pichit "Barely. I swear I just lost a few years of my life."

    raegan "And the assassin? Has he been dealt with?"

    pichit "Not exactly... I told him you were hiding in the faculty room."

    "It was a clever idea. The faculty room was in the opposite wing. It would buy us time."

#pichit "Go fight him, of course?"

#charlet "Fight? What about the guards? They'll be coming soon!"

#pichit "Not fast enough to stop him! How long do you think he'll stay once he finds out he's been duped? We need to catch him while his guard is down!"

#"Pichit had a point, but I wasn't a fighter. I'd only barely passed archery and while Makara was stronger than the average spirit, we hadn't ever had to fight anything stronger than an imp."
#"Though...the greenhouse would have plants and water. Both Fan and Makara would be at an advantage..."

    #TO DO knocking sound

    raegan "What was that?"

    pichit "I don't know. It sounded like-"

    "To my horror, the door swung open. My heart dropped. The assassin!"

    # we could potentially stop here is we don't have time.

    # End of playtesting

    pause 1.0

    "This is the end of the playtesting section. Thank you for playing!"

    return

# Battle sequences

label .phrarat_whip_dodged:
    show phrarat at character_move_to("middle_right", 0.1)
    pause 0.05
    show pichit at character_move_to("far_left", 0.1)
    play sound audio.sfx.scarf
    # interrupt scarf sound before hit for dodge sound (also covers scarf wipe in the air)
    pause 0.4
    play sound audio.sfx.swift_move1

    return

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

    call .play_blade_clash_sfx_variant(sfx_variant_number) from _call_a1s1run_play_blade_clash_sfx_variant

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
    call .play_blade_clash_sfx_variant(sfx_variant_number) from _call_a1s1run_play_blade_clash_sfx_variant_1

    return

label .play_blade_clash_sfx_variant(variant_number):
    if variant_number == 1:
        $ sfx_variant = audio.sfx.blade_clash1
    else:
        $ sfx_variant = audio.sfx.blade_clash2
    play sound sfx_variant

    return


## BATTLE SEQUENCE DRAFT

label .unused:
    "He then pulls the whip back to make me lose my balance."

    "{i}If only I could get rid of that whip! Come to think of it, how hadn’t it burned to ash already?{/i}"

    "I'm interrupted in my thoughts by the assassin jumping at me to tackle me to the ground. He raises his dagger, ready to stab me in the chest."

    pichit battle shout "Fan, now!"

    play sound audio.sfx.summon
    # Show pichit in front so companion tail doesn't hide his face
    show pichit zorder 1
    show fan neutral at companion_warp_to("far_left"), flip
    pause 0.5

    "A large bark shield weaves itself into existence around my arm, protecting me from the assault."

    play sound audio.sfx.block_shield2
    pause 1.0

    phrarat shout "So, you finally showed your spirit. But you betray our heritage by using your power for the likes of Vanich Enterprises!"

    "The assassin flicks his wrist. A rope binds my shield, searing it to pieces."

    phrarat "Your dry wood stands no chance against my flames. Let's put an end to this."

    pichit battle smile "You really thought I was just losing ground all that time, uh? Never cared having a break for a minute to appreciate the nature surrounding you?"

    show phrarat surprised

    "As we moved along the university courtyard, cobblestones made way for grass, filled with bushes and decorative flowers."

    # TODO: FX vines
    play sound audio.sfx.vines

    "My spirit blasts numerous vines through this fertile soil, blocking the Assassin’s limbs."

    pichit "Ironic coming from someone who keeps burning his own tribal cloth. What would your ancestors say?"

    phrarat "A small price to pay. Their corruption must stop. They have invaded our land, and now they are exploiting spirits to create those fake gemstones."

    "The Assassin strikes at the vines but they keep growing back."

    pichit "For someone so concerned with our native culture, I’m surprised you don’t even recognize what type kind of vines these are."

    "Perpetua plants. A smart move. The vines would regenerate faster than he could do damage. Now it was just a matter of how much energy the assassin’s spirit  had left."

    "A snap sounded in my mind. Professor Mara’s voice stirred to life. Finally, using my abilities, I snap both Pichit and Mara together into one connection."

    ## Analyze and more fight

    "I try to analyze the opponent."

    call .analyze_one_element from _call_a1s1run_analyze_one_element

    scene bg university_inside
    show pichit battle serious at character_warp_to("left")
    show phrarat determined at character_warp_to("right")

    pichit "Why Vanich? He's trying to improve our relationship with Enon and the rest of the mainlanders."

    phrarat "You really believe that? You think there’s profit in building bridges? They won't wait for spirits to die? Don’t tell me you really believe they offer their gemstones willingly? No!"
    phrarat "He takes them by force just like the rest. He just hides it better than the others."

    # show phrarat angry

    phrarat "Pen, now."

    "The telepathic connection with Pichit goes numb for a moment before the entryway erupts, caving in, my guide along with it, caked in dirt."

    pichit "That worked better than expected."

    "Smoke begins to ooze into the warehouse, Pichit wouldn’t see an attack coming before it was too late!"
    "I call upon Makara for assistance but he refused, the smoke would only render him useless."

    phrarat "No more plants, no more chances. Choose: move or die."

    "I try to analyze the opponent once more."

    call .analyze_one_element from _call_a1s1run_analyze_one_element_1

    scene bg university_inside
    show charlet neutral at character_warp_to("left")
    show raegan neutral at character_warp_to("right")

    jump .fight2

label .fight2:
    scene bg university_inside
    show pichit battle serious at character_warp_to("left")
    show phrarat determined at character_warp_to("right")

    # show phrarat sad
    # TODO: pen sad
    show pen neutral at companion_warp_to("far_right")

    play sound audio.sfx.impact_glass

    "Before I’m able to get a good look, a dagger skewers out of the shadows and toward Pichit, who barely dodges it but is sent careening into one of the exhibits. A glass case full of exquisite vases."

    phrarat "What a waste."

    # This raises guide's sympathy
    "Entirely focused on the shattered remains of the exhibit, vases shattered, dirt and seeds that had been hidden in the vases scattered across the floor. Such history, wasted."

    "Without hesitation, the Assassin flips his dagger and sends it hurling for Pichit’s head."
    "Pichit expected it, using the dirt and seeds on the floor, he springs forth spiked vines that envelop the dagger, only for them to smash whatever is left of the exhibit vases in the process."

    hide pen

    phrarat "You destroy our culture without hesitation."

    "Before Pichit can respond, the man from the military booth emerges from the open doorway behind the Assassin. His rifle aimed for the Assassin’s head."

    man_with_rifle "Freeze!!!"

    "A smirk widens across the Assassin's face and the showman pulls the trigger, but nothing happens."
    "The Assassin begins to laugh, turning away from the man who’s still fiddling with the rifle."

    phrarat "The idiot can't even shoot his rifle. Proof that even the universe wants me to succeed."

    "After knocking the gun around  enough times, the rifle erupts, knocking the man back into concrete and distracting the Assassin long enough for Pichit to strike."
    "Bringing the vines upward from the discarded dagger, Pichit slashes them across the Assassins arm who stumbles to the ground almost immediately, his spirit tossed off his shoulder in the process."

    pichit "Poison in the spikes."

    "The Assassin grips at the ground, trying to grapple his way toward his Spirit only who isn’t even moving from where it landed. It’s panting relentlessly, trying to catch its breath."

    pichit "This is over. I know your cause is a noble one, please, let me help you. I can explain everything to you."

    "The Assassin bares his teeth and with a sudden screech of his shoes, rolls upward, snatching his spirit into his arms and landing on his feet."
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

label .analyze_one_element:
    menu:
        "Analyze weapon" if not has_analyzed_assassin_weapon:
            call .analyze_weapon from _call_a1s1run_analyze_weapon
        "Analyze stone" if not has_analyzed_assassin_stone:
            call .analyze_stone from _call_a1s1run_analyze_stone

    return

label .analyze_weapon:
    # TODO: new text
    "Clothes have traditional patterns of Moacu, but are written roughly."
    "Ink mixed with blood. Shows pride but also anger and hastiness. He doesn't care about his environment enough."
    "Pichit could take advantage of this, or try to slow him down."
    $ has_analyzed_assassin_weapon = True
    return

label .analyze_stone:
    "Normally people and esp. Moacu natives wear one color, symbolic of their aptitude for an art. A few experts master and show two colors."
    "In his case, the creature is clearly Green and handles cloth creation and patterns."
    "So Red Fire must be produced by a stone, maybe stolen from the previous attack."

    "He seems to be mastering Fire because his attacks are quite eruptive and uncontrolled. Pichit could take advantage of this."
    "His spirit also seems exhausted, weaving cloth over and over again as it's burning. Maybe it will reach its limit soon..."
    $ has_analyzed_assassin_stone = True
    return
