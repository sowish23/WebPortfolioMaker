from django import forms

class DatePickerWidget(forms.DateInput):
    template_name = "widgets/picker_date.html"

    class Media:
        css = {
            'all': [
                "//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/themes/base/jquery-ui.min.css",
            ],
        }

        js = [
            "//code.jquery.com/jquery-3.4.1.min.js",
            "//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js",
        ]