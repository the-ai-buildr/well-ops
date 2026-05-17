"""The cement tool page."""

import reflex as rx

from ...templates import template


@template(route="/tools/cement", title="Cement")
def cement() -> rx.Component:
    """The cement page.

    Returns:
        The UI for the cement page.
    """
    return rx.text("Cement Page")
