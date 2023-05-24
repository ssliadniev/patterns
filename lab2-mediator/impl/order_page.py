class OrderPage:

    def __init__(self, mediator):
        self.mediator = mediator

    def select_delivery_date(self, date):
        # Update the available time slots based on the selected date
        self.mediator.update_time_slots(date)

    def toggle_recipient_another_person(self, is_another_person):
        # Toggle the visibility of the Name and Phone fields based on the checkbox state
        self.mediator.toggle_recipient_fields(is_another_person)

    def select_pickup_option(self, is_pickup):
        # Toggle the form elements' activity based on the pickup option
        self.mediator.toggle_form_activity(is_pickup)

    def toggle_pickup_from_store(self, state):
        """
        Toggle the pickup from store state and notify the mediator.
        """
        self.pickup_from_store = state
        self.mediator.notify(self, "pickup_state_changed")
