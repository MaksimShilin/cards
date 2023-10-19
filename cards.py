from random import *
from pygame import *
font.init()
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0):
        super().__init__()
        self.image_wight = image_wight
        self.image_height = image_height
        self.image = transform.scale(image.load(player_image), (image_wight, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Button():
    def __init__(self, x, y, wight, height, color):
        self.rect = Rect(x, y, wight, height)
        self.color = color
        self.x = x
        self.y = y

    def draw_rect(self, border_color=0, new_color=0):
        if border_color == 0:
            border_color = self.color
        if new_color == 0:
            new_color = self.color
        draw.rect(window, self.color, self.rect)
        draw.rect(window, border_color, self.rect, 5)
    
    def create_text(self, size):
        self.font = font.SysFont('Arial', size)

    def draw_text(self, text_color, text, xofset, yofset):
        question = self.font.render(text, True, text_color)
        window.blit(question, (self.x+xofset, self.y+yofset))


    



# bub = A
# cherv = B
# crest = C
# pic = D


x = 700
y = 550
window = display.set_mode((x, y))
display.set_caption('Дурак')
background = transform.scale(image.load('background.jpg'), (x, y))
window.blit(background, (0,0))

# jackA = GameSprite('jackA.png', 100, 100, 0, 65, 100)
# jackB = GameSprite('jackB.png', 100, 100, 0, 65, 100)
# jackC = GameSprite('jackC.png', 100, 100, 0, 65, 100)
# jackD = GameSprite('jackpic.png', 100, 100, 0, 65, 100)

# queenA = GameSprite('queenbub.png', 200, 200, 0, 65, 100)
# queenB = GameSprite('queencherv.png', 100, 100, 0, 65, 100)
# queenC = GameSprite('queencrest.png', 100, 100, 0, 65, 100)
# queenD = GameSprite('queenpic.png', 100, 100, 0, 65, 100)

# kingA = GameSprite('kingbub.png', 300, 300, 0, 65, 100)
# kingB = GameSprite('kingcherv.png', 100, 100, 0, 65, 100)
# kingC = GameSprite('kingcrest.png', 100, 100, 0, 65, 100)
# kingD = GameSprite('kingpic.png', 100, 100, 0, 65, 100)

# card = 'tooseA.png'

# tooseA = GameSprite(cards[0]+'.png', 400, 400, 0, 65, 100)
# tooseB = GameSprite('toosecherv.png', 100, 100, 0, 65, 100)
# tooseC = GameSprite('toosecrest.png', 100, 100, 0, 65, 100)
# tooseD = GameSprite('toosepic.png', 100, 100, 0, 65, 100)

start = Button(150, 300, 150, 65, (255, 255, 255))
start.draw_rect((0, 0, 0))
start.create_text(40)
start.draw_text((0, 0, 0), 'START', 30, 20)

cards = ['jackA', 'jackB', 'jackC', 'jackD', 'queenA', 'queenB', 'queenC', 'queenD', 'kingA', 'kingB', 'kingC', 'kingD', 'tooseA', 'tooseB', 'tooseC', 'tooseD']
# for i in range(6, 11):
#     cards.append(str(i)+'A')
#     cards.append(str(i)+'B')
#     cards.append(str(i)+'C')
#     cards.append(str(i)+'D')
shuffle(cards)

player1 = cards[0:6]
player2 = cards[6:12]
for i in range(12):
    cards.remove(cards[0])

best_card = cards[0]
cards.remove(cards[0])
best_card_show = GameSprite(best_card+'.png', 5, 5, 0, 65, 100)

player1_show = []
player2_show = []

x = 100
for i in range(6):
    card = GameSprite(player1[i] + '.png', x, 450, 0, 65, 100)
    player1_show.append(card)
    x += 75

x = 100
for i in range(6):
    card = GameSprite(player2[i] + '.png', x, 100, 0, 65, 100)
    player2_show.append(card)
    x += 75




font1 = font.SysFont('Arial', 35)
clock = time.Clock()
end = False
game = True
while game:
    if end:
        window.blit(background, (0,0))
        for i in range(6):
            player1_show[i].reset()
            player2_show[i].reset()
        best_card_show.reset()
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x_button, y_button = e.pos
            if start.rect.collidepoint(x_button, y_button):
                end = True
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(105)