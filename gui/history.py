import customtkinter as ctk
import mysql.connector

history_frame = None

def history(root):
    global history_frame
    
    if history_frame:
        history_frame.pack_forget()  # Hide previous frame if it exists
    
    # Create a new frame for the history page
    history_frame = ctk.CTkFrame(master=root, height=500, width=600, corner_radius=10)
    history_frame.pack(side='right', expand=False, fill='x', padx=(5, 10), pady=10)
    history_frame.pack_propagate(False)

    # Create a container frame to hold the label and button
    header_frame = ctk.CTkFrame(master=history_frame, width=580, fg_color='transparent')  # Container frame for label and button
    header_frame.pack(padx=10, pady=(20, 5), fill='x')  # Place the frame at the top

    # Add a label to the header frame
    history_label = ctk.CTkLabel(master=header_frame, text="Encryption History", font=('Arial', 30, 'underline'))
    history_label.pack(side='left', padx=20)

    # Add a "Clear History" button to the right of the label inside the header frame
    clear_button = ctk.CTkButton(master=header_frame, text="Clear History", corner_radius=50, command=lambda: clear_history(scrollable_frame))
    clear_button.pack(side='right', padx=10)

    # Frame to hold the history data in a scrollable manner
    scrollable_frame = ctk.CTkScrollableFrame(master=history_frame, width=550, height=400)
    scrollable_frame.pack(padx=10, pady=10, fill='both', expand=True)

    # Call function to fetch messages and populate history in tabular format
    populate_history(scrollable_frame)
    
def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host
        user="root",  # Replace with your MySQL username
        password="udaypali1234",  # Replace with your MySQL password
        database="Task1"  # The name of the database
    )
    
# Truncation function to limit text length and add ellipsis
def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length] + '...'
    return text

def populate_history(parent_frame):
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "SELECT * FROM encrypted_messages"
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        db.close()

        # Set colors for striping rows and text color
        even_row_color = "#F5F5F5"  # Lighter gray for even rows
        odd_row_color = "#FFFFFF"  # White for odd rows
        header_color = "#444444"  # Darker color for headers
        header_text_color = "#FFFFFF"  # White for header text
        text_color = "#000000"  # Black for normal text

        # Styling
        header_font = ('Arial', 12, 'bold')
        cell_font = ('Arial', 11)

        # Create table headers with styling
        headers = ['ID', 'Message', 'Shift', 'Encrypted Message', 'Timestamp']
        column_widths = [30, 130, 50, 130, 150]  # Adjusted column widths, increased timestamp width

        # Header row styling
        for i, header in enumerate(headers):
            header_label = ctk.CTkLabel(master=parent_frame, text=header, font=header_font, text_color=header_text_color,
                                        anchor='center', width=column_widths[i], fg_color=header_color)
            header_label.grid(row=0, column=i, padx=5, pady=5, sticky='ew')

        # Display records in a grid format with alternating row colors
        for row_num, record in enumerate(records, start=1):
            bg_color = even_row_color if row_num % 2 == 0 else odd_row_color

            # Truncate long messages and encrypted messages more aggressively
            truncated_message = truncate_text(record[1], max_length=15)  # Reduced to fit column better
            truncated_encrypted_message = truncate_text(record[3], max_length=15)

            # ID
            id_label = ctk.CTkLabel(master=parent_frame, text=record[0], anchor='center', font=cell_font, text_color=text_color,
                                    width=column_widths[0], fg_color=bg_color)
            id_label.grid(row=row_num, column=0, padx=5, pady=5, sticky='ew')

            # Message
            message_label = ctk.CTkLabel(master=parent_frame, text=truncated_message, anchor='center', font=cell_font, text_color=text_color,
                                         width=column_widths[1], fg_color=bg_color)
            message_label.grid(row=row_num, column=1, padx=5, pady=5, sticky='ew')

            # Shift
            shift_label = ctk.CTkLabel(master=parent_frame, text=record[2], anchor='center', font=cell_font, text_color=text_color,
                                       width=column_widths[2], fg_color=bg_color)
            shift_label.grid(row=row_num, column=2, padx=5, pady=5, sticky='ew')

            # Encrypted Message
            encrypted_message_label = ctk.CTkLabel(master=parent_frame, text=truncated_encrypted_message, anchor='center',
                                                   font=cell_font, text_color=text_color, width=column_widths[3], fg_color=bg_color)
            encrypted_message_label.grid(row=row_num, column=3, padx=5, pady=5, sticky='ew')

            # Timestamp
            timestamp_label = ctk.CTkLabel(master=parent_frame, text=record[4], anchor='center', font=cell_font, text_color=text_color,
                                           width=column_widths[4], fg_color=bg_color)
            timestamp_label.grid(row=row_num, column=4, padx=5, pady=5, sticky='ew')

    except mysql.connector.Error as err:
        error_label = ctk.CTkLabel(master=parent_frame, text=f"Error fetching data: {err}", font=('Arial', 16), fg_color="red")
        error_label.pack(padx=10, pady=10)

def clear_history(parent_frame):
    try:
        db = connect_db()
        cursor = db.cursor()
        query = "DELETE FROM encrypted_messages"  # Delete all records from the table
        cursor.execute(query)
        db.commit()
        cursor.close()
        db.close()

        # After clearing, refresh the history table
        for widget in parent_frame.winfo_children():
            widget.destroy()  # Clear the previous history table

        # Optionally, you can show a message to confirm that the history was cleared
        cleared_label = ctk.CTkLabel(master=parent_frame, text="History Cleared", font=('Arial', 16))
        cleared_label.pack(pady=20)

    except mysql.connector.Error as err:
        error_label = ctk.CTkLabel(master=parent_frame, text=f"Error clearing history: {err}", font=('Arial', 16), fg_color="red")
        error_label.pack(padx=10, pady=10)
