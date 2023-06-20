label a1s2:
    "Act 1: Scene 2 - Gathering Attack"
    jump .battle_outside

label .battle_outside:
    scene bg smoke
    show phrarat neutral at character_middle

    "Assassin appears in the middle of smoke"

    scene bg university_outside
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

    # Reduce amount of science here, but just enough for a JoJo/ARMS-like experience

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

# We could break analysis in smaller chunks across the fight
# Guide's PoV => MC: "do you hear me?"
# In addition, we don't need so many small chunks: power = spirit + stone could be merged

label .analyze:
    while not (has_analyzed_assassin_cloth and \
            has_analyzed_assassin_spirit and has_analyzed_assassin_stone):
        menu:
            "Analyze cloth" if not has_analyzed_assassin_cloth:
                call .analyze_cloth from _call_a1s2_analyze_cloth
            "Analyze power" if not has_analyzed_assassin_power:
                call .analyze_power from _call_a1s2_analyze_power
            "Analyze spirit" if has_analyzed_assassin_power and not has_analyzed_assassin_spirit:
                call .analyze_spirit from _call_a1s2_analyze_spirit
            "Analyze stone" if has_analyzed_assassin_power and not has_analyzed_assassin_stone:
                call .analyze_stone from _call_a1s2_analyze_stone

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

    scene bg university_inside

    show pichit neutral at character_left
    show phrarat neutral at character_right

    "Guide says he's gonna try his best but he needs an overture."

    "Guide spawns vines (e.g. Wisteria or brambles) from surrounding plantations trying to capture Assassin"

    "Assassin chuffs and tries to burn them again but this time they resist."

    pichit "No use! My perennial plants stored too much water for your fire!"
    pichit "I think you'll burn under your own fire before my vines do"

    "Assassin tsks and tries to cut the vines with blades. He manages to cut them, but Guide spawns more, Assassin won't stand very long"

    phrarat "Pen!"

    # Should spirit *always* be visible and calling their name is only for the attack?
    # Or the spirit actually appears to "public eyes" or player eyes when doing an attack?

    show pen neutral at companion_right

    "Pen appears and creates a web of cloth, open at first then shrinks to capture all the vines at once"

    "Assassin arrives from the side of Guide"

    phrarat "Phoenix's Dance!"

    "Assassin projects Guide directly inside the building."

    jump .battle_inside

