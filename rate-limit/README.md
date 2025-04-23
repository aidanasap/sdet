
Этот rate limiting с использованием Token Bucket. 

Использовано:
Python3,FastAPI, Middleware FastAPI
Uvicorn (ASGI-сервер)
Token Bucket

Принцип работы:
Есть capacity с токенами.
Токены пополняются с каким-то rate.
При каждом запросе -1 токен.
Если токенов нет — запрос отклоняется.

Почему Token Bucket?
Простая реализация, гибкий контроль и работает

![](app/rate.png)

Конфигурация в main.py:
rate_limiter = TokenBucket(capacity=5, refill_rate=1)
5 — максимальное количество токенов
1 — токены пополняются со скоростью 1 токен в секунду
