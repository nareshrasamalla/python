import logging
import os
from os.path import dirname
from pytest_bdd import scenario, given, when, then

logging.basicConfig(level=logging.INFO)


class AXISModifyCommittment(RuntimeError):
    pass

@given('Create mi order with created RQ$')
def create_mi_order_with_created_RQ():
    print("Step1")
@when('Login to AXIS-O as processor and open the application')
def login_to_AXIS_O_as_processor_and_open_the_application():
    print("Step2")
@when('Validate pricing information')
def validate_pricing_information():
    print("Step3")
@when('Re Submit MI Order with some data changes')
def re_Submit_MI_Order_with_some_data_changes():
    print("Step4")
@when('Login as solution center manager and open the application')
def login_as_solution_center_manager_and_open_the_application():
    print("Step5")
@when('Navigate to Modify commitment in actions and make some changes to the application')
def navigate_to_Modify_commitment_in_actions_and_make_some_changes_to_the_application():
    print("Step6")
@then('Validate chages in Application$')
def validate_chages_in_Application():
    print("Step7")
