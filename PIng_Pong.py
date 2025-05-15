from pygame import*

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Ping Pong")

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, wight, height, color):
        self.color = color
        self.speed = speed
        self.rect = Rect(x, y, wight, height)

    def draw(self):
        draw.rect(screen, self.color, self.rect)

player1 = GameSprite(30, 200, 5, 50, 150, "red")


runing = True
while runing:

    for ev in event.get():
        if ev.type == QUIT:
            running = False

    player1.draw()      

    dislay.update

    clock.tick(FPS)
quit()



