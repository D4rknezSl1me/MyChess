import pygame
from const import *

class Dragger():
    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.inital_row = 0
        self.inital_col = 0
    
    # Blit method
    def update_blit(self, surface):
        # Bigger Texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture

        # Img
        img = pygame.image.load(texture)
        # Rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # Update blit
        surface.blit(img, self.piece.texture_rect)
        
    # Other methods
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.inital_row = pos[1]//SQSIZE
        self.inital_col = pos[0]//SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

