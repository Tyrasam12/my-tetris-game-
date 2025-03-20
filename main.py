from settings import *
from sys import exit
from os.path import join 

#components 
from game import Game   
from score import Score 
from preview import Preview 
from buttons import Button

from random import choice 


class Main:
    def __init__(self):

        #general 
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width,window_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tyra's Tetris NEA")

        self.font = pygame.font.Font(join("code","Russo_One.ttf"),30)
        self.font_large = pygame.font.Font(join("code","Russo_One.ttf"),100)

        self.game_active = False 
        self.intructions_active = False 

        spacing_buttons = 70 

        #buttons 
        self.play_button = Button(
            "PLAY",
            self.font,
            ('white'),
            ('green'),
            (window_width //2, window_height // 2 - spacing_buttons )
        )

        self.instructions_button = Button(
            "INSTRUCTIONS",
            self.font,
            ('white'),
            ('green'),
            (window_width //2, window_height // 2)
        )

        self.exit_button = Button(
            "EXIT",
            self.font,
            ('white'),
            ('red'),
            (window_width //2, window_height // 2 + spacing_buttons )
        )



        #shapes 
        self.next_shapes = [choice(list(tetrominos.keys())) for shape in range(3)]
        

        #components 
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

        #audio 
        self.music = pygame.mixer.Sound(join("code","music.wav"))
        self.music.set_volume(0.05)
        self.music.play(-1)

    def update_score(self,lines,score,level):
         self.score.lines = lines 
         self.score.score = score
         self.score.level = level 
    
    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(tetrominos.keys())))
        return next_shape 

    def get_next_shape(self): 
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(tetrominos.keys())))
        return next_shape 

    def menu(self):
        while not self.game_active:
            self.display_surface.fill((gray))
            title = 'TETRIS'
            title_surface = self.font_large.render(title, True, ("red")) 
            title_rect = title_surface.get_rect(center=(window_width // 2, 100)) 
            self.display_surface.blit(title_surface, title_rect)

            subtitle = 'BY TYRA'
            subtitle_surface = self.font.render(subtitle, True, ("red")) 
            subtitle_rect = subtitle_surface.get_rect(center=(window_width // 2, 160)) 
            self.display_surface.blit(subtitle_surface, subtitle_rect)



            

            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.check_for_input(pygame.mouse.get_pos()):
                        self.game_active = True

                    elif self.instructions_button.check_for_input(pygame.mouse.get_pos()):
                        self.instructions_active = True
                        self.instructions()

                    elif self.exit_button.check_for_input(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()


            # Button hover effect
            self.play_button.change_color(pygame.mouse.get_pos())
            self.instructions_button.change_color(pygame.mouse.get_pos())
            self.exit_button.change_color(pygame.mouse.get_pos())

            # Draw button
            self.play_button.update(self.display_surface)
            self.instructions_button.update(self.display_surface)
            self.exit_button.update(self.display_surface)
            
            # Update display
            pygame.display.update()
            self.clock.tick(60)

    def instructions(self):
        instructions_text = [
        "Welcome to",
        "Tyra's Tetris Game!",
        "",
        "",
        "HOW TO PLAY:",
        "Use LEFT and RIGHT arrows",
        "to move the blocks.",
        "",
        "Use UP arrow to",
        "rotate the block.",
        "",
        "Use DOWN arrow to",
        "speed up the block's fall.",
        "",
        "Complete rows to",
        "gain points and level up.",
        "",
        "Press BACK to return to the main menu."
    ]
    
    # Create a Back button to return to the menu
        self.back_button = Button(
        "BACK",
        self.font,
        ('white'),
        ('blue'),
        (window_width // 2, window_height - 60)
    )
    
    # Instructions Loop
        while self.instructions_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If the window is closed
                    self.instructions_active = False  # Exit the loop and quit
                if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                    if self.back_button.check_for_input(pygame.mouse.get_pos()):  # If the Back button is clicked
                        self.instructions_active = False  # Exit the instructions and go back to the menu

            self.display_surface.fill((gray))

            text_start = 50 
            spacing = 30

            for line in instructions_text: 
                text_surface = self.font.render(line, True, (255, 255, 255))  # Create text
                self.display_surface.blit(text_surface, (window_width // 2 - text_surface.get_width() // 2, text_start))  # Center and draw
                text_start += spacing  # Move to the next line

        # Button hover and update
            self.back_button.change_color(pygame.mouse.get_pos())
            self.back_button.update(self.display_surface)

        # Update display
            pygame.display.update()
            self.clock.tick()

   
    def run(self):
        while True :
            if self.intructions_active: 
                self.instructions()
            elif not self.game_active:
                self.menu()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
            
                        pygame.quit()
                        exit()

            #display 
            self.display_surface.fill(gray)

            #components 
            self.game.run()
            self.score.run()
            self.preview.run(self.next_shapes)

            #updating the game 
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()
