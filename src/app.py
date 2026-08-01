from flask import Flask, request, jsonify,render_template
import json
import os

app = Flask(__name__)

FILE_NAME = r"D:\Smart Expense Tracker API\src\expenes"


#  Main Functions 

def load_expenses():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


# Add Expense 

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()

    required_fields = ["id", "title", "amount", "category", "date"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    expenses = load_expenses()

    if any(expense["id"] == data["id"] for expense in expenses):
        return jsonify({"error": "Expense ID already exists"}), 400

    expenses.append(data)
    save_expenses(expenses)

    return jsonify({
        "message": "Expense added successfully",
        "expense": data
    }), 201


# View All Expenses 

@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify(load_expenses())


#  Filter by Category 

@app.route("/expenses/category/<category>", methods=["GET"])
def filter_category(category):
    expenses = load_expenses()

    filtered = [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    return jsonify(filtered)


#  Total Expenses 

@app.route("/expenses/total", methods=["GET"])
def total_expenses():
    expenses = load_expenses()

    overall_total = sum(expense["amount"] for expense in expenses)

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (
            category_totals.get(category, 0)
            + expense["amount"]
        )

    return jsonify({
        "overall_total": overall_total,
        "category_totals": category_totals
    })


#  Delete Expense 

@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expenses = load_expenses()

    updated = [
        expense for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(updated) == len(expenses):
        return jsonify({"error": "Expense not found"}), 404

    save_expenses(updated)

    return jsonify({
        "message": "Expense deleted successfully"
    })
@app.route("/add")
def add_page():
    return render_template("/add_expense.html")
@app.route("/delete")
def delete_page():
    return render_template("delete_expense.html")

@app.route("/")
def home():
    return render_template("/index.html")
#  Run Server 
@app.route("/expenses/<int:expense_id>", methods=["GET"])
def get_expense_by_id(expense_id):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            return jsonify(expense), 200

    return jsonify({"error": "Expense not found"}), 404
@app.route("/expenses/category/<string:category>", methods=["GET"])
def get_expenses_by_category(category):
    expenses = load_expenses()

    filtered_expenses = [
        expense for expense in expenses
        if expense["category"].lower() == category.lower()
    ]

    if not filtered_expenses:
        return jsonify({"message": f"No expenses found for category '{category}'"}), 404

    return jsonify(filtered_expenses), 200
@app.route("/expenses/group", methods=["GET"])
def group_expenses():
    expenses = load_expenses()

    grouped = {}

    for expense in expenses:
        category = expense["category"]

        if category not in grouped:
            grouped[category] = {
                "total": 0,
                "expenses": []
            }

        grouped[category]["total"] += expense["amount"]
        grouped[category]["expenses"].append(expense)

    return jsonify(grouped)
if __name__ == "__main__":
    app.run(debug=True)