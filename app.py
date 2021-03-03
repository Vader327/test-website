from flask import Flask, render_template
import webbrowser

webbrowser.open("http://127.0.0.1:8887/")

app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")

def main():
    return render_template('index.html')

@app.route("/services")
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(port=8887, debug=True)
