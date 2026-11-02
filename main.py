import config
import expenses

try:
    print("="*20)
    print("EXPENSE TRACKER")
    print("="*20)
    print("""
    1. Add Expense
    2. View All Exepenses
    3. Delete Expense
    4. Category-wise & Total Summary
    5. Exit
            """)
    i = int(input("Enter a choice: "))
    if i > 5:
        print("Please choose one of the above choices!")
except ValueError:
    print("Enter a valid number!")

if i==1:
    n_data = expenses.get_data(config.path)
    expenses.add_data(n_data, config.path)
    print("Data added successfully!")
elif i==2:
    data = expenses.view_data(config.path)
    print(f"{'ID':<6} {'Amount':<8} {'Category':<15} {'Description':<20} {'Date':<12}")
    print("-"*65)
    for d in data:
        print(f'{d["id"]:<6} {d["amount"]:<10} {d["category"]:<15} {d["description"]:<16} {d["date"]:<8}')
elif i==3:
    id = int(input("Enter the id: "))
    expenses.drop_data(id, config.path)
elif i==4:
    n_data = expenses.view_data(config.path)
    total = {}
    for item in n_data:
        cat = item["category"]
        amt = int(item["amount"])

        total[cat] = total.get(cat,0) + amt

    grand_total = 0
    print("category Wise Total")
    print("-"*20)
    for tot in total:
        print(f'{tot:15} {total[tot]}')
        grand_total += total[tot]
    print("-"*20)
    print(f'Total Expense \t{grand_total}')
elif i==5:
    pass