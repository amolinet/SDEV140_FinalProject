# m08 - Final Project - LittleLibro Personal Library Tracker
# auther:  ANM
# created 2025-04-09
# updated 2025-04-28
# IDE used: Visual Studio Code
# CODING ASSISTANCE WAS USED to create this program
    # Code Assistance Website - https://www.youtube.com/watch?v=8m4uDS_nyCk  https://www.youtube.com/watch?v=fvIThtPt6Nc aided in pulling data entry and adding to an excel file
    # Code Assistance Website - https://www.youtube.com/watch?v=unZlSLhzNOU aided in creation of main_window_class and using it as a function for a button
    # Code Assistance Website - https://www.youtube.com/watch?v=vusUfPBsggw aided in creation of main window (LittleLibro Book Entry Form)

# pseudo code
# at least 2 windows
# use at least two images
# include at least three labels
# include at least 3 buttons
# include at least three call back functions (one per button including an exit button)
# use input validation to ensure correct data type and no empty boxes (where applicable)

# imports tkinter modules
import tkinter
from tkinter import ttk
from tkinter import messagebox

# is used to open/create a txt file that holds data
import os


# function to call the main_window (the book entry page)
def create_window():
    global main_window
    main_window = Main_Window_Class() # sets the variable to the main_window_class which in turn creates the new window when a button is pushed

# function to end the book entry window    
def close_window():
    main_window.destroy()

# function to end the program
def close_hello_window():
    hello_window.destroy()

