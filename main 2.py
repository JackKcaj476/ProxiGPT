import flask
import openai
import os
from flask import Flask, request, render_template_string
template = """
<!DOCTYPE html>
<html>
    <head>
        <title>OpenAI API</title>
        <style>
            /* Dark gray background */
            body {
                background-color: #333333;
                color: white;
                font-family: 'Arial', sans-serif;
            }

            /* Dark gray form */
            form {
                position: absolute;
                bottom: 0;
                width: 100%;
                background-color: #333333;
                font-size: 1.8em;
                padding: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            input[type="text"] {
                width: 80%;
                height: 100px;
                padding: 20px;
                background-color: #333333;
                color: white;
                border: 1px solid white;
                font-size: 1.5em;
                margin-right: 20px;
            }
            /* Response text at the top */
            p {
                position: absolute;
                top: 0;
                width: 100%;
                padding: 20px;
                font-size: 0.90em;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <input type="text" name="prompt" id="prompt" placeholder="Ask me Anything" style="width: 80%; height: 100px;">
            <input type="submit" value="Submit" style="width: 175px; height: 175px;">
        </form>
        {% if response %}
            <p>{{ response }}</p>
        {% endif %}
    </body>
</html>



"""

app = Flask(__name__)
openai.api_key = os.environ['APIKEY']
model_engine = "text-davinci-003"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=3000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        return render_template_string(template, response=response)
    return render_template_string(template)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=443)