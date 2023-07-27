__all__ = ['reg_user_commands', 'bot_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.commands.help import help_command
from bot.commands.recept_commands import random_recept, recept_with_param
from bot.commands.start import start_command


def reg_user_commands(router: Router):
    router.message.register(start_command, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(random_recept, F.text == 'Случайный рецепт')
    router.message.register(recept_with_param, F.text == 'Рецепт из имеющегося')

