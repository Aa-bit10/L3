import pgzrun 
from random import randint
WIDTH = 500
HEIGHT = 500
TITLE = "Shoot The Alien"
alien = Actor("alien")
message = ""
def draw():
    screen.clear()
    screen.fill("red")
    alien.draw()
    screen.draw.text(message, center = (250,10), fontsize = (30))


    
def update():
    pass
def position():
    alien.x = randint(50,WIDTH - 50)
    alien.y = randint(50,HEIGHT - 50)


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        position()
        message = "good shot!"
    else:
        message = "you missed!"


    
pgzrun.go()

    


