import os
import openai
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Подключаем API-ключ
openai.api_key = os.getenv("OPENAI_API_KEY")

# Пробуем отправить простой запрос
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say a short aphorism"}],
        max_tokens=50
    )
    print("Успешно! Ответ от OpenAI:")
    print(response.choices[0].message["content"])
except Exception as e:
    print("Произошла ошибка:")
    print(e)