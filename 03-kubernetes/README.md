# 🚀 03-kubernetes — Deploy Echo App in Kubernetes

В этой директории содержатся манифесты для деплоя echo-сервера (из задания 01-application) в кластер Kubernetes.

## 📦 Состав

- `namespace.yaml` — создание отдельного namespace (`echo-app`)
- `deployment.yaml` — деплой приложения в виде Deployment с 3 репликами
- `service.yaml` — сервис типа ClusterIP для доступа к подам
- `ingress.yaml` — Ingress-правило
- `secret-registry.yaml` — Docker registry secret для доступа к приватному образу
- `readiness-probe`, `liveness-probe` — реализованы в `deployment.yaml`

## ⚙️ Требования

- Kubernetes-кластер
- Установленный `kubectl`
- Созданный секрет для доступа к приватному Docker Hub registry:
  
  ```bash
  kubectl create secret docker-registry regcred \
    --docker-username=your_dockerhub_username \
    --docker-password=your_dockerhub_password \
    --docker-email=your_email@example.com \
    --namespace=echo-app
  ```
## 📄 Применение манифестов

```bash
kubectl apply -f namespace.yaml
kubectl apply -f secret-registry.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

## 📍 Namespace

Все ресурсы создаются в namespace `echo-app`:
```bash
kubectl get all -n echo-app
```

## 🧪 Проверка

```bash
kubectl get pods -n echo-app
kubectl describe pod <имя-пода> -n echo-app
kubectl logs <имя-пода> -n echo-app
```
## 🧠 Обоснование

- Используется `readinessProbe` и `livenessProbe`, чтобы Kubernetes мог определять, когда поды готовы принимать трафик и когда их нужно перезапускать
- Образ берётся из приватного Docker Hub репозитория с использованием `imagePullSecrets`
- Для отказоустойчивости деплой разворачивается в 3 репликах

---

🛠 При необходимости манифесты могут быть переписаны под Helm-chart