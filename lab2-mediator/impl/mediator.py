from api.mediator import BaseMediator


class Mediator(BaseMediator):

    def __init__(self, order_page, delivery_date_selector, recipient_fields, pickup_option):
        self.order_page = order_page
        self.delivery_date_selector = delivery_date_selector
        self.recipient_fields = recipient_fields
        self.pickup_option = pickup_option

    def update_time_slots(self, date):
        # Update the available time slots based on the selected date
        pass

    def toggle_recipient_fields(self, is_another_person):
        # Toggle the visibility of the Name and Phone fields based on the checkbox state
        pass

    def toggle_form_activity(self, is_pickup):
        # Toggle the form elements' activity based on the pickup option
        pass

    def notify_date_selected(self, date):
        # Handle the selected date notification from the delivery date selector
        pass

    def notify_recipient_visibility(self, is_visible):
        # Handle the recipient visibility notification from the recipient fields
        pass

    def notify_pickup_option(self, is_pickup):
        # Handle the pickup option notification from the pickup option component
        pass
