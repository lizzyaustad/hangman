import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((650, 640))
screen.fill((255, 255, 255))
pygame.display.set_caption('Hangman')
font = pygame.font.SysFont(None, 36)

playerPole = pygame.Rect(200, 150, 200, 10)
playerStick = pygame.Rect(200, 150, 10, 320)
playerRope = pygame.Rect(400, 150, 10, 60)

playerHead = pygame.Rect(375, 200, 60, 60)

playerBody = pygame.Rect(400, 250, 10, 130)

playerArmLeft = pygame.Rect(320, 280, 70, 10)

playerArmRight = pygame.Rect(420, 280, 70, 10)

playerUpperLegRight = pygame.Rect(420, 370, 40, 10)
playerLowerLegRight = pygame.Rect(450, 385, 10, 60)

playerUpperLegLeft = pygame.Rect(350, 370, 40, 10)
playerLowerLegLeft = pygame.Rect(350, 385, 10, 60)


main_clock = pygame.time.Clock()

lives = 6
alive = True

word1 = ['b','u','c','k','e','t']
word2 = ['c','h','o','i','r','s']
word3 = ['s','u','p','p','e','r']
word4 = ['e', 'q', 'u', 'i', 'p', 's']
word5 = ['s', 'p', 'h', 'y', 'n', 'x']
word6 = ['d', 'y', 'n', 'a', 'm', 'o']
word7 = ['p', 'u', 'z', 'z', 'l', 'e']
word8 = ['f', 'i', 'e', 'l', 'd', 's']
word9 = ['w', 'h', 'a', 'c', 'k', 'y']
word10 = ['e', 'n', 'z', 'y', 'm', 'e']
word11 = ['u', 'p', 'g', 'a', 'z', 'e']
word12 = ['p', 'i', 'c', 'k', 'u', 'p']
word13 = ['s', 'q', 'u', 'e', 'a', 'k']
word14 = ['c', 'h', 'u', 'b', 'b', 'y']
word15 = ['j', 'e', 't', 'w', 'a', 'y']
word16 = ['j', 'u', 'n', 'g', 'l', 'e']
word17 = ['q', 'u', 'a', 'r', 't', 'z']

words = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15, word16, word17]
num_correct = 0
letters_guessed = []
wrong_guesses = 0
spot = 0
correct = False
guess = ''
black = (0,0,0)
white = (255, 255, 255)
num = randint(0,16)
gameword = words[num]
check = []
keys = [K_a, K_b, K_c, K_d, K_e, K_f, K_g, K_h, K_i, K_j, K_k, K_l, K_m, K_n, K_o, K_p, K_q, K_r, K_s, K_t, K_u, K_v, K_w, K_x, K_y, K_z]
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
made_guess = False


for letter in range(0, len(gameword)):
    check.append(False)

def draw_screen():
    screen.fill((131, 183, 242))

def draw_text(display_string, font, surface, x, y, color):
    text_display = font.render(display_string, 1, color)
    text_rect = text_display.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_display, text_rect)

def draw_body_part(i):

    if i == 0:
        pygame.draw.rect(screen, white, playerHead)

    if i == 1:
        pygame.draw.rect(screen, white, playerBody)

    if i == 2:
        pygame.draw.rect(screen, white, playerArmLeft)

    if i == 3:
        pygame.draw.rect(screen, white, playerArmRight)

    if i == 4:
        pygame.draw.rect(screen, white, playerLowerLegLeft)
        pygame.draw.rect(screen, white, playerUpperLegLeft)

    if i == 5:
        pygame.draw.rect(screen, white, playerUpperLegRight)
        pygame.draw.rect(screen, white, playerLowerLegRight)

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

while True:
    num_wrong = 0
    num_correct = 0
    correct = False
    lives = 6

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if event.type == KEYDOWN:
        made_guess = True
        for i in range (0, len(keys)):
            if event.key == keys[i]:
                guess = alpha[i]
    if event.type == KEYUP:
        made_guess = False

    if made_guess == True:
        letters_guessed.append(guess)
        letters_guessed = remove_duplicates(letters_guessed)
        print(letters_guessed)

    for letter in range(0, len(gameword)):
        if (guess == gameword[letter]):
            check[letter] = True

    for letter in letters_guessed:

        correct = False
        draw_body_part(i)
        for character in gameword:
            if letter == character:
                correct = True
        if correct == False:
            num_wrong += 1
            lives-=1

    if wrong_guesses >= 6:
        alive = False
        draw_text ("Game Over!", font, screen, 100, 100, white)



    draw_screen()
    for l in range (0, len(check)):
        pygame.draw.rect(screen, white, pygame.Rect(100+(75*l), 600, 60, 10))
        if (check[l] == True):
            draw_text(gameword[l], font, screen, 120+(75*l), 570, white)
            num_correct += 1
            correct = True and made_guess == True

    for i in range (0, num_wrong):
        draw_body_part(i)

    pygame.draw.rect(screen, white, playerPole)
    pygame.draw.rect(screen, white, playerStick)
    pygame.draw.rect(screen, white, playerRope)

    if (num_correct == len(gameword)):
        draw_text("Congratulations! YOU WIN", font, screen, 200, 100, white )

    if lives <= 0:
        alive = False
        draw_text("Game Over!", font, screen, 200, 50, white)

    draw_text('Lives: %s' % (lives), font, screen, 540, 5, white)
    draw_text("Hangman", font, screen, 10, 10, white)
    pygame.display.update()
