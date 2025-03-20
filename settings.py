import pygame 

 #game size 
columns = 10 
rows = 20 
cell_size = 40
game_width, game_height = columns * cell_size, rows * cell_size 

 #sidebar size 
sidebar_width = 200 
preview_height_fraction = 0.7
score_height_fraction = 1 - preview_height_fraction 

#window 
padding = 20 
window_width = game_width + sidebar_width + padding * 3 
window_height = game_height + padding * 2 

#game behaviour 
update_start_speed = 300
move_wait_time = 200 
rotate_wait_time = 200 
block_offset = pygame.Vector2(columns //2,-1)

#colours 
yellow = '#f1e60d'
red = '#e51b20'
blue = '#204b9b'
green = '#65b32e'
purple = '#7b217f'
cyan ='#6cc6d9'
orange = '#f07e13'
gray = '#1C1C1C'
line_colour = '#FFFFFF'
white = '#FFFFFF'

#shapes 
tetrominos = {
    'T': {'shape': [(0,0),(-1,0),(1,0),(0,-1)],'colour':purple},
    'O': {'shape': [(0,0),(0,-1),(1,0,),(1,-1)],'colour':yellow},
    'J': {'shape': [(0,0),(0,-1),(0,1),(-1,1)],'colour':blue},
    'L': {'shape': [(0,0),(0,-1),(0,1),(1,1)],'colour': orange},
    'I': {'shape': [(0,0),(0,-1),(0,-2),(0,1)],'colour': cyan},
    'S': {'shape': [(0,0),(-1,0),(0,-1),(1,-1)],'colour':green},
    'Z': {'shape': [(0,0),(1,0),(0,-1),(-1,-1)],'colour':red}
}

score_data = {1: 40, 2: 100, 3: 300, 4: 1200}
