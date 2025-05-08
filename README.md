# 🌐 CloudRuCamp: тестовое задание

Репозиторий содержит решение тестового задания по развёртыванию и автоматизации веб-приложения, включающее Docker, Ansible и Kubernetes.  

📁 Каждая задача оформлена в виде отдельной директории с документацией и исходным кодом.

---

## 📂 Структура проекта
```bash
.
├── 01-application       # Echo-сервер + Dockerfile + инструкция публикации
├── 02-ansible           # Ansible playbook для деплоя приложения с балансировкой
├── 03-kubernetes        # K8s-манифесты и секреты для запуска приложения
├── 04-unix              # Блокировка выхода в интернет из контейнера
└── README.md            # Описание проекта
```
---

## 🔧 Технологии

- 🐍 Python (Flask) / 🐳 Docker
- 📦 Docker Hub (приватный реестр)
- ⚙️ Ansible (Playbook + роли)
- ☸️ Kubernetes (манифесты + ingress + probes)
- 🧪 Ubuntu 22.04, iptables, iproute2

---

## 📌 Задания

### ✅ 01 — Echo Web Application

- Простой echo-сервер на Flask (Python), выводящий:
  - IP-адрес
  - имя хоста
  - значение переменной окружения AUTHOR
- Dockerfile и образ опубликован в приватный Docker Hub registry

📄 Подробнее: [01-application/README.md](./01-application/README.md)

---

### ✅ 02 — Ansible Playbook

- Установка Docker
- Запуск 3 контейнеров с echo-сервером из приватного реестра
- Настройка Nginx-балансировщика с round-robin (обоснование внутри)

📄 Подробнее: [02-ansible/README.md](./02-ansible/README.md)

---

### ✅ 03 — Kubernetes Manifests

- Namespace, Deployment (3 реплики), Service (ClusterIP)
- Readiness и Liveness-пробы
- Проброс переменной AUTHOR
- Работа с приватным реестром через imagePullSecrets

📄 Подробнее: [03-kubernetes/README.md](./03-kubernetes/README.md)

---

### ⭐️ 04 — Unix Admin (опционально)

- Работа внутри контейнера Ubuntu с root-доступом
- Установка iptables
- Блокировка интернета двумя способами:
  1. Через iptables
  2. Удаление маршрута по умолчанию

📄 Подробнее: [04-unix/README.md](./04-unix/README.md)

---

## 📢 Примечания

- Все инструкции проверены на Fedora 41 Workstation Edition
- Развёртывание рассчитано на среду с доступом к интернету
- Для Kubernetes требуется предварительно настроенный кластер (minikube / kind / cloud)
