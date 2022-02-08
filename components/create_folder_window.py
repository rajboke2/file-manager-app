import tkinter as t
import triggers.create_folder_window as triggers
import constants.create_folder_window as const


def tk_create_folder():
    main_window = t.Tk()
    main_window.geometry(f"{const.MAIN_WINDOW_W}x{const.MAIN_WINDOW_H}")

    heading = t.Label(main_window, text=const.HEADING_TEXT, pady=const.HEADING_PADY,
                      bg=const.HEADING_BG, fg=const.HEADING_FG, font=const.HEADING_FONT)
    heading.pack(fill=t.X)

    frame1 = t.LabelFrame(main_window, padx=const.FRAME1_PADX, pady=const.FRAME1_PADY, bg=const.FRAME1_BG)
    frame1.pack(fill=t.X)

    title = t.Label(frame1, text=const.TITLE_TEXT, bg=const.TITLE_BG, pady=const.TITLE_PADY,
                    font=const.TITLE_FONT)
    title.pack()
    triggers.name_var = t.StringVar()
    e1 = t.Entry(frame1, textvariable=triggers.name_var, bg=const.ENTRY_BG, fg=const.ENTRY_FG)
    e1.pack(fill=t.X)

    frame2 = t.Frame(main_window, bg=const.FRAME2_BG, padx=const.FRAME2_PADX, pady=const.FRAME1_PADY)
    frame2.pack(fill=t.X)

    b1 = t.Button(frame2, text=const.BUTTON_TEXT, width=const.BUTTON_W, height=const.BUTTON_H,
                  activebackground=const.BUTTON_ACTIVE_BG, command=triggers.create_folder,
                  bg=const.BUTTON_BG)
    b1.pack()

    main_window.mainloop()
