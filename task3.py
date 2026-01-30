#TASK 3
orders = [
    {"order_id":101, "customer":"Ali", "total":500, "status":"delivered"},
    {"order_id":102, "customer":"Moin", "total":1200, "status":"pending"},
    {"order_id":103, "customer":"Ahmed", "total":700, "status":"delivered"},
    {"order_id":104, "customer":"Usman", "total":300, "status":"canceled"}
]
delivered_order = list(filter(lambda x: x["status"] == "delivered" , orders))
sorted_delivered_order = sorted(delivered_order , key = lambda x: x["total"])
customer_delivered = [x["customer"] for x in delivered_order]
cashback = list(map(lambda x: x["total"]*0.1 , delivered_order))
print(f"""
Delivered Customers :
{customer_delivered}

Cashback : 
{cashback}
""")
