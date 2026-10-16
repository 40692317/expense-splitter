def calculate_balances(people, expenses):
    total = sum(e["amount"] for e in expenses)
    share = total / len(people)

    paid_by_person = {p: 0 for p in people}
    for e in expenses:
        paid_by_person[e["payer"]] += e["amount"]

    balances = {}
    for p in people:
        balances[p] = paid_by_person[p] - share
    return balances