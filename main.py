from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Онлайн калькулятор работает!"

@app.route("/calc", methods=["GET"])
def calculate():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        op = request.args.get("op", "+")
        result = None

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b if b != 0 else "Ошибка: деление на ноль"
        else:
            return jsonify({"error": "Неизвестная операция"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()