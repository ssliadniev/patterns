from abc import ABC, abstractmethod


class BaseMediator(ABC):

    @abstractmethod
    def update_time_slots(self, date):
        # Update the available time slots based on the selected date
        pass

    @abstractmethod
    def toggle_recipient_fields(self, is_another_person):
        # Toggle the visibility of the Name and Phone fields based on the checkbox state
        pass

    @abstractmethod
    def toggle_form_activity(self, is_pickup):
        # Toggle the form elements' activity based on the pickup option
        pass

    @abstractmethod
    def notify_date_selected(self, date):
        # Handle the selected date notification from the delivery date selector
        pass

    @abstractmethod
    def notify_recipient_visibility(self, is_visible):
        # Handle the recipient visibility notification from the recipient fields
        pass

    @abstractmethod
    def notify_pickup_option(self, is_pickup):
        # Handle the pickup option notification from the pickup option component
        pass
