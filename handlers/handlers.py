async def warning_message(bot, callback, dev_name):
    await bot.send_message(callback.from_user.id,
                           dev_name + " - Fail ❌")


async def approval_message(bot, callback, dev_name):
    await bot.send_message(callback.from_user.id,
                           dev_name + " - OK ✅")

