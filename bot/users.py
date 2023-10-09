import os

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message

from bot import texts

users_router = Router()


@users_router.message(CommandStart(deep_link=True))
async def get_user_info(message: Message, command: CommandObject):
    args = command.args
    await message.answer(args)


@users_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(texts.GREETINGS_TEXT)


@users_router.message()
async def command_start(message: Message):
    await message.send_copy(chat_id=os.getenv('ADMIN'))
