import requests
import urls
import os
import subprocess
from handlers.handlers import warning_message
from handlers.handlers import approval_message


async def check_available_devices(bot, callback):
    # print('\n Проверки конфигуратора')
    test_name = "check_available_devices"

    for ip_dev in urls.ip_list:
        with open(os.devnull, 'w') as DEVNULL:
            try:
                subprocess.check_call(
                    ['ping', '-t', '2', ip_dev],
                    stdout=DEVNULL,  # suppress output
                    stderr=DEVNULL
                )
                await approval_message(bot, callback, ip_dev)
            except subprocess.CalledProcessError:
                await warning_message(bot, callback, ip_dev)


