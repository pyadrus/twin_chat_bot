from aiogram import types
from aiogram.dispatcher import FSMContext
from loguru import logger

from database.database import get_user_data_from_db
from keyboards.user_keyboards.user_keyboards import continue_keyboard
from keyboards.user_keyboards.user_keyboards import create_main_menu_keyboard
from keyboards.user_keyboards.user_keyboards import main_menu_ke
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "discount_on_first_order")
async def discount_on_first_order(callback_query: types.CallbackQuery, state: FSMContext):
    """Скидка на первый заказ"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        user_id = callback_query.from_user.id  # Получаем ID текущего пользователя
        user_data = get_user_data_from_db(user_id)  # Функция, которая получает данные о пользователе из базы данных
        if user_data:
            await state.finish()  # Завершаем текущее состояние машины состояний
            await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
            greeting_message = f"Выберите магазин"
            continue_key = continue_keyboard()
            await bot.send_message(callback_query.from_user.id,  # ID пользователя
                                   text=greeting_message,  # Текст
                                   reply_markup=continue_key,
                                   parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
        else:
            greeting_message = (f"Бот отправляет промокоды, которые активируют скидки до -20% на первый заказ в наших "
                                f"магазинах.\n\n"
                                
                                f"Чтобы получить промокод, заполните свои контактные данные нажав кнопку "
                                f"<b>«Да, хочу промокод»</b>.\n\n")

            main_menu_keyboard = create_main_menu_keyboard()
            await bot.send_message(callback_query.from_user.id,  # ID пользователя
                                   text=greeting_message,  # Текст
                                   reply_markup=main_menu_keyboard,
                                   parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


@dp.callback_query_handler(lambda c: c.data == "disagree")
async def disagree(callback_query: types.CallbackQuery, state: FSMContext):
    """Нет, в другой раз"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Если у вас остались вопросы или вы хотели бы уточнить наличие определённых товаров, "
                            f"свяжитесь с нами через WhatsApp менеджера интернет-магазина: 👇 Задать "
                            f"вопрос (https://wa.me/79198438647)\n\n")
        main_menu_key = main_menu_ke()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_discount_on_first_order_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(discount_on_first_order)  # Скидка на первый заказ
    dp.register_message_handler(disagree)  # Нет, в другой раз
