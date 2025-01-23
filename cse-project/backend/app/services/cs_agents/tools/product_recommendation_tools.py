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
    if not os.access(db_path, os.R.OK):
        raise PermissionError(f"Read permission denied for database file '{db_path}'")
    if not os.access(db_path, os.W.OK):
        raise PermissionError(f"Write permission denied for database file '{db_path}'")

@tool("fetch_product_information")
def fetch_product_information(config: RunnableConfig) -> dict:
    """
    Fetch product information from the database.

    Args:
        config (RunnableConfig): Configuration object containing product_id.

    Returns:
        dict: Dictionary of product information.
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

@tool("fetch_product_specifications")
def fetch_product_specifications(config: RunnableConfig) -> dict:
    """
    Fetch product specifications from the database.

    Args:
        config (RunnableConfig): Configuration object containing product_id.

    Returns:
        dict: Dictionary of product specifications.
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

@tool("fetch_product_compatibility")
def fetch_product_compatibility(config: RunnableConfig) -> dict:
    """
    Fetch product compatibility information from the database.

    Args:
        config (RunnableConfig): Configuration object containing product_id.

    Returns:
        dict: Dictionary of product compatibility information.
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

@tool("fetch_product_recommendations")
def fetch_product_recommendations(config: RunnableConfig) -> dict:
    """
    Fetch product recommendations from the database.

    Args:
        config (RunnableConfig): Configuration object containing product_id.

    Returns:
        dict: Dictionary of product recommendations.
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