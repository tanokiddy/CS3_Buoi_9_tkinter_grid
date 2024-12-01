import customtkinter

customtkinter.set_appearance_mode('system')

root = customtkinter.CTk()
root.geometry('400x400')
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# grid()
yellow = customtkinter.CTkFrame(master=root, fg_color='yellow', corner_radius=0, border_width=0)
yellow.grid(column=0, sticky="WENS")

red = customtkinter.CTkFrame(master=root, fg_color='red', corner_radius=0, border_width=0)
red.grid(column=1, row=0, sticky="WENS")

gray = customtkinter.CTkFrame(master=root, fg_color='gray', corner_radius=0, border_width=0)
gray.grid(column=0, row=1, sticky="WENS")

blue = customtkinter.CTkFrame(master=root, fg_color='blue', corner_radius=0, border_width=0)
blue.grid(column=1, row=1, sticky="WENS")


root.mainloop()