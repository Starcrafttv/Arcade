import random
import numpy as np
import pygame
import app
pygame.init()

HEIGHT = 410
WIDTH = 370

font_score = pygame.font.SysFont('comicsans', 30)
font_values = pygame.font.SysFont('comicsans', 60, True)
clock = pygame.time.Clock()


class Board2048(object):

    def __init__(self):
        self.rows = 4
        self.cols = 4
        self.fill = 0
        self.score = 0
        self.board = np.array([[self.fill for i in range(self.rows)]
                               for j in range(self.cols)])

    def move(self, move_input):
        if move_input == 0:  # Right
            for i in range(4):
                for _ in range(3):
                    if self.board[i][3] == self.fill:
                        self.board[i][3] = self.board[i][2]
                        self.board[i][2] = self.board[i][1]
                        self.board[i][1] = self.board[i][0]
                        self.board[i][0] = self.fill
                for _ in range(2):
                    if self.board[i][2] == self.fill:
                        self.board[i][2] = self.board[i][1]
                        self.board[i][1] = self.board[i][0]
                        self.board[i][0] = self.fill
                if self.board[i][1] == self.fill:
                    self.board[i][1] = self.board[i][0]
                    self.board[i][0] = self.fill
                if self.board[i][3] == self.board[i][2]:
                    self.board[i][3] *= 2
                    if self.board[i][1] == self.board[i][0]:
                        self.board[i][2] = 2 * self.board[i][1]
                        self.board[i][1] = self.fill
                        self.board[i][0] = self.fill
                    else:
                        self.board[i][2] = self.board[i][1]
                        self.board[i][1] = self.board[i][0]
                        self.board[i][0] = self.fill
                elif self.board[i][2] == self.board[i][1]:
                    self.board[i][2] *= 2
                    self.board[i][1] = self.board[i][0]
                    self.board[i][0] = self.fill
                elif self.board[i][1] == self.board[i][0]:
                    self.board[i][1] *= 2
                    self.board[i][0] = self.fill
        elif move_input == 1:  # Left
            for i in range(4):
                for _ in range(3):
                    if self.board[i][0] == self.fill:
                        self.board[i][0] = self.board[i][1]
                        self.board[i][1] = self.board[i][2]
                        self.board[i][2] = self.board[i][3]
                        self.board[i][3] = self.fill
                for _ in range(2):
                    if self.board[i][1] == self.fill:
                        self.board[i][1] = self.board[i][2]
                        self.board[i][2] = self.board[i][3]
                        self.board[i][3] = self.fill
                if self.board[i][2] == self.fill:
                    self.board[i][2] = self.board[i][3]
                    self.board[i][3] = self.fill
                if self.board[i][0] == self.board[i][1]:
                    self.board[i][0] = 2 * self.board[i][0]
                    if self.board[i][2] == self.board[i][3]:
                        self.board[i][1] = 2 * self.board[i][2]
                        self.board[i][2] = self.fill
                        self.board[i][3] = self.fill
                    else:
                        self.board[i][2] = self.board[i][2]
                        self.board[i][2] = self.board[i][3]
                        self.board[i][3] = self.fill
                elif self.board[i][1] == self.board[i][2]:
                    self.board[i][1] *= 2
                    self.board[i][2] = self.board[i][3]
                    self.board[i][3] = self.fill
                elif self.board[i][2] == self.board[i][3]:
                    self.board[i][2] *= 2
                    self.board[i][3] = self.fill
        elif move_input == 2:  # Up
            for i in range(4):
                for _ in range(3):
                    if self.board[0][i] == self.fill:
                        self.board[0][i] = self.board[1][i]
                        self.board[1][i] = self.board[2][i]
                        self.board[2][i] = self.board[3][i]
                        self.board[3][i] = self.fill
                for _ in range(2):
                    if self.board[1][i] == self.fill:
                        self.board[1][i] = self.board[2][i]
                        self.board[2][i] = self.board[3][i]
                        self.board[3][i] = self.fill
                if self.board[2][i] == self.fill:
                    self.board[2][i] = self.board[3][i]
                    self.board[3][i] = self.fill
                if self.board[0][i] == self.board[1][i]:
                    self.board[0][i] *= 2
                    if self.board[2][i] == self.board[3][i]:
                        self.board[1][i] = 2 * self.board[2][i]
                        self.board[2][i] = self.fill
                        self.board[3][i] = self.fill
                    else:
                        self.board[1][i] = self.board[2][i]
                        self.board[2][i] = self.board[3][i]
                        self.board[3][i] = self.fill
                elif self.board[1][i] == self.board[2][i]:
                    self.board[1][i] *= 2
                    self.board[2][i] = self.board[3][i]
                    self.board[3][i] = self.fill
                elif self.board[2][i] == self.board[3][i]:
                    self.board[2][i] *= 2
                    self.board[3][i] = self.fill
        elif move_input == 3:  # Down
            for i in range(4):
                for _ in range(3):
                    if self.board[3][i] == self.fill:
                        self.board[3][i] = self.board[2][i]
                        self.board[2][i] = self.board[1][i]
                        self.board[1][i] = self.board[0][i]
                        self.board[0][i] = self.fill
                for _ in range(2):
                    if self.board[2][i] == self.fill:
                        self.board[2][i] = self.board[1][i]
                        self.board[1][i] = self.board[0][i]
                        self.board[0][i] = self.fill
                if self.board[1][i] == self.fill:
                    self.board[1][i] = self.board[0][i]
                    self.board[0][i] = self.fill
                if self.board[3][i] == self.board[2][i]:
                    self.board[3][i] *= 2
                    if self.board[1][i] == self.board[0][i]:
                        self.board[2][i] = 2 * self.board[1][i]
                        self.board[1][i] = self.fill
                        self.board[0][i] = self.fill
                    else:
                        self.board[2][i] = self.board[1][i]
                        self.board[1][i] = self.board[0][i]
                        self.board[0][i] = self.fill
                elif self.board[2][i] == self.board[1][i]:
                    self.board[2][i] *= 2
                    self.board[1][i] = self.board[0][i]
                    self.board[0][i] = self.fill
                elif self.board[1][i] == self.board[0][i]:
                    self.board[1][i] *= 2
                    self.board[0][i] = self.fill
        return True

    def spawn(self):
        spawned = False
        while not spawned:
            val = random.randint(1, 20)
            if val == 1:
                val = 4
            else:
                val = 2
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.cols-1)
            if self.board[x][y] == self.fill:
                self.board[x][y] = val
                spawned = True
        self.score += val

    def lost(self):
        lost = True
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == self.board[i+1][j] or self.board[i][j] == self.board[i-1][j] or self.board[i][j] == self.board[i][j+1] or self.board[i][j] == self.board[i][j-1]:
                    lost = False
                    break
        return lost

    def get_score(self):
        return self.score

    def draw(self, screen):
        screen.fill((187, 173, 160))
        Score_txt = font_score.render(
            'Score: ' + str(self.score), 1, (0, 0, 0))
        screen.blit(Score_txt, (10, 15))
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] == self.fill:
                    pygame.draw.rect(screen, (205, 193, 181),
                                     (10+(j*90), 50+(i*90), 80, 80))
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, (238, 228, 218),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_values.render(
                        str(self.board[i][j]), 1, (126, 114, 102))
                    screen.blit(val, (35+(j*90), 75+(i*90)))
                elif self.board[i][j] == 4:
                    pygame.draw.rect(screen,  (236, 224, 201),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_values.render(
                        str(self.board[i][j]), 1, (126, 114, 102))
                    screen.blit(val, (35+(j*90), 75+(i*90)))
                elif self.board[i][j] == 8:
                    pygame.draw.rect(screen,  (242, 177, 121),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_values.render(
                        str(self.board[i][j]), 1, (252, 240, 231))
                    screen.blit(val, (35+(j*90), 75+(i*90)))
                elif self.board[i][j] == 16:
                    pygame.draw.rect(screen,  (248, 148, 99),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_values.render(
                        str(self.board[i][j]), 1, (252, 240, 231))
                    screen.blit(val, (25+(j*90), 75+(i*90)))
                elif self.board[i][j] == 32:
                    pygame.draw.rect(screen,  (244, 125, 93),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_values.render(
                        str(self.board[i][j]), 1, (252, 240, 231))
                    screen.blit(val, (25+(j*90), 75+(i*90)))
                else:
                    pygame.draw.rect(screen,  (244, 125, 93),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_values.render(
                        str(self.board[i][j]), 1, (252, 240, 231))
                    screen.blit(val, (25+(j*90), 75+(i*90)))


def main(started_from_arcade):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    game_board = Board2048()
    run = True
    moved = False
    game_board.spawn()
    game_board.spawn()
    while run or not game_board.lost():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if not started_from_arcade:
                    pygame.quit()
                else:
                    app.main()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            moved = game_board.move(1)
        elif keys[pygame.K_RIGHT]:
            moved = game_board.move(0)
        elif keys[pygame.K_UP]:
            moved = game_board.move(2)
        elif keys[pygame.K_DOWN]:
            moved = game_board.move(3)
        game_board.draw(screen)
        pygame.display.update()

        if moved:
            moved = False
            pygame.time.delay(200)
            game_board.spawn()
            game_board.draw(screen)
            pygame.display.update()
            pygame.time.delay(200)

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
