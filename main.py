import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
MAX_FPS = 1500

class Block:
    def __init__(self, pos: tuple[int, int], solid: bool, color: str, size: int = 8):
        self.pos = [float(pos[0]), float(pos[1])]
        self.solid = solid
        self.color = color
        self.size = size

    def update(self, delta):
        self.pos[1] += 1000 * delta

    def draw(self, surface: pygame.Surface):
        """
        Draw a Block on the screen
        """
        # draw rectangle centered at self.pos using self.size
        half = self.size / 2
        rect = pygame.Rect(int(self.pos[0] - half), int(self.pos[1] - half),
                           self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)

screen.fill((0, 0, 0))

blocks: list = []

while running:
    dt = clock.tick(MAX_FPS) / 10000
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

    # If mouse clicked spawn sand from class. Sand update method is defined in class
    pygame.event.get()
    clicked = pygame.mouse.get_pressed() # Check for left, right, and middle mouse input
    mouse_pos = pygame.mouse.get_pos()

    if clicked[0]: # Check if left mouse clicked
        blocks.append(Block(mouse_pos, False, "yellow"))

    for b in blocks:
        if not b.solid and b.pos[1] < pygame.display.get_window_size()[1] - 5:
            b.update(dt)

    pygame.display.flip()

    screen.fill((0, 0, 0))
    for b in blocks:
        b.draw(screen)

pygame.quit()