import tkinter as tk

class Paint(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		
		self.canvas = tk.Canvas(self, bg="white")
		self.canvas.pack(fill=tk.BOTH, expand=True)

		
		self.canvas.bind("<B1-Motion>", self.draw_pixel)

		self.selected = tk.IntVar(value=1)

		
		self.choose_color_menu = tk.Menu(self, tearoff=0)
		color_menu = tk.Menu(self.choose_color_menu, tearoff=0)
		color_menu.add_radiobutton(label="Чорний", command=self.set_black_color, value=1, variable=self.selected)
		
		color_menu.add_radiobutton(label="Синій", command=self.set_blue_color, value=2, variable=self.selected)
		
		color_menu.add_radiobutton(label="Жовтий", command=self.set_yellow_color, value=3, variable=self.selected)
		color_menu.add_command(label="Очистити", command=self.set_white_color)
	
			
		self.choose_color_menu.add_cascade(label="Колір", menu=color_menu)
		
		self.master.config(menu=self.choose_color_menu)

	def draw_pixel(self, event):
		selected = self.selected.get()
		if selected ==1:
			color = "black"
		elif selected == 2:
			color = "blue"
		elif selected ==3:
			color = "yellow"
		else:
			color = "black"
		x,y = event.x, event.y
		self.canvas.create_rectangle(x,y,x+1,y+1, fill=color, width=2, outline=color)


	def set_black_color(self):
		self.selected.set(1)
		self.update_idletasks()

	def set_white_color(self):
		self.canvas.delete("all")

	def set_blue_color(self):
		self.selected.set(2)

		self.update_idletasks()
	def set_yellow_color(self):
		self.selected.set(3)

		self.update_idletasks()
