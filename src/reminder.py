class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteReminder(PrefixedReminder):
    """[summary]

    Args:
        PrefixedReminder ([type]): [description]
    """
    def __init__(self, text, prefix="Hey, don't forget to "):
        text = prefix + text
        super().__init__(prefix='Please do =>')