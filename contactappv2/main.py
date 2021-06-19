import tkinter as tk
from tkinter import messagebox as msg

from settings import Settings
from appPage import AppPage

class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_container()
		self.create_menus()

		self.pages = {}
		self.create_appPage()

	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_menus(self):
		self.menu_bar = tk.Menu(self)
		self.configure(menu=self.menu_bar)

		self.filemenu = tk.Menu(self.menu_bar, tearoff=0)
		self.filemenu.add_command(label="Exit", command=self.exit)

		self.helpmenu = tk.Menu(self.menu_bar, tearoff=0)
		self.helpmenu.add_command(label="About", command=self.about)
		self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
		self.theme_menu.add_command(label="Black Mode", command=self.black_mode)
		self.theme_menu.add_command(label="White Mode", command=self.white_mode)

		self.menu_bar.add_cascade(label="File", menu=self.filemenu)
		self.menu_bar.add_cascade(label="Help", menu=self.helpmenu)
		self.menu_bar.add_cascade(label="Mode", menu=self.theme_menu)

	def about(self):
		msg.showinfo("About App", "Alamat : Jln.Sudirman\nPemilik Apotek : Andi\nBuka dari 08.00 - 22.00")

	def exit(self):
		quit()

	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)

	def black_mode(self):
		self.pages['appPage'].bg = "black"
		self.pages['appPage'].fg = "white"

		self.recreate()

	def white_mode(self):
		self.pages['appPage'].bg = "white"
		self.pages['appPage'].fg = "black"

		self.recreate()

	def recreate(self):

		self.pages['appPage'].left_frame.destroy()
		self.pages['appPage'].right_frame.destroy()

		self.pages['appPage'].create_left_frame()
		self.pages['appPage'].create_right_frame()


class ContactApp:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()

