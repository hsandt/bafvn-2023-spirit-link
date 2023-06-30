
label a1s2a:
    "Act 1: Scene 2 - Gathering Attack"
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

    charlet "Only a couple passed down from my grandfather. Much of her history appears lost. I hope that this expedition will allow many more of these tales to be collected and perserved for future generations."
    charlet "Who knows, maybe we'll even discover the secret behind the mist that covered the island!"

    raegan "A worthy endeavour for sure. I look forward to hearing more of your goals and the tourism business proposition."

    charlet "Of course. I have may schedule here would you like to set up time to meet?"

    show pichit intrigued at reset_brightness

    "Before Raegan could respond, a bright flash blinded us. Confused cries sounded out in the crowd and the air grew thick with the scent of smoke."
    "I turned west, watching as smoke poured out from the direction of the alchemy station. Had one of the displays malfunctioned?"

    raegan "My pardons, Pichit... Was a this part of the event?"

    show pichit smile

    "Pichit smiled, nonchalantly waving a hand to dismiss the commotion, but I could see from the tension in his shoulders he was perturbed."

    pichit "Some demonstrations must have malfunctioned. I'm sure it's nothing to be concerned about, sir."

    raegan "Are you sure, that-"

    scene bg smoke with bg_dissolve
    show phrarat neutral at character_warp_to("middle")

    stop music fadeout 1.0
    pause 0.5

# TODO an impact SFX and maybe smoke FX

    "A sudden impact steals the rest of his words. A swath of red cuts through the smoke too quick to catch. Belatedly I realize that Pichit has shoved me to the floor."
    "I look up, shocked to find Raegan half-sprawled over the table of my booth, a dark figure standing over him. A glowing shield is the only barrier between his chest and his assailant's knife."

    "A vigilante?!?"

# TODO impact SFX and hit FX

    "Before I can react, Pichit tackles him. The two men go rolling, the pamphlet's I had printed falling with them."

    "For a moment, there is only a mad tangle of limbs. Then Pichit goes flying. The assailant, stands, his knife replaced by a scarf."
    "The incongruity of me strikes me. Why is he balling up a scarf?"

    "..Then my question is answered. Flames ignite. The simple scarf transformed into a firey projectile. I brace myself..."

    pause 0.5

    "...Only to find myself safe. A wooden shield looms above me."

    show pichit shout

    pichit "Don't just sit there! Get inside now!"

    "As the shield dematerializes I see Pichit, standing before the assassin. A sword is in his hand. Vaguely I recognize it as a replica from the history booth."

#TODO Sword SFX and FX

    "Pichit's blade thrusts forward with surprising skill. Swaths of red cloth flutter to the ground."

    #TODO Sword SFX and FX

    "The assassin, enraged, lunges. Blade meets blade. The two seem near evenly matched, but I can see Pichit tiring."

    #TODO Sword SFX and FX 3x

    show pichit shout

    pichit "What are you doing here? Go!"

    #TODO Sword SFX

    "What do I do?!? What do I do?!?"

    "If I leave now, what if Pichit dies? Even with his spirit beast, how could a tour guide face off against an assassin?"

    "But what was the alternative? If Raegan was hurt, or Garuda-help us, died, what would happen to us?"

    "The proverbial death of both our careers would be the best case scenario. At worse we'd be pegged as accomplices and cast in prision, proof or no proof."
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

    vanich "We need to get away, now."

    "My gaze flicks between Pichit and Vanich. Then I nod."

    charlet "Into the school! I know somewhere we'll be safe!"

    show charlet at character_exit_to_left(0.5)
    show raegan at character_exit_to_left(0.8)

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

    ragan "A man in my position makes many enemies, Dr.Kasamsun. And there are even more that would kill me just to spite my father."

    "Raegan's expression is dark and his gaze worried. His eyes scan the room, lingering on the boxes stacked against the wall."

    raegan "Are we safe here?"

    charlet "As safe as can be. The univeristy's wards won't allow non-staff into the store rooms. You wouldn't have been able to get in without me."

    "Or my keystone rather. Setting up wards to recognize specific people was impossible."

    raegan "We should contact someone. Do you have a telestone? Can you reach the guard?"

    "I shook my head. The telestone I had was a prototype, courtesy of the charms department. The range was a few hundred meters at best."

    charlet "No. But there should be guards someone where on campus."

    "Focusing, I tried to reach out to Jamil, the head of security. Our conversation was brief and to the point. Unsurprisingly given the chaos, he was being inundated with telecalls."

    charlet "I got someone. They'll be there as soon as they can. Everything will be okay."

    "Or so I hoped. It could be minutes or hours before they came. Worry for Pichit left me deaf to Raegan's reply. Though it was risky, I couldn't help but activate the telestone again, this time reacing out for Pichit..."

    scene bg black with CropMove(0.5, "wipeleft")
    pause 0.1
    scene bg university_outside