label .battle_inside:
    scene bg university_inside

    show pichit neutral at character_left

    "Guide crashes into a wall."

    show phrarat neutral at character_right

    "Assassin enters the building and locks the door with a wall of fire"

    show charlet neutral at character_middle

    "MC asks if Guide is alright via telepathy. He jokes: Yeah, see? I lured him into the building."

    hide charlet

    "Guide is hurt but stands up, he revealed bark and vines he attached around his chest and back to reduce the impact of the damage and crash."

    phrarat "nice reaction, but it won't be enough."

    "Fight continues and as fire spreads in the entrance room. In a closer space, there is more smoke, so Assassin uses scarf to protect mouth from inhaling it."

    "Guide must use fuzzy plants from pots around (or using seeds he keeps on him), like Fountain Grasses, to absorb smoke and protect him."

    scene bg university_inside

    show charlet neutral at character_left
    show raegan neutral at character_right

    # We enter second phase here but it becomes too long
    # Instead, we could shorten the previous phase
    # Alternatively cut here and keep the second phase for a 2nd encounter with the assassin (e.g. met when leaving Investor)

    "MC and Lobbyist, who previously entered the building, notice that the fire sprinkler does nothing on its own."
    "Lobbyist remembers that although automated fire sprinklers have been developed, this is still a new patented tech and many institutions don't want to spend money on it."
    "He just thought University would at least have a proper automated one. MC curses at incompetent people who set this up."

    hide raegan
    show charlet neutral at character_middle

    "MC decides to contact University acquaintances via telepathy to know more about this. Fortunately she created enough links with many of them to create an efficient network of thoughts."
    "She asks how to fix the fire sprinkler (and optionally if there is any fighter to assist them)"

    "There is no fighter available and the police seems busy on simultaneous attacks in the city, so they are on their own."

    show charlet neutral at character_left
    show raegan neutral at character_right

    "However, the control/boiler/mechanical room should be in the basement, MC got instructions how to go there. She decides to stay watching Guide while Lobbyist goes there and she gives him instructions by telepathy."

    "She gives him her fake gemstone, Lobbyist asks if she doesn't need it as she has another one (lie) and explains both stones are connect to help telepathy."
    "Lobbyist is dubious and as an expert, notices the stone is fake (player only sees dubious expression), but accepts."

    hide raegan

    "Lobbyist leaves the room while Guide and Assassin are busy fighting, heading toward the basement"

    "MC contacts Guide again via telepathy. This time, she uses analysis skills and telepathy on opponent, which is limited as no friend, but enough to predict certain moves he thinks strongly about"

    scene bg university_inside

    show pichit neutral at character_left
    show phrarat neutral at character_right

    "Back to Guide fight: Guide exchanges a few more moves and tries a stab"

    hide phrarat

    "But Assassin uses his cape (separated?) like a magician/matador, Guide stabs into nothing and gets slow down by the cape."

    show phrarat neutral at character_left
    show pichit neutral at character_right

    "Assassin reappears behind and hit Guide, …"

    "… he crashes this time into exhibition glass containing some works of art (armor, ceramics, glass containing plant species)."

    "Guide notices the exhibition plants now released from the glass cage and tries to use them to fight."
    "Expert in fauna and esp. species from Moacu, he decides to use knowledge to his advantage."

    # This raises guide's sympathy
    "Assassin also looks at destroyed works of art esp. from Moacu and shows a sad face."

    show pichit neutral at character_left
    show phrarat neutral at character_right

    # Take advantage of environment while Assassin doesn't pay attention
    "Guide picks an armor or ceramic part and jumps on the table does a jump over Assassin while attacking. Assassin blocks. Guide falls behind him."

    "Assassin tries a quick stab, but Guide blocked with armor or ceramic."

    show fan neutral at companion_left
    show pen neutral at companion_right

    "Fan looks at Pen"

    fan "Oh, so you're a Green creature too. now that I see them more closely, your patterns are very nice."

    hide pen

    "This time, fire cannot burn the armor immediately. This gives some leeway to Guide to use his power and grow a poisonous plant left behind in the broken exhibition glass to attack from behind and stop his limbs."

    "Assassin chuffs and burns the vines. To block and burn them all, he releases all his protective cloth including scarf protecting mouth."
    "Such interior plants will never have enough water to survive like the previous ones."

    "Making Guide's power useless, he takes advantage in battle. Suddenly, he slows down and feels dizzy: Guide explains the plant's poison has started affected him."
    "Burning them did no good, as he inhaled toxic particles. Besides he removed his scarf protecting mouth to go all out: he was too offensive."

    "Guide is about to deal final blow, but Assassin stands up and dodges at the last moment, and deals a counter. Guide is hurt."

    "Guide is surprised. Assassin explains that they had to manipulate many dangerous plants for dying clothes, and that most of them are toxic. Logwood/bloodroot too."
    "While not immune, this reduced the paralysis effect tremendously."

    "Exploiting Assassin's limits: Guide is burning and about to fail, but suddenly, Assassin starts burning too"

    "Guide explains each of his attacks with plants absorbed a little water from his clothes. Combined with frequent fire attacks, he reached his limit."
    "A master of fire would have controlled the amount of combustion to last longer, but he certainly is a true user of Green and so not so much used to it."

    "Guide tries to convince Assassin to stop to save himself and his creature from suffering, both using Green powers, and should focus on creation than destruction."
    "He noticed how sad he was about works of art being destroyed."

    "But Assassin, as an ultimate resort, decides to keep burning so he can at least take the Guide down. He pushes him onto the ground."
    phrarat "At least I won't go down alone!"

    # Keep it for last battle or something
    pichit "No, wait! You don't have to sacrifice!"

    # Can move earlier as soon as Pichit notices Phrarat is a clothier
    phrarat "You know, crafting alone won't save my land… our land…"

    "Finally, the fire sprinkler system activates and water falls down, extinguishing fire."

    jump a1s3
