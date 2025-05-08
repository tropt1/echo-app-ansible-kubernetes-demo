# 🚀 01-application

## 📋 Содержание
- 📦 Описание
- ⚙️ Сборка и запуск в Docker
- 🌐 Проверка работы
- 🛠 Файлы в папке

---

## 📦 Описание
Этот веб‑приложение слушает порт 8000 и отдаёт HTML‑страницу с информацией:  
- 🖥 Hostname  
- 🌐 IP-адрес  
- 👤 Author (из переменной окружения AUTHOR)

---

## ⚙️ Сборка и запуск в Docker

### 🔑 Логин в Docker Hub  
```bash
docker login
```

### 🏗 Сборка образа
```bash
docker build -t tropt1/echo-app:latest .
```

### 📤 Пуш в приватный репозиторий
```bash
docker push tropt1/echo-app:latest
```
### 🔒 В веб‑интерфейсе Docker Hub сделайте репозиторий Private.

## 🌐 Проверка работы
```bash
docker run -e AUTHOR="tropt1 (Maxim Bolotov)" -p 8000:8000 tropt1/echo-app:latest
```
Откройте в браузере:
```
http://localhost:8000
```
---

## 🛠 Файлы в папке /01-application
| Имя файла         | Описание                       |
|-------------------|--------------------------------|
| echo_server.py  | Исходный код Python‑сервера    |
| Dockerfile      | Описание контейнера            |
| README.md       | Инструкции по сборке и запуску |
