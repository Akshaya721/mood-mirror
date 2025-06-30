import random

emotions = {
    "tired": {
        "keywords": [
            "tired", "drained", "exhausted", "sleepy", "fatigued", "no energy", "worn out", "burnt out",
            "zombie", "dead inside", "need sleep", "done for the day", "can’t move", "mentally tired",
            "low energy", "wiped", "out of fuel", "sleep deprived", "wanna crash", "dull", "slow"
        ],
        "replies": [
            "Take a breather—you’ve been at it!", "Even tired, you’re still rocking it.", "Nap time sounds perfect—go for it.",
            "You’re allowed to slow down today.", "Rest up; you deserve a chill moment."
        ]
    },
    "sad": {
        "keywords": [
            "sad", "unhappy", "down", "gloomy", "tearful", "crying", "upset", "blue", "depressed",
            "low", "feeling empty", "hurting", "broken", "lost spark", "in pain", "emotional", "not okay",
            "hurt", "heart feels heavy", "shattered", "moody", "did not achieve", "nothing went right",
            "lost hope"
        ],
        "replies": [
            "It’s cool to feel this—let it be.", "I’m with you, even in the down moments.", "Sad vibes fade—hang tight.",
            "Your feelings are real, and that’s okay.", "Take it easy; I’ve got your back."
        ]
    },
    "angry": {
        "keywords": [
            "angry", "pissed", "irritated", "mad", "raging", "boiling", "fuming", "snapped",
            "annoyed", "short tempered", "exploding", "can't take it", "done", "infuriated", "losing it",
            "ticked off", "lost control", "triggered", "burning", "punch something", "sick of this"
        ],
        "replies": [
            "Let it out—then take a beat.", "Anger’s loud, but you’re still solid.", "Cool off when you can—you’ve got this.",
            "It’s okay to feel fired up—what’s next?", "Blow off steam; you’re human."
        ]
    },
    "anxious": {
        "keywords": [
            "anxious", "worried", "panicked", "overthinking", "stressed", "shaky",
            "can’t breathe", "tension", "paranoid", "racing thoughts", "heart pounding",
            "sweaty", "uncertain", "fearful", "restless", "shivering", "on edge", "mind spinning", "doubtful",
            "don’t know how", "unsure what to do", 
        ],
        "replies": [
            "Breathe slow—you’ve got this in you.", "Worry’s loud, but you’re stronger.", "Pause if you need—it’s all good.",
            "You’re not alone in that stress.", "One step at a time; you’re doing it."
        ]
    },
    "happy": {
        "keywords": [
            "happy", "excited", "joyful", "cheerful", "good mood", "vibing", "on top of the world",
            "smiling", "laughing", "bright day", "energetic", "feeling good", "glowing", "satisfied",  "positive", 
            "sunny", "uplifted", "achieved something", "feeling on top"
        ],
        "replies": [
            "That joy’s awesome—keep it up!", "You’re glowing—love that for you!", "Happiness looks good on you.",
            "Soak in those good vibes—you earned it.", "Keep that energy—it’s contagious!"
        ]
    },
    "frustrated": {
        "keywords": [
            "frustrated", "annoyed", "fed up", "done with this", "rejections", "hit a wall", "can’t get it",
            "stuck again", "no progress"
        ],
        "replies": [
            "That frustration’s tough—give it a break.", "You’re not failing; this is just a bump.",
            "Rejections sting, but you’re still in the game.", "Take a step back—you’ve got more to give.",
            "It’s okay to feel stuck; you’ll move forward."
        ]
    },
    "helpless": {
        "keywords": [
            "helpless", "lost", "don’t know what to do", "out of options", "no way out", "stuck in a rut",
            "can’t deal", "over my head", "confused", "no direction", "blank", "off track",
            "wandering", "nothing makes sense", "nowhere to go", "numb", "detached", "zoned out",
            "don’t feel like myself", "where am i", "what is the point", "disoriented", "disconnected",
            "not in control", "zero clarity", "mind fog", "emotionally flat"
        ],
        "replies": [
            "Feeling lost is okay—I’m here with you.", "You’re not alone; we’ll figure this out.",
            "Helplessness passes—take it one bit at a time.", "You’re stronger than this moment—lean on that.",
            "No way out yet, but you’re not done."
        ]
    },
    "bored": {
        "keywords": [
            "bored", "blah", "nothing to do", "yawn", "uninterested", "flat", "same old",
            "bored out of mind", "dragging", "meh", "zombie mode"
        ],
        "replies": [
            "Shake it up with something small—your call!", "Boredom’s a sign to try something new.",
            "Even a little change can spark things.", "You’re too cool for dull days—mix it up.",
            "Take a break, then find a fun twist."
        ]
    },
    "grumpy": {
        "keywords": [
            "grumpy", "cranky", "moody", "grouchy", "snappy", "off mood", "sour", "testy", "edgy", "grrr",
            "bad vibe", "pouty", "irky", "touchy"
        ],
        "replies": [
            "Grumpy days happen—ride it out.", "It’s okay to feel off—give yourself space.",
            "You’re still awesome, even when cranky.", "Take it easy; mood swings pass.",
            "Let that grump fade—you’ve got this."
        ]
    },
    "nervous": {
        "keywords": [
            "nervous", "jittery", "butterflies", "scared", "hesitant", "doubting", "wobbly",
            "uneasy", "twitchy", "fidgety", "spooked", "antsy"
        ],
        "replies": [
            "Take it slow—you’ve got this nerve.", "Nerves mean you care—nice!",
            "You’re stronger than those jitters.", "Breathe—it’s okay to feel this.",
            "You’ll shine through this—trust yourself."
        ]
    },
    "relaxed": {
        "keywords": [
            "relaxed", "chill" , "chillax", "calm", "peaceful", "easy", "chilled out", "laid back", "unwind",
            "cozy", "at ease", "smooth", "zen"
        ],
        "replies": [
            "Love that calm vibe—enjoy it!", "You’re rocking that chill energy.", "Peace looks good on you—stay there.",
            "Take in that relaxation—you earned it.", "Keep that zen going—it’s perfect!"
        ]
    },
    "insecure": {
        "keywords": [
            "insecure", "not enough", "self doubt", "jealous", "comparing", "ugly", "not good", "worthless",
            "dumb", "imposter", "i don’t belong", "nobody likes me", "awkward", "ashamed", "hiding", "no confidence",
            "not capable", "everyone’s better", "self hate", "overthinking myself", "not proud", "can’t accept me"
        ],
        "replies": [
            "You are enough. Just as you are.", "Comparison steals your joy—you are on your own path.",
            "The way you see yourself isn’t always the truth.", "You are worthy of love, respect, and space.",
            "Your uniqueness is your superpower."
        ]
    },
    "overwhelmed": {
        "keywords": [
            "overwhelmed", "too much", "everything at once", "stressed out", "can’t handle", "breaking down",
            "crushed", "no space", "flooded", "under pressure", "out of control", "buried", "suffocating",
            "burning out", "swamped", "chaotic", "too fast", "mind is full", "crowded head", "spiraling",
            "drowning"
        ],
        "replies": [
            "Pause. You’re allowed to step away.", "One breath at a time. You don’t need to do it all.",
            "It’s okay to break things into smaller pieces.", "You are not the chaos. You are the calm inside it.",
            "Even machines crash. You’re human—be kind to you."
        ]
    },
    "grateful": {
        "keywords": [
            "grateful", "thankful", "appreciate", "blessed", "content", "feel lucky", "heart full",
            "present", "gratitude", "abundant", "thank you", "so glad", "warm inside", "thankful heart",
            "feel good", "thank the universe", "thankful for today", "mindful", "happy tears", "holding close",
            "grateful soul"
        ],
        "replies": [
            "That warmth you feel—hold onto it.", "Gratitude multiplies joy. Let it flow.",
            "Noticing the good makes more of it appear.", "You’re growing into someone grounded and kind.",
            "Small joys build big peace. Keep seeing them."
        ]
    },
    "hopeful": {
        "keywords": [
            "hopeful", "looking forward", "can’t wait", "good things coming", "optimistic", "new start",
            "light ahead", "fresh beginning", "not giving up", "bounce back", "positive vibes", "better days",
            "faith", "trust the process", "new chapter", "feeling strong", "moving on", "letting go",
            "excited for tomorrow", "second chance", "rebuilding", "healing"
        ],
        "replies": [
            "That hope you feel? It’s powerful.", "Better days are not just possible—they’re coming.",
            "The fact that you believe is already strength.", "Hold tight to that little spark.",
            "Every ending creates space for something new."
        ]
    },
    "motivated": {
        "keywords": [
            "motivated", "pumped", "let’s go", "on fire", "ready to grind", "focused", "in the zone",
            "locked in", "determined", "energized", "driven", "goal mode", "i got this", "no stopping me",
            "watch me", "mindset shift", "in beast mode", "power up", "feel powerful", "stronger now",
            "unstoppable", "dialed in"
        ],
        "replies": [
            "Let’s gooo! The energy is real 🔥", "You’re moving like you mean it—proud of you.",
            "Fuel that fire. Today’s yours.", "You’re not just dreaming—you’re doing.",
            "Stay sharp. You’ve got momentum."
        ]
    },
    "lonely": {
        "keywords": [
            "lonely", "alone", "isolated", "no one", "by myself", "left out", "no one cares",
            "nobody there", "abandoned", "ghosted", "ignored", "emotionally alone", "cut off",
            "silent", "no friends", "i feel empty", "unseen", "i’m invisible", "miss connection",
            "feel unwanted", "not included", "shut out"
        ],
        "replies": [
            "You may feel alone, but I’m here with you right now.", "Some days feel isolating—and it’s okay to say that.",
            "Your feelings are valid. You're not invisible.", "Even the quietest pain deserves to be heard.",
            "You matter—even when no one else sees it."
        ]
    },
    "unknown": {
        "keywords": [],
        "replies": [
            "Sounds like a lot—share what you can, I’m here.", "I might not get it all, but you’re not alone.",
            "Even without a label, your feelings matter.", "That situation’s tough—I’ve got your back.",
            "You’re doing enough just by opening up."
        ]
    }
}

