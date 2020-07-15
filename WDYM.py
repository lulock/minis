# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:41:59 2020

@author: Lulock
"""

## What do you Meme?

## TODOs:
## feed memes and texts as csv files and read into lists.
## Handle text overflow (calculate boundaries of meme images and split text accordingly)
## Change font style and colour
## Consider standardizing size of meme (resize) and placing black borders for text and readibilty
## Add rounds until cards run out
## Finish encapsulating main game actions into functions!! 
## Handle exceptions!!!

## Future considerations:
## Multi-player 
## Add voting system

from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO
import random

memes = ['https://pbs.twimg.com/media/BuxGM7_CMAI9uRv.jpg', 
         'https://i.redd.it/30vgf4svkxo41.jpg', 
         'https://i.ytimg.com/vi/IWwZAg9zt8U/hqdefault.jpg',
         'https://memeguy.com/photos/images/i-noticed-you-posted-a-meme-using-only-a-title-and-an-image-but-no-text-19782.jpg',
         'https://i.imgflip.com/2y9xpk.jpg',
         'https://i.kym-cdn.com/entries/icons/original/000/022/978/yNlQWRM.jpg',
         'https://s3.r29static.com/bin/entry/b3e/x,80/1621855/image.jpg',
         'https://static01.nyt.com/images/2016/08/05/us/05onfire1_xp/05onfire1_xp-videoSixteenByNineJumbo1600-v2.jpg'
         ]


deck = ["When you're so broke, you need to go to sleep for dinner.",
        "When your heart says yes but your restraining order says no.",
        "When you realise you've never been in an empty room.",
        "When someone asks you if butter is a carb.",
        "When you call your friend to go out and she fakes being sick on the phone.",
        "When you're arguing with someone and Wikipedia decides you're right.",
        "When you open a bag of chips and there's only like 5 and a half chips in there.",
        "When you have to cry but your mascara was $40."]

def meme_generator(memes):
    random.shuffle(memes)

    return memes.pop()

def deal_cards(deck, count):
    cards = []
    random.shuffle(deck)
    for i in range(count):
        cards.append(deck.pop())
    return cards, deck
 
meme = meme_generator(memes)
response = requests.get(meme)
img = Image.open(BytesIO(response.content))

#resize image
width = 500
img_w = float(img.size[0])
img_h = float(img.size[1])
wpercent = float(width/(img_w))
hsize = int((img_h)*(wpercent))
rmg = img.resize((width,hsize), Image.ANTIALIAS)
rmg.show()

number=3
hand,deck = deal_cards(deck, number)


while (True):
    for i in range(number):
        card=hand[i]
        print(f"{i+1}:{card}")
    
    choice = input("Choose a card for the displayed meme (insert corresponding number):\n")

    try:
        winning_card = hand.pop(int(choice) - 1)
        break
    except:
        print("Sorry, that's not an option. Please insert corresponding number.")

font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 16)
# updated_img = Image.new("RGBA", (200,200), (120,20,20))
draw = ImageDraw.Draw(rmg)

# dont allow for text overflow
# Set boundaries along x
# 20% to the left and 80% to the left for max floor division to return quotient 
x_min = (rmg.size[0] * 5) // 100
x_max = (rmg.size[0] * 80) // 100

lines = []
        
# If the text width is smaller than the image width, then no need to split
# just add it to the line list and return
if font.getsize(winning_card)[0]  <= x_max:
    lines.append(winning_card)
    
else:
#split
    words = winning_card.split(' ')
    i = 0
    # append every word to a line while its width is shorter than the image width
    print(words)
    while i < len(words):
        line = ''
        
        while i < len(words) and font.getsize(line + words[i])[0] <= x_max:
            
            line = line + words[i]+ " "
            i += 1

        lines.append(line)

line_height = font.getsize('hg')[1]

x = x_min
y = (rmg.size[1] * 10) //100   # 90% to the bottom

for line in lines:

    draw.text((x,y), line, fill=(209, 239, 8), font=font)
    y = y + line_height    # update y-axis for new line

print(lines)

rmg.save("a_test.png")
rmg.show()

# print("player chose:\n")
# print(f"{winning_card}")
# print("\n")