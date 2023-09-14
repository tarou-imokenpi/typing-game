import ctypes
from threading import Thread
from tkinter import *
from tkinter import ttk
import pandas as pd
from loguru import logger

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
        self.select_data_single_frame = Frame()
        self.single_player_frame = Frame()
        self.multi_player_frame = Frame()

        # grid setting
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.select_data_single_frame.grid(row=0, column=0, sticky="nsew")
        self.single_player_frame.grid(row=0, column=0, sticky="nsew")
        self.multi_player_frame.grid(row=0, column=0, sticky="nsew")

        self.start_flag = False
        self.quit_flag = False
        self.typed_key = "0"
        self.choiced_data = ""
        self.target_row = ""
        # -----------------------------------main_frame-----------------------------
        self.titleLabel = Label(
            self.main_frame,
            text="Typing Game",
            font=("Helvetica", "35"),
        )
        self.single_changePage = self.ttk_btn_change_frame(
            self_frame=self.main_frame,
            text="シングルプレイで始める",
            change_frame=self.select_data_single_frame,
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
        # ----------------------------select_datasets_frame(single)-----------------

        self.select_df_title = ttk.Label(
            self.select_data_single_frame,
            text="タイプするテキストを選択してください。",
            font=("Helvetica", "35"),
        )
        self.ai_text_label = ttk.Label(
            self.select_data_single_frame,
            text="テキストボックスに生成したいジャンルや単語を入力してください。",
            font=(("Helvetica", "16")),
        )
        self.use_default_data_btn = self.ttk_btn_change_frame(
            self_frame=self.select_data_single_frame,
            text="事前に用意されたテキストをランダムで出題する",
            change_frame=self.single_player_frame,
            style="back.TButton",
        )
        self.use_gpt_btn = self.ttk_btn_change_frame(
            self_frame=self.select_data_single_frame,
            text="AIでタイプテキストを生成する",
            change_frame=self.single_player_frame,
            style="back.TButton",
        )
        self.use_gpt_text_input = ttk.Entry(self.select_data_single_frame)

        # bind func
        def use_default_btn_event(event):
            # datasetsの選択
            self.choiced_data = "datasets/General Programming Terms.csv"
            self.target_row = "programming term"

        def use_gpt_btn_event(event):
            self.gpt_intput_text: str = self.use_gpt_text_input.get()
            print(self.gpt_intput_text)
            self.typing_text["text"] = "未対応(( ﾟДﾟ))"

        # bind
        self.use_gpt_btn.bind("<Button-1>", use_gpt_btn_event)
        self.use_default_data_btn.bind("<Button-1>", use_default_btn_event)

        # pack
        self.select_df_title.pack(pady=50)
        self.use_default_data_btn.pack(pady=(0, 50))
        self.ai_text_label.pack(pady=(0, 30))
        self.use_gpt_text_input.pack(pady=(0, 30))
        self.use_gpt_btn.pack()
        # --------------------------------------------------------------------------
        # ----------------------------single_player_frame---------------------------
        self.single_back_btn = self.ttk_btn_change_frame(
            self_frame=self.single_player_frame,
            text="タイトルに戻る",
            change_frame=self.main_frame,
            style="back.TButton",
        )
        self.typing_text = ttk.Label(
            self.single_player_frame,
            text="スタートするには\n開始を押してください",
            font=("Helvetica", "40"),
        )
        self.typing_start_btn = ttk.Button(
            self.single_player_frame,
            text="開始",
            style="TOP_menu.TButton",
        )
        self.typed_text = ttk.Label(
            self.single_player_frame,
            font=("Helvetica", "40"),
            foreground="#547BA8",  # font color
        )
        self.next_type_text = ttk.Label(
            self.single_player_frame,
            font=("Helvetica", "40"),
            foreground="#999999",  # font color
        )

        # bind func
        def btn_click(event):
            self.start_flag = True
            self.typing_start_btn.destroy()
            self.typing_text["font"] = ("Helvetica", "64")

        # bind
        self.typing_start_btn.bind("<Button-1>", btn_click)

        # pack
        self.single_back_btn.pack(anchor="w", padx=(10, 0), pady=(10, 0))
        self.typing_text.pack(pady=(30, 50))
        self.typing_start_btn.pack()
        self.typed_text.pack(side="left", anchor="n", padx=(500, 0))
        self.next_type_text.pack(side="left", anchor="n")

        # --------------------------------------------------------------------------
        # ----------------------------multi_player_frame---------------------------
        self.titleLabel = ttk.Label(
            self.multi_player_frame,
            text="あると思ったら大間違い(^^♪\n残念、まだありません",
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
        self.start_flag = False
        self.quit_flag = False
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
    def start_question(self):
        while not self.quit_flag:
            if self.start_flag:
                print("game start!!")
                self.create_df(csv_path=self.choiced_data)
                for i in range(self.df.size):
                    key_word: str = str.lower(self.df.at[i, self.target_row])
                    print(key_word)
                    self.typing_text["text"] = key_word
                    self.typed_text["text"] = ""
                    for j, key in enumerate(key_word):
                        self.next_type_text["text"] = key_word[j:]
                        print(f"waiting for {key}")
                        while not self.quit_flag:
                            if key == self.typed_key:
                                self.typed_text["text"] += key
                                print(key)
                                break

                self.typing_text["text"] = "スタートするには\n開始を押してください"
                self.next_type_text["text"] = ""
                self.typed_text["text"] = ""
                self.start_flag = False


if __name__ == "__main__":
    app = App()
    app.mainloop()
