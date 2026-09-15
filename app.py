import streamlit as st

st.title("Expense Splitter")
st.write("Split shared costs with friends and see who owes who.")

# Step 1: how many people
people_input = st.text_input("Enter names separated by commas (e.g. Abdul, Sara, Ali)")

if people_input:
    people = [name.strip() for name in people_input.split(",")]
    st.write("People:", people)

    st.subheader("Add an expense")
    payer = st.selectbox("Who paid?", people)
    amount = st.number_input("Amount paid", min_value=0.0, step=1.0)
    description = st.text_input("What was it for? (e.g. Dinner)")

    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    if st.button("Add expense"):
        st.session_state.expenses.append({
            "payer": payer,
            "amount": amount,
            "description": description
        })
        st.success(f"Added: {payer} paid {amount} for {description}")

    if "expenses" in st.session_state and st.session_state.expenses:
        st.subheader("All expenses")
        for e in st.session_state.expenses:
            st.write(f"{e['payer']} paid {e['amount']} for {e['description']}")

        total = sum(e["amount"] for e in st.session_state.expenses)
        share = total / len(people)
        st.subheader("Summary")
        st.write(f"Total spent: {total}")
        st.write(f"Each person's fair share: {share:.2f}")

        st.subheader("Who owes who")
        paid_by_person = {p: 0 for p in people}
        for e in st.session_state.expenses:
            paid_by_person[e["payer"]] += e["amount"]

        for p in people:
            balance = paid_by_person[p] - share
            if balance > 0:
                st.write(f"{p} should receive {balance:.2f}")
            elif balance < 0:
                st.write(f"{p} owes {-balance:.2f}")
            else:
                st.write(f"{p} is settled up")