import random

emotions = {
    "tired": {
        "keywords": [
            "tired", "drained", "exhausted", "sleepy", "fatigued", "no energy", "worn out", "burnt out",
            "zombie", "dead inside", "need sleep", "done for the day", "can’t move", "mentally tired",
            "low energy", "wiped", "out of fuel", "sleep deprived", "wanna crash", "dull", "slow"
        ],
        "replies": [
            "You’re feeling tired, and that’s okay after a long day. Take a moment to rest and recharge—you’ve earned it.",
            "Exhaustion is real, but you’re still pushing through. Grab a quick nap or some water to lift your energy.",
            "You sound wiped out, which happens to everyone. Try a short break or a cozy drink to feel a bit fresher.",
            "Feeling low on energy is tough, but you’re doing great. Pause for a deep breath or a quick stretch—it helps."
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
            "You’re feeling sad, and it’s okay to let it out. Try a small comfort, like music or a walk, to ease the weight.",
            "Feeling down is heavy, but you’re not alone. Reach out to someone or do something kind for yourself today.",
            "Sadness can hit hard, and that’s normal. Give yourself a moment to breathe or journal—it’ll pass with time.",
            "Your heart’s feeling heavy, and that’s valid. Try a favorite show or a chat with a friend to lift your spirits."
        ]
    },
    "angry": {
        "keywords": [
            "angry", "pissed", "irritated", "mad", "raging", "boiling", "fuming", "snapped",
            "annoyed", "short tempered", "exploding", "can't take it", "done", "infuriated", "losing it",
            "ticked off", "lost control", "triggered", "burning", "punch something", "sick of this"
        ],
        "replies": [
            "You’re angry, and that’s okay—it shows you care. Take a deep breath or step away to cool off a bit.",
            "Feeling mad can be intense, but you’ve got this. Try a quick walk or venting to let that heat settle.",
            "Anger’s tough, but you’re tougher. Pause for a moment or listen to music to shift that energy.",
            "You sound fired up, and that’s human. Try writing it down or moving your body to ease the tension."
        ]
    },
    "anxious": {
        "keywords": [
            "anxious", "worried", "panicked", "overthinking", "stressed", "shaky",
            "can’t breathe", "tension", "paranoid", "racing thoughts", "heart pounding",
            "sweaty", "uncertain", "fearful", "restless", "shivering", "on edge", "mind spinning", "doubtful",
            "don’t know how", "unsure what to do"
        ],
        "replies": [
            "You’re feeling anxious, and that’s normal when things feel big. Take a slow breath to calm your nerves.",
            "Anxiety can be loud, but you’re stronger. Try focusing on one thing or a quick grounding exercise.",
            "You sound on edge, and that’s okay. Sip some water or count your breaths to ease into calm.",
            "Those anxious vibes are tough, but you’ve got this. Try a short meditation or a moment of stillness."
        ]
    },
    "happy": {
        "keywords": [
            "happy", "excited", "joyful", "cheerful", "good mood", "vibing", "on top of the world",
            "smiling", "laughing", "bright day", "energetic", "feeling good", "glowing", "satisfied", "positive",
            "sunny", "uplifted", "achieved something", "feeling on top"
        ],
        "replies": [
            "You’re glowing with happiness—love that! Keep spreading those good vibes wherever you go.",
            "Feeling joyful is the best—nice work! Share that energy or soak it up with something fun.",
            "You sound so happy, and it’s awesome. Celebrate with a favorite activity or tell someone about it.",
            "Your good mood is contagious—keep it up! Maybe dance it out or enjoy this moment fully."
        ]
    },
    "frustrated": {
        "keywords": [
            "frustrated", "annoyed", "fed up", "done with this", "rejections", "hit a wall", "can’t get it",
            "stuck again", "no progress"
        ],
        "replies": [
            "Frustration’s tough, but you’re still in the game. Take a quick break to reset and try again.",
            "You sound fed up, and that’s okay. Step back for a moment or talk it out to clear your head.",
            "Hitting a wall is rough, but you’re not stuck forever. Try a new angle or a short pause to regroup.",
            "Feeling frustrated is real, but you’ve got this. Take a breath or jot down what’s bugging you."
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
            "Feeling helpless is heavy, but you’re not alone. Try a small step or reach out for a chat to ground you.",
            "You sound lost, and that’s okay for now. Take a moment to breathe or do something familiar to reconnect.",
            "Not knowing what’s next is tough, but you’re enough. Try a quick journal or a walk to clear the fog.",
            "Feeling stuck is hard, but you’re still here. Pause, maybe listen to music, to find a bit of clarity."
        ]
    },
    "bored": {
        "keywords": [
            "bored", "blah", "nothing to do", "yawn", "uninterested", "flat", "same old",
            "bored out of mind", "dragging", "meh", "zombie mode"
        ],
        "replies": [
            "Boredom’s dragging you down, but you can shake it. Try something new, like a quick hobby or a fun video.",
            "You sound uninterested, and that’s okay. Pick a small activity, like doodling or music, to spark some fun.",
            "Feeling blah is no fun, but you’ve got options. Maybe explore a new playlist or take a short walk.",
            "Bored out of your mind? Mix it up! Try a quick game or something creative to break the monotony."
        ]
    },
    "grumpy": {
        "keywords": [
            "grumpy", "cranky", "moody", "grouchy", "snappy", "off mood", "sour", "testy", "edgy", "grrr",
            "bad vibe", "pouty", "irky", "touchy"
        ],
        "replies": [
            "You’re feeling grumpy, and that’s alright. Take a deep breath or grab a snack to soften the mood.",
            "Crankiness happens to everyone—don’t sweat it. Try a quick laugh, like a funny video, to shift gears.",
            "You sound a bit moody, and that’s okay. Maybe listen to music or step outside to reset your vibe.",
            "Feeling grouchy is tough, but it’ll pass. Treat yourself to something small, like a cozy drink."
        ]
    },
    "nervous": {
        "keywords": [
            "nervous", "jittery", "butterflies", "scared", "hesitant", "doubting", "wobbly",
            "uneasy", "twitchy", "fidgety", "spooked", "antsy"
        ],
        "replies": [
            "You’re feeling nervous, and that’s totally normal. Take a slow breath or shake it out to feel steadier.",
            "Those jitters are real, but you’re stronger. Try focusing on one thing or sipping water to calm down.",
            "Nervousness can be intense, but you’ve got this. Count to ten or stretch to ease those butterflies.",
            "You sound a bit antsy, and that’s okay. Ground yourself with a deep breath or a quick walk."
        ]
    },
    "relaxed": {
        "keywords": [
            "relaxed", "chill", "chillax", "calm", "peaceful", "easy", "chilled out", "laid back", "unwind",
            "cozy", "at ease", "smooth", "zen"
        ],
        "replies": [
            "You’re feeling relaxed—love that vibe! Keep soaking in the calm with a cozy moment or soft music.",
            "Chill mode looks good on you! Enjoy this peace with a favorite activity or just keep breathing easy.",
            "You sound so calm and collected—nice! Stay in that zen with a warm drink or a quiet moment.",
            "Feeling laid back is the best! Lean into it with something relaxing, like reading or a gentle stretch."
        ]
    },
    "insecure": {
        "keywords": [
            "insecure", "not enough", "self doubt", "jealous", "comparing", "ugly", "not good", "worthless",
            "dumb", "imposter", "i don’t belong", "nobody likes me", "awkward", "ashamed", "hiding", "no confidence",
            "not capable", "everyone’s better", "self hate", "overthinking myself", "not proud", "can’t accept me"
        ],
        "replies": [
            "You’re feeling insecure, but you’re enough just as you are. Try a small affirmation or a kind act for yourself.",
            "Self-doubt is tough, but it doesn’t define you. Write down one thing you like about yourself to shift focus.",
            "Feeling not good enough is hard, but you’re unique. Do something you enjoy to remind yourself of your worth.",
            "Insecurity can creep in, but you’re still amazing. Try a deep breath or a chat with a friend to feel grounded."
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
            "You’re feeling overwhelmed, and that’s a lot to carry. Take one small step or a quick break to ease the load.",
            "Everything at once is tough, but you’re not alone. Try writing a list or pausing to breathe for a moment.",
            "Feeling swamped is hard, but you’ve got this. Focus on one thing or step away for a quick reset.",
            "Overwhelm can feel chaotic, but you’re stronger. Take a deep breath or do something small to find calm."
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
            "You’re feeling grateful, and that’s beautiful! Keep noticing the good—maybe share it with someone today.",
            "That thankful vibe is so warm—love it! Reflect on one thing you’re grateful for to keep it growing.",
            "Your gratitude shines bright—keep it up! Try writing it down or telling someone to spread the joy.",
            "Feeling thankful is powerful—nice work! Lean into it with a moment of mindfulness or a kind act."
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
            "You’re feeling hopeful, and that’s a spark to hold onto! Keep looking forward with a small step today.",
            "That optimism is powerful—love it! Dream about what’s next or jot down a goal to keep it alive.",
            "You sound excited for what’s coming—awesome! Stay focused on that light with a positive action.",
            "Hopeful vibes are strong in you! Keep it going with a little plan or a moment to visualize the future."
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
            "You’re so motivated—let’s go! Channel that energy into a goal or a quick win to keep it rolling.",
            "That driven vibe is fire—keep it up! Tackle one task or make a plan to ride this momentum.",
            "You sound unstoppable—love that! Take a small step toward your goal to stay in the zone.",
            "Feeling pumped is awesome—own it! Try focusing on one thing or a quick workout to fuel that drive."
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
            "You’re feeling lonely, and that’s tough but valid. Reach out to someone or do something kind for yourself.",
            "Feeling alone is heavy, but you’re not invisible. Try a small connection, like a text or a favorite hobby.",
            "Loneliness can sting, but you’re still enough. Listen to music or reach out to feel a bit more connected.",
            "You sound isolated, and that’s okay to feel. Try a cozy activity or a quick chat to lift your spirits."
        ]
    },
    "unknown": {
        "keywords": [],
        "replies": [
            "You’re feeling something tough to name, and that’s okay. Share a bit more or take a moment to breathe.",
            "Not sure what’s up, but I’m here for you. Try a small step, like journaling, to sort it out.",
            "Your feelings are valid, even if unclear. Pause for a deep breath or do something you enjoy.",
            "Sounds like a lot—don’t worry about labeling it. Try a quick walk or talking it out to find some ease."
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
                "You’re tired but happy—such a cool mix! Take a quick rest to keep those good vibes flowing.",
                "Feeling drained yet joyful is awesome! Grab a cozy break to recharge and enjoy the moment.",
                "Tired with a happy spark—love it! Pause for a breath or a snack to boost that energy.",
                "You sound exhausted but uplifted—nice! Try a short nap to keep shining bright."
            ],
            ("tired", "sad"): [
                "Tired and sad is a heavy combo, but you’re strong. Rest up or listen to music to ease the load.",
                "You’re worn out and down—totally valid. Try a cozy drink or a quick cry to feel a bit lighter.",
                "Feeling tired and sad is tough, but you’ve got this. Take a break or reach out to someone close.",
                "Exhausted and blue? It’s okay—pause for a moment or do something gentle to lift your mood."
            ],
            ("angry", "anxious"): [
                "Angry and anxious is intense, but you’re in control. Take a deep breath or walk to calm things down.",
                "You’re mad and nervous—tough mix! Try venting or a quick stretch to release that tension.",
                "Anger plus anxiety is a lot, but you’re stronger. Pause for a moment or listen to calming music.",
                "Feeling fired up and jittery? It’s okay—try a slow breath or a short break to find your balance."
            ],
            ("happy", "relaxed"): [
                "Happy and relaxed—what a perfect vibe! Keep soaking it in with a fun activity or chill moment.",
                "You’re joyful and chill—love that! Enjoy this peace with a cozy drink or favorite song.",
                "Feeling happy and laid back is awesome! Stay in that zone with a walk or something you love.",
                "Happy with a relaxed edge—nice! Keep the good vibes going with a moment of mindfulness."
            ],
            ("frustrated", "helpless"): [
                "Frustrated and helpless is rough, but you’re not stuck. Take a break or try a new approach to move forward.",
                "Feeling fed up and lost is hard, but you’re enough. Step back or talk it out to find some clarity.",
                "Frustration and helplessness are tough, but you’ve got this. Try a small step or a quick reset.",
                "You sound stuck and frustrated—okay for now. Pause or jot down your thoughts to ease the tension."
            ],
            ("overwhelmed", "anxious"): [
                "Overwhelmed and anxious is a lot, but you’re strong. Take one deep breath or focus on a single task.",
                "Feeling swamped and nervous is tough, but you’ve got this. Try a quick walk or a moment to pause.",
                "Overwhelm plus anxiety is heavy, but you’re not alone. Write a list or take a break to calm down.",
                "You sound flooded and jittery—okay to feel this. Try a slow breath or something small to ground you."
            ],
            ("insecure", "lonely"): [
                "Insecure and lonely is hard, but you’re enough. Reach out to someone or do a kind act for yourself.",
                "Feeling unsure and alone is tough, but you’re not invisible. Try a small connection or a favorite hobby.",
                "Insecurity and loneliness sting, but you matter. Listen to music or text a friend to feel grounded.",
                "You sound isolated and doubtful—valid feelings. Try a cozy activity or a quick chat to lift your mood."
            ],
            ("default", "default"): [
                "You’re feeling {} and {}—that’s a lot! Take a breath or try something small to balance it out.",
                "{} with a touch of {} is intense, but you’re handling it. Pause or do something you enjoy to reset.",
                "Mixing {} and {} is tough, but you’ve got this. Try a quick walk or a moment to ground yourself.",
                "{} and {} together? You’re strong—take a break or lean into something that feels good."
            ]
        }

        # Get combined reply based on emotion pair, fallback to generic
        pair = (primary_emotion, secondary_emotion)
        replies = combined_replies.get(pair, combined_replies[("default", "default")])
        generic_reply = random.choice(replies).format(primary_emotion, secondary_emotion)
        return f"{primary_emotion} and {secondary_emotion}", generic_reply