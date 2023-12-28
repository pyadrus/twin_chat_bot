from aiogram import types
from aiogram.dispatcher import FSMContext  # Состояния пользователя
from loguru import logger

from keyboards.user_keyboards.user_keyboards import main_menu_key_perfumery
from system.dispatcher import bot, dp


@dp.callback_query_handler(lambda c: c.data == "Perfumery")
async def Perfumery(callback_query: types.CallbackQuery, state: FSMContext):
    """Парфюмерия"""
    try:
        await state.finish()  # Завершаем текущее состояние машины состояний
        await state.reset_state()  # Сбрасываем все данные машины состояний, до значения по умолчанию
        greeting_message = (f"Благодарим за обращение! 🙌\n"
                            f"«TWIN» дарит Вам промокод 🔥«10БОТ»🔥 на первый заказ\n\n"
                            f"Как активировать промокод? 👇\n"
                            f"1️⃣ Вернитесь на сайт «TWIN» по ссылке (https://twin-perfume.ru/)👈\n"
                            f"2️⃣ Добавьте в корзину парфюмерию, которую хотите заказать 🛒\n"
                            f"3️⃣ Откройте корзину и нажмите: Оформить заказ\n"
                            f"4️⃣ Заполните контактную информацию для связи и введите «10БОТ» в поле «Промокод»\n\n"
                            f"Готово ❗\n"
                            f"Ваш заказ оформлен и на него применилась скидка 10% 😍")
        main_menu_key = main_menu_key_perfumery()
        await bot.send_message(callback_query.from_user.id,  # ID пользователя
                               text=greeting_message,  # Текст для приветствия 👋
                               reply_markup=main_menu_key,
                               parse_mode=types.ParseMode.HTML)  # Текст в HTML-разметки
    except Exception as error:
        logger.exception(error)


def register_Perfumery_handler():
    """Регистрируем handlers для бота"""
    dp.register_message_handler(Perfumery)
