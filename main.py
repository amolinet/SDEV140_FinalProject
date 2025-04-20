import tkinter
from tkinter import ttk


window = tkinter.Tk()
window.title = ("LittleLibro Book Entry Form")

frame = tkinter.Frame(window)
frame.pack()

book_info_frame =tkinter.LabelFrame(frame, text="Book Information")
book_info_frame.grid(row = 0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(book_info_frame, text="Author First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(book_info_frame
                                , text = "Author Last Name")
last_name_label.grid(row=0, column = 1)


first_name_entry = tkinter.Entry(book_info_frame)
last_name_entry = tkinter.Entry(book_info_frame)
first_name_entry.grid(row=1, column =0)
last_name_entry.grid(row=1, column=1)


media_type_label = tkinter.Label(book_info_frame, text="Media Type")
media_type_combobox = ttk.Combobox(book_info_frame, values =["Audiobook", "eBook", "Physical Copy"])
media_type_label.grid(row=0, column=2)
media_type_combobox.grid(row=1, column=2)

book_title_label = tkinter.Label(book_info_frame,text="Book title")
book_title_entry = tkinter.Entry(book_info_frame)
book_title_label.grid(row = 2, column = 0)
book_title_entry.grid(row = 3, column = 0)

genre_label = tkinter.Label(book_info_frame, text="Genre")
genre_entry = tkinter.Entry(book_info_frame)
genre_label.grid(row= 2, column = 1)
genre_entry.grid(row = 3, column = 1)

book_list_label = tkinter.Label(book_info_frame, text="Book Shelf")
book_list_combobox = ttk.Combobox(book_info_frame, values =["Read", "To-Read", "Did Not Finish", "Reading"])
book_list_label.grid(row = 2, column = 2)
book_list_combobox.grid(row = 3, column = 2)

rating_label = tkinter.Label(book_info_frame, text="Rating")
rating_combobox = ttk.Combobox(book_info_frame, values = ["Hated it", "It was OK", "Liked it", "Loved it", "Instant favorite"])
rating_label.grid(row = 4, column = 0)
rating_combobox.grid(row = 5, column = 0)


for widget in book_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 10)


window.mainloop()