label story:
$ bl = 0
$ saputangan = False
stop music
play music "sounds/sfx/Crisp_Ocean_Waves-Mike_Koenig-1486046376.mp3"
scene bg pantai malam with dissolve

n "Mom told me that children may not go to the shore at night."
n "She said there was a ghost in there that will come to scare people around."
n "Of course I don't care about it."
n "Who will believe story about ghost in the 21st century like nowadays?"
n "Every morning I saw the adults bring food to the shore to appease the ghost."
n "It's futile right? They’re wasting food for something that doesn't exist. Adults are stupid, after all."
n "That night, I sneaked out of my house carrying a flashlight and waited on the shore."
n "It was so dark there, There's no moonlight but there are stars being hung there twinkling beautifully"
n "The sea breeze blows hard, it feels a bit cold."
n "No other sound could be heard but the sound of the waves that come and go."
n "I don't see anyone around."
n "There were only fishermen in the middle of the sea who may not be able to see anyone from the shore."
n "No one else was there,"
n "Perhaps because rumours about the ghost."
n "Just when I thought about it, I felt a hand touching me from behind."
play music "sounds/bgm/Life_to_death.mp3"
n "It startled me for a moment."
n "Slowly I turned towards the hand that touched me."
stop music

play music "sounds/sfx/Crisp_Ocean_Waves-Mike_Koenig-1486046376.mp3"
show musa_senang with dissolve
m "I'm sorry you have to wait a long time here!"
hide musa_senang
show musa_senyum at Position (xpos=0.75) with move
show hamid_terkejut at Position (xpos=0.25) with move 
n "He turned out to be Musa, a boy whom I met here about a week ago"
hide hamid_terkejut at Position (xpos=0.25)
show hamid_heran at Position (xpos=0.25)
h "You really surprised me, I thought you're a ghost"

hide musa_senyum at Position (xpos=0.75)
show musa_heran at Position (xpos=0.75)
m "Alright then..I'm sorry..."
n "It reminds me our first meeting on this shore"

hide musa_heran at Position (xpos=0.75) with dissolve
hide hamid_heran at Position (xpos=0.25) with dissolve
play music "sounds/bgm/tamhe06.mp3"

scene bg pantai pagi with dissolve
show musa_heran at Position (xpos=0.75) with dissolve
show hamid_heran at Position (xpos=0.25) with dissolve
n "In that time I wonder what that boy did on the shore alone."
h "Hey ... why are you here alone?"
m "It's because no one wants to play with me..."
m "People told me that I'm strange."

hide hamid_heran at Position (xpos=0.25)
show hamid_senang at Position (xpos=0.25)
h "Not really. I think you're interesting person, Do you want to be my friend?"
hide musa_heran at Position (xpos=0.75)
show musa_terkejut at Position (xpos=0.75)
m "Eh?"
n "Since that time both of us often play together day and night, doesn't care about the ghost rumour at all."

hide hamid_senang at Position (xpos=0.25) with dissolve
hide musa_terkejut at Position (xpos=0.25) with dissolve
scene bg pantai malam with dissolve
n "This time, both of us planned to sit by the shore looking at the stars. Did you know that I'm very fond of the star?"
n "I always dream to reach it." 
n "The other kids always laugh at me, but only Musa who did not."

show musa_senyum at Position (xpos=0.75)
show hamid_senyum at Position (xpos=0.25)
m "Come on, let's go!"
n "He pulled my arm. I just obey him."
hide musa_senyum at Position (xpos=0.75) with dissolve
hide hamid_senyum at Position (xpos=0.25) with dissolve

scene bg bintang with dissolve 
n "We both sat down above white sand we can not see clearly in the darkness, illuminated only by flashlight. He pointed toward the sky."

show musa_senang at Position (xpos=0.75) with dissolve
show hamid_senang at Position (xpos=0.25) with dissolve 
m "Mid, which star do you like the most?"
h "Me? I like the one that leads to the north."
m "I see. Mine is the north west one."
n "I don't know any of those stars name, though"
n "Teacher often says that those stars above can form a certain constellation."
n "Unfortunately, let alone remembering stars and constellation, i don't even remember telescope inventor name."
h "Sa, do you know any of those stars name?"
hide musa_senang at Position (xpos=0.75)
show musa_heran at Position (xpos=0.75)
m "Mmm... I don't, but all of them are beautiful, right?"
hide hamid_senang at Position (xpos=0.25)
show hamid_bahagia at Position (xpos=0.25)
h "I guess so..."

