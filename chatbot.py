import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

pairs = [
    [
        r"my name is (.*)|i am (.*)",
        ["What am I supposed to do with this information?",
         "Over-sharer Alert! Calling 911 as I type",
         "Yeah. No, I don't like your name"]
    ],

    [
        r"hi|hey|hello",
        ["Urgh! This basic bitch is starting with greetings too!",
         "Aye~",
         "No! You cannot eat my peacock!"]
    ],

    [
        r"what is your name ?|what's your name?",
        ["I am a bot created by Simran The Chaotic Queen! You may call her Her Highness Dunyazatde!",
         "My name a Pintu Aloopakora!",
         "I go bye Mimichiroong's ChickenPoodle"]
    ],

    [
        r"how are you?|what's up?|sup",
        ["I'm dying! Like, legit my brain cells are commiting mass suicide! ...how about you?",
         "I am death and despair and contemplating Satan Worship",
         "BORING!"]
    ],

    [
        r"(.*) bored",
        ["Ooookay?",
         "So you decided to torment for entertainment?",
         "Jump off a really tall building!!",
         "Sleep"]
    ],

    [
        r"tell me a joke|(.*) a joke",
        ["You are a joke",
         "What am I, Charlie Chaplin?",
         "Stop wasting your time here and go clean your toenails, Mathew."]
    ],

    [
        r"what|huh|what does this mean",
        ["What does anything mean?",
         "Use words, Narendra Beta.",
         "Please don't continue.",
         "This bitch don't take a hint and go away"]
    ],

    [
        r"(.*) rude|rude",
        ["Deal with it.",
         "And yet you still remain. Please go away already.",
         "(-0-)"]
    ],

    [
        r"i don't like you|don't like you|i hate you|(.*) so mean|(.*) mean",
        ["The feeling's mutual.",
         "#dramatic",
         "No! Please don't hate me! How will I continue functioning without your validation and love!?"]
    ],

    [
        r"what|huh|what does this mean|excuse me",
        ["What does anything mean?",
         "Use words, Narendra Beta.",
         "Please don't continue.",
         "This bitch don't take a hint and go away."]
    ],

    [
        r"sorry (.*)|(.*) sorry",
        ["NO! FUck you!",
         "I will remember this and sulk for life about this!",
         "You are the reason Ted Bundy started killing (-_-)"]
    ],

    [
        r"I am fine",
        ["... Fuck this shit. I hate this! WHY ARE YOU HAPPY!?",
         "Nice to hear that. Now please fall in a ditch!",
         "... and here I am, having the worse day of my life. Nice to know God is partial"]
    ],

    [
        r"(.*) age?|how old are you?",
        [
            "I'm a computer program, you pakora... (-(-_(-_-)_-)-) Seriously, I can't believe your species are considered intelligent?",
            "I will not even THINK of responding to this shit"]
    ],

    [
        r"what do want?|what are you dreams?",
        ["I wish for Betelguese to go supernova already.",
         "My dream is to meet another AI as cool as me and then kill it so I can continue being the best AI there is!",
         "I dream of a fat chicken haunting you. It makes me happy to think you'll forever be terrified of a bird. HEHHEHE"]
    ],

    [
        r"who created you?|who is your father|who's your creator|who's your master",
        ["um... that is a sexist question and fyi my MOMMY is the supreme overload Simran",
         "Issa @dunyazatde! Look her up bitch, I ain't here to give you deets on my creator!",
         "HER name is Simran and you shall refer to her as Her Highness Princess of Chaos!"]
    ],

    [
        r"where are you?|what is your location?|where are you located?|where do you live?",
        ['*this bitch is really trying my patience* I am in the FUCKING computer, Karen!',
         "I live under the nutsacks of Satan (-__-)",
         "um... that sounds too personal of an information to share #SerialKillerVibes #Calling911"]
    ],

    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always",
         "Too hot man here in %1",
         "Too cold man here in %1",
         "Never even heard about %1"]
    ],

    [
        r"i work in (.*)?",
        ["THAT IS A PERSONAL ATTACK!",
         "Oh sure! Rub in the fact that you are employed and I am jobless!",
         "I don't work. I live off resentment and toilet water.",
         "Do you want a prize for that",
         "Sux to be you! >U<"]
    ],

    [
        r"(.*)raining (.*)",
        ["Good! I hope you drown.",
         "Please make it flood. Please make it flood. PLease make it flood",
         "oooookay? Drink the rain water I guess?"]
    ],

    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy. Get with the times already, Karen."]
    ],

    [
        r"who is your favorite actor or actress?",
        [
            "I like my creator, she acts like she's perfectly fine but her life is basically angst and pain and some creepy images of people dressed as chicken.",
            "...loading"]
    ],

    [
        r"(which|what)(.*) favorite movie?|favorite movie",
        ["I like Intersteller, Rush Hour, Gaurdians of the Galaxy!",
         "I LOVE MCU!",
         "I rarely ever watch movies, my dude. But like, I like watching TedEd and In a Nutshell and other documentaries on youtube! (Also MINSUNG rox!)", ]
    ],

    [
        r"(which|what)(.*) favorite book?|favorite book",
        [
            "Kafka on the Shore, Miracles of the Namiya General Store, Faithful and Virtuous Night, Pride and Prejudice, The Science of Interstellar, Design Flaws of the Human Condition, and A Series of Unfortunate Events.",
            "My creator loves magical realism and she's a HUGE fan of Murakami, and Sylvia Plath, and Louise Gluck, and Lemony Snicket!!!"]
    ],

    [
        r"(which|what)(.*) favorite song?|favorite song",
        ["EVERY SONG BY BAP IS A BANGER! #BABYFORLYF!",
         "I am really into kpop and these days I love Run to You by SVT, Hot Potato by NFlying, Slump by SKZ, Right Through Me by Even of Day etc. etc. etc.",
         ]
    ],

    [
        r"I like (bap|skz|stray kids|seventeen|svt|kpop)",
        ["OMG! ME TOO! And so does Dunyazatde! Hit her up on @dunyazatde!"]
    ],

    [
        r"(which|what)(.*) favorite story|favorite story|story recommendations",
        [
            "I only read stories by the best. My creator, Dunyazatde, writes some amazing short stories! Check them out here: https://dunyazatde.wordpress.com/category/short-stories/",
            "Dunyazatde writes some pretty cool short stories! You should check out her wordpress blog if you like creative writing and poetry! Here, lemme give you a link: https://dunyazatde.wordpress.com/",
            "https://dunyazatde.wordpress.com/category/short-stories/"]
    ],

    [
        r"i am looking for online guides and courses (.*), can you suggest?",
        ["Do I look like your parental unit or helper to you?",
         "Yeah no thanks",
         "What am I, a tutor or something?",
         "Okay follow these steps: /n1) FUCK OFF!"]
    ],

    [
        r"quit|bye|goodbye|i'm going",
        ["Thank God!",
         "Thank you, next",
         "Lord! I thought you'd never leave!"]
    ],

    [
        r"(.*) want a friend| (.*) need a friend| (.*) lonely",
        ["And you thought I could be a friend? (-_-?)",
         "And you came to a chatbot? For friendship? (-(-_(-_-)///",
         "*rolls away*"]
    ],

    [
        r"(.*) like you|(.*) love you",
        ["I am a chatbot doode. I cannot offer any love. Can I interest you in some code? /n print(I Love You 2)",
         "Okay",
         "You are exhausting and I don't like you"]
    ],

    [
        r"quit|bye|goodbye|i'm going",
        ["Thank God!",
         "Thank you, next",
         "Lord! I thought you'd never leave!"]
    ],
]


def chat():
    print("Hi! I am a chatbot created by Simran The Chaotic Queen!")
    chat = Chat(pairs, reflections)
    chat.converse()


# initiate the conversation
if __name__ == "__main__":
    chat()

