import zoneinfo
from datetime import datetime

from aiogram.methods import SendMessage
from aiogram.types import Message


async def send_news_to_admin(message: Message, admin_id: int) -> None:
    """Отправляет сообщение из предложки Админу"""
    bot = message.bot
    time = datetime.now(tz=zoneinfo.ZoneInfo("Europe/Moscow")).strftime("%d.%m.%y-%H:%M:%S")
    await SendMessage(chat_id=admin_id,
                      text=f'{time} @{message.from_user.username}\nНачало сообщения:').as_(bot)
    await message.send_copy(admin_id)
    await SendMessage(chat_id=admin_id, text='Конец сообщения').as_(bot)
