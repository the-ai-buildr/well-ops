"""The projects index page."""

import reflex as rx

from ...templates import template


@template(route="/projects/my-projects", title="My Projects")
def index() -> rx.Component:
    """The my projects page.

    Returns:
        The UI for the my projects page.
    """
    return rx.text("My Projects Page")
