import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('400x400')

# pack()
row1 = customtkinter.CTkFrame(master=root, fg_color='transparent', bg_color='transparent', corner_radius=0, border_width=0)
row1.pack(side='top', expand=True, fill='both')
yellow = customtkinter.CTkFrame(master=row1, fg_color='yellow', corner_radius=0, border_width=0)
yellow.pack(side='left', expand=True, fill='both')

red = customtkinter.CTkFrame(master=row1, fg_color='red', corner_radius=0, border_width=0)
red.pack(side='right', expand=True, fill='both')

row2 = customtkinter.CTkFrame(master=root, fg_color='transparent', corner_radius=0, border_width=0)
row2.pack(side='bottom', expand=True, fill='both')
gray = customtkinter.CTkFrame(master=row2, fg_color='gray', corner_radius=0, border_width=0)
gray.pack(side='left', expand=True, fill='both')

blue = customtkinter.CTkFrame(master=row2, fg_color='blue', corner_radius=0, border_width=0)
blue.pack(side='right', expand=True, fill='both')


root.mainloop()