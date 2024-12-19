from typing import Literal
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import ToolMessage
from app.services.cs_agents.assistants.common import Assistant
from app.services.cs_agents.assistants.flight_booking_assistant import update_flight_runnable, update_flight_safe_tools, update_flight_sensitive_tools
from app.services.cs_agents.assistants.hotel_booking_assistant import book_hotel_runnable, book_hotel_safe_tools, book_hotel_sensitive_tools
from app.services.cs_agents.assistants.car_rental_assistant import book_car_rental_runnable, book_car_rental_safe_tools, book_car_rental_sensitive_tools
from app.services.cs_agents.assistants.excursion_assistant import book_excursion_runnable, book_excursion_safe_tools, book_excursion_sensitive_tools
from app.services.cs_agents.assistants.home_charger_assistant import home_charger_runnable, home_charger_safe_tools, home_charger_sensitive_tools
from app.services.cs_agents.assistants.primary_assistant import primary_assistant_runnable, primary_assistant_tools
from app.services.cs_agents.utils import create_entry_node, create_tool_node_with_fallback
from app.services.cs_agents.state import State
from app.services.cs_agents.tools import fetch_customer_information 
from app.services.cs_agents.routes import (
    route_update_flight,
    route_book_car_rental,
    route_book_hotel,
    route_book_excursion,
    route_home_charger,
    route_primary_assistant,
    route_to_workflow,
)

builder = StateGraph(State)

def user_info(state: State):
    return {"user_info": fetch_customer_information.invoke({})}

builder.add_node("fetch_user_info", user_info)
builder.add_edge(START, "fetch_user_info")


# Flight booking assistant
# builder.add_node(
#     "enter_update_flight",
#     create_entry_node("Flight Updates & Booking Assistant", "update_flight"),
# )
# builder.add_node("update_flight", Assistant(update_flight_runnable))
# builder.add_edge("enter_update_flight", "update_flight")
# builder.add_node(
#     "update_flight_sensitive_tools",
#     create_tool_node_with_fallback(update_flight_sensitive_tools),
# )
# builder.add_node(
#     "update_flight_safe_tools",
#     create_tool_node_with_fallback(update_flight_safe_tools),
# )

# builder.add_edge("update_flight_sensitive_tools", "update_flight")
# builder.add_edge("update_flight_safe_tools", "update_flight")
# builder.add_conditional_edges(
#     "update_flight",
#     route_update_flight,
#     ["update_flight_sensitive_tools", "update_flight_safe_tools", "leave_skill", END],
# )


# # Car rental assistant
# builder.add_node(
#     "enter_book_car_rental",
#     create_entry_node("Car Rental Assistant", "book_car_rental"),
# )
# builder.add_node("book_car_rental", Assistant(book_car_rental_runnable))
# builder.add_edge("enter_book_car_rental", "book_car_rental")
# builder.add_node(
#     "book_car_rental_safe_tools",
#     create_tool_node_with_fallback(book_car_rental_safe_tools),
# )
# builder.add_node(
#     "book_car_rental_sensitive_tools",
#     create_tool_node_with_fallback(book_car_rental_sensitive_tools),
# )

# builder.add_edge("book_car_rental_sensitive_tools", "book_car_rental")
# builder.add_edge("book_car_rental_safe_tools", "book_car_rental")
# builder.add_conditional_edges(
#     "book_car_rental",
#     route_book_car_rental,
#     [
#         "book_car_rental_safe_tools",
#         "book_car_rental_sensitive_tools",
#         "leave_skill",
#         END,
#     ],
# )

# # Hotel booking assistant
# builder.add_node(
#     "enter_book_hotel", create_entry_node("Hotel Booking Assistant", "book_hotel")
# )
# builder.add_node("book_hotel", Assistant(book_hotel_runnable))
# builder.add_edge("enter_book_hotel", "book_hotel")
# builder.add_node(
#     "book_hotel_safe_tools",
#     create_tool_node_with_fallback(book_hotel_safe_tools),
# )
# builder.add_node(
#     "book_hotel_sensitive_tools",
#     create_tool_node_with_fallback(book_hotel_sensitive_tools),
# )

