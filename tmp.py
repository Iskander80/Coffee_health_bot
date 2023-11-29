async def first_message(bot, callback):
    await bot.send_message(callback.from_user.id, "fo")
