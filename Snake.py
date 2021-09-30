import random
import pygame
import app
pygame.init()

HEIGHT = 600
WEIDTH = 600
SNAKE_VEL = 20
font_score = pygame.font.SysFont('comicsans', 30)
clock = pygame.time.Clock()


class snake(object):

    def __init__(self):
        self.score = 1
        n = random.randint(1, 4)
        if n == 1:
            x = 1
            y = 0
        elif n == 2:
            x = -1
            y = 0
        elif n == 3:
            y = 1
            x = 0
        elif n == 4:
            y = -1
            x = 0
        self.snake_body = []
        self.snake_body.append(
            [round((WEIDTH/SNAKE_VEL)/2)*SNAKE_VEL, round((HEIGHT/SNAKE_VEL)/2)*SNAKE_VEL, x, y])
        self.treat_x = 0
        self.treat_y = 0
        self.new_treat()

    def move(self):
        lost = False
        for part in self.snake_body:
            if part[0] + SNAKE_VEL*part[2] >= 0 and part[0] + SNAKE_VEL*part[2] < WEIDTH and part[1] + SNAKE_VEL*part[3] >= 0 and part[1] + SNAKE_VEL*part[3] < HEIGHT:
                part[0] += SNAKE_VEL*part[2]
                part[1] += SNAKE_VEL*part[3]
            else:
                lost = True
                for part in self.snake_body:
                    part[2] = 0
                    part[3] = 0
                return(lost)

        for i in range(1, len(self.snake_body)):
            if self.snake_body[0][0] == self.snake_body[i][0] and self.snake_body[0][1] == self.snake_body[i][1]:
                lost = True
                for part in self.snake_body:
                    part[2] = 0
                    part[3] = 0
                return(lost)

        for i in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[i][2] = self.snake_body[i-1][2]
            self.snake_body[i][3] = self.snake_body[i-1][3]

        if self.snake_body[0][0] == self.treat_x and self.snake_body[0][1] == self.treat_y:
            self.new_treat()
            self.snake_body.append(
                [self.snake_body[-1][0], self.snake_body[-1][1], 0, 0])

    def change(self, x, y):
        if self.snake_body[0][2] != -y or self.snake_body[0][3] != -x:
            self.snake_body[0][2] = y
            self.snake_body[0][3] = x

    def draw(self, screen):
        for part in self.snake_body:
            pygame.draw.rect(screen, (255, 255, 255),
                             (part[0], part[1], SNAKE_VEL, SNAKE_VEL))
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.treat_x, self.treat_y, SNAKE_VEL, SNAKE_VEL))
        Score_txt = font_score.render(
            'Score: ' + str(self.score), 1, (255, 255, 255))
        screen.blit(Score_txt, (10, 10))

    def new_treat(self):
        spawned = False
        while not spawned:
            spawned = True
            x = random.randint(0, round(WEIDTH/SNAKE_VEL)-1)*SNAKE_VEL
            y = random.randint(0, round(HEIGHT/SNAKE_VEL)-1)*SNAKE_VEL
            for part in self.snake_body:
                if x == part[0] or y == part[1]:
                    spawned = False
        self.treat_x = x
        self.treat_y = y
        self.score += 1


def main(started_from_arcade):
    screen = pygame.display.set_mode((WEIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    run = True
    while run:
        lost = False
        started = False
        snake_player = snake()
        snake_player.score = 1
        screen.fill((0, 0, 0))
        Score_txt = font_score.render(
            "Press Space to start the Game", 1, (255, 255, 255))
        screen.blit(Score_txt, (WEIDTH/2-150, HEIGHT/2-50))
        snake_player.draw(screen)
        pygame.display.update()
        while not started and run:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                started = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    if not started_from_arcade:
                        pygame.quit()
                    else:
                        app.main()
        while run and not lost:
            pygame.time.delay(70)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    if not started_from_arcade:
                        pygame.quit()
                    else:
                        app.main()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                snake_player.change(-1, 0)
            elif keys[pygame.K_DOWN]:
                snake_player.change(1, 0)
            elif keys[pygame.K_LEFT]:
                snake_player.change(0, -1)
            elif keys[pygame.K_RIGHT]:
                snake_player.change(0, 1)
            lost = snake_player.move()
            screen.fill((0, 0, 0))
            snake_player.draw(screen)
            pygame.display.update()
        pygame.time.delay(500)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if not started_from_arcade:
                    pygame.quit()
                else:
                    app.main()


if __name__ == "__main__":
    main(False)
