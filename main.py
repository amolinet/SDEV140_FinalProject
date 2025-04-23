# m08 - Final Project - LittleLibro Personal Library Tracker
# auther:  ANM
# created 2025-04-09
# updated 2025-04-22
# IDE used: Visual Studio Code


# imports tkinter modules
import tkinter
from tkinter import ttk

# creates a new window and gives it the title "LittleLibro Book Entry Form
window = tkinter.Tk()
window.title = ("LittleLibro Book Entry Form")

# creates the main frame
frame = tkinter.Frame(master=window, height=100, bg="pink")
frame.pack(fill=tkinter.X)

# creates a frame within "frame"
book_info_frame =tkinter.LabelFrame(master=frame, text="Book Information", bg = "antique white")
book_info_frame.grid(row = 0, column=0, padx=20, pady=20)

# creates label's for Author's first and last names also places them within the grid
first_name_label = tkinter.Label(book_info_frame, text="Author First Name", bg = "antique white")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(book_info_frame, text = "Author Last Name", bg = "antique white")
last_name_label.grid(row=0, column = 1)

# creates entry widget for author's first and last name also places them within grid
first_name_entry = tkinter.Entry(book_info_frame)
last_name_entry = tkinter.Entry(book_info_frame)
first_name_entry.grid(row=1, column =0)
last_name_entry.grid(row=1, column=1)

# creates label and combobox widget for media type also places them within the grid
media_type_label = tkinter.Label(book_info_frame, text="Media Type", bg = "antique white")
media_type_combobox = ttk.Combobox(book_info_frame, values =["Audiobook", "eBook", "Physical Copy"])
media_type_label.grid(row=0, column=2)
media_type_combobox.grid(row=1, column=2)

# creates label and entry widget for book title, places them in the grid
book_title_label = tkinter.Label(book_info_frame,text="Book title", bg = "antique white")
book_title_entry = tkinter.Entry(book_info_frame)
book_title_label.grid(row = 2, column = 0)
book_title_entry.grid(row = 3, column = 0)

# creates label and entry widget for genre, places within the grid
genre_label = tkinter.Label(book_info_frame, text="Genre", bg = "antique white")
genre_entry = tkinter.Entry(book_info_frame)
genre_label.grid(row= 2, column = 1)
genre_entry.grid(row = 3, column = 1)

# creates label and combobox widget for adding book to a book list
book_list_label = tkinter.Label(book_info_frame, text="Book Shelf",bg = "antique white" )
book_list_combobox = ttk.Combobox(book_info_frame, values =["Read", "To-Read", "Did Not Finish", "Reading"])
book_list_label.grid(row = 2, column = 2)
book_list_combobox.grid(row = 3, column = 2)

# creates label and combobox widget for ratings
rating_label = tkinter.Label(book_info_frame, text="Rating", bg = "antique white")
rating_combobox = ttk.Combobox(book_info_frame, values = ["Hated it", "It was OK", "Liked it", "Loved it", "Instant favorite"])
rating_label.grid(row = 4, column = 0)
rating_combobox.grid(row = 5, column = 0)

# creates label and textbox for user reviews of books
review_textbox_label = tkinter.Label(book_info_frame, text="Review", bg = "antique white")
review_textbox_label.grid(row=5, column=1)
review_textbox = tkinter.Text(book_info_frame)
review_textbox.grid(row=6, column=1, columnspan=2)

# for loop that spaces out the widgets evenly
for widget in book_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 10)

# needed for opening the window
window.mainloop()