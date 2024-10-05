import customtkinter as ctk 
import gui.navbar
import gui.home

def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green") 

    root = ctk.CTk()
    root.geometry("800x500")
    root.title("Caesar Cipher Tool by Uday")
    
    root.resizable(False, False)
    root.maxsize(800, 500)
    
    gui.navbar.navbar(root)
    gui.home.home(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
