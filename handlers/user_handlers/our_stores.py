from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import main_menu_ke
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "our_stores")
async def our_stores(callback_query: types.CallbackQuery, state: FSMContext):
    """Наши магазины"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f'🛒 TWIN на Avito (http://avito.ru/brands/twin) 🛒\n\n'
                            
                            f'👟 Кроссовки (https://twin-shoes.ru/) 👟\n\n'
                            
                            f'🛍 Парфюмерия (https://twin-perfume.ru/) 🛍\n\n'
                            
                            f'🧸 Игрушки (https://twin-toys.ru/) 🧸\n')
        main_menu_key = main_menu_ke()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_key,
                               parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_our_stores_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(our_stores)  # Наши магазины
