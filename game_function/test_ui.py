import customtkinter as ct

app = ct.CTk()
app.title("test app")
app.geometry("400x400")


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.button = ct.CTkButton(self, text="クリックしてください", command=self.button_click)
        self.counter = ct.CTkLabel(self, text="0", font=("", 20))
        self.button.grid(row=0, column=0, padx=20, pady=20)
        self.counter.grid(row=0, column=1, padx=20, pady=20)

    def button_click(self):
        print("ボタンがクリックされました。")
        self.count += 1
        self.counter.configure(text=self.count)


app = App()
app.mainloop()
