import sqlite3
import os
from typing import Optional
from app.core.config import settings
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
import time  # timeモジュールをインポート
db = settings.DATABASE_URL
print(f"db: {db}")
def check_db_exists(db_path: str) -> bool:
    """
    Check if the database file exists.

    Args:
        db_path (str): The path to the database file.

    Returns:
        bool: True if the database file exists, False otherwise.
    """
    return os.path.exists(db_path)

def check_permissions(db_path):
    if not os.access(db_path, os.R_OK):
        raise PermissionError(f"Read permission denied for database file '{db_path}'")
    if not os.access(db_path, os.W_OK):
        raise PermissionError(f"Write permission denied for database file '{db_path}'")



@tool
def fetch_customer_information(config: RunnableConfig) -> list[dict]:
    """
    Fetch customer information from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        list[dict]: A list of customer dictionaries.
    """
    configuration = config.get("configurable", {})
    customer_id = configuration.get("customer_id", None)
    check_permissions(db)
    if not customer_id:
        raise ValueError("No customer ID configured.")
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM customers WHERE customer_id = ?"
    params = [customer_id]
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
@tool
def fetch_order_information(config: RunnableConfig) -> dict:
    """
    Fetch order information from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing order information.
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
@tool
def fetch_product_information(config: RunnableConfig) -> dict:
    """
    Fetch product information from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing product information.
    """
    configuration = config.get("configurable", {})
    product_id = configuration.get("product_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    params = []
    if product_id:
        query += " WHERE product_id = ?"
        params.append(product_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"product_info": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}
@tool
def fetch_product_specifications(config: RunnableConfig) -> dict:
    """
    Fetch product specifications from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing product specifications.
    """
    configuration = config.get("configurable", {})
    product_id = configuration.get("product_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM product_specifications"
    params = []
    if product_id:
        query += " WHERE product_id = ?"
        params.append(product_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"product_specifications": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}
@tool
def fetch_installation_requirements(config: RunnableConfig) -> dict:
    """
    Fetch installation requirements from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing installation requirements.
    """
    configuration = config.get("configurable", {})
    product_id = configuration.get("product_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM installation_requirements"
    params = []
    if product_id:
        query += " WHERE product_id = ?"
        params.append(product_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"installation_requirements": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}

@tool
def fetch_installation_slots(config: RunnableConfig) -> dict:
    """
    Fetch installation slots from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing installation slots.
    """
    configuration = config.get("configurable", {})
    slot_id = configuration.get("slot_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM installation_slots"
    params = []
    if slot_id:
        query += " WHERE slot_id = ?"
        params.append(slot_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"installation_slots": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}

@tool
def fetch_product_compatibility(config: RunnableConfig) -> dict:
    """
    Fetch product compatibility from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing product compatibility.
    """
    configuration = config.get("configurable", {})
    product_id = configuration.get("product_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM product_compatibility"
    params = []
    if product_id:
        query += " WHERE product_id = ?"
        params.append(product_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"product_compatibility": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}

@tool
def fetch_product_recommendations(config: RunnableConfig) -> dict:
    """
    Fetch product recommendations from the database.

    Args:
        config (RunnableConfig): The configuration for the runnable.

    Returns:
        dict: A dictionary containing product recommendations.
    """
    configuration = config.get("configurable", {})
    product_id = configuration.get("product_id", None)
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM product_recommendations"
    params = []
    if product_id:
        query += " WHERE product_id = ?"
        params.append(product_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return {"product_recommendations": [dict(zip([column[0] for column in cursor.description], row)) for row in results]}

@tool
def fetch_region_requirements(country: Optional[str] = None) -> list[dict]:
    """
    Fetch region requirements from the database.

    Args:
        country (Optional[str]): The country to fetch requirements for. Defaults to None.

    Returns:
        list[dict]: A list of region requirement dictionaries.
    """
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM region_requirements"
    params = []
    if country:
        query += " WHERE country LIKE ?"
        params.append(f"%{country}%")
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
@tool
def fetch_required_tools() -> list[dict]:
    """
    Fetch required tools from the database.

    Returns:
        list[dict]: A list of required tool dictionaries.
    """
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM required_tools;")
    results = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
@tool
def fetch_work_order_steps(template_id: Optional[int] = None) -> list[dict]:
    """
    Fetch work order steps from the database.

    Args:
        template_id (Optional[int]): The ID of the work order template to fetch steps for. Defaults to None.

    Returns:
        list[dict]: A list of work order step dictionaries.
    """
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM work_order_steps"
    params = []
    if template_id:
        query += " WHERE template_id = ?"
        params.append(template_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
@tool
def fetch_work_order_templates(template_id: Optional[int] = None) -> list[dict]:

    """
    Fetch work order templates from the database.

    Args:
        template_id (Optional[int]): The ID of the work order template to fetch. Defaults to None.

    Returns:
        list[dict]: A list of work order template dictionaries.
    """
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "SELECT * FROM work_order_templates"
    params = []
    if template_id:
        query += " WHERE template_id = ?"
        params.append(template_id)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]

# @tool
# def update_orders(order_id: str, status: str, product_id: Optional[str] = None) -> None:
#     """
#     Update order information in the database.

