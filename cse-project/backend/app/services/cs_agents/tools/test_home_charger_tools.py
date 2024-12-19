from home_charger_tools import (
    fetch_customer_information,
    fetch_order_information,
    fetch_product_information,
    fetch_product_specifications,
    fetch_region_requirements,
    fetch_required_tools,
    fetch_work_order_steps,
    fetch_work_order_templates,
)
from langchain_core.runnables import RunnableConfig

customer_id = "CUST-001"
thread_id = "THREAD-001"

def test_fetch_customer_information():
    print("Testing fetch_customer_information...")
    config = {
        "configurable": {
            "customer_id": customer_id,
            "thread_id": thread_id,
        }
    }
    customers = fetch_customer_information(config)  # invoke メソッドを使用
    for customer in customers:
        print(customer)

def test_fetch_order_information():
    print("Testing fetch_order_information...")
    orders = fetch_order_information(customer_id=customer_id)
    for order in orders:
        print(order)

def test_fetch_product_information():
    print("Testing fetch_product_information...")
    products = fetch_product_information(product_id="P50-HOME")
    for product in products:
        print(product)

def test_fetch_product_specifications():
    print("Testing fetch_product_specifications...")
    specifications = fetch_product_specifications(product_id="P50-HOME")
    for spec in specifications:
        print(spec)

def test_fetch_region_requirements():
    print("Testing fetch_region_requirements...")
    requirements = fetch_region_requirements(country="USA")
    for requirement in requirements:
        print(requirement)

if __name__ == "__main__":
    test_fetch_customer_information()
    test_fetch_order_information()
    test_fetch_product_information()
    test_fetch_product_specifications()
    test_fetch_region_requirements()