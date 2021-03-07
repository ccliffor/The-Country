# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Agape")
define p = Character("Philautia")
define g = Character("Pragma")
define ath = Character("Athena")
define u = Character("???")

# image defs
image black = "#000"

# agape
image agape :
                "agape/agape.png"
                yalign 0.25
image agape concern = "agape/concern.png"

# phil
image phil : 
                "phil/phil.png"
                yalign 0.25
image phil concern = "phil/concern.png"
image phil excite = "phil/excite.png"

#pragma
image pragma :
                "pragma/pragma.png"
                yalign 0.25
image pragma concern = "pragma/concern.png"
image pragma smile = "pragma/smile.png"
image pragma welcome = "pragma/welcome.png"

#transforms
transform left:
                yalign 0.25
                xalign 0.0
transform right:
                yalign 0.25
                xalign 1.0
transform center:
                yalign 0.25
                xalign 0.5

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene post
  

    "Have you read the disclaimer?"

    "Thank you, please enjoy your time in The Country"   
   
label outsider:   
    
                scene black
                "Athena" " ..."
                "Athena" " ..."
                "Athena" " … where"
                "Athena" "Where am I?"
                "Athena" "Where is this?"

                scene beach
                "Athena" "*I don't remember how I got here*"
                "Athena" "*Where is this place?*"
                "Athena" "*Oh no, where is everyone, where am I*"
                "Athena" "*Why am I not in bed*"
                "Athena" "*Where is my bed*"
                "Athena" "*Is this... sand?*"
                
                show phil 
            
                "???" "Oh hello! Who are you?"
                "???" "Where did you come from?"
               
                "Athena" "I.."
                "Athena" "My name is Athena…"
                
                
                "Athena" "But I have no idea how I got here.."

                show phil concern
                "???" "Huh.."
                scene beach  
                show phil
                "???" "Would you like to come to meet Grandma? Maybe she can help you figure it out!"
                "???" "Grandma is really smart and knows a lot about Outsiders"
                
                "Athena" "Outsiders? "
                "Athena" "Wait, don’t you know it’s dangerous to just bring in strangers??"

                show phil excite
                "???" "You’re in need of help, and as Agapian I should help you!"
                "???" "Plus if you think that I'm a stranger, my name is Philautia!"
                "Philautia" "See? We're no longer strangers! We know each other by name!"
                
                "Athena" "That doesn't just magically fix everything, you know"
                "Philautia" "Sure it does! C'mon, let's go get you to Grandma to see if she can't help fix you up and get you a place to stay!"
                with dissolve
                hide phil
                
