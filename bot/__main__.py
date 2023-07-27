import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from sqlalchemy import create_engine, URL

from bot.commands.bot_commands import bot_commands
from commands import reg_user_commands


async def main() -> None:
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host="127.0.0.1",
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )

    engine = create_engine(postgres_url)
    engine.connect()
    print(engine)
    logging.basicConfig(level=logging.DEBUG)
    dp = Dispatcher()
    bot = Bot(os.getenv("TELEGRAM_KITCHEN_API"))
    await bot.set_my_commands(commands=commands_for_bot)

    reg_user_commands(router=dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print("Bot stopped")
