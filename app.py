from flask import Flask
from app import create_app  # импортируем функцию создания приложения

# создаем экземпляр приложения
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # запускаем приложение в режиме отладки
