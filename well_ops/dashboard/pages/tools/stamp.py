"""The about page."""

from pathlib import Path

import reflex as rx

from ... import styles
from ...templates import template


@template(route="/tools/stamp", title="Stamp")
def stamp() -> rx.Component:
    """The stamp page.

    Returns:
        The UI for the stamp page.
    """
    return rx.text("Stamp")
