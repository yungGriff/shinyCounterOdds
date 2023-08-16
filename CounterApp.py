import tkinter as tk



class NumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Counter")
        self.root.configure(bg="black")

        self.number = 0
        self.label = tk.Label(root, text=str(self.number), font=("Courier New", 512), fg="green", bg="black")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label2 = tk.Button(root, text="Your Current Odds:", command=self.what_odds, font=("Helvetica", 32),
                                fg="green", bg="black")
        self.label2.grid(row=3, column=0, columnspan=2, sticky="nsew")

        self.increment_plus = tk.Button(root, text="+", command=self.increment_by_10, font=("Helvetica", 32),
                                        fg="green", bg="black")
        #self.increment_plus.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        self.increment_minus = tk.Button(root, text="-", command=self.decrement_by_10, font=("Helvetica", 32),
                                         fg="green", bg="black")
        #self.increment_minus.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        self.root.bind("<Button-1>", self.increase_number)
        self.root.bind("<Button-3>", self.decrease_number)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=2)

        self.update_label()
        self.root.bind("<Configure>", self.on_window_resize)
    def increase_number(self, event):
        self.number += 1
        self.update_label()

    def decrease_number(self, event):
        self.number -= 1
        self.update_label()

    def update_label(self):
        self.label.config(text=str(self.number))
        self.what_odds()

    def what_odds(self):
        full = (self.number / 4096) * 100
        charm = (self.number / 2044) * 100
        matsuda = (self.number / 682) * 100
        charmtsuda = (self.number / 512) * 100
        """
        fullText = full
        charmText = charm
        matsudaText = matsuda
        charmtsudaText = charmtsuda
        odds_text = "" + fullText + "\n" + charmText + "\n" + matsudaText + "\n" + charmtsudaText + ""
        """
        odds_text = (
            f"Full Odds: {full:.2f}%\n"
            f"Shiny Charm Odds: {charm:.2f}%\n"
            f"Matsuda Method Odds: {matsuda:.2f}%\n"
            f"Shiny Charm + Matsuda Method Odds: {charmtsuda:.2f}%"
        )
        self.label2.config(text=odds_text)

    def increment_by_10(self):
        self.number += 9
        self.update_label()

    def decrement_by_10(self):
        self.number -= 9
        self.update_label()

    def on_window_resize(self, event):
        app_width = self.root.winfo_width()
        app_height = self.root.winfo_height()
        button_size = 50
        self.increment_plus.place(x=app_width - button_size, rely=0.4, anchor="e", width=button_size,
                                  height=button_size)

        self.increment_minus.place(x=app_width - button_size, rely=0.5, anchor="e", width=button_size,
                                   height=button_size)


if __name__ == "__main__":
    root = tk.Tk()
    app = NumberApp(root)

    root.geometry("1000x800")

    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    app_width = 1000
    app_height = 800
    x_position = (screen_width - app_width) // 2
    y_position = (screen_height - app_height) // 2

    root.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
    #button_size = app_height // 10
    button_size = 50
    
    app.increment_plus.place(x=app_width - button_size, y=(app_height - button_size) // 2, width=button_size,
                             height=button_size)
    app.increment_minus.place(x=app_width - button_size, y=(app_height + button_size) // 2, width=button_size,
                              height=button_size)
   
    app.increment_plus.place(x=app_width - button_size, rely=0.5, anchor="e", width=button_size, height=button_size)
    app.increment_minus.place(x=app_width - button_size, rely=0.5, anchor="e", width=button_size, height=button_size)
    """
    root.mainloop()
