# -*- coding: utf-8 -*-
# @Time: 2023/7/19 19:12 
# @FileName: Controller.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import asyncio
import telebot
from App import Event
from loguru import logger
from telebot import util
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage


class BotRunner(object):
    def __init__(self, config, fadian):
        self.bot = config.bot
        self.proxy = config.proxy
        self.config = config
        self.fadian = fadian

    def botcreate(self):
        bot = AsyncTeleBot(self.bot.botToken, state_storage=StateMemoryStorage())
        return bot, self.bot

    def run(self):
        logger.success("Bot Start")
        bot, _config = self.botcreate()
        if self.proxy.status:
            from telebot import asyncio_helper
            asyncio_helper.proxy = self.proxy.url
            logger.success("Proxy Set")

        @bot.inline_handler(lambda query: True)
        async def my_chi_tang(query):
            if query.query:
                await Event.chi_tang(bot, query, self.fadian, name=query.query)
            else:
                await Event.chi_tang(bot, query, self.fadian)

        from telebot import asyncio_filters
        bot.add_custom_filter(asyncio_filters.IsAdminFilter(bot))
        bot.add_custom_filter(asyncio_filters.ChatFilter())
        bot.add_custom_filter(asyncio_filters.StateFilter(bot))

        async def main():
            await asyncio.gather(bot.polling(non_stop=True, allowed_updates=util.update_types))

        asyncio.run(main())
