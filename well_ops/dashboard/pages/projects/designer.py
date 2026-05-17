"""The project designer page."""

import reflex as rx

from ...templates import template


@template(route="/projects/designer", title="Designer")
def designer() -> rx.Component:
    """The project designer page.

    Returns:
        The UI for the project page.
    """
    return rx.text("Project Page")
