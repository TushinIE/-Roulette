import pygame
import game

pygame.init()

display_width= 600
display_height= 600
button_sound = pygame.mixer.Sound('music\stone.wav')
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Lucky Roulette')
icon = pygame.image.load(r'image\icon.png')
pygame.display.set_icon(icon)


def run_game():
    game = True
    button = Button(50,50)
    button.draw(20,100,'Start game')
    show_menu()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit ()
                quit()

        display.fill((255, 255, 255))
        pygame.display.update()


def print_text (message, x , y, font_color=(0,0,0), font_type = r'fonts\font.ttf',font_size = 30):
    font_type = pygame.font.Font (font_type,font_size)
    text = font_type.render(message,True,font_color)
    display.blit (text,(x,y))


class Button():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13,162,58)
        self.active_color = (23,204,58)

    def draw(self, x,y,message, actioin = None,font_size = 30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse [0] < x + self.width:
            if  y < mouse [1] < y + self.height:
                pygame.draw.rect (display, self.active_color,(x,y,self.width,self.height))

                if click [0] == 1:
                    pygame.mixer.Sound.play (button_sound)
                    pygame.time.delay (300)
                    if actioin==quit:
                        quit()
                    else:
                        actioin ()

        else:
            pygame.draw.rect (display,self.inactive_color,(x,y,self.width,self.height))

        print_text(message=message,x= x+10,y= y+10, font_size= font_size)


def show_menu ():
    menu_bckgr = pygame.image.load (r'image\menu.jpg')
    show = True
    start_button = Button (288,70)
    quit_btn = Button (120,70)

    while show:
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:

                pygame.quit ()
                quit()

        display.blit(menu_bckgr,(0,0))
        start_button.draw (85,200,'Start game', game.game_start,30)
        quit_btn.draw(85,300,'Quit',quit, 30)
        pygame.display.update ()

        pygame.time.Clock().tick(60)


run_game()
