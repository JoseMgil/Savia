import pygame
from GameObjectClass import * 

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# This function get the clock for the game
clock = pygame.time.Clock()


class Game: 
    
    # With this variable we set the FTP will have the loop
    TICK_RATE = 60
    # 1 - easiest - 3 - hardest
    DIFFICULTY = 3

    
    
    def __init__(self, title, width, height): 
        self.title = title
        self.width = width
        self.height = height

        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.game_screen.fill(WHITE_COLOR)

        # Name of the title window 
        pygame.display.set_caption(title)
        pygame.font.init()
        self.screen_font = pygame.font.SysFont('Courier New', 30)

    def run_game(self): 

        self.run_start_screen()

        self.run_game_loop()

    def run_game_over_screen(self, game_result): 

        surface_text_title = ""
        if game_result: 
            surface_text_title = self.screen_font.render('YOU WIN!! - Press any key to quit', False, WHITE_COLOR)
        else: 
            surface_text_title = self.screen_font.render('GAME OVER - Press any key to quit', False, WHITE_COLOR)

        press = False
        while not press: 
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN: 
                    press = True
            self.game_screen.fill(BLACK_COLOR)
            self.game_screen.blit(surface_text_title, (100, 300))
            # Dont forget to update the display after printing something
            pygame.display.update()
                
            clock.tick(self.TICK_RATE)

    def run_start_screen(self): 

        surface_text_title = self.screen_font.render('Savia Game - Press Enter', False, WHITE_COLOR)

        press = False
        while not press: 
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: 
                        press = True
            self.game_screen.fill(BLACK_COLOR)
            self.game_screen.blit(surface_text_title, (100, 300))
            # Dont forget to update the display after printing something
            pygame.display.update()
                
            clock.tick(self.TICK_RATE)

            
    def run_game_loop(self): 
        # Set default value 
        is_game_over = False
        # Direction of the movement (-1 is UP and +1 is DOWN)
        direction = 0

        # Remember: Position x and y are 0 from the left-top corner of the screen
        #player = PlayerCharacter("player.png", 375, 700, 50, 50)
        player = PlayerCharacter("cupcake.jpg", 375, 700, 50, 50)
        
        treasure = GameObject("treasure.jpg", 375, 0, 50, 50)

        enemies = []
        if self.DIFFICULTY >= 3: 
            enemies.append(EnemyCharacter("ghost.png", 20, 400, 50, 50))
            enemies.append(EnemyCharacter("ghost.png", 700, 200, 50, 50))
            enemies.append(EnemyCharacter("ghost.png", 20, 100, 50, 50))
        elif self.DIFFICULTY == 2: 
            enemies.append(EnemyCharacter("ghost.png", 700, 200, 50, 50))
            enemies.append(EnemyCharacter("ghost.png", 20, 100, 50, 50))
        else:
            enemies.append(EnemyCharacter("ghost.png", 20, 400, 50, 50))


        while not is_game_over: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN: 
                    if event.key ==  pygame.K_UP: 
                        direction = 1
                    elif event.key == pygame.K_DOWN: 
                        direction = -1
                elif event.type == pygame.KEYUP: 
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                        direction = 0
                print(event)

            # This fix the re-draw of the player character
            self.game_screen.fill(WHITE_COLOR)

            treasure.draw(self.game_screen)
            player.move(direction, self.height)
            player.draw(self.game_screen)

            for e in enemies: 
                e.move(self.width)
                e.draw(self.game_screen)

            
            pygame.display.update()
                    
            clock.tick(self.TICK_RATE)

            game_result = True
            # end-game conditions
            if player.y_pos == treasure.y_pos + 50: 
                is_game_over = True
                game_result = True
            elif player.checkColision(enemies):
                is_game_over = True
                game_result = False


        self.run_game_over_screen(game_result)

