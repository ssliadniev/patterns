class DeliveryDateSelector:
    def __init__(self, mediator):
        self.mediator = mediator

    def select_date(self, date):
        # Notify the mediator about the selected date
        self.mediator.notify_date_selected(date)
