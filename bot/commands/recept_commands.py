from aiogram import types


async def random_recept(message: types.Message):
    await message.answer(
        'random_recept'
    )


async def recept_with_param(message: types.Message):
    await message.answer(
        'recept_with_param'
    )
