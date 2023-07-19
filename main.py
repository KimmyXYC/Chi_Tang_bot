# -*- coding: utf-8 -*-
# @Time: 2023/7/19 19:09 
# @FileName: main.py
# @Software: PyCharm
# @GitHub: KimmyXYC
from pathlib import Path
from Utils.Base import ReadConfig
from Utils.Json import get_config_file
from App.Controller import BotRunner
from loguru import logger
import sys

logger.remove()
handler_id = logger.add(sys.stderr, level="INFO")
logger.add(sink='run.log',
           format="{time} - {level} - {message}",
           level="INFO",
           rotation="20 MB",
           enqueue=True)
config = ReadConfig().parse_file(str(Path.cwd()) + "/Config/app.toml")
fadian = get_config_file()
App = BotRunner(config, fadian)
App.run()
