from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# Инициализируем счетчик
counter = 0

@app.route('/')
def hello_world():
    global counter
    # Используем render_template_string для генерации HTML с кнопкой
    return render_template_string('''
        <h1>Hello World!</h1>
        <p>Количество нажатий: {{ counter }}</p>
        <form method="POST" action="/increment">
            <button type="submit">Нажми меня</button>
        </form>
    ''', counter=counter)

@app.route('/increment', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    # Перенаправляем обратно на главную страницу
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
