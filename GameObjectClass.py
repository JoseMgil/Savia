import pygame

class GameObject: 

    def __init__(self, image_path, x, y, width, height): 
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background): 
        background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObject):

    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        if direction > 0: 
            self.y_pos -= self.SPEED
        elif direction < 0: 
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 50: 
            self.y_pos = max_height - 50
        elif self.y_pos < 0: 
            self.y_pos = 0

    def checkColision(self, enemy_list): 

        colision = False
        for e in enemy_list: 
            if (e.x_pos == self.x_pos or e.x_pos == self.x_pos + 50)  and (e.y_pos > self.y_pos  and e.y_pos < self.y_pos + 50): 
                colision = True
            elif (e.x_pos > self.x_pos and e.x_pos < self.x_pos + 50 ) and (e.y_pos == self.y_pos or e.y_pos == self.y_pos + 50): 
                colision = True

        return colision


class EnemyCharacter(GameObject): 

    SPEED = 10

    def __init__(self, image_path, x, y, width, height): 
        super().__init__(image_path, x, y, width, height)  

    def move(self, max_width):

        if self.x_pos <= 20: 
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20: 
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED