# -*- coding: utf-8 -*-
# @Time: 2023/7/19 19:19
# @FileName: Event.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import random
from telebot.types import InlineQueryResultArticle, InputTextMessageContent


async def chi_tang(bot, query, fadian, name="池塘"):
    fadian_texts = random.sample(fadian, 3)
    result = []
    for id_number in range(3):
        result.append(InlineQueryResultArticle(
            id=id_number+1,
            title='嘿嘿嘿~~~立即发癫',
            description=f"{fadian_texts[id_number].format(name=name)[:50]}...",
            input_message_content=InputTextMessageContent(
                message_text=fadian_texts[id_number].format(name=name)
            )
        ))
    await bot.answer_inline_query(query.id, result, cache_time=0)
