import gtts

with open("Txt Files/epic.txt", 'r') as file:
    text =  file.read()


text = """
I'm in the thick of it, everybody knows
They know me where it snows, I skied in and they froze
I don't know no nothin' 'bout no ice, I'm just cold
40-somethin' milli' subs or so, I've been told
I'm in my prime, and this ain't even final form
They knocked me down, but still, my feet, they find the floor
I went from livin' rooms straight out to sold-out tours
Life's a fight, but trust, I'm ready for the war
Whoa-oh-oh
This is how the story goes
Whoa-oh-oh
I guess this is how the story goes
I'm in the thick of it, everybody knows
They know me where it snows, I skied in and they froze
I don't know no nothin' 'bout no ice, I'm just cold
40-somethin' milli' subs or so, I've been told
From the screen to the ring, to the pen, to the king
Where's my crown? That's my bling, always drama when I ring
See, I believe that if I see it in my heart
Smash through the ceilin' 'cause I'm reachin' for the stars
Whoa-oh-oh
This is how the story goes
Whoa-oh-oh
I guess this is how the story goes
I'm in the thick of it, everybody knows
They know me where it snows, I skied in and they froze (whoo)
I don't know no nothin' 'bout no ice, I'm just cold
40-somethin' milli' subs or so, I've been told
Highway to heaven, I'm just cruisin' by my lone'
They cast me out, left me for dead, them people cold
My faith in God, mind in the sun, I'm 'bout to sow (yeah)
My life is hard, I took the wheel, I cracked the code
Yeah (whoa-oh-oh)
Ain't nobody gon' save you, man, this life will break you
(Whoa-oh-oh) in the thick of it
This is how the story goes
I'm in the thick of it, everybody knows
They know me where it snows, I skied in and they froze (whoo)
I don't know no nothin' 'bout no ice, I'm just cold
40-somethin' milli' subs or so, I've been told
I'm in the thick of it, everybody knows (everybody knows)
They know me where it snows, I skied in, and they froze (yeah)
I don't know no nothin' 'bout no ice, I'm just cold
40-somethin' milli' subs or so, I've been told (ooh-ooh)
Whoa-oh-oh (na-na-na-na-na, ay-ay)
This is how the story goes
Whoa-oh-oh (na-na)
I guess this is how the story goes

"""

tts = gtts.gTTS(text, lang='en')

tts.save('skibidi.mp3')