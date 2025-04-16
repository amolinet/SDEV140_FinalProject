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


window.mainloop()