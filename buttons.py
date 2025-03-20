class Button:
    def __init__(self, diplay_text, font, base_color, hovering_color, pos):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.diplay_text = diplay_text

        self.text = self.font.render(self.diplay_text, True, self.base_color)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        if self.text_rect.collidepoint(position):
            return True
        return False

    def change_color(self, position):
        if self.text_rect.collidepoint(position):
            self.text = self.font.render(self.diplay_text, True, self.hovering_color)
        else:
            self.text = self.font.render(self.diplay_text, True, self.base_color)
