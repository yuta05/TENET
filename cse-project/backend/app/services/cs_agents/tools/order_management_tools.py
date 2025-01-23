import sqlite3
import os
from typing import Optional
from app.core.config import settings
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
import time

db = settings.DATABASE_URL

def check_db_exists(db_path: str) -> bool:
    return os.path.exists(db_path)

def check_permissions(db_path):
    if not os.access(db_path, os.R_OK):
        raise PermissionError(f"Read permission denied for database file '{db_path}'")
    if not os.access(db_path, os.W_OK):
        raise PermissionError(f"Write permission denied for database file '{db_path}'")

@tool("fetch_order_information")
def fetch_order_information(config: RunnableConfig) -> dict:
    """
    Fetch order information from the database.

    Args:
        config (RunnableConfig): Configuration object containing customer_id.

    Returns:
        dict: Dictionary of order information.
    """
    configuration = config.get("configurable", {})
    customer_id = configuration.get("customer_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM orders"
    params = []
    if customer_id:
        query += " WHERE customer_id = ?"
        params.append(customer_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"messages": [{"order_info": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}]}

@tool("add_orders")
def add_orders(
    order_id: str,
    customer_id: str,
    product_id: str,
    order_date: str,
    status: str,
    delivery_status: str,
    estimated_delivery: str,
    *,
    config: RunnableConfig
) -> str:
    """
    Add a new order to the database.

    Args:
        order_id (str): Order ID.
        customer_id (str): Customer ID.
        product_id (str): Product ID.
        order_date (str): Order date.
        status (str): Order status.
        delivery_status (str): Delivery status.
        estimated_delivery (str): Estimated delivery date.
        config (RunnableConfig): Configuration object.

    Returns:
        str: Success message.
    """
    print(f"Attempting to add order: {order_id}, {customer_id}, {product_id}, {order_date}, {status}, {delivery_status}, {estimated_delivery}")
    configuration = config.get("configurable", {})
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    check_permissions(db)

    retries = 1
    while retries > 0:
        try:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            query = """
            INSERT INTO orders (
                order_id, customer_id, product_id, order_date, status, delivery_status, estimated_delivery
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            params = [order_id, customer_id, product_id, order_date, status, delivery_status, estimated_delivery]
            print(f"Executing query: {query} with params: {params}")
            cursor.execute(query, params)
            conn.commit()
            print("Order successfully added.")
            return "Order successfully added."
        except sqlite3.OperationalError as e:
            print(f"OperationalError: {e}")
            if 'database is locked' in str(e):
                retries -= 1
                print(f"Retrying... {retries} retries left.")
                time.sleep(1)  # Wait for 1 second before retrying
            else:
                raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    raise sqlite3.OperationalError("Failed to add order after multiple retries due to database lock.")

@tool("update_orders")
def update_orders(
    order_id: str,
    status: str,
    product_id: Optional[str] = None,
    *,
    config: RunnableConfig
) -> str:
    """
    Update an existing order in the database.

    Args:
        order_id (str): Order ID.
        status (str): New status of the order.
        product_id (Optional[str]): Product ID for new orders.
        config (RunnableConfig): Configuration object.

    Returns:
        str: Success message.
    """
    configuration = config.get("configurable", {})
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    check_permissions(db)

    retries = 5
    while retries > 0:
        try:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            if status == "cancelled":
                query = "UPDATE orders SET status = ? WHERE order_id = ?"
                params = [status, order_id]
            elif status == "new":
                if not product_id:
                    raise ValueError("Missing product_id for new order.")
                query = """
                INSERT INTO orders (
                    order_id, customer_id, product_id, order_date, status, delivery_status, estimated_delivery
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """
                params = [order_id, "CUST-001", product_id, "2024-07-15", "confirmed", "scheduled", "2024-Q3"]
            else:
                raise ValueError(f"Invalid status '{status}'.")
            cursor.execute(query, params)
            conn.commit()
            return "Order successfully updated."
        except sqlite3.OperationalError as e:
            if 'database is locked' in str(e):
                retries -= 1
                time.sleep(1)  # Wait for 1 second before retrying
            else:
                raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    raise sqlite3.OperationalError("Failed to update order after multiple retries due to database lock.")