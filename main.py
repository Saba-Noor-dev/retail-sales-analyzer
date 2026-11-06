import csv

def max_revenue_product(product_revenue):
    product = max(product_revenue, key=product_revenue.get)
    revenue = max(product_revenue.values())
    return product, revenue

def max_revenue_category(category_sales):
    category = max(category_sales, key=category_sales.get)
    revenue = max(category_sales.values())
    return category, revenue

def max_quantity_product(product_sales):
    product = max(product_sales, key=product_sales.get)
    quantity = max(product_sales.values())
    return product, quantity

def max_revenue_month(monthly_revenue):
    month = max(monthly_revenue, key=monthly_revenue.get)
    revenue = max(monthly_revenue.values())
    return month, revenue

def max_quantity_month(monthly_quantity):
    month = max(monthly_quantity, key=monthly_quantity.get)
    quantity = max(monthly_quantity.values())
    return month, quantity

def display_summary(total_revenue, total_quantity, total_orders, average_order_value, max_product, max_quantity, max_rev_product, max_rev, max_rev_category, max_revenue, max_month_revenue, max_monthly_revenue, max_month_quantity, max_monthly_quantity):
    print("=======Overall Sales Summary=======")
    print("Total Revenue: ", total_revenue)
    print("Total Quantity Sold: ", total_quantity)
    print("Total Orders: ", total_orders)
    print("Average Order Value: ", average_order_value)
    print("Best Selling Product: ", max_product, "with quantity sold: ", max_quantity)
    print("Product with Highest Revenue: ", max_rev_product, "with revenue: ", max_rev)
    print("Category with Highest Revenue: ", max_rev_category, "with revenue: ", max_revenue)
    print("Month with Highest Revenue: ", max_month_revenue, "with revenue: ", max_monthly_revenue)
    print("Month with Highest Quantity Sold: ", max_month_quantity, "with quantity: ", max_monthly_quantity)

def analyze_sales():
    total_revenue = 0
    total_quantity = 0
    total_orders = 0
    product_sales = {}
    product_revenue = {}
    category_sales = {}
    monthly_revenue = {}
    monthly_quantity = {}
    try:
        with open("sales_data.csv", "r") as open_csv:
            csv_reader = csv.DictReader(open_csv)
            for rows in csv_reader:
                try:
                    quantity = int(rows["Quantity"])
                    price = int(rows["Unit_Price"])
                except ValueError:
                    print(f"Invalid data found in row: {rows}")
                    continue
                if quantity <= 0 or price < 0:
                    print(f"Invalid data found: {rows}")
                    continue
                if not rows["Product"] or not rows["Category"] or not rows["Date"]:
                    print(f"Missing data found in row: {rows}")
                    continue
                total_quantity += quantity
                total_orders += 1
                revenue = quantity * price
                total_revenue += revenue
                product = rows["Product"]
                if product in product_sales:
                    product_sales[product] += quantity
                else:
                    product_sales[product] = quantity

                if product in product_revenue:
                    product_revenue[product] += revenue
                else:
                    product_revenue[product] = revenue

                category = rows["Category"]
                if category in category_sales:
                    category_sales[category] += revenue
                else:
                    category_sales[category] = revenue

                date = rows["Date"]
                month = date[:7] # extracting year and month in YYYY-MM format
                if month in monthly_revenue:
                    monthly_revenue[month] += revenue
                else:
                    monthly_revenue[month] = revenue

                if month in monthly_quantity:
                    monthly_quantity[month] += quantity
                else:
                    monthly_quantity[month] = quantity

        if total_orders == 0:
            print("No Orders Found!")
        else:
            max_rev_product, max_rev = max_revenue_product(product_revenue)

            max_rev_category, max_revenue = max_revenue_category(category_sales)

            max_product, max_quantity = max_quantity_product(product_sales)

            average_order_value = total_revenue / total_orders

            max_month_revenue, max_monthly_revenue = max_revenue_month(monthly_revenue)

            max_month_quantity, max_monthly_quantity = max_quantity_month(monthly_quantity)

        ## OVERALL SALES SUMMARY
            display_summary(total_revenue, total_quantity, total_orders, average_order_value, max_product, max_quantity, max_rev_product, max_rev, max_rev_category, max_revenue, max_month_revenue, max_monthly_revenue, max_month_quantity, max_monthly_quantity)

    except FileNotFoundError:
        print("The file sales_data.csv was not found!")

analyze_sales()