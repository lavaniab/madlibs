"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment_list = []
    compliment = choice(AWESOMENESS)
    compliment_list.append(compliment)
    compliment2 = choice(AWESOMENESS)
    compliment_list.append(compliment2)
    compliment3 = choice(AWESOMENESS)
    compliment_list.append(compliment3)

    return render_template("compliment.html",
                           person=player,
                           compliment_list= compliment_list)


@app.route('/game')
def show_madlib_form():
    """ Submitting form"""
    y_n_game = request.args.get("y_n_game")
    player = request.args.get("person")

    if y_n_game == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html", person=player)


@app.route('/madlib')
def show_madlib():
    """ play the madlib game, should fill the person and adjective provided by
    the user into a MadLibs-style story
    """
    proper_noun = request.args.get("proper_noun")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    verb = request.args.get("verb")
    adverb = request.args.get("adverb")
    location = request.args.get("location")
    return render_template("madlib.html", proper_noun=proper_noun,
                            color=color, noun=noun,
                            adjective=adjective, verb=verb,
                            adverb=adverb, location=location)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
