# 🛡 04-unix — Блокировка выхода в интернет из контейнера

В этом задании демонстрируется, как можно заблокировать выход в интернет для контейнера изнутри самого контейнера, не изменяя флаги запуска или настройки демона Docker.

---

## 🎯 Цель

1. Запустить ВМ с ОС Ubuntu 22.04;
2. Установить пакет docker-ce
1. Запустить контейнер ubuntu с доступом в интернет;
2. Убедиться, что apt-get update работает;
3. Заблокировать интернет изнутри контейнера;
4. Убедиться, что apt-get update больше не работает;
5. (Доп. задача) Найти второй способ блокировки интернета.

---

## ⚙️ Подготовка

### 🔸 Запуск ВМ

```bash
qemu-system-x86_64 \
-enable-kvm \
-m 4096 \
-smp 2 \
-cpu host \
-machine type=q35 \
-drive file=ubuntu22.qcow2,format=qcow2,if=virtio \
-cdrom ubuntu-22.04.iso \
-boot d \
-display gtk \
-device virtio-net,netdev=net0 \
-netdev user,id=net0,hostfwd=tcp::2222-:22
```

ВМ запущено:

```bash
tropt1@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-40-generic #40~22.04.3-Ubuntu SMP PREEMPT_DYNAMIC Tue Jul 30 17:30:19 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
```

### 🔸 Установка docker-ce
```bash
apt update
apt-get install docker-ce
```

Проверка установки:
```bash
tropt1@ubuntu:~$ docker --version
Docker version 28.1.1, build 4eba377
```

### 🔸 Запуск контейнера с необходимыми правами:

```bash
sudo docker run -it --rm --privileged --cap-add=NET_ADMIN ubuntu bash
```

> Флаг --privileged обязателен для доступа к iptables изнутри контейнера.

### 🔸 Установка iptables:

```bash
apt update
apt install -y iptables iproute2
```

## ✅ Проверка подключения к интернету

```bash
apt-get update
```
Запрос работает и пакеты обновились

## 🚫 Блокировка интернета

```bash
root@1d16eb72b87d:/# iptables -I OUTPUT -j DROP
```

## 🔍 Проверка:

```bash
root@1d16eb72b87d:/# apt-get update
```

Вывод:

```bash
Ign:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Ign:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Ign:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Ign:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Ign:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Ign:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Ign:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Ign:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Ign:2 http://archive.ubuntu.com/ubuntu jammy InRelease
Ign:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
Ign:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
Ign:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
Err:1 http://security.ubuntu.com/ubuntu jammy-security InRelease
  Temporary failure resolving 'security.ubuntu.com'
Err:2 http://archive.ubuntu.com/ubuntu jammy InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Err:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Err:4 http://archive.ubuntu.com/ubuntu jammy-backports InRelease
  Temporary failure resolving 'archive.ubuntu.com'
Reading package lists... Done
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/jammy/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/jammy-updates/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/jammy-backports/InRelease  Temporary failure resolving 'archive.ubuntu.com'
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/jammy-security/InRelease  Temporary failure resolving 'security.ubuntu.com'
W: Some index files failed to download. They have been ignored, or old ones used instead.
```

## 🧪 Доп. способ (метод 2: маршрутная таблица)

```bash
ip route del default
```

> Удаляет маршрут по умолчанию — контейнер теряет доступ к внешней сети.

## Проверка:

```bash
ping 8.8.8.8             # Не работает
apt-get update           # Не работает
```
