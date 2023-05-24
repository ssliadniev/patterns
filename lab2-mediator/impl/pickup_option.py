class PickupOption:
    def __init__(self, mediator):
        self.mediator = mediator

    def toggle_pickup(self, is_pickup):
        # Notify the mediator about the pickup option
        self.mediator.notify_pickup_option(is_pickup)
