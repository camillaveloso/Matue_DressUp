import pygame
import tkinter as tk
from tkinter import filedialog
from button import Button
def capture_screen(surface, width, height, buttons_to_hide = None):
    if buttons_to_hide:
        if isinstance(buttons_to_hide, list):
            for botao in buttons_to_hide:
                botao.hidden_rect = botao.rect.copy()  #Salva a posição original do botão
                botao.rect = pygame.Rect(0, 0, 0, 0)  #Define a posição do botão como invisível
        elif isinstance(buttons_to_hide, Button):
            buttons_to_hide.hidden_rect = buttons_to_hide.rect.copy()
            buttons_to_hide.rect = pygame.Rect(0, 0, 0, 0)
    
    capture = pygame.Surface((width, height))
    capture.blit(surface, (0,0))

    if buttons_to_hide:
        if isinstance(buttons_to_hide, list):
            for button in buttons_to_hide:
                button.rect = button.hidden_rect
        elif isinstance(buttons_to_hide, Button):
            buttons_to_hide.rect = buttons_to_hide.hidden_rect
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    root.destroy()

    if file_path:
        pygame.image.save(capture, file_path) #salvando no diretório escolhido
    
    if buttons_to_hide: #nossa lista de botões a serem escondidos
        for botao in buttons_to_hide:
            botao.rect = botao.hidden_rect