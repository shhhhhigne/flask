from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def index():
    '''This returns the homepage'''


    return render_template('index.html')


@app.route('/application-form')
def show_application_form():
    '''This returns the form for the user to enter info for the application'''

    jobs = ['software engineer', 'qa engineer', 'product manager']

    return render_template("application-form.html",
                           jobs=jobs)

@app.route('/application-success', methods=['POST'])
def show_successful_submission():
    '''This returns a response that confirms acknowledges the users application'''

    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    job = request.form.get('job-type')
    salary = request.form.get('salary').replace(',', '')
    flash(salary)
    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           job=job,
                           salary=salary)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
