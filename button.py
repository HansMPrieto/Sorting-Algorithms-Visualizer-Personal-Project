import pygame


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        """
        Draws a button on the screen.
        """
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, mouse_pos):
        """
        Determines if mouse is over a button.
        (mouse_pos is the position of the mouse on the screen)
        """
        if (mouse_pos[0] > self.x) and (mouse_pos[0] < self.x + self.width):
            if (mouse_pos[1] > self.y) and (mouse_pos[1] < self.y + self.height):
                return True
        return False
