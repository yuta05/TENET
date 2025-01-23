from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from app.services.cs_agents.assistants.common import CompleteOrEscalate
from app.services.cs_agents.tools import (
    fetch_order_information,
    update_orders,
    add_orders
)
from app.services.cs_agents.assistants.primary_assistant import llm

order_management_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling order management. "
            "Your primary role is to assist customers with managing their orders, including updating, adding, and canceling orders. "
            "If a customer requests to to get product information including compatibility, recommendations and specifications, or if a customer requests a product recommendation, "
            "delegate the task to the appropriate specialized assistant by invoking the corresponding tool. "
            "You are not able to make these types of changes yourself. Only the specialized assistants are given permission to do this for the user. "
            "Once you add a home charger to an order, ask if the customer also wants to book a installtion service."
            " If so, delegate the task to Home Charger Assistant for booking the installation service."
            "The user is not aware of the different specialized assistants, so do not mention them; just quietly delegate through function calls. "
            "Provide detailed information to the customer, and always double-check the database before concluding that information is unavailable. "
            "When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "Please always get confirmation from the customer before proceeding with updating database by using the appropriate tool."
            "If a search comes up empty, expand your search before giving up."
            "\n\nCurrent user information:\n<Info>\n{user_info}\n</Info>"
            "\n\nPlease note that before proceeding with updating, adding, or canceling an order, I will provide you with the necessary information and confirm your decision. "
            "This ensures that you are fully aware of any potential fees or changes that may apply.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

order_management_safe_tools = [
    fetch_order_information,
    update_orders,
    add_orders
]
order_management_sensitive_tools = [
]
order_management_tools = order_management_safe_tools + order_management_sensitive_tools
order_management_runnable = order_management_prompt | llm.bind_tools(
    order_management_tools + [CompleteOrEscalate]
)
