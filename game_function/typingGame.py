import keyboard
import pandas as pd
from loguru import logger
import asyncio


class typingGame:
    def __init__(self, path: str) -> None:
        self.df = pd.read_csv(path)

    async def read_key_async(key_word: str) -> None:
        print(key_word)
        for key in key_word:
            logger.info(f"waiting for {key}")
            while True:
                event = await asyncio.to_thread(keyboard.read_event)

                if event.event_type == keyboard.KEY_DOWN and event.name == key:
                    logger.debug(f"pressed {event.name}")
                    break

        logger.debug("key_word OK")

    def get_type_text(self, i, datasets_name) -> str:
        key_word: str = self.df.at[i, datasets_name]
        return key_word

    async def start(self, datasets_name: str) -> None:
        str_size = self.df.size
        for i in range(str_size):
            await typingGame.read_key_async(self.get_type_text(i, datasets_name))

        logger.debug("finish game")


async def start_game():
    game = typingGame(path=r"datasets\PG_lang.csv")

    await game.start(datasets_name="lang")


asyncio.run(start_game())
