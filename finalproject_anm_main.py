# m08 - Final Project - LittleLibro Personal Library Tracker
# auther:  ANM
# created 2025-04-09
# updated 2025-04-27
# IDE used: Visual Studio Code
# CODING ASSISTANCE WAS USED to create this program
    # Code Assistance Website - https://www.youtube.com/watch?v=8m4uDS_nyCk aided in pulling data entry and adding to an excel file
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

# is used to open/create an excel file that holds data.
import openpyxl 


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
class Main_Window_Class (tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('LittleLibro Book Entry Form')
        self.geometry('1225x625')
        frame = tkinter.Frame(self, height=1025, bg="pink")
        frame.pack(fill=tkinter.X)

        # creates a frame within "frame"
        book_info_frame =tkinter.LabelFrame(master=frame, text="Entry Form", bg = "antique white")
        book_info_frame.grid(row = 0, column=0, padx=20, pady=20)

        # creates entry widget for author's first and last name also places them within grid
        author_info_label = tkinter.Label(book_info_frame, text="Author Information", bg = "antique white")
        author_info_label.grid(row = 0, column = 0)
        
        first_name_entry = tkinter.Entry(book_info_frame)
        first_name_entry.grid(row=1, column =0)
        first_name_entry.insert(0, "Author's First Name")
        first_name_entry.bind("<FocusIn>", lambda e: first_name_entry.delete("0", "end")) # deletes the entry so that user can type whatever they want
        
        last_name_entry = tkinter.Entry(book_info_frame)
        last_name_entry.insert(0, "Author's Last Name")
        last_name_entry.bind("<FocusIn>", lambda e: last_name_entry.delete("0", "end"))
        last_name_entry.grid(row=1, column=1)

        # creates label and combobox widget for media type also places them within the grid
        media_type_label = tkinter.Label(book_info_frame, text="Media Type", bg = "antique white")
        media_type_combobox = ttk.Combobox(book_info_frame, values =["Audiobook", "eBook", "Physical Copy"])
        media_type_label.grid(row=4, column=0)  
        media_type_combobox.grid(row=5, column=0)

        # creates label and entry widget for book title, places them in the grid
        book_info_label = tkinter.Label(book_info_frame, text="Book Information", bg = "antique white")
        book_info_label.grid(row = 2, column = 0)
        book_title_entry = tkinter.Entry(book_info_frame)
        book_title_entry.insert(0, "Enter Book Title")
        book_title_entry.bind("<FocusIn>", lambda e: book_title_entry.delete("0", "end"))
        book_title_entry.grid(row = 3, column = 0)

        # creates label and entry widget for genre, places within the grid
        genre_entry = tkinter.Entry(book_info_frame)
        genre_entry.insert(0, "Enter genre")
        genre_entry.bind("<FocusIn>", lambda e: genre_entry.delete("0", "end"))
        genre_entry.grid(row = 3, column = 1)

        # creates label and combobox widget for adding book to a book list
        book_list_label = tkinter.Label(book_info_frame, text="Book Shelf",bg = "antique white" )
        book_list_combobox = ttk.Combobox(book_info_frame, values =["Read", "To-Read", "Did Not Finish", "Reading"])
        book_list_label.grid(row = 6, column = 0)
        book_list_combobox.grid(row = 7, column = 0)

        # creates label and combobox widget for ratings
        rating_label = tkinter.Label(book_info_frame, text="Rating", bg = "antique white")
        rating_combobox = ttk.Combobox(book_info_frame, values = ["Hated it", "It was OK", "Liked it", "Loved it", "Instant favorite"])
        rating_label.grid(row = 8, column = 0)
        rating_combobox.grid(row = 9, column = 0)

        # creates label and textbox for user reviews of books
        review_textbox_label = tkinter.Label(book_info_frame, text="Review", bg = "antique white")
        review_textbox_label.grid(row=0, column=3)
        review_textbox = tkinter.Text(book_info_frame, height = 5)
        review_textbox.grid(row=1, column=3, columnspan=2)

        # insert entry into table button
        insert_button = ttk.Button(book_info_frame, text = "Add Book", command=insert_book)
        insert_button.grid(row = 3, column= 3)

        exit_button = ttk.Button(book_info_frame, text = "Click here to close book entry page.", command = close_window)
        exit_button.grid(row=4, column=3)

        # for loop that spaces out the widgets evenly
        for widget in book_info_frame.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)
    
        # inserts entry into table
        def insert_book(): # STILL WORKING ON THIS; GOAL IS TO MAKE THIS FUNCTION THE COMMAND FOR THE INSERT_BUTTON
            # retrieve entry data
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            book_title = book_title_entry.get()
            genre = genre_entry.get()
            media_type = media_type_combobox.get()
            book_shelf = book_list_combobox.get()
            rating = rating_combobox.get()
            review = review_textbox.get()

            # insert into excel sheet

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