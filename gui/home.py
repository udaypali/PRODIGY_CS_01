import customtkinter as ctk 

home_frame = None

def home(root):
    global home_frame
    
    home_frame = ctk.CTkFrame(master=root, height=500, width=600, corner_radius=10)
    home_frame.pack(side='right', expand=False, fill='x', padx=(5,10), pady=10)
    home_frame.pack_propagate(False)

    # Title Section
    title_label = ctk.CTkLabel(master=home_frame, text="Welcome to the Caesar Cipher Tool", 
                               font=('Arial', 30, 'bold'), anchor='center')
    title_label.pack(pady=(50, 20))  # Added vertical padding for spacing

    # Subtitle Section
    subtitle_label = ctk.CTkLabel(master=home_frame, text="Encrypt and Decrypt Your Messages Easily", 
                                  font=('Arial', 20), anchor='center')
    subtitle_label.pack(pady=(0, 40))  # Padding between subtitle and buttons

    # "How It Works" Section: Explaining the Caesar Cipher
    explanation_frame = ctk.CTkFrame(master=home_frame)
    explanation_frame.pack(pady=30, padx=30, fill="x")

    how_it_works_label = ctk.CTkLabel(master=explanation_frame, text="How Does Caesar Cipher Work?",
                                      font=('Arial', 22, 'bold'), anchor='center')
    how_it_works_label.pack(pady=(10, 10))  # Space between title and text

    # Caesar Cipher Explanation Text
    explanation_text = ("Caesar Cipher is a simple substitution cipher where each letter in the plaintext "
                        "is shifted by a certain number of positions down the alphabet. "
                        "For example, with a shift of 3, A becomes D, B becomes E, and so on. "
                        "This method is one of the oldest encryption techniques used in history.")
    
    # Adjust wraplength and justify to better fit the frame
    explanation_label = ctk.CTkLabel(master=explanation_frame, text=explanation_text,
                                     font=('Arial', 14), wraplength=500, justify="left")
    explanation_label.pack(pady=(0, 20))

    # Footer Section
    footer_label = ctk.CTkLabel(master=home_frame, text="© 2024 Uday's Caesar Cipher Tool", 
                                font=('Arial', 12), anchor='center')
    footer_label.pack(side='bottom', pady=20)
