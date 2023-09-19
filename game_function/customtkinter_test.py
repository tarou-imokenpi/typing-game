import customtkinter as ct


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        # window title
        self.title("AI-based-question-typing-game")

        # window size
        # self.geometry("1200x800")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create frame
        self.main_f = ct.CTkFrame(self)
        self.select_data_single_f = ct.CTkFrame(self)
        self.single_player_f = ct.CTkFrame(self)
        self.multi_player_f = ct.CTkFrame(self)

        # grid setting
        self.main_f.grid(row=0, column=0, sticky="nsew")
        self.select_data_single_f.grid(row=0, column=0, sticky="nsew")
        self.single_player_f.grid(row=0, column=0, sticky="nsew")
        self.multi_player_f.grid(row=0, column=0, sticky="nsew")

        self.main_title = ct.CTkLabel(self.main_f, text="Typing Game")

        # 配置
        self.main_title.grid(row=0, column=0)


app = App()
app.mainloop()