# made a class for the entry form window so that it could be used in a function as a variable. This allows the user to click a button and have a separate window open for the entry form.
class Main_Window_Class(tkinter.Toplevel):
    def __init__(self): # using self so that functions can access attributes, allows me to break up chunks of code into functions/methods
        super().__init__()
        self.title('LittleLibro Book Entry Form')
        self.geometry('1225x625')
        self.create_main_frame()
        self.create_book_info_frame()
        self.create_tree_view()
        self.load_data_to_treeview()

    def create_main_frame(self):
        self.frame = tkinter.Frame(self, height=1025, bg="pink")
        self.frame.pack(fill=tkinter.X) #makes sure that the whole screen is filled

        # creates a subframe titled "Entry Form"
    def create_book_info_frame(self):
        book_info_frame = tkinter.LabelFrame(master=self.frame, text="Entry Form", bg="antique white")
        book_info_frame.grid(row=0, column=0, padx=20, pady=20)

        # calling the methods that hold the widgets and places them in the book_info_frame
        self.create_author_info(book_info_frame)
        self.create_media_type(book_info_frame)
        self.create_book_info(book_info_frame)
        self.create_book_title_entry(book_info_frame)
        self.create_genre_entry(book_info_frame)
        self.create_book_list(book_info_frame)
        self.create_rating(book_info_frame)
        self.create_review_textbox(book_info_frame)
        self.create_buttons(book_info_frame)

        # Space out widgets evenly
        for widget in book_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # author info widgets
        # creates a label that denotes the section of the form that is for the Author's information
    def create_author_info(self, frame):
        author_info_label = tkinter.Label(frame, text="Author Information", bg="antique white")
        author_info_label.grid(row=0, column=0)
        
        # entry widgets for author's first and last name
        first_name_entry = tkinter.Entry(frame)
        first_name_entry.grid(row=1, column=0)
        first_name_entry.insert(0, "Author's First Name") # fills entry box with a default "Author's First Name", makes clear to user what the widget expects as input. 
        first_name_entry.bind("<FocusIn>", lambda e: first_name_entry.delete("0", "end")) # clears the box when the user clicks on it.

    
        last_name_entry = tkinter.Entry(frame)
        last_name_entry.insert(0, "Author's Last Name") # fills entry box with a default "Author's Last Name", makes clear to user what the widget expects as input.
        last_name_entry.bind("<FocusIn>", lambda e: last_name_entry.delete("0", "end"))
        last_name_entry.grid(row=1, column=1)


        
        # creates a label for the section of the form that is for book specific information like title and genre.
    def create_book_info(self, frame):
        book_info_label = tkinter.Label(frame, text="Book Information", bg="antique white")
        book_info_label.grid(row=2, column=0)

        # creates an entry box for the user to enter the book title into
    def create_book_title_entry(self, frame):
        book_title_entry = tkinter.Entry(frame)
        book_title_entry.insert(0, "Enter Book Title") # default enter's "Enter Book Title" in the entry box to make it clear what the user is supposed to do.
        book_title_entry.bind("<FocusIn>", lambda e: book_title_entry.delete("0", "end")) # clears the entry box when the user clicks on it. 
        book_title_entry.grid(row=3, column=0)    
       
        # label and dropdown box with the media type that user can use to tag the book with
    def create_media_type(self, frame):
        media_type_label = tkinter.Label(frame, text="Media Type", bg="antique white")
        media_type_combobox = ttk.Combobox(frame, values=["Audiobook", "eBook", "Physical Copy"])
        media_type_label.grid(row=4, column=0)
        media_type_combobox.grid(row=5, column=0)

        # creates an entry box for user to enter the genre into. I chose this instead of a drop down so that they can add genres as they wish and aren't stuck with prefilled ones
    def create_genre_entry(self, frame):
        genre_entry = tkinter.Entry(frame)
        genre_entry.insert(0, "Enter genre")
        genre_entry.bind("<FocusIn>", lambda e: genre_entry.delete("0", "end"))
        genre_entry.grid(row=3, column=1)

        # creates a label and dropdown box with the "Book Shelf" that user can add a book to. 
    def create_book_list(self, frame):
        book_list_label = tkinter.Label(frame, text="Book Shelf", bg="antique white")
        book_list_combobox = ttk.Combobox(frame, values=["Read", "To-Read", "Did Not Finish", "Reading"])
        book_list_label.grid(row=6, column=0)
        book_list_combobox.grid(row=7, column=0)

        # creates a label and a dropdown box that a user can select a rating from and assign it to a book
    def create_rating(self, frame):
        rating_label = tkinter.Label(frame, text="Rating", bg="antique white")
        rating_combobox = ttk.Combobox(frame, values=["Hated it", "It was OK", "Liked it", "Loved it", "Instant favorite"])
        rating_label.grid(row=8, column=0)
        rating_combobox.grid(row=9, column=0)

        # creates a label and a text box, which is like an entry box but bigger and allows more characters. Users can leave custom reviews in this box. 
    def create_review_textbox(self, frame):
        review_textbox_label = tkinter.Label(frame, text="Review", bg="antique white")
        review_textbox_label.grid(row=0, column=3)
        review_textbox = tkinter.Text(frame, height=5)
        review_textbox.grid(row=1, column=3, columnspan=2)

        # creates two buttons. 
    def create_buttons(self, frame):
        insert_button = ttk.Button(frame, text="Add Book") # insert is used for adding book to a text file and to the tree view which is a table in the GUI
        insert_button.grid(row=3, column=3)

        exit_button = ttk.Button(frame, text="Click here to close book entry page.", command=close_window) # closes the entry form window but not the program
        exit_button.grid(row=4, column=3)

        # treeview shows up as a table within the GUI. Let's users view their inventory from the GUI
    def create_tree_view(self):
        tree_frame = tkinter.Frame(self)
        tree_frame.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20)

        tree_scroll = tkinter.Scrollbar(tree_frame) #  lets user scroll up and down on the table
        tree_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.tree_view = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, columns=("Author First Name", "Author Last Name", "Book Title", "Genre", "Media Type", "Book Shelf"), show="headings") # table headings
        self.tree_view.pack(fill=tkinter.BOTH, expand=True)

        tree_scroll.config(command=self.tree_view.yview) # conficures the scroll bar

        # table headings
        self.tree_view.heading("Author First Name", text="Author First Name")
        self.tree_view.heading("Author Last Name", text="Author Last Name")
        self.tree_view.heading("Book Title", text="Title")
        self.tree_view.heading("Genre", text="Genre")
        self.tree_view.heading("Media Type", text="Media Type")
        self.tree_view.heading("Book Shelf", text="Book Shelf")

        # column width
        self.tree_view.column("Author First Name", pady=100)
        self.tree_view.column("Author Last Name", pady=100)
        self.tree_view.column("Book Title", pady=100)
        self.tree_view.column("Genre", pady=100)
        self.tree_view.column("Media Type", pady=100)
        self.tree_view.column("Book Shelf", pady=100)


# opens the landing page of the program
hello_window = tkinter.Tk()
hello_window.title("LittleLibro Landing Page")
hello_window.geometry("300x200")

# opens the book entry window
entry_button = ttk.Button(hello_window, text = "Click here to enter a new book.", command = create_window)
entry_button.pack(expand = True)

# closes the landing page/whole program
exit_button = ttk.Button(hello_window, text = "Click here to end application.", command = close_hello_window)
exit_button.pack(expand = True)


# needed for opening the window
hello_window.mainloop()