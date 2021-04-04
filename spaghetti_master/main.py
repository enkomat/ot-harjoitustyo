import pygame
import os

width, height = 8*64, 9*64
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("spaghetti_master")
background_tile = pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti_master/assets/colored_tilemap_packed_140.bmp")
background_rect = background_tile.get_rect()
tile_pixel_size = 32
map_tiles = [pygame.image.load("/Users/mazi/Documents/ot-harjoitustyo/spaghetti_master/assets/colored_tilemap_packed_140.bmp")] * 256;

white = (255, 255, 255)

fps = 60

def load_tile_images():
    i = 0
    for filename in os.listdir("/Users/mazi/Documents/ot-harjoitustyo/spaghetti_master/assets/"):
        path = "/Users/mazi/Documents/ot-harjoitustyo/spaghetti_master/assets/" + filename
        print(path)
        if 'bmp' in path: 
            map_tiles[i] = pygame.image.load(path)
            print(map_tiles[i])
            i += 1

def draw_window():
    window.fill(white)
    x = 0
    y = 0
    for tile in map_tiles:
        current_rect = map_tiles[0].get_rect()
        current_rect.x = x
        current_rect.y = y
        window.blit(map_tiles[0], current_rect)
        x += tile_pixel_size
        if(x >= width):
            x = 0 
            y += tile_pixel_size

    pygame.display.update()

def main():
    load_tile_images()
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main() 