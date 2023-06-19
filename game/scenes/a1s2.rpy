label a1s2:
    "Act 1: Scene 2 - Gathering Attack"

    scene bg smoke
    show phrarat neutral at character_middle

    "Assassin appears in the middle of smoke"

    show phrarat neutral at character_right
    show raegan neutral at character_left

    "Assassin detaches some cloth, burn it and throw it at Lobbyist like an arrow"

    show pichit neutral at character_middle

    "Guide protects lobbyist, deviating arrow with a blade. Guide uses single long blade."

    hide phrarat
    show charlet neutral at character_left
    show raegan neutral at character_middle
    show pichit neutral at character_right

    "Guide: go away and take refuge in building!"

    hide charlet
    hide raegan

    "MC and Lobbyist enter building"

    show pichit neutral at character_left
    show phrarat neutral at character_right

    phrarat "Don't get in my way!"

    "Assassin unsheathes two short blades (fire whip is controlled from his neck?)"
    "Guide and Assassin cross blades a few times. Assassin also uses fire whip, which Guide must dodge."

    "At some point, Assassin dodges one slash and use cloth whip to catch Guide's arm"
    "Assassin use fire to burn whip and Guide's arm at the same time. Assassin chains with a slash with the other arm."

    pichit "Fan!"

    scene battle_splash
    show fan neutral at companion_middle

    "Fan appears."

    show pichit neutral at character_left
    show fan neutral at companion_left
    show phrarat neutral at character_right

    "Guide generates bark shield to protect himself, then cuts cloth whip from arm and throws it away."
    "Notices how long it stays burning without disappearing"

    pichit "Phew, thanks!"
    fan "nice scarf!"

    phrarat "so you have a spirit and you waste your power to protect continentals? Don't you see what they are doing?!"
    pichit "and you, aren't you afraid of burning an important Moacu symbol in your rage?"

    scene assassin_cloth
    show phrarat neutral at character_middle

    "Skill reveal: Assassin says he uses a high quality cloth made of *strongwool* soaked in a mix of alum and hot water, making it fire-resistant."
    "Alum is used to dye clothes already anyway. Complains that the industry heartlessly extracts these substances less for other use or to make low-quality cloth."

    phrarat "You'll burn to ashes before my scarf"

    "They keep fighting and Guide uses the shield again, but this time Assassin understands the trick and uses fire on it"

    phrarat "You thought you could stop fire with plants?"

    "The shield is too dry and burns too fast, so Guide must cancel it to avoid burning his arm."
    "Assassin uses this opportunity for a strong hit powered by fire like a rocket. Guide blocks it but gets projected onto grass."

    scene university_building
    show charlet neutral at character_middle

    "Meanwhile, MC uses her vision skills to analyze Assassin from inside the building"


label .analyze:
    while not (has_analyzed_assassin_cloth and \
            has_analyzed_assassin_spirit and has_analyzed_assassin_stone):
        menu:
            "Analyze cloth" if not has_analyzed_assassin_cloth:
                call .analyze_cloth
            "Analyze power" if not has_analyzed_assassin_power:
                call .analyze_power
            "Analyze spirit" if has_analyzed_assassin_power and not has_analyzed_assassin_spirit:
                call .analyze_spirit
            "Analyze stone" if has_analyzed_assassin_power and not has_analyzed_assassin_stone:
                call .analyze_stone

    jump .after_analysis


label .analyze_cloth:
    "Clothes have traditional patterns of Moacu, but are written roughly."
    "Ink mixed with blood. Shows pride but also anger and hastiness. He doesn't care about his environment enough."
    "Guide could take advantage of this, or try to slow him down."
    $ has_analyzed_assassin_cloth = True
    return

label .analyze_power:
    "Normally people and esp. Moacu natives are specialized in one color. A few experts master two colors."
    "In his case, the creature (that she can see) is clearly Green and handles cloth creation and patterns."
    "So Red Fire must be produced by the stone, maybe stolen from the previous attack."
    $ has_analyzed_assassin_power = True
    return

label .analyze_spirit:
    "He seems to be mastering Fire less and attacks are quite brutal and uncontrolled. Guide could take advantage of this."
    $ has_analyzed_assassin_spirit = True
    return

label .analyze_stone:
    "Creature seems exhausted, maybe by the usage of Fire on top of its works. Maybe he can't create more cloth during fight and is limited?"
    $ has_analyzed_assassin_stone = True
    return

label .after_analysis:
    show charlet neutral at character_left
    show raegan neutral at character_right

    "In addition, Lobbyist notices a fire sprinkler inside the building. MC transmits the info and tell Guide to lure him inside the building."

    jump a1s3
