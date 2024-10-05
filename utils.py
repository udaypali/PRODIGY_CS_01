import os 
import sys
import gui.home
import gui.navbar
import gui.encode
import gui.decode
import gui.history
import customtkinter as ctk

def destory_pages():
    
    if gui.home.home_frame is not None:
        gui.home.home_frame.destroy()

    if gui.encode.encode_frame is not None:
        gui.encode.encode_frame.destroy()
        
    if gui.decode.decode_frame is not None:
        gui.decode.decode_frame.destroy()
        
    if gui.history.history_frame is not None:
        gui.history.history_frame.destroy()
        
def load_fonts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(base_dir, 'assets', 'fonts', 'Exo2-SemiBoldItalic.ttf')
    if os.path.exists(font_path):
        ctk.FontManager.load_font(font_path)
    else:
        print(f"Font not found at {font_path}") 
        
def exit_button():
    sys.exit(0)
    
def home_button(root):
    destory_pages()
    gui.home.home(root)
    
def encode_button(root):
    destory_pages()
    gui.encode.encode(root)
    
def decode_button(root):
    destory_pages()
    gui.decode.decode(root)
    
def history_button(root):
    destory_pages()
    gui.history.history(root)