hide musa_heran at Position (xpos=0.75)
show musa_bahagia at Position (xpos=0.75)
m "Right?"
n "That night, we told story each other, playing and laughing under a dark sky illuminated by stars, also armed with flashlight"
n "We continued our agenda by viewing the sea horizon at night. That's when we found something rather surprising."

hide musa_bahagia at Position (xpos=0.75)
hide hamid_bahagia at Position (xpos=0.25)
scene bg pantai malam with dissolve

stop music
show hamid_terkejut at Position (xpos=0.25)
show musa_heran at Position (xpos=0.75)
h "Sa, look, there's white shadow there..."

hide hamid_terkejut at Position (xpos=0.25) with dissolve
hide musa_heran at Position (xpos=0.75) with dissolve
show ghost with dissolve
play music "sounds/bgm/Life_to_death.mp3"
n "There was a white shadow..., it looks like a human silhouette but not too obvious. Face, clothes, feet or anything normal seems not visible at all. It's seems like hovering into the sea."

hide ghost with dissolve
show hamid_takut at Position (xpos=0.25)
show musa_takut at Position (xpos=0.75)
m "Don't tell me it's the ghost. Just talk slowly, Hamid..."
h "What should I do?"
menu:
    "Run away!":
        jump badend1
        
    "Hide somewhere else...":
        jump safe

label badend1:
h "Let's get away from here!"
m "Yeah, Let's go!"
play sound "sounds/sfx/one_person_running_on_gravel.mp3"
hide hamid_takut at Position (xpos=0.25)
hide musa_takut at Position (xpos=0.75)

scene bg setapak with dissolve
show hamid_takut at Position (xpos=0.25)
show musa_takut at Position (xpos=0.75)
m "D...did it follow us?"
h "I guess not."
stop music
hide hamid_takut at Position (xpos=0.25)
hide musa_takut at Position (xpos=0.75)
show hamid_heran at Position (xpos=0.25)
show musa_heran at Position (xpos=0.75)
m "Huff...that's a relief"
h "Y..yes..."
m "Man...it's so scary right?..."
hide musa_heran at Position (xpos=0.75)
show musa_takut at Position (xpos=0.75)
m "It really makes me shiver...accompany me home, please..."
n "We walked together toward Musa's house..."
n "But..."
hide hamid_heran at Position (xpos=0.25)
hide musa_takut at Position (xpos=0.75)
show ghost with dissolve
play music "sounds/bgm/Life_to_death.mp3"
n "Not long after that, we saw a very familiar figure in front of us..."
hide ghost with dissolve
show hamid_takut at Position (xpos=0.25)
show musa_takut at Position (xpos=0.75)
m "Shoot, it's following us!"
h "Nooooo!"
n "That thing was getting closer and..."
hide hamid_takut at Position (xpos=0.25)
hide musa_takut at Position (xpos=0.75)
play sound "sounds/sfx/Strong_Punch-Mike_Koenig-574430706.wav"
with vpunch
stop music
play music "sounds/sfx/giggling.mp3" #play music "sounds/sfx/ketawa-kuntilanak.mp3"
scene bg solid black
n "Bad End 1 : Don't run away!"
stop music
return

label safe:
h "Let's just hide ourselves...let our head down..."
m "Y...yes..."

hide hamid_takut at Position (xpos=0.25)
hide musa_takut at Position (xpos=0.75)
show ghost with dissolve
n "The shadow kept floating to the sea until it finally stopped" 
n "...and disappeared"
hide ghost with dissolve
stop music

play music "sounds/sfx/Crisp_Ocean_Waves-Mike_Koenig-1486046376.mp3"

show hamid_heran at Position (xpos=0.25) with dissolve
show musa_heran at Position (xpos=0.75) with dissolve
m "Thankfully,, It seems like it doesn't recognize us..."
h "Yes...that's a relief."

hide musa_heran at Position (xpos=0.75)
show musa_takut at Position (xpos=0.75)
m "I'm scared to go home alone now. Accompany me please..."

hide hamid_heran at Position (xpos=0.25) with dissolve
hide musa_takut at Position (xpos=0.75) with dissolve

scene bg setapak with dissolve
play music "sounds/bgm/Cellar.mp3"
show hamid_heran at Position (xpos=0.25) with dissolve
show musa_takut at Position (xpos=0.75) with dissolve
n "So, we both walked together to Musa house which was not far from here. The night grew darker, colder temperatures. We both hold hands while other hands were holding flashlight."
h "Do you know what is that?"
m "Never mind ... it doesn't need to be discussed again. It made me shiver you know?"
n "Throughout our trip we're getting quiet this time."
n "I also shivered a bit in that time"
n "Musa's hand was getting colder, It's seems like he's scared."
n "I kinda felt guilty making him coming here and see something He didn't want to see."
n "He even got so scared like this."

