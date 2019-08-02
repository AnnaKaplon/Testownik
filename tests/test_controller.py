import pytest


def test_load_new_question_if_remained(controller, sample_question_list):
    """Test that new question is loaded correctly."""
    controller.checked = True

    assert controller.current_question == sample_question_list[0].question

    controller.load_new_question()

    assert not controller.checked
    assert controller.current_question == sample_question_list[1].question


def test_load_new_question_completed(controller):
    """Test that status is set to completed when no question left."""
    controller.counter = 3

    assert not controller.completed
    controller.load_new_question()
    assert controller.completed


@pytest.mark.parametrize("clicked_answer, result, points", (('good_1', ('good_1', None), {'good': 1, 'wrong': 0}),
                                                    ('wrong_11', ('good_1', 'wrong_11'), {'good': 0, 'wrong': 1}),
                                                    (None, ('good_1', None), {'good': 0, 'wrong': 1})))
def test_check_answer(controller, clicked_answer, result, points):
    """Test that proper answers are returned to color green/red and status is set to checked"""
    assert controller.check_answer(clicked_answer) == result
    assert controller.good_points == points['good']
    assert controller.wrong_points == points['wrong']
    assert controller.checked


@pytest.mark.parametrize('clicked_answer', ('good_1', 'wrong_11'))
def test_check_answer_already_checked(controller, clicked_answer):
    """Test that nothing is happening when question's been already checked"""
    controller.checked = True
    assert controller.check_answer(clicked_answer) == (None, None)
    assert controller.good_points == 0
    assert controller.wrong_points == 0


