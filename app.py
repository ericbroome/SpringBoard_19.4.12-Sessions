from flask import Flask, flash, request, session, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import Question, satisfaction_survey, personality_quiz
import pdb

# In code, to set a breakpoint:
#   import pdb
#   pdb.set_trace()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty'
app.debug = True
toolbar = DebugToolbarExtension(app)

survey = None
surveys = [satisfaction_survey, personality_quiz]
responses = []
nextQuestion = -1

@app.route("/", methods=["GET"])
def do_home():
    """Display the home page"""
    global survey, nextQuestion
    s = request.args.get('s', '')
    if(s == '0' or s == '1'):
        # We have selected the satisfaction survey
        survey = surveys[int(s)]
        print(s)
#        pdb.set_trace()
        nextQuestion = 0
        return redirect(f"questions/{nextQuestion}", 307)
    return render_template("home.html", surveys=surveys)

@app.route("/questions/<int:index>", methods=['GET', 'POST'])
def do_questions(index):
    """Handle survey question"""
    global nextQuestion
    global responses
    if(index >= len(survey.questions) or index < 0):
        #DO SOMETHING ABOUT INDEX OUT OF RANGE
        flash("Question index is out of range. You must answer each question sequentially", category="warning")
    if(index != nextQuestion):
        flash("Do not attempt to manually overridethe correct sequence for questions...", category="warning")
        return redirect(f"{nextQuestion}", 307)
    return render_template("questions.html", question=survey.questions[index])

@app.route("/answer", methods=["POST"])
def do_answer():
    """Accept or reject an answer and proceed to next question"""
    global nextQuestion, responses
    answer = request.form['answer']
    responses.append(answer)
    nextQuestion += 1
    if nextQuestion >= len(survey.questions):
        return redirect("/thanks")
    return redirect(f"/questions/{nextQuestion}")

@app.route("/reset")
def do_reset():
    """ Reset the survey data to start over """
    global responses, nextQuestion, survey
    session['responses'] = responses = []
    nextQuestion = 0
    return redirect("/")

@app.route("/thanks")
def do_thanks():
    """Thank the user for participating and show results"""
    results = {"survey":survey, "responses":responses}
    return render_template("thanks.html", results=results)