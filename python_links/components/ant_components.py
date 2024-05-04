import reflex as rx

class FloatButton(rx.Component):
    library = "antd"
    tag= "FloatButton"
    icon = rx.image(src="/icons/donation.svg")
    href= "https://buymeacoffee.com/juanppdev"
    target= "_blank"
    badge = { "dot": True } 

float_button = FloatButton.create