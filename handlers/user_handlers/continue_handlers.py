from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import continue_keyboard
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "continue")
async def continue_h(callback_query: types.CallbackQuery, state: FSMContext):
    """Кнопка продолжить"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = f"Выберите магазин"
        continue_key = continue_keyboard()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=continue_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_continue_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(continue_h)
