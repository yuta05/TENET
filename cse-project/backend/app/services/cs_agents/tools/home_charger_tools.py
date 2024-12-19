import sqlite3
import os
from typing import Optional
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

db = os.getenv("DATABASE_URL", "/app/services/sample_data.db")
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
    print(f"customer_id : {customer_id}")
    print(f"db: {db}")
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
def fetch_order_information(customer_id: Optional[int] = None) -> list[dict]:
    """
    Fetch order information from the database.

    Args:
        customer_id (Optional[int]): The ID of the customer to fetch orders for. Defaults to None.

    Returns:
        list[dict]: A list of order dictionaries.
    """
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
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
@tool
def fetch_product_information(product_id: Optional[str] = None) -> list[dict]:
    """
    Fetch product information from the database.

    Args:
        product_id (Optional[str]): The ID of the product to fetch information for. Defaults to None.

    Returns:
        list[dict]: A list of product dictionaries.
    """
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
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
@tool
def fetch_product_specifications(product_id: Optional[str] = None) -> list[dict]:
    """
    Fetch product specifications from the database.

    Args:
        product_id (Optional[str]): The ID of the product to fetch specifications for. Defaults to None.

    Returns:
        list[dict]: A list of product specification dictionaries.
    """
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
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
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