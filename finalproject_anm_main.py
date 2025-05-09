# m08 - Final Project - LittleLibro Personal Library Tracker
# auther:  ANM
# created 2025-04-09
# updated 2025-05-06
# IDE used: Visual Studio Code
# CODING ASSISTANCE WAS USED to create this program
    # Code Assistance Website - https://www.youtube.com/watch?v=8m4uDS_nyCk  https://www.youtube.com/watch?v=fvIThtPt6Nc aided in pulling data entry and then adding to text file
    # Code Assistance Website - https://www.youtube.com/watch?v=unZlSLhzNOU aided in creation of main_window_class and using it as a function for a button
    # Code Assistance Website - https://www.youtube.com/watch?v=vusUfPBsggw aided in creation of main window (LittleLibro Book Entry Form)
    # Code Assistance AI - Used GitHub Copilot throughout code for help with debugging and organization
    # Code Assistance AI - Used GitHub Copilot to help with centering images and making them fill the frame, as well as creating the clear data button
    # Code Assistance AI - Used GitHub Copilot to help with creating the book table window and the remove duplicates button


# pseudo code
# at least 2 windows
# use at least two images
# include at least three labels
# include at least 3 buttons
# include at least three call back functions (one per button including an exit button)
# use input validation to ensure correct data type and no empty boxes (where applicable)

# imports classes and methods
import tkinter
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os


# function to call the main_window (the book entry page)
def create_window():
    global main_window
    main_window = Main_Window_Class() # sets the variable to the main_window_class which in turn creates the new window when a button is pushed

def create_book_table():
    global book_table_window
    book_table_window = BookTable() # sets the variable to the BookTable class which in turn creates the new window when a button is pushed

# function to end the book entry window    
def close_window():
    global main_window
    main_window.destroy()

# function to end the program
def close_hello_window():
    hello_window.destroy()

