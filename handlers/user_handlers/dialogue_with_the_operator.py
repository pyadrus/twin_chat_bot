from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import main_menu_ke
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "operator")
async def dialogue_with_the_operator(callback_query: types.CallbackQuery, state: FSMContext):
    """Диалог с оператором"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Если у вас остались вопросы или вы хотели бы уточнить наличие обретённых моделей вашего "
                            f"размера, свяжитесь с нами через WhatsApp менеджера интернет-магазина: "
                            f"👇 Задать вопрос (https://wa.me/79198438647)\n\n"
                            f"Или позвоните нам! Менеджер на связи и с радостью вас проконсультирует: +79198438647")
        main_menu_key = main_menu_ke()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_dialogue_with_the_operator_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(dialogue_with_the_operator)  # Диалог с оператором
