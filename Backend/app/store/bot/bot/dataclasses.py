from enum import Enum

class DialogueState(Enum):
    INIT = "INIT"
    AUTH = "AUTH"
    READING = "QUESTION_SELECT"
    REVIEW = "QUESTION_ANSWERING"