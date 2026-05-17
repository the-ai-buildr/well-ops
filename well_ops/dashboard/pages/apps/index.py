"""The tools index page."""

import reflex as rx

from ...templates import template


@template(route="/apps/index", title="Apps")
def index() -> rx.Component:
    """The tools index page.

    Returns:
        The UI for the apps index page.
    """
    return rx.text("Apps Index")
