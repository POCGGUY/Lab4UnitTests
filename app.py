from flask import Flask, render_template, request
from collections import Counter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            text = file.read().decode('utf-8')
            words = text.lower().split()
            most_common_words = Counter(words).most_common(5)
            result = most_common_words
            return render_template('index.html', result=result)
        else:
            return render_template('index.html', result=None)  # Ничего не загружено
    else:
        return render_template('index.html', result=None)  # GET запрос

if __name__ == '__main__':
    app.run(debug=True)