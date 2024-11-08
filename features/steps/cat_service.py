from behave import given, when, then
from common import CatService

@given("I have initialized the cat service")
def step_initialize_cat_service(context):
    context.cat_service = CatService()

@when("I request all cats")
def step_request_all_cats(context):
    context.response = context.cat_service.get_cats()

@then("I should receive a list of cats")
def step_receive_list_of_cats(context):
    assert isinstance(context.response, list), "Expected a list of cats"
    assert len(context.response) > 0, "Expected at least one cat in the list"

@when('I request a cat with ID {cat_id}')
def step_request_cat_by_id(context, cat_id):
    context.response = context.cat_service.get_cat(cat_id)

@then("I should receive the details for that cat")
def step_receive_cat_details(context):
    assert isinstance(context.response, dict), "Expected a dictionary with cat details"
    assert "id" in context.response and "name" in context.response, "Expected 'id' and 'name' in cat details"
