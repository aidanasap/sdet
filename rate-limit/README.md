
Этот микросервис реализует **rate limiting** с использованием алгоритма **Token Bucket**.

---

##  Использовано

- **Python 3**
- **FastAPI, Middleware FastAPI**
- **Uvicorn** (ASGI-сервер)
- **Token Bucket**

---

##  Принцип работы Token Bucket

1. Есть `capacity` — максимальное количество токенов в "ведре".
2. Токены пополняются с определённой скоростью (`refill_rate`).
3. Каждый запрос потребляет **1 токен**.
4. Если токенов нет — запрос **отклоняется** (`429 Too Many Requests`).

---

## Почему Token Bucket?

Простая реализация, гибкий контроль и работает


![Token Bucket Diagram](/rate-limit/rate.png)

---

## Конфигурация (main.py)

```python
rate_limiter = TokenBucket(capacity=5, refill_rate=1)
