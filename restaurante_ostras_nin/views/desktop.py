import reflex as rx

from restaurante_ostras_nin.components.apreciations import apreciations
from restaurante_ostras_nin.components.button_whastapp import button_whastapp
from restaurante_ostras_nin.components.contact_box import contact_box
from restaurante_ostras_nin.components.image_oyster import image_oyster
from restaurante_ostras_nin.components.logo import logo
from restaurante_ostras_nin.components.main_text import main_text
from restaurante_ostras_nin.styles import utils as utils


def desktop() -> rx.Component:
    return rx.desktop_only(
        rx.box(
            rx.hstack(
                rx.vstack(
                    logo(),
                    rx.heading(utils.title, size="8"),
                    main_text(utils.text_below_title_one),
                    main_text(utils.text_below_title_two),
                    contact_box(),
                    apreciations(),
                    button_whastapp(),
                    align_items="start",
                    justify="center",
                    gap="24px",
                    padding_right="480px",
                ),
                image_oyster(
                    position="absolute",
                    right="0px",
                    bottom="0px",
                ),
            ),
            width="100%",
            flex="1 0 0",
            padding="30px 80px 86px 30px",
            height="100vh",
        ),
    )
