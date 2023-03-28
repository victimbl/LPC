class RainbowText:
    def __init__(self, screen, text, font, x, y, delay):
        self.screen = screen
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.delay = delay
        self.colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 127, 255), (0, 0, 255),
                       (139, 0, 255)]
        self.color_index = 0
        self.timer = 0

    def update(self):
        # Increment the timer
        self.timer += 1

        # Change the color every delay frames
        if self.timer == self.delay:
            self.color_index = (self.color_index + 1) % len(self.colors)
            self.timer = 0

        # Render the text with the current color
        color = self.colors[self.color_index]
        text_surface = self.font.render(self.text, True, color)

        # Draw the text surface to the screen
        self.screen.blit(text_surface, (self.x, self.y))
