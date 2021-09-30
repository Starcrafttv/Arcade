import numpy as np
import random
import pygame
import app
pygame.init()

HEIGHT = 800
WEIDTH = 400
FPS = 30
PLAYER_VEL = 7
PLATFORM_WEIDTH = 50
PLATFORM_HEIGHT = 5
font_score = pygame.font.SysFont('comicsans', 30)

clock = pygame.time.Clock()


class player(object):

    def __init__(self):
        self.score = 0
        self.height = 40
        self.weidth = 15
        self.x = round(WEIDTH/2)
        self.y = 300
        self.jump_height = 20
        self.counter = self.jump_height*2

    def draw(self, screen):
        Score_txt = font_score.render(
            'Score: ' + str(round(self.score/10)), 1, (0, 0, 0))
        screen.blit(Score_txt, (10, 15))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.x, self.y, self.weidth, self.height))

    def move_x(self, input):
        if input == 0:
            if self.x + PLAYER_VEL + 15 > WEIDTH:
                self.x = 0
            self.x += PLAYER_VEL
        else:
            if self.x - PLAYER_VEL < 0:
                self.x = WEIDTH-15
            self.x -= PLAYER_VEL

    def move_y(self, platforms_pos):
        if self.y < HEIGHT:
            n = 1
            if self.counter >= self.jump_height*2:
                move = self.jump_height
            elif self.counter <= self.jump_height:
                move = self.jump_height-self.counter
                n = -1
                self.counter += 1
            elif self.counter > self.jump_height:
                move = self.counter - self.jump_height
                self.counter += 1

            for _ in range(move):
                if self.counter != 0:
                    if self.y + 1*n < 250:
                        for part in platforms_pos:
                            part[1] += 1
                        self.score += 1
                    else:
                        self.y += 1*n
                for platform in platforms_pos:
                    if self.y+self.height == platform[1] and self.counter > self.jump_height:
                        if self.x >= platform[0] and self.x <= platform[0]+PLATFORM_WEIDTH:
                            self.counter = 0
                        elif self.x+self.weidth >= platform[0] and self.x+self.weidth <= platform[0]+PLATFORM_WEIDTH:
                            self.counter = 0
        return(platforms_pos)


class platforms(object):

    def __init__(self):
        self.platforms = []
        self.platforms.append([round(WEIDTH/2)-10, round(HEIGHT/4*3)+40])

    def draw(self, screen):
        for part in self.platforms:
            pygame.draw.rect(screen, (0, 0, 0),
                             (part[0], part[1], PLATFORM_WEIDTH, PLATFORM_HEIGHT))

    def get_platforms(self):
        return(self.platforms)

    def new_platform(self, y1, y2):
        x = random.randint(0, WEIDTH-PLATFORM_WEIDTH)
        y = random.randint(y1, y2)
        self.platforms.append([x, y])

    def set_platforms(self, platforms_new):
        self.platforms = platforms_new

        for part in self.platforms:
            if part[1] > HEIGHT:
                self.platforms.remove(part)
                self.new_platform(0, 90)


class projectile(object):
    def __init__(self):
        self.projectiles = []

    def draw(self, screen):
        for projectil in self.projectiles:
            pygame.draw.circle(screen, (255, 0, 0),
                               (projectil[0], projectil[1]), 5)

    def shoot(self, x, y):
        self.projectiles.append([x, y])

    def move(self):
        for projectil in self.projectiles:
            if projectil[1] - 10 > 0:
                projectil[1] -= 10
            else:
                self.projectiles.remove(projectil)


def main(started_from_arcade):
    screen = pygame.display.set_mode((WEIDTH, HEIGHT))
    pygame.display.set_caption("Doodle Jump")
    player1 = player()
    platforms1 = platforms()
    projectile1 = projectile()
    for y in range(0, HEIGHT+200, 90):
        platforms1.new_platform(y, y+90)
    shoot_cd = 0
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if not started_from_arcade:
                    pygame.quit()
                else:
                    app.main()
        if shoot_cd > 0:
            shoot_cd -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1.move_x(1)
        if keys[pygame.K_RIGHT]:
            player1.move_x(0)
        if keys[pygame.K_SPACE] and shoot_cd == 0:
            projectile1.shoot(player1.x, player1.y)
            shoot_cd = 15
        projectile1.move()
        platforms_new = player1.move_y(platforms1.get_platforms())
        platforms1.set_platforms(platforms_new)
        screen.fill((255, 255, 255))
        platforms1.draw(screen)
        projectile1.draw(screen)
        player1.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main(False)
