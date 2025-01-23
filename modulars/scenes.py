import tkinter as tk


class Paint(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = PaintCanvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>",
                         lambda event: self.canvas.draw_pixel(event, sub_color_menu.selected_variable.get(), brash_size_menu.selected_variable.get()))


        self.main_menu = tk.Menu(self, tearoff=0)








        sub_color_menu = Submenu(self.main_menu, tearoff=0)
        sub_color_menu.add_radiobutton(label="Чорний", command=lambda: sub_color_menu.set_variable(1), value=1,
                                       variable=sub_color_menu.selected_variable)
        sub_color_menu.add_radiobutton(label="Синій", command=lambda: sub_color_menu.set_variable(2), value=2,
                                       variable=sub_color_menu.selected_variable)
        sub_color_menu.add_radiobutton(label="Жовтий", command=lambda: sub_color_menu.set_variable(3), value=3,
                                       variable=sub_color_menu.selected_variable)
        sub_color_menu.add_command(label="Очистити", command=self.set_clean_all)

        self.main_menu.add_cascade(label="Колір", menu=sub_color_menu)

        brash_size_menu = Submenu(self.main_menu, tearoff=0)
        brash_size_menu.add_radiobutton(label="1 піксель", command=lambda: brash_size_menu.set_variable(1), value=1,
                                        variable=brash_size_menu.selected_variable)
        brash_size_menu.add_radiobutton(label="10 піксель", command=lambda: brash_size_menu.set_variable(2), value=2,
                                        variable=brash_size_menu.selected_variable)
        brash_size_menu.add_radiobutton(label="25 піксель", command=lambda: brash_size_menu.set_variable(3), value=3,
                                        variable=brash_size_menu.selected_variable)
        brash_size_menu.add_radiobutton(label="50 піксель", command=lambda: brash_size_menu.set_variable(4), value=4,
                                        variable=brash_size_menu.selected_variable)

        self.main_menu.add_cascade(label="Розмір", menu=brash_size_menu)

        self.master.config(menu=self.main_menu)

    def set_clean_all(self):
        self.canvas.delete("all")





class Submenu(tk.Menu):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.selected_variable: tk.IntVar = tk.IntVar(value=1)

    def set_variable(self, new_value):
        self.selected_variable.set(new_value)
        self.update_idletasks()


class PaintCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def draw_pixel(self, event, color_selected: int, brash_selected: int):

        if color_selected == 1:
            color = "black"
        elif color_selected == 2:
            color = "blue"
        elif color_selected == 3:
            color = "yellow"
        else:
            color = "black"

        if brash_selected == 1:
            size = 1
        elif brash_selected == 2:
            size = 10
        elif brash_selected == 3:
            size = 25
        elif brash_selected == 4:
            size = 50
        else:
            size = 1

        x, y = event.x, event.y
        self.create_rectangle(x, y, x, y, fill=color, width=size, outline=color)




