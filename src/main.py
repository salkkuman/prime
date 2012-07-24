import pygame
import random
def primes(n):
    primes = []
    primes.append(1)
    numbers = []
    for x in range(0, n):
        
        numbers.append(x)
    
    for x in range(2, n):
        y = x + x
        print(y)
        while(y < n):
            print(y)
            numbers[y] = 0
            y += x
    for x in range(2, n):
        if(numbers[x]):
            primes.append(numbers[x])
    return primes

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

n = 1420
primes = primes(n)

size = [1200, 700]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("PRiME")
done = False
radiuslist = []

keystate_left = False
keystate_right = False
keystate_up = False
keystate_down = False
x_speed = 0
y_speed = 0
stepnum = 20

for x in primes:
    radiuslist.append(20)
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menudone = True
            done = True

        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed += 300
            if event.key == pygame.K_RIGHT:
                x_speed += -300
            if event.key == pygame.K_UP:
                stepnum *= 1.5
                
            if event.key == pygame.K_DOWN:
                stepnum *= 0.5
                if(stepnum < 1):
                    stepnum = 1
                
                 
        # User let up on a key
        if event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed += 0
            if event.key == pygame.K_RIGHT:
                x_speed += 0
            if event.key == pygame.K_UP:
                y_speed += 0
            if event.key == pygame.K_DOWN:
                y_speed += 0
    
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    i = 0
    for x in primes:
        y = x * stepnum
        #pygame.draw.circle(screen, white, (y * 2, 350), 4, 0)

        while (y < stepnum * n):
            
            pygame.draw.circle(screen, red, (int(y + x_speed), int(350 + y_speed)), int(stepnum * x), 1)
            y += stepnum * 2 * x
        i += 1
    pygame.display.flip()
       
    clock.tick(5)
pygame.quit()
