import sqlite3


def recording_data_email(user_id, username, email, registration_date):
    """Запись данных пользователей запустивших бота"""
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_email (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        email TEXT,
                        join_date TEXT)''')
    cursor.execute("INSERT OR REPLACE INTO users_email (user_id, username, email, registration_date) "
                   "VALUES (?, ?, ?, ?)", (user_id, username, email, registration_date))
    conn.commit()
    conn.close()


def get_user_data_from_db_email(user_id):
    """Чтение данных с базы данных your_database.db"""
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_email (user_id INTEGER,
                                                        username TEXT,
                                                        email TEXT,
                                                        registration_date TEXT)''')
    # Выполните SQL-запрос для получения данных о пользователе по его user_id
    cursor.execute("SELECT * FROM users_email WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()  # Получите данные первой найденной записи
    conn.close()
    # Верните данные о пользователе как словарь, если они существуют, или None, если пользователя нет
    if user_data:
        _, username, email, registration_date = user_data
        return {'username': username, 'email': email, 'registration_date': registration_date}
    else:
        return None


def insert_user_data_to_database(user_id, name, phone_number, registration_date):
    """Записывает данные пользователя в базу данных"""
    try:
        conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER,
                                                            name TEXT,
                                                            phone_number TEXT,
                                                            registration_date TEXT)''')
        cursor.execute("INSERT INTO users (user_id, name, phone_number, registration_date) "
                       "VALUES (?, ?, ?, ?)",
                       (user_id, name, phone_number, registration_date))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при записи данных в базу данных: {e}")
    finally:
        conn.close()


def update_phone_in_db(user_id, new_phone):
    try:
        # Подключаемся к базе данных (предполагается, что она уже существует)
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        # SQL-запрос для обновления имени
        update_query = "UPDATE users SET phone_number = ? WHERE user_id = ?"
        cursor.execute(update_query, (new_phone, user_id))
        conn.commit()  # Применяем изменения к базе данных
        conn.close()  # Закрываем соединение с базой данных
        return True  # Возвращаем True в случае успешного обновления
    except Exception as e:
        print("Ошибка при обновлении фамилии:", str(e))
        return False  # Возвращаем False в случае ошибки


def recording_data_of_users_who_launched_the_bot(user_id, username, first_name, last_name, join_date):
    """Запись данных пользователей запустивших бота"""
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_start (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        join_date TEXT)''')
    cursor.execute("INSERT OR REPLACE INTO users_start (user_id, username, first_name, last_name, join_date) "
                   "VALUES (?, ?, ?, ?, ?)", (user_id, username, first_name, last_name, join_date))
    conn.commit()
    conn.close()


def get_user_data_from_db(user_id):
    """Чтение данных с базы данных your_database.db"""
    conn = sqlite3.connect("your_database.db")  # Замените "your_database.db" на имя вашей базы данных
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER,
                                                        name TEXT,
                                                        phone_number TEXT,
                                                        registration_date TEXT)''')
    # Выполните SQL-запрос для получения данных о пользователе по его user_id
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()  # Получите данные первой найденной записи
    conn.close()
    # Верните данные о пользователе как словарь, если они существуют, или None, если пользователя нет
    if user_data:
        _, name, phone_number, registration_date = user_data
        return {'name': name, 'phone_number': phone_number, 'registration_date': registration_date}
    else:
        return None


# Функция для изменения имени в базе данных по ID
def update_name_in_db(user_id, new_name):
    try:
        # Подключаемся к базе данных (предполагается, что она уже существует)
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        # SQL-запрос для обновления имени
        update_query = "UPDATE users SET name = ? WHERE user_id = ?"
        cursor.execute(update_query, (new_name, user_id))
        conn.commit()  # Применяем изменения к базе данных
        conn.close()  # Закрываем соединение с базой данных
        return True  # Возвращаем True в случае успешного обновления
    except Exception as e:
        print("Ошибка при обновлении имени:", str(e))
        return False  # Возвращаем False в случае ошибки
