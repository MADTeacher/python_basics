import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv

from database.init_database import init_database
from missedbot import bot

load_dotenv()


async def main():
    init_database()
    path = Path.cwd()
    Path(path.joinpath(
        os.getenv("TEMP_REPORT_DIR")
    )).mkdir(parents=True, exist_ok=True)
    await asyncio.gather(
        bot.infinity_polling(request_timeout=90),
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
