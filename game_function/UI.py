import asyncio
import ctypes
from concurrent.futures import ThreadPoolExecutor
from tkinter import *
from tkinter import ttk
from threading import Thread
import keyboard
import pandas as pd
from loguru import logger
from typingGame import typingGame

# 高DPIに設定
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception:
    pass


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # window title
        self.title("AI-based-question-typing-game")

        # window size
        self.geometry("1200x800")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ttk button style
        style = ttk.Style()
        style.configure("TOP_menu.TButton", font=("Helvetica", 26))
        style.configure("back.TButton", font=("Helvetica", 16))

        # create frame
        self.main_frame = Frame()
        self.single_player_frame = Frame()
        self.multi_player_frame = Frame()

        # grid setting
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.single_player_frame.grid(row=0, column=0, sticky="nsew")
        self.multi_player_frame.grid(row=0, column=0, sticky="nsew")

        self.start_flag = False
        self.quit_flag = False
        self.typed_key = "0"
        # -----------------------------------main_frame-----------------------------
        self.titleLabel = Label(
            self.main_frame,
            text="Typing Game",
            font=("Helvetica", "35"),
        )
        self.single_changePage = self.ttk_btn_change_frame(
            self_frame=self.main_frame,
            text="シングルプレイで始める",
            change_frame=self.single_player_frame,
            style="TOP_menu.TButton",
        )
        self.multi_changePage = self.ttk_btn_change_frame(
            self_frame=self.main_frame,
            text="マルチプレイで始める",
            change_frame=self.multi_player_frame,
            style="TOP_menu.TButton",
        )

        # pack
        self.titleLabel.pack(anchor="center", pady=(50, 0))
        self.single_changePage.pack(pady=(200, 0), ipadx=150, ipady=10)
        self.multi_changePage.pack(pady=(50, 0), ipadx=166, ipady=10)

        # --------------------------------------------------------------------------
        # ----------------------------single_player_frame---------------------------
        self.titleLabel = ttk.Label(
            self.single_player_frame,
            text="Frame 1",
            font=("Helvetica", "35"),
        )
        self.single_back_btn = self.ttk_btn_change_frame(
            self_frame=self.single_player_frame,
            text="タイトルに戻る",
            change_frame=self.main_frame,
            style="back.TButton",
        )
        self.typing_text = ttk.Label(
            self.single_player_frame,
            text="スタートするには開始を押してください",
            font=("Helvetica", "26"),
        )
        self.typing_start_btn = ttk.Button(
            self.single_player_frame,
            text="開始",
        )

        def btn_click(event):
            self.start_flag = True

        self.typing_start_btn.bind("<Button-1>", btn_click)

        # pack
        self.single_back_btn.pack(anchor="w", padx=(10, 0), pady=(10, 0))
        self.typing_text.pack()
        self.typing_start_btn.pack()

        # --------------------------------------------------------------------------
        # ----------------------------multi_player_frame---------------------------
        self.titleLabel = ttk.Label(
            self.multi_player_frame,
            text="Frame 1",
            font=("Helvetica", "35"),
        )
        self.multi_back_btn = self.ttk_btn_change_frame(
            self_frame=self.multi_player_frame,
            text="タイトルに戻る",
            change_frame=self.main_frame,
            style="back.TButton",
        )

        # pack
        self.multi_back_btn.pack(anchor="w", padx=(10, 0), pady=(10, 0))
        self.titleLabel.pack(anchor="center", expand=True)

        # --------------------------------------------------------------------------
        self.bind("<KeyPress>", self.key_event)
        # raise main_frame
        self.main_frame.tkraise()

        thread1 = Thread(target=self.start_question, daemon=True)
        thread1.start()

    def changePage(self, page):
        page.tkraise()

    # 共通コンポーネント
    def ttk_btn_change_frame(self, self_frame, text, change_frame, style=None):
        if style:
            btn = ttk.Button(
                self_frame,
                text=text,
                style=style,
                command=lambda: self.changePage(change_frame),
            )
        else:
            btn = ttk.Button(
                self_frame,
                text=text,
                command=lambda: self.changePage(change_frame),
            )
        return btn

    # typing game

    # read key
    def key_event(self, e):
        self.typed_key: str = e.keysym

    # create data frame
    def create_df(self, csv_path: str = None, excel_path: str = None):
        if csv_path:
            self.df = pd.read_csv(csv_path)
        elif excel_path:
            self.df = pd.read_excel(excel_path)

    # start question
    def start_question(self, target_row="lang"):
        while not self.quit_flag:
            if self.start_flag:
                print("game start!!")
                self.create_df(csv_path=r"datasets\PG_lang.csv")
                data_size = self.df.size
                for i in range(data_size):
                    key_word: str = self.df.at[i, target_row]
                    print(key_word)
                    self.typing_text["text"] = key_word
                    for key in key_word:
                        print(f"waiting for {key}")
                        while True:
                            if key == self.typed_key:
                                print(key)
                                break
                print("finish game")
                self.start_flag = False


if __name__ == "__main__":
    app = App()
    app.mainloop()