# made a class for the entry form window so that it could be used in a function as a variable. This allows the user to click a button and have a separate window open for the entry form.
class Main_Window_Class(tkinter.Toplevel):
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()
        self.title('LittleLibro Book Entry Form')

        # Create the main frame and subframes
        self.create_main_frame()
        self.create_picture_frame()
        self.create_book_info_frame()
        self.create_button_frame(self)

    def create_main_frame(self):
        self.frame = tkinter.Frame(self, bg="antique white")
        self.frame.grid(row=0, column=0, sticky="nsew")  # Fill the entire window
        self.frame.pack(fill=tkinter.BOTH, expand=True)  # Ensures the frame fills the entire window

    def create_button_frame(self, frame):
        self.button_frame = tkinter.Frame(frame, bg="antique white")
        self.button_frame.grid(row=0, column=1, sticky="nsew")  # Create a separate frame for buttons

    def create_picture_frame(self): # used GitHub Copilot to center image and make it fill the frame
        picture_frame = tkinter.LabelFrame(master=self.frame, bg="antique white")
        picture_frame.grid(row=0, column=2, sticky="nsew")  # Allow the frame to expand and fill available space
        try:
            # Get the path to the library image
            modulePath = os.path.dirname(os.path.realpath(__file__))
            libraryPath = os.path.join(modulePath, 'george_peabody_library.jpg')

            # Load and resize the image
            library_image = Image.open(libraryPath)
            library_image = library_image.resize((200, 200))
            library_image = ImageTk.PhotoImage(library_image)

            # Display the image in the picture_frame
            library_image_label = ttk.Label(picture_frame, image=library_image, background="antique white")
            library_image_label.image = library_image  # Keep a reference to avoid garbage collection
            library_image_label.grid(row=0, column=0, padx=10, pady=10)  # Centers the image within the frame
        except FileNotFoundError:
            # Display an error message if the image is not found
            error_label = ttk.Label(picture_frame, text="Error: george_peabody_library.jpg not found.", background="antique white", foreground="red")
            error_label.grid(row=0, column=0, padx=10, pady=10)  # Centers the error message

        # Add alt text below the image
        library_image_label_alt_text = ttk.Label(picture_frame, text="Image of shelves from the George Peabody Library in Baltimore", background="antique white")
        library_image_label_alt_text.grid(row=1, column=0, padx=0, pady=0)  # Centers the alt text

        # Configure row and column weights for centering and resizing
        picture_frame.grid_rowconfigure(0, weight=1)
        picture_frame.grid_columnconfigure(0, weight=1)

        # creates a subframe titled "Entry Form"
    def create_book_info_frame(self):
        book_info_frame = tkinter.LabelFrame(master=self.frame, text="Entry Form", bg="antique white")
        book_info_frame.grid(row=0, column=0, sticky="nsew")  # Fill the entire window
        book_info_frame.grid_rowconfigure(0, weight=1)  # Allow the frame to expand and fill available space

        # calling the methods that hold the widgets and places them in the book_info_frame
        self.create_author_info(book_info_frame)
        self.create_media_type(book_info_frame)
        self.create_book_info(book_info_frame)
        self.create_book_title_entry(book_info_frame)
        self.create_genre_entry(book_info_frame)
        self.create_book_list(book_info_frame)
        self.create_rating_list(book_info_frame)

        # creates a button frame and calls the method that holds the buttons and places them in the button_frame
        self.create_button_frame(self.frame)
        self.create_buttons(self.button_frame)

        # Space out widgets evenly
        for widget in book_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # author info widgets
        # creates a label that denotes the section of the form that is for the Author's information
    def create_author_info(self, frame):
        author_info_label = tkinter.Label(frame, text="Author Information", bg="antique white")
        author_info_label.grid(row=0, column=0)
        
        # entry widgets for author's first and last name
        self.first_name_entry = tkinter.Entry(frame)
        self.first_name_entry.grid(row=1, column=0)
        self.first_name_entry.insert(0, "Author's First Name") # fills entry box with a default "Author's First Name", makes clear to user what the widget expects as input. 
        self.first_name_entry.bind("<FocusIn>", lambda e: self.first_name_entry.delete("0", "end")) # clears the box when the user clicks on it.
        self.first_name_entry.bind("<FocusIn>", lambda e: self.first_name_entry.delete("0", "end")) # clears the box when the user clicks on it.
        self.last_name_entry = tkinter.Entry(frame)
        self.last_name_entry.insert(0, "Author's Last Name") # fills entry box with a default "Author's Last Name", makes clear to user what the widget expects as input.
        self.last_name_entry.bind("<FocusIn>", lambda e: self.last_name_entry.delete("0", "end"))
        self.last_name_entry.grid(row=1, column=1) # places the last name entry box next to the first name entry box
        
        # creates a label for the section of the form that is for book specific information like title and genre.
    def create_book_info(self, frame):
        book_info_label = tkinter.Label(frame, text="Book Information", bg="antique white")
        book_info_label.grid(row=2, column=0)

        # creates an entry box for the user to enter the book title into
    def create_book_title_entry(self, frame):
        self.book_title_entry = tkinter.Entry(frame)
        self.book_title_entry.insert(0, "Enter Book Title") # default enter's "Enter Book Title" in the entry box to make it clear what the user is supposed to do.
        self.book_title_entry.bind("<FocusIn>", lambda e: self.book_title_entry.delete("0", "end")) # clears the entry box when the user clicks on it. 
        self.book_title_entry.grid(row=3, column=0)    
       
        # label and dropdown box with the media type that user can use to tag the book with
    def create_media_type(self, frame):
        media_type_label = tkinter.Label(frame, text="Media Type", bg="antique white")
        self.media_type_combobox = ttk.Combobox(frame, values=["Audiobook", "eBook", "Physical Copy"])
        media_type_label.grid(row=4, column=0)
        self.media_type_combobox.grid(row=5, column=0)

        # creates an entry box for user to enter the genre into. I chose this instead of a drop down so that they can add genres as they wish and aren't stuck with prefilled ones
    def create_genre_entry(self, frame):
        self.genre_entry = tkinter.Entry(frame)
        self.genre_entry.insert(0, "Enter genre")
        self.genre_entry.bind("<FocusIn>", lambda e: self.genre_entry.delete("0", "end"))
        self.genre_entry.grid(row=3, column=1)  # places the genre entry box next to the book title entry box

        # creates a label and dropdown box with the "Book Shelf" that user can add a book to. 
    def create_book_list(self, frame):
        book_list_label = tkinter.Label(frame, text="Book Shelf", bg="antique white")
        self.book_list_combobox = ttk.Combobox(frame, values=["Read", "To-Read", "Did Not Finish", "Reading"])
        book_list_label.grid(row=4, column=1)
        self.book_list_combobox.grid(row=5, column=1)

    def create_rating_list(self, frame):
        rating_label = tkinter.Label(frame, text="Rating", bg = 'antique white')
        rating_label.grid(row=8, column=0)
        self.rating_combobox = ttk.Combobox(frame, values=['1 star', '2 stars', '3 stars', '4 stars', '5 stars'])
        self.rating_combobox.grid(row=9, column=0)
        
        # creates a separate frame for buttons and adds buttons to it
    def create_buttons(self, frame):
        button_width = 20  # Set a fixed width for all buttons

        insert_file_button = ttk.Button(self.button_frame, text="Add Book to .txt file", width=button_width, command=self.add_book_to_file)
        insert_file_button.grid(row=3, column=0, padx=5)

        clear_button = ttk.Button(self.button_frame, text="Clear Entry Boxes", width=button_width, command=lambda: [
            self.first_name_entry.delete(0, 'end'), self.last_name_entry.delete(0, 'end'),
            self.book_title_entry.delete(0, 'end'), self.genre_entry.delete(0, 'end')
        ])
        clear_button.grid(row=3, column=1, padx=5)

        clear_combo_button = ttk.Button(self.button_frame, text="Clear Combo Boxes", width=button_width, command=lambda: [
            self.media_type_combobox.set(''), self.book_list_combobox.set(''), self.rating_combobox.set('')
        ])
        clear_combo_button.grid(row=4, column=1, padx=5)

        exit_button = ttk.Button(self.button_frame, text="Close book entry page.", width=button_width, command=self.destroy)
        exit_button.grid(row=5, column=1, padx=5)

    # Function to save book details to a text file
    def add_book_to_file(self):
        # Retrieve data from the form
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        book_title = self.book_title_entry.get()
        genre = self.genre_entry.get()
        media_type = self.media_type_combobox.get()
        book_shelf = self.book_list_combobox.get()
        ratings = self.rating_combobox.get()

        # Validate input (ensure no empty fields)
        if not all([first_name, last_name, book_title, genre, media_type, book_shelf]): # leaving rating out of the input validation because it's possible the book hasn't been read yet
            tkinter.messagebox.showerror("Error", "All fields must be filled!")
            return
        try:
            with open("anm_LittleLibroInventory.txt", "a") as file:
                file.write(f"{first_name},{last_name},{book_title},{genre},{media_type},{book_shelf},{ratings}\n")

            # Show success message
            tkinter.messagebox.showinfo("Success", "Book added successfully!")
        except Exception as e:
            
            # Show error message
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")
class BookTable(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Books Table")
        self.geometry("800x400")

        # Create a Treeview widget
        columns = ("First Name", "Last Name", "Book Title", "Genre", "Media Type", "Book Shelf", "Rating")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill=tkinter.BOTH, expand=True)

        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")  # Allow auto-resizing

        # Load data from the text file
        self.add_books_to_table(columns)

        # Adjust column widths to fit content
        self.auto_fit_columns()

        # Add a button to remove duplicate data
        remove_duplicates_button = ttk.Button(self, text="Remove Duplicates", command=self.remove_duplicates)
        remove_duplicates_button.pack(pady=10)

    # Adds the books to the table from the text file. It only adds the last 10 entries to the table so that it doesn't get too long and cluttered.
    def add_books_to_table(self, columns):
        try:
            with open("anm_LittleLibroInventory.txt", "r") as file:
                lines = file.readlines()[-10:]  # Get the 10 most recent entries
                for line in lines:
                    data = line.strip().split(",")
                    if len(data) == len(columns):
                        self.tree.insert("", tkinter.END, values=data)
        except FileNotFoundError:
            tkinter.messagebox.showerror("Error", "Inventory file not found!")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")

    # Automatically adjust column widths to fit content
    def auto_fit_columns(self):
        for col in self.tree["columns"]:
            max_width = max(
                len(str(self.tree.set(item, col))) for item in self.tree.get_children("")
            )
            max_width = max(max_width, len(col))  # Account for column header length
            self.tree.column(col, width=max_width * 10)  # Adjust width multiplier as needed

    # Remove duplicate entries from the text file and refresh the table
    def remove_duplicates(self):
        try:
            with open("anm_LittleLibroInventory.txt", "r") as file:
                lines = file.readlines()

            # Remove duplicates while preserving order
            unique_lines = list(dict.fromkeys(lines))

            with open("anm_LittleLibroInventory.txt", "w") as file:
                file.writelines(unique_lines)

            # Refresh the table
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.add_books_to_table(self.tree["columns"])

            tkinter.messagebox.showinfo("Success", "Duplicates removed successfully!")
        except FileNotFoundError:
            tkinter.messagebox.showerror("Error", "Inventory file not found!")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"An error occurred: {e}")

