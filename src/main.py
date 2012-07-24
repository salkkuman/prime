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

n = 100
primes = primes(n)

size = [20 * n + 100, 700]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("PRiME")
done = False
radiuslist = []
for x in primes:
    radiuslist.append(20)
while done == False:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    i = 0
    for x in primes:
        y = x * 20
        #pygame.draw.circle(screen, white, (y * 2, 350), 4, 0)
        radiuslist[i] += random.randint(-1, 1)
        if(radiuslist[i] > 40):
            radiuslist[i] = 40
        if(radiuslist[i] < 1):
            radiuslist[i] = 1
        while (y < 20 * n):
            
            pygame.draw.circle(screen, red, (y, 350), (radiuslist[i] * x), 1)
            y += 40 * x
        i += 1
    pygame.display.flip()
       
    clock.tick(60)
pygame.quit()
