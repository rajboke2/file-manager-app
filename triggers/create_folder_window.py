import os
import logging
import tkinter.messagebox


name_var = None


def create_folder():
    logging.info("Creating folder")
    title = "Message"
    try:
        folder_name = name_var.get()
        os.mkdir(folder_name)
        message = f"{folder_name} folder is Created..!!"
        tkinter.messagebox.showinfo(title, message)
    except Exception as e:
        logging.error(f"Error in create_folder: {e}")
        message = "Some Error Occurred TRY Again Later..!!"
        tkinter.messagebox.showerror(title, message)
