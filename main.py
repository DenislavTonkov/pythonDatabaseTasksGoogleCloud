from sqlite_inserting_data import total_sales_per_customer
from sqlite_inserting_data import total_sales_per_product
from sqlite_inserting_data import total_sales_per_year

from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/report1")
async def report1():
    # your code to generate the report 1 data
    df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    return {"data": df.to_dict("records")}


@app.get("/report2")
async def report2():
    # your code to generate the report 2 data
    df = pd.DataFrame({"col3": [7, 8, 9], "col4": [10, 11, 12]})
    return {"data": df.to_dict("records")}


@app.get("/salesCustomer")
async def report3():
    # your code to generate the report 3 data
    # df = pd.DataFrame({"col5": [13, 14, 15], "col6": [16, 17, 18]})
    df = total_sales_per_customer
    # arr = df.items.tolist()
    # for i in df.items():
    #     arr.append(i)
    return {"Total sales per customer:\n": df.to_dict('records')}


@app.get("/salesPerProduct")
async def report4():
    # your code to generate the report 3 data
    df = total_sales_per_customer

    return {"Total sales per product:": df.to_dict('records')}, "\t"


@app.get("/salesPerYear")
async def report5():
    # your code to generate the report 3 data
    df = total_sales_per_year

    return {"Total sales per year:": df.to_dict('records')}

# @app.get("/totSales")
# async def report3():
#     # your code to generate the report 3 data
#     df = total_sales_per_customer
#     sales_data = []
#     for i, row in df.iterrows():
#         sales_data.append({
#             "customer_id": i,
#             "product_price": row["product_price"],
#             "order_quantity": row["order_quantity"],
#             "total_sales": row["total_sales"]
#         })
#     return {"Total sales per customer": sales_data}


# @app.get("/report3")
# async def report3():
#     # your code to generate the report 3 data
#     df = pd.DataFrame({"col5": [13, 14, 15], "col6": [16, 17, 18]})
#     return {"data": df.to_dict("records")}
