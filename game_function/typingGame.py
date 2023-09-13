import keyboard
import pandas as pd
from loguru import logger
import asyncio


class typingGame:
    def __init__(self, path: str) -> None:
        self.df = pd.read_csv(path)

    async def read_key_async(self, key_word: str):
        print(key_word)
        for key in key_word:
            logger.info(f"waiting for {key}")
            while True:
                event = await asyncio.to_thread(keyboard.read_event)
                if event.event_type == keyboard.KEY_DOWN and event.name == key:
                    logger.debug(f"pressed {event.name}")
                    break

        logger.debug("key_word OK")

    async def start(self, datasets_name: str) -> None:
        str_size = self.df.size
        for i in range(str_size):
            key_word: str = self.df.at[i, datasets_name]
            await self.read_key_async(key_word)

        logger.debug("finish game")


async def start_game():
    game = typingGame(path=r"datasets\PG_lang.csv")

    await game.start(datasets_name="lang")


# asyncio.run(start_game())
