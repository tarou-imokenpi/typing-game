from tkinter import *
from tkinter import ttk


class App(Tk):
    # 呪文
    def __init__(self, *args, **kwargs):
        # 呪文
        Tk.__init__(self, *args, **kwargs)

        # ウィンドウタイトルを決定
        self.title("Tkinter change page")

        # ウィンドウの大きさを決定
        self.geometry("800x600")

        # ウィンドウのグリッドを 1x1 にする
        # この処理をコメントアウトすると配置がズレる
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # -----------------------------------main_frame-----------------------------
        # メインページフレーム作成
        self.main_frame = Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel = Label(
            self.main_frame, text="Main Page", font=("Helvetica", "35")
        )
        self.titleLabel.pack(anchor="center", expand=True)
        # フレーム1に移動するボタン
        self.changePageButton = ttk.Button(
            self.main_frame,
            text="Go to frame1",
            command=lambda: self.changePage(self.frame1),
        )
        self.changePageButton.pack()
        # --------------------------------------------------------------------------
        # -----------------------------------frame1---------------------------------
        # 移動先フレーム作成
        self.frame1 = Frame()
        self.frame1.grid(row=0, column=0, sticky="nsew")
        # タイトルラベル作成
        self.titleLabel = ttk.Label(
            self.frame1, text="Frame 1", font=("Helvetica", "35")
        )
        self.titleLabel.pack(anchor="center", expand=True)
        # フレーム1からmainフレームに戻るボタン
        self.back_button = ttk.Button(
            self.frame1, text="Back", command=lambda: self.changePage(self.main_frame)
        )
        self.back_button.pack()
        # --------------------------------------------------------------------------

        # main_frameを一番上に表示
        self.main_frame.tkraise()

    def changePage(self, page):
        """
        画面遷移用の関数
        """
        page.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
