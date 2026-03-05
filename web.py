from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My Small Python Website</h1>
    <p>Welcome to my web application.</p>
    <p>Here We Goo..</p>
    <a href='/about'>Go to About Page</a>
    """

@app.route("/about")
def about():
    return """
    <h2>About</h2>
    <p>This is a simple website made using Python and Flask.</p>
    <a href='/'>Back to Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True) #new comment

