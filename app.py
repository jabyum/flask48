from flask import (Flask, render_template, request,
                   redirect, url_for)

from question.questions import question_bp
from user.user import user_bp

app = Flask(__name__)
# база данных с вопросами
questions = [{"id": 1, "title": "Кто придумал Python?",
              "content": "подскажите, очень хочу знать"},
             {"id": 2, "title": "Как работать на flask?",
              "content": "что нужно для работы в flask?"}]
# база с ответами(комментами)
answers = [{"id": 1, "question_id": 1,
            "answer": "Все знают, что создателем является Акмал"},
           {"id": 2, "question_id": 2,
            "answer": "нужно прописать pip install flask"}]
# Настройка для защиты
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'timofeyakmal8389188abbos'
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", questions=questions)
@app.route("/question/<int:question_id>")
def question(question_id):
    question = next((q for q in questions if q.get("id") == question_id), None)
    if question:
        question_answers = [a for a in answers if a.get("question_id") == question_id]
        return render_template("question.html", question=question,
                               question_answers=question_answers)
    else:
        return "Вопрос не найден"
# добавление вопросов
@app.route("/ask", methods=["GET", 'POST'])
def ask():
    if request.method  == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_content = {"id": len(questions)+1, 'title':title, "content": content}
        questions.append(new_content)
        return redirect(url_for("home"))
    else:
        return render_template("ask.html")
# дз создать html для получения новых вопросов (мужики, верю в вас)
app.register_blueprint(user_bp)
app.register_blueprint(question_bp)



app.run(debug=True)
