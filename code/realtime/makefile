# Цель по умолчанию
.DEFAULT_GOAL := help

# Цель для установки зависимостей
install:
	@echo "Установка зависимостей..."
	pip install --upgrade pip
	pip install -r requirements.txt

# Цель для запуска программы
run:
	@echo "Запуск программы..."
	python3 main.py

# Цель для отображения справки
help:
	@echo "Доступные цели:"
	@echo "  make install    - Установить зависимости"
	@echo "  make run        - Запустить программу"
	@echo "  make help       - Показать эту справку"


