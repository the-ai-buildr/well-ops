"""The project setup page."""

import reflex as rx

from ...templates import template

def_project_stepper() -> rx.Component:
    """The project setup page.

    Returns:
        The UI for the project setup page.
    """
    container = rx.container(
        rx.vstack(
            rx.heading("Project Setup", size="5"),
            rx.text("This is the project setup page."),
        )
    )
    
    return rx.text("Project Setup Page")



@template(route="/projects/setup", title="Setup")
def setup() -> rx.Component:
    """The setup page.

    Returns:
        The UI for the setup page.
    """
    return rx.text("Setup Page")
