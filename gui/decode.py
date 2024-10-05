import customtkinter as ctk
import pyperclip

decode_frame = None

def decode(root):
    global decode_frame
    
    decode_frame = ctk.CTkFrame(master=root, height=500, width=600, corner_radius=10)
    decode_frame.pack(side='right', expand=False, fill='x', padx=(5,10), pady=10)
    decode_frame.pack_propagate(False)
    
    home_label = ctk.CTkLabel(master=decode_frame, text='Decrpyt you message', font=('Arial', 40, 'underline'))
    home_label.pack(padx=20, pady=20)
    
    # Message input section
    message_frame = ctk.CTkFrame(master=decode_frame, fg_color='transparent')
    message_frame.pack(padx=10, pady=10, fill='x', expand=True)
    
    message_label = ctk.CTkLabel(master=message_frame, text='Enter your encrypted message')
    message_label.pack(padx=5, pady=(10, 10))  # Consistent padding
    
    message_entry = ctk.CTkEntry(master=message_frame)
    message_entry.pack(padx=5, pady=(10, 10), fill='x', expand=True)  # Expanding the entry field to fill space
    
    # Shift slider frame
    shift_frame = ctk.CTkFrame(master=decode_frame, fg_color='transparent')
    shift_frame.pack(padx=10, pady=10, fill='x', expand=True)
    
    shift_label = ctk.CTkLabel(master=shift_frame, text='Enter your Shift')
    shift_label.pack(padx=5, pady=(10, 10))  # Consistent padding
    
    # Slider for shift value
    shift_slider = ctk.CTkSlider(master=shift_frame, from_=1, to=25, number_of_steps=24, width=300)
    shift_slider.set(3)  # Set default to 3
    shift_slider.pack(padx=5, pady=(10, 10), fill='x', expand=True)

    # Label to display the current slider value
    shift_value_label = ctk.CTkLabel(master=shift_frame, text=f'Shift Value: {int(shift_slider.get())}')
    shift_value_label.pack(padx=5, pady=(10, 10))  # Keep padding consistent

    # Function to update shift value label when slider is moved
    def update_shift_value(value):
        shift_value_label.configure(text=f'Shift Value: {int(value)}')

    # Attach the update function to the slider's value change event
    shift_slider.configure(command=update_shift_value)

    # Decrypt Now button
    decrypt_button = ctk.CTkButton(master=decode_frame, text="Decrypt Now", corner_radius=50, command=lambda: decrypt_message(message_entry.get(), int(shift_slider.get())))
    decrypt_button.pack(padx=10, pady=(10, 10), expand=True)  # Expand button as well

    # Frame to hold decrypted message entry and copy button side by side
    result_frame = ctk.CTkFrame(master=decode_frame, fg_color='transparent')
    result_frame.pack(padx=10, pady=(10, 10), fill='x', expand=True)

    # Entry to display the decrypted message
    decrypted_message_entry = ctk.CTkEntry(master=result_frame, state='normal', width=400)
    decrypted_message_entry.pack(side='left', padx=5, pady=10, fill='x', expand=True)

    # Copy button to copy decrypted message to clipboard
    copy_button = ctk.CTkButton(master=result_frame, text="Copy", corner_radius=50, command=lambda: copy_to_clipboard(decrypted_message_entry.get()))
    copy_button.pack(side='left', padx=5, pady=10)

    # Decryption function (Caesar cipher)
    def decrypt_message(message, shift):
        if not message:
            decrypted_message_entry.delete(0, 'end')  # Clear the entry if empty
            decrypted_message_entry.insert(0, "Please enter a message")
            return
        
        decrypted_message = ""
        for char in message:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            else:
                decrypted_message += char  # Keep non-alphabetic characters as is

        decrypted_message_entry.delete(0, 'end')  # Clear the previous decrypted message
        decrypted_message_entry.insert(0, decrypted_message)  # Insert the new decrypted message

    # Copy to clipboard function
    def copy_to_clipboard(text):
        if text:
            pyperclip.copy(text)  # Copy the text to clipboard