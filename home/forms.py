from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit


SERVICE_CHOICES = [
    ("gestion_produccion_evento", "Gestión / Producción de Eventos"),
    ("promocion_difusion", "Promoción & Difusión"),
    ("desarrollo_web", "Web & Presencia Digital"),
    ("booking", "Booking & Representación"),
]


class ContactForm(forms.Form):
    name = forms.CharField(label="NOMBRE", max_length=100)
    email = forms.EmailField(label="EMAIL")
    services = forms.MultipleChoiceField(
        label="¿Qué necesitas?",
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    message = forms.CharField(
        label="MENSAJE",
        widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Explica cómo te podemos ayudar con tus propias palabras ...",
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = ""
        self.helper.form_tag = True

        self.helper.layout = Layout(
            Div(Field("name"), css_class="form-group"),
            Div(Field("email"), css_class="form-group"),
            Fieldset(
                "¿Qué necesitas?",
                Field("services"),
                css_class="form-group form-options",
            ),
            Div(Field("message"), css_class="form-group"),
            Submit(
                "submit",
                "ENVIAR MENSAJE",
                css_class="contact-submit-btn",
            ),
        )