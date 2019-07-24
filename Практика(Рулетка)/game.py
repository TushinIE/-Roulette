import pygame, random

pygame.init()

# Const

display_width = 600
display_height = 600

clock = pygame.time.Clock()

board = pygame.image.load(r"image\Board.png")

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Roulette pygame")


# Загрузка изображений в список

arr_image_logo = [pygame.image.load(r"image\logoset\1.gif"),
                              pygame.image.load(r"image\logoset\2.gif"),
                              pygame.image.load(r"image\logoset\3.gif"),
                              pygame.image.load(r"image\logoset\4.gif"),
                              pygame.image.load(r"image\logoset\5.gif"),
                              pygame.image.load(r"image\logoset\6.gif"),
                              pygame.image.load(r"image\logoset\7.gif"),
                              pygame.image.load(r"image\logoset\8.gif"),
                              pygame.image.load(r"image\logoset\9.gif"),
                              pygame.image.load(r"image\logoset\10.gif"),
                              pygame.image.load(r"image\logoset\11.gif"),
                              pygame.image.load(r"image\logoset\12.gif"),
                              pygame.image.load(r"image\logoset\13.gif"),
                              pygame.image.load(r"image\logoset\14.gif"),
                              pygame.image.load(r"image\logoset\15.gif"),
                              pygame.image.load(r"image\logoset\16.gif"),
                              pygame.image.load(r"image\logoset\17.gif"),
                              pygame.image.load(r"image\logoset\18.gif"),
                              pygame.image.load(r"image\logoset\19.gif"),
                              pygame.image.load(r"image\logoset\20.gif"),
                              pygame.image.load(r"image\logoset\21.gif"),
                              pygame.image.load(r"image\logoset\22.gif"),
                              pygame.image.load(r"image\logoset\23.gif"),
                              pygame.image.load(r"image\logoset\24.gif"),
                              pygame.image.load(r"image\logoset\25.gif"),
                              pygame.image.load(r"image\logoset\26.gif"),
                              pygame.image.load(r"image\logoset\27.gif"),
                              pygame.image.load(r"image\logoset\28.gif"),
                              pygame.image.load(r"image\logoset\29.gif"),
                              pygame.image.load(r"image\logoset\30.gif"),
                              pygame.image.load(r"image\logoset\31.gif"),
                              pygame.image.load(r"image\logoset\32.gif"),
                              pygame.image.load(r"image\logoset\33.gif"),
                              pygame.image.load(r"image\logoset\34.gif"),
                              pygame.image.load(r"image\logoset\35.gif"),
                              pygame.image.load(r"image\logoset\36.gif"),
                              pygame.image.load(r"image\logoset\37.gif"),
                              pygame.image.load(r"image\logoset\38.gif"),
                              pygame.image.load(r"image\logoset\39.gif") ]




# Объект списка логотипов

class Logo:

    def __init__(self, x, y, width, height, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed

    def move(self):

        if self.y <= display_height - 100:
            display.blit(self.image, (self.x, self.y))
            self.y += self.speed
            return True
        else:
            self.y = display_height - 400
            return False

    def stop_arr(self):
        if self.y >= 280 and self.y < 380:
            self.speed =0
            self.y = 280
            return True
        else:
            return False

    def image_arr(self):
        n = self.image
        return n


    def return_self(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        display.blit(self.image, (self.x, self.y))




# Добавляем в список логотипы

def create_logo_arr(array1, array2, array3):

    choice = random.randrange(0,39)
    image = arr_image_logo[choice]
    array1.append(Logo(78, 200, 150, 70, image, 10))

    choice = random.randrange(0, 39)
    image = arr_image_logo[choice]
    array2.append(Logo(227, -200, 150, 70, image, 10))

    choice = random.randrange(0, 39)
    image = arr_image_logo[choice]
    array3.append(Logo(375, 0, 150, 70, image, 10))



# Выводим список логотипов на дисплей

def draw_array(array1, array2, array3):
    for logo in array1:
        check = logo.move()
        if not check:
            choice = random.randrange(0,39)
            image = arr_image_logo[choice]
            logo.return_self(78, 200, image)

    for logo in array2:
        check = logo.move()
        if not check:
            choice = random.randrange(0,39)
            image = arr_image_logo[choice]
            logo.return_self(227, 200, image)

    for logo in array3:
        check = logo.move()
        if not check:
            choice = random.randrange(0,39)
            image = arr_image_logo[choice]
            logo.return_self(375, 200, image)



# Функция которая сравнивает картинки и определяет победу или порожение

def win(array1, array2, array3):
    for logo in array1:
        image1 = logo.image_arr()

    for logo in array2:
        image2 = logo.image_arr()

    for logo in array3:
        image3 = logo.image_arr()

    if image1 == image2 and image1 == image3:
         print_text("You WIN!Exit the ESC bar", 146, 173)

    else:

        print_text("You lost.Try again SPACE", 146, 173)



# Фукция для написания текста на дисплее

def print_text(message, x, y, font_color = (255,22,0), font_type = r"fonts\font.ttf", fon_size = 30):
    font_type = pygame.font.Font(font_type, fon_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))



# Основной цикл

def game_start():

    game = True

    while game:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

         keys = pygame.key.get_pressed()
         if keys[pygame.K_SPACE]:
             game = False
             run_arr()

         display.fill((255, 255, 255))

         display.blit(board, (0,0))

         print_text("Press SPEACE to start", 175, 173)

         pygame.display.update()

         clock.tick(80)

# Логотипы начинают движение

def run_arr():
    game = True

    logo1_arr = []
    logo2_arr = []
    logo3_arr = []

    create_logo_arr(logo1_arr, logo2_arr, logo3_arr)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            stop_arr(logo1_arr, logo2_arr, logo3_arr)
        else:
            display.fill((255, 255, 255))

            draw_array(logo1_arr, logo2_arr, logo3_arr)

            display.blit(board, (0, 0))

            print_text("Press the ENTER bar", 175, 173)

        pygame.display.update()

        clock.tick(80)


# При нажатии ENTЕR столбец останавливается

def stop_arr(array1, array2, array3):
    for logo in array1:
        check1 = logo.stop_arr()
        if check1:

            for logo in array2:
                check2 = logo.stop_arr()
                if check2:

                    for logo in array3:
                        check3 = logo.stop_arr()
                        if check3:
                            return game_over(array1, array2, array3)


#Заканчиваем игру или предлогаем повторить

def game_over(array1, array2, array3):
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            stopped = True
            game_start()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit()

        display.fill((255, 255, 255))

        display.blit(board, (0, 0))

        win(array1, array2, array3)

        pygame.display.update()

        clock.tick(80)
