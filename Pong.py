import random
import pygame
import app
pygame.init()


HEIGHT = 500
WEIDTH = 1000
FPS = 30
PLAYER_HEIGHT = round(HEIGHT*0.077)
PLAYER_WEIDTH = round(WEIDTH*0.00615)
PLAYER_VEL = round(HEIGHT*0.0062*(30/FPS))
BALL_X_VEL = round(WEIDTH*0.006*(30/FPS))
BALL_RADIUS = round(HEIGHT*0.0077)

font_score = pygame.font.SysFont('comicsans', 30)
clock = pygame.time.Clock()


class player(object):
    def __init__(self, name, x, y, height, weidth, left=True):
        self.name = name
        self.x = x
        self.y = y
        self.x_start = x
        self.height = height
        self.weidth = weidth
        self.vel = PLAYER_VEL
        self.score = 0
        if left:
            self.x_txt = 50
        else:
            self.x_txt = WEIDTH-200

    def down(self):
        if self.y + self.vel + self.height - 3 < HEIGHT:
            self.y += self.vel

    def up(self):
        if self.y - self.vel - 35 > 0:
            self.y -= self.vel

    def add_score(self, val=1):
        self.score += val

    def reset(self):
        self.y = (HEIGHT-35)//2
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x,
                                                   self.y, self.weidth, self.height))
        Score_txt = font_score.render(
            self.name+": " + str(self.score), 1, (255, 255, 255))
        screen.blit(Score_txt, (self.x_txt, 10))


class ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_vel = BALL_X_VEL
        # Ball starts going Left or right from start on
        start_vel = random.randint(0, 1)
        if start_vel == 1:
            self.x_vel *= -1
        self.y_vel = random.uniform(-2.5, 2.5)  # Random inital y speed
        self.radius = BALL_RADIUS
        self.counter = 0

    def move(self):
        self.counter += 0.1

        if self.y + self.y_vel - self.radius < 35 or self.y + self.y_vel + self.radius > HEIGHT:
            self.y_vel *= -1
            self.y_vel *= random.uniform(0.9, 1.1)

        self.x += int(self.x_vel)
        self.y += int(self.y_vel)

        if self.counter == 7.5:  # Ball gets faster every 10 sec
            self.x_vel *= 1.1
            self.counter = 0

    def reset(self):
        self.counter = 0
        self.x = WEIDTH//2
        self.y = (HEIGHT-40)//2
        self.x_vel = BALL_X_VEL
        start_vel = random.randint(0, 1)
        if start_vel == 1:
            self.x_vel *= -1
        self.y_vel = random.uniform(-3.0, 3.0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0),
                           (self.x, self.y), self.radius)


def main(started_from_arcade):

    screen = pygame.display.set_mode((WEIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    player1 = player("Player One", 15, (HEIGHT-35)//2,
                     PLAYER_HEIGHT, PLAYER_WEIDTH, True)
    player2 = player("Player Two", WEIDTH-25, (HEIGHT-35) //
                     2, PLAYER_HEIGHT, PLAYER_WEIDTH, False)
    play_ball = ball(WEIDTH//2, (HEIGHT-40)//2)
    run = True
    hit_cd = 0
    p1_mem = 0
    p2_mem = 0
    counter = 0
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if not started_from_arcade:
                    pygame.quit()
                else:
                    app.main()

        if hit_cd > 0:
            hit_cd -= 1
        play_ball.move()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.up()
            p1_mem = random.uniform(1, 2.5)
            counter = 7
        if keys[pygame.K_s]:
            player1.down()
            p1_mem = -random.uniform(1, 2.5)
            counter = 7
        if keys[pygame.K_UP]:
            player2.up()
            p2_mem = random.uniform(1, 2.5)
            counter = 7
        if keys[pygame.K_DOWN]:
            player2.down()
            p2_mem = -random.uniform(1, 2.5)
            counter = 7

        if play_ball.x - play_ball.radius < 5:
            play_ball.reset()
            player2.add_score()
        elif play_ball.x + play_ball.radius > WEIDTH-5:
            play_ball.reset()
            player1.add_score()

        if play_ball.x - play_ball.radius < player1.x + player1.weidth and play_ball.y > player1.y and play_ball.y < player1.y+player1.height and hit_cd == 0:
            play_ball.x_vel *= -1
            play_ball.y_vel += p1_mem
            hit_cd = 20
        elif play_ball.x > player2.x - player2.weidth and play_ball.y > player2.y and play_ball.y < player2.y+player2.height and hit_cd == 0:
            play_ball.x_vel *= -1
            play_ball.y_vel += p2_mem
            hit_cd = 20

        if counter == 0:
            p1_mem = 0
            p2_mem = 0
        elif counter > 0:
            counter -= 1

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (0, 35, WEIDTH, 2))
        pygame.draw.rect(screen, (255, 255, 255),
                         ((WEIDTH-1)//2, 35, 2, HEIGHT))
        player1.draw(screen)
        player2.draw(screen)
        play_ball.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main(False)
