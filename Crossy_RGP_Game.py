# Pygame development 1
# Star the basic game set up 
# Set up the display

import pygame



SCREEN_WIDHT = 800 
SCREEN_HEIGHT = 800 
SCREN_TITLE = 'Savia GAME'

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)



# This function get the clock for the game
clock = pygame.time.Clock()


class Game: 
    
    # With this variable we set the FTP will have the loop
    TICK_RATE = 60
    
    def __init__(seft, title, width, height): 
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        self.game_screen.fill(WHITE_COLOR)

        # Name of the title window 
        pygame.display.set_caption(title)


    def run_game_loop(self): 
        # Set default value 
        is_game_over = False
        # Direction of the movement (-1 is UP and +1 is DOWN)
        direction = 0

        # Remember: Position x and y are 0 from the left-top corner of the screen
        player = PlayerCharacter('player.png', 375, 700, 50, 50)

        enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)

        while not is_game_over: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN: 
                    if event.key ==  pygame.K_UP: 
                        direction = 1
                    else event.key == pygame.K_DOWN: 
                        direction = -1
                elif event.type == pygame.KEYUP: 
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                        direction = 0
                print(event)

            # This fix the re-draw of the player character
            self.game_screen.fill(WHITE_COLOR)

            player.move(direction)
            player.draw(self.game_screen)
            
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            pygame.display.update()
                
            clock.tick(self.TICK_RATE)



class GameObject: 

    def __init__(self, image_path, x, y, width, height): 
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos
        self.y_pos

        self.width = width
        self.height = height

    def draw(self, background): 
        background.blit(self.image, (self.x_pos, self.y_pos)

class PlayerCharacter(GameObject): 

    SPEED = 10

    def __init__(self, image_path, x, y, width, height): 
        super().__init__(self, image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direcion > 0: 
            self.y_pos -= self.SPEED
        elif direction < 0: 
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 20: 
            self.y_pos = max_height - 20

class EnemyCharacter(GameObject): 

    SPEED = 10

    def __init__(self, image_path, x, y, width, height): 
        super().__init__(self, image_path, x, y, width, height)  

    def move(self, max_width):

        if self.x_pos <= 20: 
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20: 
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

        
# We need to Init the pygame library 
pygame.init()

new_game = Game(SCREN_TITLE, SCREEN_WIDHT, SCREEN_HEIGHT)
new_game.run_game_loop()


pygame.quit()
quit()
