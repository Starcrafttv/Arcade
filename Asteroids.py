import app
import pygame
import random
import math
pygame.init()

HEIGHT = 600
WEIDTH = 600
FPS = 30
clock = pygame.time.Clock()

ship_img = pygame.image.load('2019-11-29_Arcade/images/space_ship.png')
ship_img = pygame.transform.scale(ship_img, (25, 25))
ship_img = pygame.transform.rotate(ship_img, -50)
TURN_SPEED = 8
SHIP_ACCALERATION = 0.5


class space_ship(object):
    def __init__(self):
        self.x = round(WEIDTH/2)
        self.y = round(HEIGHT/2)
        self.angle = 0
        self.x_velocity = 0
        self.y_velocity = 0
        self.projectiles = []

    def draw(self, screen):
        for projectile in self.projectiles:
            pygame.draw.circle(screen, (255, 0, 0),
                               (round(projectile[0]), round(projectile[1])), 5)

        screen.blit(pygame.transform.rotate(
            ship_img, self.angle), (self.x, self.y))

    def turn(self, input_direction=1):
        self.angle += TURN_SPEED * input_direction

        if self.angle >= 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def accelerate(self, input_direction=1):
        self.x_velocity += SHIP_ACCALERATION * \
            math.sin(math.radians(self.angle))*input_direction
        self.y_velocity += SHIP_ACCALERATION * \
            math.cos(math.radians(self.angle))*input_direction

        if abs(self.x_velocity) > 10:
            tmp = self.x_velocity/abs(self.x_velocity)
            self.x_velocity = 10 * tmp
        if abs(self.y_velocity) > 10:
            tmp = self.y_velocity/abs(self.y_velocity)
            self.y_velocity = 10 * tmp

    def move(self):
        for projectile in self.projectiles:
            projectile[0] -= projectile[2]
            projectile[1] -= projectile[3]
            if projectile[0] < 0 and projectile[0] > WEIDTH:
                self.projectiles.remove(projectile)
            elif projectile[1] < 0 and projectile[1] > HEIGHT:
                self.projectiles.remove(projectile)

        self.x += self.x_velocity
        self.y += self.y_velocity

        if self.x < 0:
            self.x = WEIDTH-20
        elif self.x > WEIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT-20
        elif self.y > HEIGHT:
            self.y = 0

    def shoot(self):
        self.projectiles.append(
            [self.x+25, self.y+25, self.x_velocity+30 * math.sin(math.radians(self.angle)), self.y_velocity+30*math.cos(math.radians(self.angle))])


class asteroids(object):
    def __init__(self):
        self.asteroids = []
        # [[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5],x_vel,y_vel,hp]

    def draw(self, screen):
        for asteroid in self.asteroids:
            pygame.draw.polygon(
                screen, (255, 255, 255), (asteroid[1], asteroid[2], asteroid[3], asteroid[4], asteroid[5]))

    def new_asteroid(self):
        points = []
        plus_x = random.randint(-1, 1)*350
        plus_x = random.randint(-1, 1)*350
        for _ in range(5):
            x = random.randint(WEIDTH/2-5, WEIDTH/+5)+plus_x
            y = random.randint(HEIGHT/2-5, HEIGHT/+5)+plus_y
            points.append([x, y])

        x_vel = random.randint(-5, 5)
        y_vel = random.randint(-5, 5)
        hp = 3
        self.asteroids.append([points, x_vel, y_vel, hp])

    def move(self):
        for asteroid in self.asteroids:
            asteroid[0][0] += asteroid[5]
            asteroid[1][0] += asteroid[5]
            asteroid[2][0] += asteroid[5]
            asteroid[3][0] += asteroid[5]
            asteroid[4][0] += asteroid[5]
            asteroid[5][0] += asteroid[5]
            asteroid[0][1] += asteroid[6]
            asteroid[1][1] += asteroid[6]
            asteroid[2][1] += asteroid[6]
            asteroid[3][1] += asteroid[6]
            asteroid[4][1] += asteroid[6]
            asteroid[5][1] += asteroid[6]

            if asteroid[0][0] < -100 or asteroid[0][0] > WEIDTH+100 or asteroid[0][1] < -100 or asteroid[0][1] > HEIGHT+100:
                self.asteroids.remove(asteroid)


def main(started_from_arcade):
    screen = pygame.display.set_mode((WEIDTH, HEIGHT))
    pygame.display.set_caption("Asteroids")
    run = True

    while run:
        started = False
        lost = False
        player = space_ship()
        asteroid = asteroids()
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

        cd = 10
        asteroid.new_asteroid()
        while run and not lost:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    if not started_from_arcade:
                        pygame.quit()
                    else:
                        app.main()

            if cd > 0:
                cd -= 1

            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                print(pygame.mouse.get_pos())

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player.accelerate(-1)
            elif keys[pygame.K_DOWN]:
                player.accelerate()
            if keys[pygame.K_LEFT]:
                player.turn()
            elif keys[pygame.K_RIGHT]:
                player.turn(-1)
            if keys[pygame.K_SPACE] and cd == 0:
                player.shoot()
                cd = 10

            player.move()
            asteroid.move()

            screen.fill((0, 0, 0))
            player.draw(screen)
            pygame.display.update()


if __name__ == "__main__":
    main(False)
