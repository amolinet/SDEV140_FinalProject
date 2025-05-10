>>> The purpose of this GUI application is to store your personal library in a text file. You should be able to enter the author's first and last name, the book title, and the genre. From the dropdown boxes you can assign the book to a "book-shelf", assign a media type and assign a rating.

>>> This program uses Tkinter, pillow and os. If you do not have tkinter installed, in the terminal type: pip install Tkinter do the same to install pillow. Os does not need to be installed as it is already included. 

>>> To use this application run it in your IDE. 
        1. A window should open titled "LittleLibro by ANM"
        2. In this window you can choose from three buttons:
            a. Enter a new book. This will open a new window that has an entry form. 
            b. View Book Table: This will show you the 10 most recent entries made and saved to the text file.
            c. End application: This will end the application, you can click this with the other windows open and it will kill the whole session.

        3. If you clicked on "Enter a new book." A new window titled " LittleLibro Book Entry Form" will open.
            a. In this window there will be several fields that must be filled in order to add the entry to the text file. The ONLY field that can be left blank is the rating field. 
            b. Once you have entered all required fields you can click "Add Book to .txt file" if it is successful a message box will appear saying so. If an error occurs a message box will appear with the error. 
            c. Successful book additions will also update on the book table. 
            d. If you wan to clear all of the entry boxes for any reason click "Clear Entry Boxes"
            e. If you want to clear all of the comboboxes for any reason click "Clear comboboxes."
            f. Clicking on "Close book entry page" will return you back to the first window. 

        4. If you click "View Book Table" a new window named "Books Table" will open. This will show the 10 most recent additions to the text file. If there are fewer than 10 books added it will show all of the books. 
            a. If there are duplicate books on the table then you can click on "Remove Duplicates" and that will remove the duplicate from the table and the text file. 
        


>>> The txt file will be named anm_LittleLibroInventory.txt and is included in the zip file with entries already made.
"