import numpy as np
import pygame
import app
pygame.init()

HEIGHT = 320
WEIDTH = 280
font_score = pygame.font.SysFont('comicsans', 30)
font_vals = pygame.font.SysFont('comicsans', 60)
clock = pygame.time.Clock()


class game_board_ttt(object):
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.fill = 0
        self.moves = 0
        self.score = [0, 0]
        self.board = np.array([[self.fill for i in range(self.rows)]
                               for j in range(self.cols)])

    def move(self, x, y, player):
        if self.board[x][y] == self.fill:
            self.board[x][y] = player
            self.moves += 1
            return (True)
        else:
            return(False)

    def check_for_win(self):
        won = 0
        for p in range(1, 3):
            for i in range(self.rows):
                if self.board[i][0] == p and self.board[i][1] == p and self.board[i][2] == p:
                    won = p
            for i in range(self.rows):
                if self.board[0][i] == p and self.board[1][i] == p and self.board[2][i] == p:
                    won = p
            if self.board[0][0] == p and self.board[1][1] == p and self.board[2][2] == p:
                won = p
            if self.board[0][2] == p and self.board[1][1] == p and self.board[2][0] == p:
                won = p

        if won == 1:
            self.score[0] += 1
            return (won)
        elif won == 2:
            self.score[1] += 1
            return (won)
        elif self.moves == 9:
            return(3)
        else:
            return(won)

    def draw(self, screen):
        screen.fill((187, 173, 160))
        Score_txt = font_score.render(
            'Game Score: '+str(self.score[0])+" - "+str(self.score[1]), 1, (0, 0, 0))
        screen.blit(Score_txt, (35, 15))
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] == self.fill:
                    pygame.draw.rect(screen, (205, 193, 181),
                                     (10+(j*90), 50+(i*90), 80, 80))
                elif self.board[i][j] == 1:
                    pygame.draw.rect(screen, (238, 228, 218),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_vals.render("X", 1, (126, 114, 102))
                    screen.blit(val, (35+(j*90), 75+(i*90)))
                elif self.board[i][j] == 2:
                    pygame.draw.rect(screen, (238, 228, 218),
                                     (10+(j*90), 50+(i*90), 80, 80))
                    val = font_vals.render("O", 1, (126, 114, 102))
                    screen.blit(val, (35+(j*90), 75+(i*90)))

    def reset(self):
        self.board = np.array([[self.fill for i in range(self.rows)]
                               for j in range(self.cols)])
        self.moves = 0


def main(started_from_arcade):
    screen = pygame.display.set_mode((WEIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    game_board = game_board_ttt()
    run = True
    player = 1
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if not started_from_arcade:
                    pygame.quit()
                else:
                    app.main()

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            pos = pygame.mouse.get_pos()
            pygame.time.delay(200)
            x = None
            y = None

            if pos[0] >= 10 and pos[0] <= 90:
                x = 0
            elif pos[0] >= 100 and pos[0] <= 180:
                x = 1
            elif pos[0] >= 190 and pos[0] <= 270:
                x = 2

            if pos[1] >= 60 and pos[1] <= 130:
                y = 0
            elif pos[1] >= 140 and pos[1] <= 220:
                y = 1
            elif pos[1] >= 240 and pos[1] <= 310:
                y = 2

            if x != None and y != None:
                if game_board.move(y, x, player):
                    if player == 1:
                        player = 2
                    else:
                        player = 1
        game_board.draw(screen)
        pygame.display.update()

        if game_board.check_for_win() != 0:
            pygame.time.delay(500)
            game_board.reset()


if __name__ == "__main__":
    main(False)
