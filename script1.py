from flask import Flask # dont know why this returns a warning

app = Flask(__name__)  # create a variable to store Flask instance.
                        # i.e., you are instantiating the Flask object.
                        # __name__ is a special variable that gets as a value the name of the python script.
                        # executed alone, it defaults to the name main.
                        # if it were not "main," it would just be "script1" (the file name as is)
@app.route('/') # a decorator for the route to the homepage
def home():
    return "Website content goes here!"

if __name__ == "__main__": # Python assigns the name of "main" to the file.
    app.run(debug=True) # means "if name == main, then go ahead and run the app."
