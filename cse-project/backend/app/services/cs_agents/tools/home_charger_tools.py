import sqlite3
import os
from typing import Optional
from app.core.config import settings
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

db = settings.DATABASE_URL

def check_db_exists(db_path: str) -> bool:
    return os.path.exists(db_path)

def check_permissions(db_path):
    if not os.access(db_path, os.R_OK):
        raise PermissionError(f"Read permission denied for database file '{db_path}'")
    if not os.access(db_path, os.W_OK):
        raise PermissionError(f"Write permission denied for database file '{db_path}'")

@tool("fetch_customer_information")
def fetch_customer_information(config: RunnableConfig) -> list[dict]:
    """
    Fetch customer information from the database.

    Args:
        config (RunnableConfig): Configuration object containing customer_id.

    Returns:
        list[dict]: List of customer information dictionaries.
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

@tool("fetch_installation_requirements")
def fetch_installation_requirements(config: RunnableConfig) -> dict:
    """
    Fetch installation requirements from the database.

    Args:
        config (RunnableConfig): Configuration object containing product_id.

    Returns:
        dict: Dictionary of installation requirements.
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

@tool("fetch_installation_slots")
def fetch_installation_slots(config: RunnableConfig) -> dict:
    """
    Fetch installation slots from the database.

    Args:
        config (RunnableConfig): Configuration object containing slot_id.

    Returns:
        dict: Dictionary of installation slots.
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

@tool("fetch_region_requirements")
def fetch_region_requirements(country: Optional[str] = None) -> list[dict]:
    """
    Fetch region requirements from the database.

    Args:
        country (Optional[str]): Country to filter the requirements.

    Returns:
        list[dict]: List of region requirements dictionaries.
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

@tool("fetch_required_tools")
def fetch_required_tools() -> list[dict]:
    """
    Fetch required tools from the database.

    Returns:
        list[dict]: List of required tools dictionaries.
    """
    if not check_db_exists(db):
        raise FileNotFoundError(f"Database file '{db}' not found.")
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM required_tools;")
    results = cursor.fetchall()
    conn.close()
    return [dict(zip([column[0] for column in cursor.description], row)) for row in results]

@tool("fetch_work_order_steps")
def fetch_work_order_steps(template_id: Optional[int] = None) -> list[dict]:
    """
    Fetch work order steps from the database.

    Args:
        template_id (Optional[int]): Template ID to filter the steps.

    Returns:
        list[dict]: List of work order steps dictionaries.
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

@tool("fetch_work_order_templates")
def fetch_work_order_templates(template_id: Optional[int] = None) -> list[dict]:
    """
    Fetch work order templates from the database.

    Args:
        template_id (Optional[int]): Template ID to filter the templates.

    Returns:
        list[dict]: List of work order templates dictionaries.
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

@tool("update_installation_service")
def update_installation_service(slot_id: int, available: str) -> None:
    """
    Update installation service availability in the database.

    Args:
        slot_id (int): Slot ID to update.
        available (str): Availability status.

    Returns:
        None
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