# builder.add_edge("book_hotel_sensitive_tools", "book_hotel")
# builder.add_edge("book_hotel_safe_tools", "book_hotel")
# builder.add_conditional_edges(
#     "book_hotel",
#     route_book_hotel,
#     ["leave_skill", "book_hotel_safe_tools", "book_hotel_sensitive_tools", END],
# )

# # Excursion assistant
# builder.add_node(
#     "enter_book_excursion",
#     create_entry_node("Trip Recommendation Assistant", "book_excursion"),
# )
# builder.add_node("book_excursion", Assistant(book_excursion_runnable))
# builder.add_edge("enter_book_excursion", "book_excursion")
# builder.add_node(
#     "book_excursion_safe_tools",
#     create_tool_node_with_fallback(book_excursion_safe_tools),
# )
# builder.add_node(
#     "book_excursion_sensitive_tools",
#     create_tool_node_with_fallback(book_excursion_sensitive_tools),
# )

# builder.add_edge("book_excursion_sensitive_tools", "book_excursion")
# builder.add_edge("book_excursion_safe_tools", "book_excursion")
# builder.add_conditional_edges(
#     "book_excursion",
#     route_book_excursion,
#     ["book_excursion_safe_tools", "book_excursion_sensitive_tools", "leave_skill", END],
# )

# Home charger assistant
builder.add_node(
    "enter_home_charger",
    create_entry_node("Home Charger Assistant", "home_charger"),
)
builder.add_node("home_charger", Assistant(home_charger_runnable))
builder.add_edge("enter_home_charger", "home_charger")
builder.add_node(
    "home_charger_safe_tools",
    create_tool_node_with_fallback(home_charger_safe_tools),
)
builder.add_node(
    "home_charger_sensitive_tools",
    create_tool_node_with_fallback(home_charger_sensitive_tools),
)

builder.add_edge("home_charger_sensitive_tools", "home_charger")
builder.add_edge("home_charger_safe_tools", "home_charger")
builder.add_conditional_edges(
    "home_charger",
    route_home_charger,
    ["home_charger_safe_tools", "home_charger_sensitive_tools", "leave_skill", END],
)

# This node will be shared for exiting all specialized assistants
def pop_dialog_state(state: State) -> dict:
    """Pop the dialog stack and return to the main assistant.

    This lets the full graph explicitly track the dialog flow and delegate control
    to specific sub-graphs.
    """
    messages = []
    if state["messages"][-1].tool_calls:
        # Note: Doesn't currently handle the edge case where the llm performs parallel tool calls
        messages.append(
            ToolMessage(
                content="Resuming dialog with the host assistant. Please reflect on the past conversation and assist the user as needed.",
                tool_call_id=state["messages"][-1].tool_calls[0]["id"],
            )
        )
    return {
        "dialog_state": "pop",
        "messages": messages,
    }

builder.add_node("leave_skill", pop_dialog_state)
builder.add_edge("leave_skill", "primary_assistant")

# Primary assistant
builder.add_node("primary_assistant", Assistant(primary_assistant_runnable))
builder.add_node(
    "primary_assistant_tools", create_tool_node_with_fallback(primary_assistant_tools)
)

# The assistant can route to one of the delegated assistants,
# directly use a tool, or directly respond to the user
builder.add_conditional_edges(
    "primary_assistant",
    route_primary_assistant,
    [
        # "enter_update_flight",
        # "enter_book_car_rental",
        # "enter_book_hotel",
        # "enter_book_excursion",
        "enter_home_charger",
        "primary_assistant_tools",
        END,
    ],
)
builder.add_edge("primary_assistant_tools", "primary_assistant")

builder.add_conditional_edges("fetch_user_info", route_to_workflow)

# Compile graph
memory = MemorySaver()
part_4_graph = builder.compile(
    checkpointer=memory,
    # Let the user approve or deny the use of sensitive tools
    interrupt_before=[
        # "update_flight_sensitive_tools",
        # "book_car_rental_sensitive_tools",
        # "book_hotel_sensitive_tools",
        # "book_excursion_sensitive_tools",
        "home_charger_sensitive_tools",
    ],
)