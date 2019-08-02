from copy import deepcopy
import pytest

from testownik.controller import QuestionListController
from testownik.question import Question


@pytest.fixture
def sample_question_list():
    return [
        Question("example_1", "good_1", ["wrong_11", "wrong_12"]),
        Question("example_2", "good_2", ["wrong_21", "wrong_22"]),
        Question("example_3", "good_3", ["wrong_31", "wrong_32"]),
    ]


@pytest.fixture
def controller(sample_question_list):
    return QuestionListController(deepcopy(sample_question_list))