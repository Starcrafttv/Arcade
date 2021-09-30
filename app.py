import pygame
import Snake
import Doodle_Jump
import Pong
import Tic_Tac_Toe
import two_forty_eight

pygame.init()

GAMES = ["Snake", "Pong", "Tic Tac Toe", "Doodle Jump", "2048"]
HEIGHT = len(GAMES)*65+35
WIDTH = 400
font = pygame.font.SysFont('comicsans', 50)


def draw(screen):
    screen.fill((0, 0, 0))
    for i in range(len(GAMES)):
        text = font.render(GAMES[i], 1, (255, 255, 255))
        screen.blit(text, (40, i*65+35))
    pygame.display.update()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Arcade")

    run = True
    draw(screen)
    while run:
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            pos = pygame.mouse.get_pos()
            if 0 <= pos[1] < 100:
                Snake.main(True)
            elif 100 <= pos[1] < 165:
                Pong.main(True)
            elif 165 <= pos[1] < 230:
                Tic_Tac_Toe.main(True)
            elif 230 <= pos[1] < 295:
                Doodle_Jump.main(True)
            elif 295 <= pos[1] < 360:
                two_forty_eight.main(True)


if __name__ == "__main__":
    main()
