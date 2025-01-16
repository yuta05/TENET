import sys
import os
import pytest
from langchain_core.runnables import RunnableConfig

# プロジェクトのルートディレクトリを追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from app.services.cs_agents.tools.home_charger_tools import (
    fetch_customer_information,
    fetch_order_information,
    fetch_product_information,
    fetch_product_specifications,
    fetch_installation_requirements,
    fetch_installation_slots,
    fetch_product_compatibility,
    fetch_product_recommendations,
    fetch_region_requirements,
    fetch_required_tools,
    fetch_work_order_steps,
    fetch_work_order_templates,
    add_orders,
    update_orders,
    update_installation_service,
    insert_order  # insert_order関数をインポート
)

# テスト用の設定
customer_id = "CUST-001"
config = RunnableConfig(configurable={"customer_id": customer_id})

def test_fetch_customer_information():
    print("Testing fetch_customer_information...")
    customers = fetch_customer_information.invoke(input={}, config=config)
    assert len(customers) > 0
    for customer in customers:
        print(customer)

def test_fetch_order_information():
    print("Testing fetch_order_information...")
    orders = fetch_order_information.invoke(input={}, config=config)
    assert "messages" in orders
    for order in orders["messages"]:
        print(order)

def test_fetch_product_information():
    print("Testing fetch_product_information...")
    products = fetch_product_information.invoke(input={}, config=config)
    assert "product_info" in products
    for product in products["product_info"]:
        print(product)

def test_fetch_product_specifications():
    print("Testing fetch_product_specifications...")
    specifications = fetch_product_specifications.invoke(input={}, config=config)
    assert "product_specifications" in specifications
    for spec in specifications["product_specifications"]:
        print(spec)

def test_fetch_installation_requirements():
    print("Testing fetch_installation_requirements...")
    requirements = fetch_installation_requirements.invoke(input={}, config=config)
    assert "installation_requirements" in requirements
    for requirement in requirements["installation_requirements"]:
        print(requirement)

def test_fetch_installation_slots():
    print("Testing fetch_installation_slots...")
    slots = fetch_installation_slots.invoke(input={}, config=config)
    assert "installation_slots" in slots
    for slot in slots["installation_slots"]:
        print(slot)

def test_fetch_product_compatibility():
    print("Testing fetch_product_compatibility...")
    compatibility = fetch_product_compatibility.invoke(input={}, config=config)
    assert "product_compatibility" in compatibility
    for comp in compatibility["product_compatibility"]:
        print(comp)

def test_fetch_product_recommendations():
    print("Testing fetch_product_recommendations...")
    recommendations = fetch_product_recommendations.invoke(input={}, config=config)
    assert "product_recommendations" in recommendations
    for recommendation in recommendations["product_recommendations"]:
        print(recommendation)

def test_fetch_region_requirements():
    print("Testing fetch_region_requirements...")
    requirements = fetch_region_requirements.invoke(input={}, config=config)
    assert len(requirements) > 0
    for requirement in requirements:
        print(requirement)

def test_fetch_required_tools():
    print("Testing fetch_required_tools...")
    tools = fetch_required_tools.invoke(input={}, config=config)
    assert len(tools) > 0
    for tool in tools:
        print(tool)

def test_fetch_work_order_steps():
    print("Testing fetch_work_order_steps...")
    steps = fetch_work_order_steps.invoke(input={}, config=config)
    assert len(steps) > 0
    for step in steps:
        print(step)

def test_fetch_work_order_templates():
    print("Testing fetch_work_order_templates...")
    templates = fetch_work_order_templates.invoke(input={}, config=config)
    assert len(templates) > 0
    for template in templates:
        print(template)

def test_add_orders():
    print("Testing add_orders...")
    result = add_orders.invoke(
        input={
            "order_id": "ORD-2024-0715-003",
            "customer_id": "CUST-001",
            "product_id": "F100-WALL",
            "order_date": "2024-07-15",
            "status": "confirmed",
            "delivery_status": "scheduled",
            "estimated_delivery": "2024-Q3"
        },
        config=config
    )
    print(result)

def test_update_orders():
    print("Testing update_orders...")
    result = update_orders.invoke(
        input={
            "order_id": "ORD-2024-0715-003",
            "status": "cancelled"
        },
        config=config
    )
    print(result)

def test_update_installation_service():
    print("Testing update_installation_service...")
    update_installation_service.invoke(
        input={
            "slot_id": 1,
            "available": "FALSE"
        },
        config=config
    )
    slots = fetch_installation_slots.invoke(input={}, config=config)
    assert any(slot["slot_id"] == 1 and slot["available"] == "FALSE" for slot in slots["installation_slots"])

def test_insert_order():
    print("Testing insert_order...")
    result = insert_order.invoke(
        input={
            "order_id": "ORD-2024-0715-001",
            "customer_id": "CUST-001",
            "product_id": "PX-VPX1B",
            "order_date": "2024-07-15",
            "status": "confirmed",
            "delivery_status": "scheduled",
            "estimated_delivery": "2024-Q3"
        },
        config=config
    )
    print(result)

if __name__ == "__main__":
    # test_fetch_customer_information()
    # test_fetch_order_information()
    # test_fetch_product_information()
    # test_fetch_product_specifications()
    # test_fetch_installation_requirements()
    # test_fetch_installation_slots()
    # test_fetch_product_compatibility()
    # test_fetch_product_recommendations()
    # test_fetch_region_requirements()
    # test_fetch_required_tools()
    # test_fetch_work_order_steps()
    # test_fetch_work_order_templates()
    # test_add_orders()
    test_update_orders()
    test_update_installation_service()
    # test_insert_order()  # insert_orderのテストを実行