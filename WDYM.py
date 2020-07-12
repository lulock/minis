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
         'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a3e0c8fd-898c-4941-b4e7-33fbe3c12def/d4xlxzj-1860ba4c-77e3-489f-b36a-52f390019d33.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYTNlMGM4ZmQtODk4Yy00OTQxLWI0ZTctMzNmYmUzYzEyZGVmXC9kNHhseHpqLTE4NjBiYTRjLTc3ZTMtNDg5Zi1iMzZhLTUyZjM5MDAxOWQzMy5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.VhAgSbCsnL6JIGfY9vGyndmC-57y59ve3cexEyTResE', 
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
img.show()

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
draw = ImageDraw.Draw(img)
draw.text((0,0), winning_card, (0,0,0), font=font)
draw = ImageDraw.Draw(img)
img.save("a_test.png")
img.show()

# print("player chose:\n")
# print(f"{winning_card}")
# print("\n")