# TODO Switch to Pichit POV, fade screen, maybe new BG angle or zoom in?

# BATTLE WITH PICHIT

    show phrarat determined at bump_left
    pause 0.1
    show pichit battle serious at character_move_to("middle", 0.25)
    pause 0.25
    play sound audio.sfx.throw
    pause 0.5

    show pichit battle serious at character_move_to("left")
    show phrarat at character_move_to("right")

    pause 1.0

    assassin "Don't get in my way! My quarrel is not with you!"

    pichit "Who are you? Why are you attacking us?"

    assassin "A hero here to save you from {i}them{/i}."

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

    "The assassin lunges at me. His makeswift whip swings towards my face, the heat of leaving my skin hot."

    play sound audio.sfx.slash_impact3
    pause 0.15

    "Thankfully, Fan blocks the worst of it. Another strike. I dance out of reach, narrowly losing a finger."

    "{i}It looks like all the sword dance lessons my mother forced me to learn are finally paying off...{/i}"

    play sound audio.sfx.slash_impact3
    pause 0.15

    show pichit at character_move_to_easein_elastic("middle_left", 0.4)
    show phrarat at bump_left(0.05, 0.1)

    pause 0.25

    show phrarat at character_move_to("middle_right", 0.25)
    show bg at hpunch_powerful

    "A jab. Another twist. I rush forward, slashing forward with my blade."
    "He blocks it and puts me on the defensive. Sweat beads on my forehead as I strain to keep away while stopping his attempts to run."

    assassin "Traitor! You dishonor our people by siding with the likes of him! Have you no pride?"

    pichit "I don't know what you're talking about!"

    "I vault over a booth, kicking at its legs. It sags, the canopy falling to obstruct the assassin."

    assassin "Stop this! Just let me get rid of that worm and I'll leave you be!"

    "The sword gives me better reach, but this close the advantage is lost. He slices forward with his dagger. Quick strikes that force me backward."
    "As our blades clash I inch closer to the fountain and the biology team's plant display. The Fan more has to work with, the better."

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

    "Our blades lock. A stalemate. I feel my self tiring. At this rate I'll die."

    play sound audio.sfx.scarf
    pause 0.5
    play sound audio.sfx.catch
    pause 0.1

    show phrarat at bump_left(0.05, 0.1)
    show pichit at fall_left

#todo show fan
    fan "To your right!"

    "I jump back. A blade slices down. It narrowly misses me. Without Fan's warning I would have died."

    "{i}Fan! Shield!{/i} I cry as the assassin wrist flicks forward. Too late. A length of flame wraps aound my left leg. Agony paralyzes me."

    "Only a second. It is enough. My feet fly out from beneath me. My back slams into a nearby crate, the wind knocked out of me."

    "{i}That damn whip. If only I could get rid of it!{/i}."

    "{i}...Wait a minute, why hadn’t it burned to ash already? How much fabric did this guy have?!?{/i}"

    "My thoughts scatter as the assassin lunges at me, whip at ready. I recognize the stance."

    pichit "Fan, now!"

    show fan neutral at companion_warp_to("left")

    "A large bark shield weaves halts materializes in time to stop this newest volley."

    assassin "Neat parlor trick! Too bad it'll be gone before long! How many stikes would it take? Three?"

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

    "The assasin is on me in moments. The flat of his dagger presses into my throat, close enough I know the simplest movement will slice my skin to ribbons."

    "I swallow, suddenly realizing just how big a risk I am taking."

    pichit "You win! I give up! He's in the school! In the faculty room!"

    assassin "How do you know that?"

    pichit "My friend. She told me!"

    "The assassin eyes narrow with suspicion. My heart races in my throad as the seconds pass.  The the pressure of the knife eases."

    assassin "Thank you...friend."

    "Then the assassin turns, disappearing neatly into the crowd."

    # pichit telepathy "He's coming your way. Get ready!"

    scene bg black with CropMove(0.5, "wipeleft")

# CHARLET POV SWITCH

    pause 0.5

    scene bg university_inside with bg_dissolve
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
