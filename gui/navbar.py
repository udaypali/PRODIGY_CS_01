import customtkinter as ctk
import utils

navbar_frame = None 

def navbar(root):
    global navbar_frame
    
    #main frame
    navbar_frame = ctk.CTkFrame(master=root, height=500, corner_radius=10)
    navbar_frame.pack(side='left', expand=False, fill='y', padx=(10,5), pady=10)
    
    #button frame for the top buttons
    button_frame1 = ctk.CTkFrame(master=navbar_frame, fg_color='transparent')
    button_frame1.pack(side='top', pady=10, fill='x')
    
    #home button
    home_button = ctk.CTkButton(master=button_frame1, text='Home', cursor='hand2', height=40, width=150, corner_radius=50, command=lambda:utils.home_button(root))
    home_button.pack(padx=20, pady=(20,10))
    
    #encode button
    encode_button = ctk.CTkButton(master=button_frame1,text='Encode', cursor='hand2', height=40, width=150, corner_radius=50, command=lambda:utils.encode_button(root))
    encode_button.pack(padx=20, pady=(10,10))
    
    #decode button
    deocde_frame = ctk.CTkButton(master=button_frame1, text='Decode', cursor='hand2', height=40, width=150, corner_radius=50, command=lambda:utils.decode_button(root))
    deocde_frame.pack(padx=20, pady=(10,20))
    
    #button frame for the bottom buttons
    button_frame2 = ctk.CTkFrame(master=navbar_frame, fg_color='transparent')
    button_frame2.pack(side='bottom', pady=10, fill='x')
    
    #history button
    history_button = ctk.CTkButton(master=button_frame2, text='History', cursor='hand2', height=40, width=150, corner_radius=50, command=lambda:utils.history_button(root))
    history_button.pack(padx=20, pady=(20,10))
    
    #exit button
    exit_button = ctk.CTkButton(master=button_frame2, text='Exit', cursor='hand2', height=50, width=150, corner_radius=50, fg_color='#FF6C6C', hover_color='#FD2121', command=lambda:utils.exit_button())
    exit_button.pack(padx=20, pady=(10,20))