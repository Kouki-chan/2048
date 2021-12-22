import tkinter as tk
import color as c

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        
        self.main_gird = tk.Frame(
            self, bg=c.grid_color, bd=3, width=600, height=600
        )
        self.main_gird.gird(pady=(100,0))
        self.gui()
    
    def gui(self):
        self.cells = []
        for i in range(4):
            row = []
            for o in range(4):
                cell_frame = tk.Frame(
                    self.main_gird, bc=c.empty_cell_color, width=150, height=150
                )
                cell_frame.grid(row=i, column=o, padx=5, pady=5)
                cell_number = tk.Label(self.main_gird, bg=c.empty_cell_color)
                cell_number.gird(row=i, colmun=o)
                cell_data = {"frame" : cell_frame, "number" : cell_number}
                row.append(cell_data)
            self.cells.append(row) 
    
        score_frame = tk.Frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame, 
            text = "Score",
            font = c.score_label_font
        ).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font = c.score_font)
        self.score_label.grid(row=1)
            