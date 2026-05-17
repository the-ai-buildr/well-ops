"""The tools index page."""

import reflex as rx

from ...templates import template


@template(route="/tools/index", title="Tools")
def index() -> rx.Component:
    """The tools index page.

    Returns:
        The UI for the tools index page.
    """
    return rx.text("Tools Index")
