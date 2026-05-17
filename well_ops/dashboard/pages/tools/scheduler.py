"""The scheduler page."""

import reflex as rx

from ...templates import template


@template(route="/tools/scheduler", title="Scheduler")
def scheduler() -> rx.Component:
    """The scheduler page.

    Returns:
        The UI for the scheduler page.
    """
    return rx.text("Scheduler Page")
