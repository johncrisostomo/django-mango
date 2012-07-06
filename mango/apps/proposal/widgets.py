from django.forms import MultiWidget, TextInput, Select


class TimeDurationWidget(MultiWidget):
    def __init__(self, attrs=None, choices=None):
        widgets = (TextInput(attrs=attrs),
                   Select(attrs=attrs, choices=choices))
        super(TimeDurationWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split()
        return [None, None]


class TimeDurationHiddenWidget(TimeDurationWidget):
    is_hidden = True

    def __init__(self, *args, **kwargs):
        super(TimeDurationHiddenWidget, self).__init__(*args, **kwargs)
        for widget in self.widgets:
            widget.input_type = 'hidden'
            widget.is_hidden = True