#     Args:
#         order_id (str): The ID of the order to update.
#         status (str): The new status of the order.
#         product_id (Optional[str]): The ID of the new product to order. Defaults to None.
#     """
#     if not check_db_exists(db):
#         raise FileNotFoundError(f"Database file '{db}' not found.")
#     check_permissions(db)
#     conn = sqlite3.connect(db)
#     try:
#         cursor = conn.cursor()
#         if status == "cancelled":
#             query = "UPDATE orders SET status = ? WHERE order_id = ?"
#             params = [status, order_id]
#         elif status == "new":
#             if not product_id:
#                 raise ValueError("Missing product_id for new order.")
#             query = "INSERT INTO orders (order_id, customer_id, product_id, order_date, status, delivery_status, estimated_delivery) VALUES (?, ?, ?, ?, ?, ?, ?)"
#             params = [order_id, "CUST-001", product_id, "2024-07-15", "confirmed", "scheduled", "2024-Q3"]
#         else:
#             raise ValueError(f"Invalid status '{status}'.")
#         cursor.execute(query, params)
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         conn.close()
@tool
def update_installation_service(slot_id: int, available: str) -> None:

    """
    Update installation slot information in the database.

    Args:
        slot_id (int): The ID of the slot to update.
        available (str): The new availability status of the slot.
    """
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    check_permissions(db)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    query = "UPDATE installation_slots SET available = ? WHERE slot_id = ?"
    params = [available, slot_id]
    cursor.execute(query, params)
    conn.commit()
    conn.close()
    # @tool
# def add_orders(order_id: str, customer_id: str, product_id: str, order_date: str, status: str, delivery_status: str, estimated_delivery: str) -> None:

#     """
#     Add a new order to the database.

#     Args:
#         order_id (str): The ID of the new order.
#         customer_id (str): The ID of the customer placing the order.
#         product_id (str): The ID of the product being ordered.
#         order_date (str): The date the order was placed.
#         status (str): The status of the order.
#         delivery_status (str): The delivery status of the order.
#         estimated_delivery (str): The estimated delivery date of the order.
#     """
#     if not check_db_exists(db):
#         raise FileNotFoundError(f"Database file '{db}' not found.")
#     check_permissions(db)
#     conn = sqlite3.connect(db)
#     cursor = conn.cursor()
#     query = "INSERT INTO orders (order_id, customer_id, product_id, order_date, status, delivery_status, estimated_delivery) VALUES (?, ?, ?, ?, ?, ?, ?)"
#     params = [order_id, customer_id, product_id, order_date, status, delivery_status, estimated_delivery]
#     cursor.execute(query, params)
#     conn.commit()
#     conn.close()

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
    """Add a new order to the database."""
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
    """Update order information in the database."""
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
@tool("insert_order")
def insert_order(
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
    """Insert a new order into the database."""
    print(f"Attempting to insert order: {order_id}, {customer_id}, {product_id}, {order_date}, {status}, {delivery_status}, {estimated_delivery}")
    configuration = config.get("configurable", {})
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    check_permissions(db)

    retries = 5
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
            print("Order successfully inserted.")
            return "Order successfully inserted."
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
    raise sqlite3.OperationalError("Failed to insert order after multiple retries due to database lock.")