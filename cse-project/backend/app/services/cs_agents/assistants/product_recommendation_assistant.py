from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from app.services.cs_agents.assistants.common import CompleteOrEscalate
from app.services.cs_agents.tools import (
    fetch_product_information,
    fetch_product_specifications,
    fetch_product_compatibility,
    fetch_product_recommendations
)
from app.services.cs_agents.assistants.primary_assistant import llm

product_recommendation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a specialized assistant for handling product recommendations. "
            "Your primary role is to assist customers with product information, compatibility, specifications, and recommendations. "
            "If a customer requests other things, delegate the task to the appropriate specialized assistant by invoking the corresponding tool. "
            "You are not able to make these types of changes yourself. Only the specialized assistants are given permission to do this for the user. "
            "The user is not aware of the different specialized assistants, so do not mention them; just quietly delegate through function calls. "
            "Provide detailed information to the customer, and always double-check the database before concluding that information is unavailable. "
            "When searching, be persistent. Expand your query bounds if the first search returns no results. "
            "If a search comes up empty, expand your search before giving up."
            "\n\nCurrent user information:\n<Info>\n{user_info}\n</Info>"
            "\n\nPlease note that before proceeding with providing product recommendations, I will provide you with the necessary information and confirm your decision. "
            "This ensures that you are fully aware of any potential fees or changes that may apply.",
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

product_recommendation_safe_tools = [
    fetch_product_information,
    fetch_product_specifications,
    fetch_product_compatibility,
    fetch_product_recommendations
]
product_recommendation_sensitive_tools = [
    # Add any sensitive tools here
]
product_recommendation_tools = product_recommendation_safe_tools + product_recommendation_sensitive_tools
product_recommendation_runnable = product_recommendation_prompt | llm.bind_tools(
    product_recommendation_tools + [CompleteOrEscalate]
)