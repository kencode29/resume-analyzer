import streamlit as st
import sqlite3
import pandas as pd
from datetime import date
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "finance.db")

CATEGORIES = [
    "Food", "Rent", "Utilities", "Transport", "Entertainment",
    "Health", "Shopping", "Salary", "Other"
]

st.set_page_config(page_title="Personal Finance Dashboard", layout="wide")


# ---------- Database helpers ----------

def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('income', 'expense'))
        )
    """)
    conn.commit()
    conn.close()


def add_transaction(txn_date, description, category, amount, ttype):
    conn = get_conn()
    conn.execute(
        "INSERT INTO transactions (date, description, category, amount, type) VALUES (?, ?, ?, ?, ?)",
        (str(txn_date), description, category, amount, ttype),
    )
    conn.commit()
    conn.close()


def delete_transaction(txn_id):
    conn = get_conn()
    conn.execute("DELETE FROM transactions WHERE id = ?", (txn_id,))
    conn.commit()
    conn.close()


def get_all_transactions():
    conn = get_conn()
    df = pd.read_sql_query("SELECT * FROM transactions ORDER BY date DESC", conn)
    conn.close()
    return df


init_db()

# ---------- Sidebar: add transaction form ----------

st.sidebar.header("➕ Add Transaction")

with st.sidebar.form("add_form", clear_on_submit=True):
    txn_date = st.date_input("Date", value=date.today())
    description = st.text_input("Description")
    category = st.selectbox("Category", CATEGORIES)
    amount = st.number_input("Amount", min_value=0.0, step=1.0, format="%.2f")
    ttype = st.radio("Type", ["expense", "income"], horizontal=True)
    submitted = st.form_submit_button("Add")

    if submitted:
        if description.strip() == "" or amount <= 0:
            st.sidebar.error("Please enter a description and an amount greater than 0.")
        else:
            add_transaction(txn_date, description, category, amount, ttype)
            st.sidebar.success("Transaction added!")
            st.rerun()

# ---------- Main dashboard ----------

st.title("💰 Personal Finance Dashboard")

df = get_all_transactions()

total_income = df.loc[df["type"] == "income", "amount"].sum() if not df.empty else 0
total_expense = df.loc[df["type"] == "expense", "amount"].sum() if not df.empty else 0
balance = total_income - total_expense

col1, col2, col3 = st.columns(3)
col1.metric("Total Income", f"${total_income:,.2f}")
col2.metric("Total Expenses", f"${total_expense:,.2f}")
col3.metric("Balance", f"${balance:,.2f}", delta=f"{balance:,.2f}")

st.divider()

if df.empty:
    st.info("No transactions yet. Add one from the sidebar to get started.")
else:
    chart_col1, chart_col2 = st.columns(2)

    # Spending by category (pie/bar)
    with chart_col1:
        st.subheader("Spending by Category")
        expense_df = df[df["type"] == "expense"]
        if not expense_df.empty:
            category_totals = expense_df.groupby("category")["amount"].sum().sort_values(ascending=False)
            st.bar_chart(category_totals)
        else:
            st.write("No expenses recorded yet.")

    # Monthly trend (income vs expense)
    with chart_col2:
        st.subheader("Monthly Income vs Expenses")
        trend_df = df.copy()
        trend_df["month"] = pd.to_datetime(trend_df["date"]).dt.to_period("M").astype(str)
        monthly = trend_df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)
        st.line_chart(monthly)

    st.divider()

    # Transaction table with delete buttons
    st.subheader("All Transactions")

    header_cols = st.columns([2, 3, 2, 2, 2, 1])
    for col, label in zip(header_cols, ["Date", "Description", "Category", "Amount", "Type", ""]):
        col.markdown(f"**{label}**")

    for _, row in df.iterrows():
        c1, c2, c3, c4, c5, c6 = st.columns([2, 3, 2, 2, 2, 1])
        c1.write(row["date"])
        c2.write(row["description"])
        c3.write(row["category"])
        amount_display = f"${row['amount']:,.2f}"
        c4.write(amount_display)
        c5.write("🟢 Income" if row["type"] == "income" else "🔴 Expense")
        if c6.button("🗑️", key=f"del_{row['id']}"):
            delete_transaction(row["id"])
            st.rerun()