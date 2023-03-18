import random
from turtle import st
from pygame.time import Clock
import pygame

heart = [[4, 0], [5, 0], [6, 0], [10, 0], [11, 0], [12, 0], [3, 1], [7, 1], [9, 1], [13, 1], [2, 2], 
[8, 2], [14, 2], [1, 3], [1, 4], [1, 5], [1, 6], [15, 3], [15, 4], [15, 5], [15, 6], [2, 7], [3, 8], 
[4, 9],[5,10],[6,11],[7,12],[8,13],[14,7],[13,8],[12,9],[11,10],[10,11],[9,12]]


def is_in_heart(x,y):
    for a in heart:
        if a[0] == x and a[1] == y:
            return True
    return False

def main():
    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    clock = pygame.time.Clock()

    running = True

    map_width = 36
    map_height = 36

    ticks = 0

  
    tile_size = 720/36
    map = []
    new_fire = []
    for y in range(map_height):
        row = []
        new_fire_row = []
        for x in range(map_width):
            green = random.randint(10, 16)
            if green < 0:
                green = 0
            row.append(green)
            new_fire_row.append(0)
        map.append(row)
        new_fire.append(new_fire_row)

    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))

        for y in range(map_height):
            for x in range(map_width):
                color = (0, 0, 0)
                if map[x][y] < 0:
                    color = (min(map[x][y]*-15,255), -map[x][y]*random.randint(3,4), 0)
                elif map[x][y] > 0:
                    color = (0,min(map[x][y]*15,255), 0)

                pygame.draw.rect(screen, color, pygame.Rect(
                    x*tile_size, y*tile_size, tile_size, tile_size))

        if ticks % 20 == 0:
            for y in range(map_height):
                for x in range(map_width):
                    if map[x][y] < 0:
                        spread = 1 
                        if x > 0 and map[x-1][y] > 0:
                            new_fire[x-1][y] += spread
                        if x+1 < map_width and map[x+1][y] > 0:
                            new_fire[x+1][y] += spread

                        if y > 0 and map[x][y-1] > 0:
                            new_fire[x][y-1] += spread
                        if y+1 < map_height and map[x][y+1] > 0:
                            new_fire[x][y+1] += spread

                        # Uncomment to get a cute heart shown after fire has spread
                        # if not is_in_heart(x,y):
                        #     if map[x][y] < 0:
                        #         map[x][y] += 1

            for y in range(map_height):
                for x in range(map_width):
                    if new_fire[x][y] > 0 and map[x][y] > 0:
                        map[x][y] = -(map[x][y]+new_fire[x][y])
                        new_fire[x][y] = 0
                    elif map[x][y] < 0:
                        map[x][y] += 1
                        

        if pygame.mouse.get_pressed(3)[0]:
            x, y = pygame.mouse.get_pos()
            if x < map_width*tile_size and y < map_height*tile_size:
                tile_x = int(x/tile_size)
                tile_y = int(y/tile_size)
                if map[tile_x][tile_y] > 0:
                    fire = -map[tile_x][tile_y]
                    map[tile_x][tile_y] = fire

        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        ticks += 1


if __name__ == '__main__':
    main()