# opens the landing page of the program
hello_window = tkinter.Tk()
hello_window.title("LittleLibro by ANM")
hello_window.configure(bg="antique white")

try:
    # Get the path to the bookshelf image
    modulePath = os.path.dirname(os.path.realpath(__file__))
    bookshelfPath = os.path.join(modulePath, 'bookshelf.jpg')

    # Load and resize the image
    bookshelf_image = Image.open(bookshelfPath)
    bookshelf_image = bookshelf_image.resize((200, 200))
    bookshelf_image = ImageTk.PhotoImage(bookshelf_image)

    # Display the image in the hello_window
    bookshelf_image_label = ttk.Label(hello_window, image=bookshelf_image, background="antique white")
    bookshelf_image_label.image = bookshelf_image  # Keep a reference to avoid garbage collection
    bookshelf_image_label.pack(padx=10, pady=10, expand=True)  # Centers the image
except FileNotFoundError:
    # Display an error message if the image is not found
    error_label = ttk.Label(hello_window, text="Error: bookshelf.jpg not found.", background="antique white", foreground="red")
    error_label.pack(padx=10, pady=10, expand=True)  # Centers the error message

# Add alt text below the image
bookshelf_image_label_alt_text = ttk.Label(hello_window, text="Image of a bookshelf", background="antique white")
bookshelf_image_label_alt_text.pack(padx=0, pady=0, expand=True)  # Centers the alt text

# opens the book entry window
entry_button = ttk.Button(hello_window, text="Enter a new book.", command=create_window)
entry_button.pack(expand=True)

# opens the book table window
book_table_button = ttk.Button(hello_window, text="View Book Table.", command=create_book_table)
book_table_button.pack(expand=True)

# closes the landing page/whole program
exit_button = ttk.Button(hello_window, text="End application.", command=close_hello_window)
exit_button.pack(expand=True)

# needed for opening the window
hello_window.mainloop()
