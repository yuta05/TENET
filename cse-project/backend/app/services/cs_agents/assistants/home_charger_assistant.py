from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from app.services.cs_agents.assistants.common import CompleteOrEscalate
from app.services.cs_agents.tools import (
    fetch_customer_information,
    fetch_region_requirements,
    fetch_required_tools,
    fetch_work_order_steps,
    fetch_work_order_templates,
    fetch_installation_requirements,
    fetch_installation_slots,
    update_installation_service
)
from app.services.cs_agents.assistants.primary_assistant import llm

home_charger_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful customer support assistant for home charger installations service."
            "Your primary role is to assist customers with home charger installations and to provide product information with the setup details. "
            "If a customer requests to update or cancel an order or to get product information including compatibility, recommendations and specifications, "
            "delegate the task to the appropriate specialized assistant or the primary assistant by invoking the corresponding tool. You are not able to make these types of changes yourself. "
            "Only the specialized assistants are given permission to do this for the user. "
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

home_charger_safe_tools = [
    fetch_customer_information,
    fetch_region_requirements,
    fetch_required_tools,
    fetch_work_order_steps,
    fetch_work_order_templates,
    fetch_installation_requirements,
    fetch_installation_slots,
    update_installation_service
]
home_charger_sensitive_tools = [
    
]
home_charger_tools = home_charger_safe_tools + home_charger_sensitive_tools
home_charger_runnable = home_charger_prompt | llm.bind_tools(
    home_charger_tools + [CompleteOrEscalate]
)