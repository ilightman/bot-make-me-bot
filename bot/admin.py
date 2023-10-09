import logging
import os

from aiogram import Router, F
from aiogram.exceptions import TelegramForbiddenError
from aiogram.filters import Command
from aiogram.types import Message

from bot.filters import ChatTypeFilter

admin_router = Router()


@admin_router.message(F.from_user.id == os.getenv('ADMIN'), Command("help"), ChatTypeFilter(chat_type=['private']))
async def admin_start(message: Message) -> None:
    await message.answer('help admin')


@admin_router.message(F.from_user.id == os.getenv('ADMIN'))
async def any_message_from_admin(message: Message):
    await message.answer('any message')


@admin_router.message(ChatTypeFilter(chat_type=['group', 'supergroup']))
async def safety_filter(message: Message) -> None:
    """При добавлении в группы - выходит из них"""
    try:
        await message.chat.leave()
    except TelegramForbiddenError:
        logging.info(msg='leaving_chat')
