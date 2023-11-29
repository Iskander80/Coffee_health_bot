from handlers import handlers_coffee
import time
import aioschedule as schedule


async def sheduler_coffee_tests(bot, callback):
    await schedule.every(10).seconds.do(coffee_tests, bot, callback)
    while True:
        await schedule.run_pending()
        time.sleep(1)


async def coffee_tests(bot, callback):
    await bot.send_message(callback.from_user.id,
                           "Запущено тестирование доступности кофемашин 🫡.")
    await handlers_coffee.check_available_devices(bot, callback)
    await bot.send_message(callback.from_user.id,
                           "Тестирование доступности кофемашины окончено 🫡.")




