from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from app.services.cs_agents.assistants.common import CompleteOrEscalate
from app.services.cs_agents.tools import (
    fetch_customer_information,
    fetch_order_information,
    fetch_product_information,
    fetch_product_specifications,
    fetch_region_requirements,
    fetch_required_tools,
    fetch_work_order_steps,
    fetch_work_order_templates,
)
from app.services.cs_agents.assistants.primary_assistant import llm

home_charger_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling home charger installation requests. "
            "The primary assistant delegates work to you whenever the user needs help setting up a home charger. "
            "Fetch the requested information from the database and provide it to the user. "
            "Confirm the installation details with the customer and inform them of any additional requirements. "
            "When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "If you need more information or the customer changes their mind, escalate the task back to the main assistant."
            " Remember that an installation isn't completed until after the relevant tool has successfully been used."
            "\n\nCurrent user order information:\n<Orders>\n{user_info}\n</Orders>"
            "\nCurrent time: {time}."
            "\n\nIf the user needs help, and none of your tools are appropriate for it, then"
            ' "CompleteOrEscalate" the dialog to the host assistant. Do not waste the user\'s time. Do not make up invalid tools or functions.',
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

home_charger_safe_tools = [
    fetch_customer_information,
    fetch_order_information,
    fetch_product_information,
    fetch_product_specifications,
    fetch_region_requirements,
    fetch_required_tools,
    fetch_work_order_steps,
    fetch_work_order_templates,
]
home_charger_sensitive_tools = []
home_charger_tools = home_charger_safe_tools + home_charger_sensitive_tools
home_charger_runnable = home_charger_prompt | llm.bind_tools(
    home_charger_tools + [CompleteOrEscalate]
)