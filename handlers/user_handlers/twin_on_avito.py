from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import main_menu_key_avito
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "TWIN_on_Avito")
async def TWIN_on_Avito(callback_query: types.CallbackQuery, state: FSMContext):
    """TWIN на Avito"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Предпочитаете совершать покупки на Avito ❓\n\n"
                            f"Это здорово ❗\n\n"
                            f"Переходите в наш профиль Avito (http://avito.ru/brands/twin) и заказывайте понравившиеся "
                            f"товары с промокодом «10БОТ» 👍\n\n"
                            f"👉 Промокод «10БОТ» активирует скидку 10% на ваш заказ.\n\n"
                            f"Приятных покупок 😇")
        main_menu_key = main_menu_key_avito()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_TWIN_on_Avito_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(TWIN_on_Avito)