def get_emotion_and_reply(user_input):
    if not isinstance(user_input, str):
        return "unknown", "Please enter some text to reflect."
    
    input_lower = user_input.lower()
    emotion_scores = {}

    # Score all emotions
    for emotion, data in emotions.items():
        score = sum(1 for keyword in data["keywords"] 
                   if keyword in input_lower 
                   and not any(neg in input_lower.split(keyword, 1)[0] for neg in ["not", "no"]))
        if score > 0:  # Only store emotions with at least one match
            emotion_scores[emotion] = score

    if not emotion_scores:
        # Check for intent-based fallback
        if any(neg in input_lower for neg in ["not", "don’t", "no", "failed", "rejection"]):
            return "helpless", random.choice(emotions["helpless"]["replies"])
        elif any(pos in input_lower for pos in ["achieved", "excited", "great"]):
            return "happy", random.choice(emotions["happy"]["replies"])
        return "unknown", random.choice(emotions["unknown"]["replies"])

    # Sort by score and get top emotions (e.g., top 2)
    sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
    top_emotions = sorted_emotions[:2]  # Limit to 2 emotions for simplicity

    if len(top_emotions) == 1:
        emotion = top_emotions[0][0]
        return emotion, random.choice(emotions[emotion]["replies"])
    else:
        primary_emotion, _ = top_emotions[0]
        secondary_emotion, _ = top_emotions[1]
        
        # Define combined replies for common emotion pairs
        combined_replies = {
            ("tired", "happy"): [
                "You’re tired but happy—rest up and savor those good vibes!",
                "Even when tired, that happiness shines—take it easy and enjoy.",
                "Tired yet happy? You’ve earned a break and that joy—keep it going!",
                "Feeling tired with a happy twist—recharge while soaking in the glow.",
                "You’re rocking tired and happy—rest a bit and let that joy lift you."
            ],
            ("tired", "sad"): [
                "Tired and sad? Rest is key—give yourself space to heal.",
                "You’re worn out and down—take a break, you’re not alone.",
                "Tiredness plus sadness—ease up and let those feelings pass.",
                "Feeling tired and sad? A nap might help—you’re worth it.",
                "Tired with a sad edge—rest and know you’re still enough."
            ],
            ("angry", "anxious"): [
                "Angry and anxious? Take a breath and let it settle.",
                "You’re fired up and nervous—pause and you’ve got this.",
                "Anger with anxiety? Cool down slow—you’re stronger than it.",
                "Feeling mad and jittery? Step back, you’re doing fine.",
                "Angry plus anxious—breathe it out, you’re in control."
            ],
            ("happy", "relaxed"): [
                "Happy and relaxed? Perfect combo—keep that zen vibe!",
                "You’re happy and chill—love that easy joy!",
                "Happy with a relaxed twist—enjoy every second of it.",
                "Feeling happy and laid back? You’re owning that peace.",
                "Happy and relaxed—let that good energy flow!"
            ],
            ("frustrated", "helpless"): [
                "Frustrated and helpless? Take a step back—you’re still moving forward.",
                "Those rejections sting, and feeling lost is okay—give yourself time.",
                "Frustration with helplessness? You’re not stuck forever—hang in there.",
                "Hit a wall and unsure? You’ve got strength to push through.",
                "Frustrated yet lost? Rest a bit—you’re worth the effort."
            ],
            ("overwhelmed", "anxious"): [
                "Overwhelmed and anxious? Pause—break it down one step at a time.",
                "Feeling flooded and nervous? You’re not alone—take a breath.",
                "Overwhelm plus anxiety? Slow down—you’re doing your best.",
                "Too much and shaky? Step back—you’ve got this under control.",
                "Overwhelmed with nerves? Rest a bit—you’re stronger than this."
            ],
            ("insecure", "lonely"): [
                "Insecure and lonely? You’re enough, and I’m here with you.",
                "Feeling unsure and alone? Your worth shines through—hang on.",
                "Insecurity with loneliness? You belong—you’re not invisible.",
                "Not enough and isolated? You matter more than you know.",
                "Insecure yet lonely? Take it easy—you’re not alone in this."
            ],
            ("default", "default"): [
                "You’re feeling {} and {}—that’s a lot! Take it easy and you’re still amazing.",
                "{} with a touch of {}? You’re handling it like a champ.",
                "Mixing {} and {}—give yourself grace, you’re doing great.",
                "{} and {} together? Rest or enjoy—you’ve got this mix!",
                "{} with {} vibes—keep going, you’re enough as is."
            ]
        }

        # Get combined reply based on emotion pair, fallback to generic
        pair = (primary_emotion, secondary_emotion)
        replies = combined_replies.get(pair, combined_replies[("default", "default")])
        generic_reply = random.choice(replies).format(primary_emotion, secondary_emotion)
        return f"{primary_emotion} and {secondary_emotion}", generic_reply