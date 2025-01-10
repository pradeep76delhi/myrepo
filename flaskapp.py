from flask import Flask, render_template_string, request

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Operations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            width: 300px;
        }
        h1 {
            color: #333;
        }
        .input-group {
            margin: 15px 0;
        }
        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 45%;
            padding: 10px;
            margin: 5px;
            border: none;
            border-radius: 4px;
            color: #fff;
            background-color: #007bff;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        #result {
            margin-top: 20px;
            font-size: 18px;
            color: #007bff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Number Operations V4</h1>
        <form method="POST">
            <div class="input-group">
                <label for="num1">Number 1:</label>
                <input type="text" id="num1" name="num1" placeholder="Enter first number">
            </div>
            <div class="input-group">
                <label for="num2">Number 2:</label>
                <input type="text" id="num2" name="num2" placeholder="Enter second number">
            </div>
            <div>
                <button type="submit" name="operation" value="add">Add</button>
                <button type="submit" name="operation" value="subtract">Subtract</button>
            </div>
        </form>
        <h2 id="result">{{ result }}</h2>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def number_operations():
    result = ""
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1', 0))
            num2 = float(request.form.get('num2', 0))
            operation = request.form.get('operation')

            if operation == 'add':
                result = f"Result: {num1 + num2}"
            elif operation == 'subtract':
                result = f"Result: {num1 - num2}"
        except ValueError:
            result = "Please enter valid numbers"

    return render_template_string(html_code, result=result)

if __name__ == '__main__':
    app.run(debug=True)
