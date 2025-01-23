from typing import Literal
from langgraph.prebuilt import tools_condition
from langgraph.graph import END
from app.services.cs_agents.assistants.common import CompleteOrEscalate
from app.services.cs_agents.assistants.primary_assistant import ToFlightBookingAssistant, ToBookCarRental, ToHotelBookingAssistant, ToBookExcursion, ToHomeChargerAssistant, ToOrderManagementAssistant, ToProductRecommendationAssistant
from app.services.cs_agents.state import State
from app.services.cs_agents.assistants.flight_booking_assistant import update_flight_safe_tools
from app.services.cs_agents.assistants.hotel_booking_assistant import book_hotel_safe_tools
from app.services.cs_agents.assistants.car_rental_assistant import book_car_rental_safe_tools
from app.services.cs_agents.assistants.excursion_assistant import book_excursion_safe_tools
from app.services.cs_agents.assistants.home_charger_assistant import home_charger_safe_tools
from app.services.cs_agents.assistants.order_management_assistant import order_management_safe_tools
from app.services.cs_agents.assistants.product_recommendation_assistant import product_recommendation_safe_tools

def route_update_flight(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    safe_toolnames = [t.name for t in update_flight_safe_tools]
    if all(tc["name"] in safe_toolnames for tc in tool_calls):
        return "update_flight_safe_tools"
    return "update_flight_sensitive_tools"

def route_book_car_rental(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    safe_toolnames = [t.name for t in book_car_rental_safe_tools]
    if all(tc["name"] in safe_toolnames for tc in tool_calls):
        return "book_car_rental_safe_tools"
    return "book_car_rental_sensitive_tools"

def route_book_hotel(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    tool_names = [t.name for t in book_hotel_safe_tools]
    if all(tc["name"] in tool_names for tc in tool_calls):
        return "book_hotel_safe_tools"
    return "book_hotel_sensitive_tools"

def route_book_excursion(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    tool_names = [t.name for t in book_excursion_safe_tools]
    if all(tc["name"] in tool_names for tc in tool_calls):
        return "book_excursion_safe_tools"
    return "book_excursion_sensitive_tools"

def route_home_charger(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    tool_names = [t.name for t in home_charger_safe_tools]
    if all(tc["name"] in tool_names for tc in tool_calls):
        return "home_charger_safe_tools"
    return "home_charger_sensitive_tools"

def route_order_management(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    tool_names = [t.name for t in order_management_safe_tools]
    if all(tc["name"] in tool_names for tc in tool_calls):
        return "order_management_safe_tools"
    return "order_management_sensitive_tools"

def route_product_recommendation(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "leave_skill"
    tool_names = [t.name for t in product_recommendation_safe_tools]
    if all(tc["name"] in tool_names for tc in tool_calls):
        return "product_recommendation_safe_tools"
    return "product_recommendation_sensitive_tools"

def route_primary_assistant(state: State):
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        if tool_calls[0]["name"] == ToFlightBookingAssistant.__name__:
            return "enter_update_flight"
        elif tool_calls[0]["name"] == ToBookCarRental.__name__:
            return "enter_book_car_rental"
        elif tool_calls[0]["name"] == ToHotelBookingAssistant.__name__:
            return "enter_book_hotel"
        elif tool_calls[0]["name"] == ToBookExcursion.__name__:
            return "enter_book_excursion"
        elif tool_calls[0]["name"] == ToHomeChargerAssistant.__name__:
            return "enter_home_charger"
        elif tool_calls[0]["name"] == ToOrderManagementAssistant.__name__:
            return "enter_order_management"
        elif tool_calls[0]["name"] == ToProductRecommendationAssistant.__name__:
            return "enter_product_recommendation"
        return "primary_assistant_tools"
    raise ValueError("Invalid route")

def route_to_workflow(state: State) -> Literal[
    "primary_assistant",
    # "update_flight",
    # "book_car_rental",
    # "book_hotel",
    # "book_excursion",
    "home_charger",
    "order_management",
    "product_recommendation",
]:
    """If we are in a delegated state, route directly to the appropriate assistant."""
    dialog_state = state.get("dialog_state")
    if not dialog_state:
        return "primary_assistant"
    return dialog_state[-1]