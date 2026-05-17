"""The stamp page."""

import reflex as rx

from ...templates import template


@template(route="/tools/stamp", title="Stamp")
def stamp() -> rx.Component:
    """The stamp page.

    Returns:
        The UI for the stamp page.
    """
    return rx.text("Stamp Page")