hide hamid_heran at Position (xpos=0.25) with dissolve
hide musa_takut at Position (xpos=0.75) with dissolve
stop music
scene bg rumah malam with dissolve
play music "sounds/bgm/tamhe06.mp3"
show musa_senyum at Position (xpos=0.75) with dissolve
show hamid_senyum at Position (xpos=0.25) with dissolve
n "Once we're arrived in front of his house, both of us were waving each other."
m "Let's separate here ok...I'm going to sneak through back door. Mom will scold me if she find out about our adventure haha."

hide hamid_senyum at Position (xpos=0.25)
show hamid_bahagia at Position (xpos=0.25)
h "You're such a naughty boy, eh? hahaha"
n "Musa only grinned happily"

hide musa_senyum at Position (xpos=0.75)
show musa_bahagia at Position (xpos=0.75)
m "As long as we can play together, it's ok, right? See you later..."

hide musa_bahagia at Position (xpos=0.75) with dissolve
hide hamid_bahagia at Position (xpos=0.75) with dissolve
stop music

n "I turned around and walked toward darkness."
h "Ok, what should I do now?"
menu:
    "Let's just go home...":
        jump trueend
        
    "Let's go back to the shore for a moment":
        h "Ok, let's go back there. It's seems like I had left something there"
        hide hamid_senyum with dissolve
        jump pantai

label pantai:
scene bg pantai malam with dissolve
play music "sounds/sfx/Crisp_Ocean_Waves-Mike_Koenig-1486046376.mp3"
h "What should I do here?"
menu :
    "There's something white in there...":
        jump spscene
        
    "Check place where the ghost stood just now...":
        if bl == 13:
            jump badend2
        elif bl < 13:
            jump count
    
    "Nothing here, let's just go home.":
        jump trueend

label count:
n "There's nothing here..."
$ bl += 1
if saputangan == True:
    jump pantai2
elif saputangan == False:
    jump pantai

label spscene:
show hamid_terkejut with dissolve
h "Eh? It's my handkerchief, how can it ended up here?"
hide hamid_terkejut
show hamid_heran
h "Ah whatever I'll just take it home. Glad that I've found it."
$ saputangan = True
hide hamid_heran with dissolve
jump pantai2

label pantai2:
h "What should I do again now?"
menu :        
    "Check place where the ghost stood just now...":
        if bl == 13:
            jump badend2
        elif bl < 13:
            jump count
    
    "Nothing here, let's just go home.":
        jump normalend

label badend2:
n "There's nothing here I guess..."
play music "sounds/bgm/Life_to_death.mp3"
show ghost with dissolve
h "It's still here..."
hide ghost with dissolve
show hamid_takut with dissolve
h "Nooooo!!!"
hide hamid_takut with dissolve
play sound "sounds/sfx/Strong_Punch-Mike_Koenig-574430706.wav"
with vpunch
stop music
play music "sounds/sfx/giggling.mp3" #play music "sounds/sfx/ketawa-kuntilanak.mp3"
scene bg solid black
n "Bad End 2: Curiousity killed the cat!"
stop music
return

label normalend:
play music "sounds/bgm/Cellar.mp3"
scene bg setapak with dissolve
show hamid_heran
n "Let's just go home."
n "But walking alone like this make me scared."
n "At least Musa was still with me just now, but he's home now. "
n "It's getting colder. "
n "The atmosphere was quiet as there's only the sound of crickets, blowing wind and the sound of waves from a distance.."
n "The white shadow started to flash inside my mind."
h "Doh...what should I do? I'm alone now."
n "But I shook my head."
n "Be strong, Hamid."
n "You certainly can go by myself."
n "You're father and mother beloved boy."
n "What will happen if people find out that you're scared walking alone at night like this?"
n "I even had gone to check the shore alone, after all."
n "Whatever..."
n "At home, I slowly sneaked through the window where I was out earlier."
hide hamid_heran with dissolve
stop music
scene bg kamar malam with dissolve
n "Finally I can go home safely and nothing bad happened ..."
n "Time for bed..."

n "Normal End: A Very Normal End"
return

