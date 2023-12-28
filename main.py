from aiogram import executor
from loguru import logger

from handlers.admin_handlers.admin_greeting_handlers import register_admin_greeting_handler
from handlers.user_handlers.continue_handlers import register_continue_handler
from handlers.user_handlers.dialogue_with_the_operator import register_dialogue_with_the_operator_handler
from handlers.user_handlers.greeting_handlers import register_greeting_handler
from handlers.user_handlers.discount_on_first_order import register_discount_on_first_order_handler
from handlers.user_handlers.guide_25_ways_to_tie_your_shoelaces import \
    register_shoelaces_handler
from handlers.user_handlers.kids_toys import register_kids_toys_handler
from handlers.user_handlers.our_stores import register_our_stores_handler
from handlers.user_handlers.perfumery import register_Perfumery_handler
from handlers.user_handlers.size_table import register_size_table_handler
from handlers.user_handlers.sneakers import register_Sneakers_handler
from handlers.user_handlers.twin_on_avito import register_TWIN_on_Avito_handler
from system.dispatcher import dp

logger.add("logs/log.log", retention="1 days", enqueue=True)  # Логирование бота


def main() -> None:
    """Запуск бота https://t.me/cforb_bot"""
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as error:
        logger.exception(error)
    register_greeting_handler()  # Приветствие
    register_dialogue_with_the_operator_handler()  # Диалог с оператором
    register_discount_on_first_order_handler()  # Скидка на первый заказ
    register_our_stores_handler()  # Наши магазины
    register_size_table_handler()  # Таблица размеров
    register_shoelaces_handler()  # Гайд 25 способов завязать шнурки
    register_continue_handler()  # Кнопка продолжить
    register_TWIN_on_Avito_handler()  # TWIN на Avito
    register_Perfumery_handler()  # Парфюмерия
    register_Sneakers_handler()  # Кроссовки
    register_kids_toys_handler()  # Детские игрушки
    register_admin_greeting_handler()  # Админ панель


if __name__ == '__main__':
    try:
        main()  # Запуск бота
    except Exception as e:
        logger.exception(e)
