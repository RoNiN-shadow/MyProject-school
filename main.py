import tkinter as tk

from modulars.scenes import Paint
class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Paint")
		self.geometry("640x480")
		
		paint = Paint(self)
		paint.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
	app = App()
	app.mainloop()