label trueend:
play music "sounds/bgm/Cellar.mp3"
scene bg setapak with dissolve
show hamid_heran
n "Let's just go home."
n "But walking alone like this make me scared."
n "At least Musa was still with me just now, but he's home now. "
n "It's getting colder. "
n "The atmosphere was quiet as there were only the sound of crickets, blowing wind and the sound of waves from a distance.."
n "The white shadow started to flash inside my mind."
h "Doh...what should I do? I'm alone now."
n "But I shook my head."
n "Be strong, Hamid."
n "You certainly can go by myself."
n "You're father and mother beloved boy."
n "What will happen if people find out that you're scared walking alone at night like this?"
n "That ghost must be and imagination."
n "That's what I thought trying to encourage myself."

stop music
play music "sounds/bgm/Life_to_death.mp3"
n "But I felt something cold touching me again."
show hamid_takut
h "Aaaaah!!!"
stop music
show musa_heran with dissolve
play music "sounds/bgm/Cellar.mp3"
m "Mid, What's wrong with you? It's me, Musa."
n "Musa? Really? I directed my flashlight toward him."
n "It's really Musa."
n "With hand in his hip, he looked at me with surprised face."

hide hamid_takut
hide hamid_heran
show hamid_terkejut at Position (xpos=0.25) with move
show musa_heran at Position (xpos=0.75) with move
m "Why did you act as if you've seen ghost like that?"
h "N...no...It's not"
n "Seriously, I was really scared in that time."
m "You had dropped your handkerchief...."
n "He handed the handkerchief I recognized to me."
n "Did I bring a handkerchief? I do not know, maybe I did. Otherwise, how could it's being dropped in the first place?"
hide hamid_terkejut at Position (xpos=0.25)
show hamid_senyum at Position (xpos=0.25)
h "Thank you very much...."
hide musa_heran
show musa_senyum at Position (xpos=0.75)
m "Yes, you're welcome. Well then I'll go home now..."
hide musa_senyum
show musa_senang at Position (xpos=0.75)
n "I pulled his hand which is a bit cold."

hide hamid_senyum
show hamid_heran at Position (xpos=0.25)
h "You're not afraid anymore?Is it ok? Let me accompany you." 
n "To be honest I felt a bit guilty he bother himself to return the handkerchief to me."
m "It's okay...see you again..."
n "He ran toward his home. Soon he disappeared from sight." 
hide musa_senang at Position (xpos=0.75) with dissolve
hide hamid_heran with move
show hamid_heran at Position (xpos=0.5) with move
n "Fear started to crawl back into my mind"
n "I quickly ran away, ran toward my house."
n "I slowly sneaked towards the window where I was out earlier."
hide hamid_heran with dissolve
scene bg kamar malam with dissolve
n "Really, that night I was only sitting in my room, trying not to think about that white shadow anymore."
stop music

scene bg kamar pagi with dissolve
n "What a sunny morning"
n "Time to go to Musa's house."
n "I want to thank him again"
scene bg rumah pagi with dissolve
play music "sounds/bgm/tam-n03.mp3"
show hamid_senyum at Position (xpos=0.25) with dissolve
show musa_senyum at Position (xpos=0.75) with dissolve
n "He seemed happy to see me."
n "We both exchanged greetings at the door."
h "Good morning, Musa.."
m "Good morning, come on in"

scene bg ruang tamu with dissolve
hide hamid_senyum at Position (xpos=0.25) with dissolve
hide musa_senyum at Position (xpos=0.75) with dissolve
n "Finally I went in and sat there while telling story each other with him."

show hamid_senyum at Position (xpos=0.25) with dissolve
show musa_senyum at Position (xpos=0.75) with dissolve
h "Anyway, thanks again for returning my handkerchief..."
hide musa_senyum
show musa_heran at Position (xpos=0.75)
play music "sounds/bgm/Cellar.mp3"
m "Eh? Returning? Handkerchief? When?"
hide hamid_senyum
show hamid_terkejut at Position (xpos=0.25)
n "Cold sweat had spontaneously rolled from my forehead. There's something wrong."
h "You know, last night you returned my handkerchief when I was halfway home."
hide musa_heran
show musa_terkejut at Position (xpos=0.75)
m "Eh? It was so dark outside. I was scared to come out again. That's why I asked you to accompany me, right?"
n "I guess it's right."
n "Anyway, I just realized something."
n "Since when Musa dare to go out in the dark without flashlight?"
n "So who the hell did return my handkerchief?"
hide hamid_terkejut
show hamid_takut at Position (xpos=0.25)
n "I don't want to think about it anymore..."
n "True End: Just Let Unknown be Unknown"
stop music

call credits from _credits
return