label meet:
    
                scene town
               
                show phil at left
                "Athena" "Whoa..."
                "Athena" "Where is this?"
               
                with None
                "Philautia" "This is town! You must not really know anything about us huh?"
                "Philautia" "We live in Agape, the place my sister was named after!"
                "Philautia" "Grandma says this country was an experiment for something, but you'd have to talk to her about it more, I never quite paid attention to it all"
                "Athena" "Huh, um okay"
                "Philautia" "OOO look! Grandma is right over there lets go talk to her!"

                show pragma welcome at right with dissolve
                "???" "Hello child, what brings you here? It's extremely rare that we get Outsiders here anymore. My name is Pragma, I hope to help you during your stay here."
                "Athena" "Uh hello"
                "Athena" "You and Agape both used that word, what does it mean?"
                
                show phil
                "Philautia" "An Outsider?? It means someone from the outer countries! They're typically different from us for a lot of reasons but we love them no matter who they are, right Grandma?"
                
                show pragma smile
                "Pragma" "Yes child, you've learned quite well from the family haven't you"
                
                show pragma
                "Pragma" "Philautia here has been a wonderful student learning about our culture and practices."
                "Athena" "Practices? What do you mean?"
                "Pragma" "Hopefully you'll get to learn while you're here child, but instead shall we go look over your wounds for now? It must have been a rough trek over to us."
                
                with dissolve
                hide phil
                hide pragma
                scene room:
                                size (1500, 1000)
                show pragma
                with None
                "Pragma" "There"
                "Pragma" "Your wounds should be all healed now!"
                "Pragma" "Shall we talk about how you came here?"
                "Athena" "I can't remember"
                "Athena" "Last thing I remember was sleeping, and then I woke up here, well on the beach."
                "Pragma" "Hm. I see. Well, I'll have to look into that more for you."
                "Pragma" "While you're here, do you have any questions for me?"
                "Athena" "Can you tell me more about this place?"
                "Pragma""This place is Agape."
                "Pragma" "I'm sure Phila told you a bit about it already, but this place was originally an experiment into human behavior."
                "Pragma""Agape was created in order to try and nourish a utopia by splitting of a select group of people."
                "Pragma""Although frowned upon at the time, selectivity would end up paying off. The team in charge of the creation used specific questions to try and understand a person's most internal motives to see if they were a good fit for the program"
                "Pragma" "They only selected about 20 adults and double as many children to begin the country."
                "Pragma" "There are a few of us Selected still alive, but we're almost 110 years old now. Since then, we've had quite a few generations come after us, but no new Selected will ever join."
                "Pragma""The creators of the program only thought that only their time and era was perfect for creating these altruists. They believed that anyone before and after not raised by the Selected or the Selected's kin would not be able to harbor a utopia."
                "Athena" "Wait, altruists?"
                
                show pragma smile
                "Pragma" "Ah yes, altruists are the most kind. They sacrifice all they have and love all people. They are not concerned for themselves and help others become self actualized beings."
               
                "Pragma" "Altruists consist only of love and therefore the creators decided that there could be no utopia without them. They then began to realize just how vicious others were."
                show pragma concern
                "Pragma" "When the others began to take advantage of the altruists they decided that there was nothing to save them. They were being taken care of and yet still wished harm on them."
                "Pragma" "There was no saving them..."
                "Pragma" "There was nothing we could do. But now we have a thriving community and I am thankful for the changes made. I helped raise Philautia and Agape when their mother passed away and now all I can do is share my love with the community while I can."
                "Athena" "Wow..."
                "Athena" "I never thought a place like that could exist..."
                "Pragma" "Do you have more questions for me child?"
                "Athena" "I don't think so, I just... I don't know what I'm doing"
                "Pragma" "My apologies, I hope that we can help you feel comforted in your time here."
                with dissolve
                hide pragma
                
                show agape
                with None
                "Agape" "Hello all and welcome new one, I hope you've enjoyed your time here thus far"
                "Athena" "I have, I hope to spend my time here wisely before I try finding a way back home"
                "Athena" "You guys really have it nice here..."
                "Athena" "Where I live, it's never really been nice, but at least I had decent people around"
                "Agape" "What are they like? Why only decent?"
                "Athena" "They are really smart people. They love to work hard, but we never checked in on each other. There's a lot of time we spent together where we never checked on each other"
                "Athena" "It would get really rough sometimes and there would be weeks where we never talked"
                show agape concern
                "Agape" "You call that friendship?"
                "Agape" "There's so much more to friendship than calling each other friends"
                "Agape" "Caring for one another is an integral part of being friends. Would you say that your friends care about you no matter what you offer them? Would you do anything for them?"
                "Athena" "..."
                "Athena" "No I don't think I would"
                "Agape" "Then I hope while you are here you may begin to learn to co-exist with us until you can remove yourself. While I will care for you, I care for the others as well and must take their lives into consideration."
              
                with dissolve
                hide agape
                "Athena thought to her self for awhile. Did she even want to go home? She could live here and feign care for others. They would be easy to get along with." 
                "But did she even have what it took to live here? Would jealousy consume her? These people have lived here in peace and all Athena got was an abusive childhood."
                "How could Athena live here for her life? Could she overcome her anxieties and become an embodiment of self-compassion and altruism?"
                
                show beach
                "What is altruistic love? Is it love despite all jealousy and hate?"
                "Is it the sacrifice of ease in order to show love to another?"
                "What is self-compassion? Is it to love yourself despite the things you think are bad?"
                "Is it the ability to heal yourself from your own thoughts?"
                "Wherever you are in life, skills in self-compassion and loving others becomes extremely important"
                "To become a person capable of helping others, your needs must first also be met"
                
                show town
                "Are you safe? Do you have access to your most basic needs?"
               
                show pragma at left
                "Do you have friends and family who love you? Do they embody Pragma, a long and enduring love?"
                show phil at center
                "Do you respect yourself? Do you love yourself? Do you embody Philautia, a love of self? Have you a desire to become the most you can be?"
                show agape at right
                "With these, do you help others realize their ambitions? Are you an embodiment of Agape, a truly selfless love that encompasses all?"
                
                "Would you be able to live like the Agapians? Do you care about others enough, no matter who they are and what they've done to you?"
                "To exist like this takes patience and practice. It doesn't come in one day. You must commit yourself every day to love and honor others."
                
                scene black
                "I hope that this short demo of the concept of Tabletop Therapy has helped you envision how storytelling can be both an art and act of self-realization."
                "Though completely short, A Country Called Agape has grown in my head for years, but I've never had the opprotunity to make it grow"
                "Story telling is close to my heart and I wanted to create something that affected people's thoughts and future actions."
                "I hope to continue working on this project in many other forms to create a future version of Tabletop Therapy to help others have an easier time expressing themselves."
                
                "Thank you for playing"
                



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # This ends the game.
return
