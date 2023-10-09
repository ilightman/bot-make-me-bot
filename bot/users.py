import os

from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.methods import SendMessage
from aiogram.types import Message

from bot import texts
from bot.functions import send_news_to_admin

users_router = Router()


@users_router.message(CommandStart())
async def command_start(message: Message, command: CommandObject):
    if command.args == 'fdaa':
        # TODO здесь фиксируем что это по qr коды с машины заход
        await SendMessage(chat_id=os.getenv('ADMIN'), text=f'QR машина {command.args}')
    await message.answer(texts.GREETINGS_TEXT)


@users_router.message()
async def command_start(message: Message):
    await send_news_to_admin(message=message, admin_id=int(os.getenv('ADMIN')))
