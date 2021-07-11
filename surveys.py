from time import time
import copy


class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False, id = f"sm_{time()}"):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self._question = question
        self._choices = choices
        self._allow_text = allow_text
        self._responses = [] #use a list in case there is text. The first [0] is the answer, [1] is text
        self._id = id
#---------------------------------------------------------------------------------------
    def get_question(self):
        return self._question
    question = property(get_question)
#---------------------------------------------------------------------------------------
    def get_choices(self):
        return self._choices
    choices = property(get_choices)
#---------------------------------------------------------------------------------------
    def get_allow_text(self):
        return self._allow_text
    allow_text = property(get_allow_text)
#---------------------------------------------------------------------------------------
    def get_responses(self):
        return self._responses
#---------------------------------------------------------------------------------------
    def set_responses(self, responses):
        self._responses = copy.deepcopy(responses)
        return self._responses
    responses = property(get_responses, set_responses)
#---------------------------------------------------------------------------------------
    def get_id(self):
        return self._id
    id = property(get_id)

#***************************************************************************************

class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions, id=f"s_{time()}"):
        """Create questionnaire."""
        self._title = title
        self._instructions = instructions
        self._questions = questions
        self._id = id
#---------------------------------------------------------------------------------------
    def get_id(self):
        return self._id
    id = property(get_id)
#---------------------------------------------------------------------------------------
    def get_title(self):
        return self._title
    title = property(get_title)
#---------------------------------------------------------------------------------------
    def get_instructions(self):
        return self._instructions
    instructions = property(get_instructions)
#---------------------------------------------------------------------------------------
    def get_questions(self):
        return self._questions
    questions = property(get_questions)




satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

goat_survey = Survey(
    "Goat Survey",
    "Please fill out a survey about your experience with goats.",
    [
        Question("Have you petted a goat before?"),
        Question("Have you eaten goat meat?"),
        Question("Have you tried goat dairy products?",
                 ["Just goat milk", "Just goat cheese", "Both goat milk and cheese"]),
        Question("Are you likely to give a goat a home if you had a home which could accomodate a goat?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "goats": goat_survey
}