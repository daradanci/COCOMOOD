from enum import Enum

class DialogueState(Enum):
    INIT = "INIT"
    AUTH = "AUTH"
    READING = "READING"
    REVIEW = "REVIEW"
    SCORE = "SCORE"