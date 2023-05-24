class RecipientFields:
    def __init__(self, mediator):
        self.mediator = mediator

    def toggle_visibility(self, is_visible):
        # Notify the mediator about the visibility of the recipient fields
        self.mediator.notify_recipient_visibility(is_visible)
