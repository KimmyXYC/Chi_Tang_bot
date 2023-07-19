# -*- coding: utf-8 -*-
# @Time: 2023/7/19 19:19
# @FileName: Event.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import random
from telebot.types import InlineQueryResultArticle, InputTextMessageContent


async def chi_tang(bot, query, fadian, name="池塘"):
    fadian_text = random.choice(fadian).format(name=name)
    result = InlineQueryResultArticle(
        id='1',
        title='嘿嘿嘿~~~立即发癫',
        input_message_content=InputTextMessageContent(
            message_text=fadian_text
        )
    )
    await bot.answer_inline_query(query.id, [result], cache_time=0)
