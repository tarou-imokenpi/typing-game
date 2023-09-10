import keyboard
import pandas as pd
from loguru import logger


class typingGame:
    def __init__(self, path: str) -> None:
        self.df = pd.read_csv(path)

    @staticmethod
    def __read_key(key: str) -> None:
        while True:
            if keyboard.read_key() == key:
                logger.debug(f"plessed {key}")
                break

    @staticmethod
    def __get_KeyWord_input(key_word: str) -> None:
        print(key_word)
        for i in key_word:
            logger.info(f"waiting for {i}")
            typingGame.__read_key(key=i)

        logger.debug("key_word OK")

    def __get_KeyWord(self, i, datasets_name) -> str:
        key_word: str = self.df.at[i, datasets_name]
        return key_word

    def start(self, datasets_name: str) -> None:
        str_size = self.df.size
        for i in range(str_size):
            typingGame.__get_KeyWord_input(self.__get_KeyWord(i, datasets_name))

        logger.debug("finish game")


game = typingGame(path=r"datasets\PG_lang.csv")

game.start(datasets_name="lang")
