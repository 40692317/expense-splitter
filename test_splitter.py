from pytest import approx
from splitter import calculate_balances


def test_one_person_pays_30_for_three():
    people = ["Abdul", "Sara", "Ali"]
    expenses = [{"payer": "Abdul", "amount": 30}]
    result = calculate_balances(people, expenses)
    assert result["Abdul"] == 20
    assert result["Sara"] == -10
    assert result["Ali"] == -10


def test_everyone_paid_the_same_so_all_settled():
    people = ["Abdul", "Sara", "Ali"]
    expenses = [
        {"payer": "Abdul", "amount": 10},
        {"payer": "Sara", "amount": 10},
        {"payer": "Ali", "amount": 10},
    ]
    result = calculate_balances(people, expenses)
    assert result["Abdul"] == 0
    assert result["Sara"] == 0
    assert result["Ali"] == 0


def test_fifty_pound_dinner():
    people = ["Abdul", "Sara", "Ali"]
    expenses = [{"payer": "Abdul", "amount": 50}]
    result = calculate_balances(people, expenses)
    assert result["Abdul"] == approx(33.33, abs=0.01)
    assert result["Sara"] == approx(-16.67, abs=0.01)