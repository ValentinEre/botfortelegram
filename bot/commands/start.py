import asyncpg
from aiogram import types
from aiogram.utils.keyboard import (ReplyKeyboardBuilder, KeyboardButton)


async def start_command(message: types.Message) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.row(
        KeyboardButton(
            text='Случайный рецепт'
        ),
        KeyboardButton(
            text='Рецепт из имеющегося'
        )
    )

    await message.answer(
        'Выберите кнопку',
        reply_markup=menu_builder.as_markup(resize_keyboard=True),
    )
