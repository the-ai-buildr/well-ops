"""The project setup page."""

import reflex as rx

from ...components.card import card
from ...components.stepper import StepperStep, horizontal_stepper
from ...templates import template


PROJECT_SETUP_STEPS = [
    StepperStep("Details", "clipboard-list", "Scope"),
    StepperStep("Design", "drafting-compass", "Layout"),
    StepperStep("Review", "search-check", "Verify"),
    StepperStep("Launch", "rocket", "Ship"),
]


@template(route="/projects/setup", title="Setup")
def setup() -> rx.Component:
    """The setup page.

    Returns:
        The UI for the setup page.
    """
    return rx.vstack(
        rx.heading("Project Setup", size="5"),
        horizontal_stepper(
            PROJECT_SETUP_STEPS,
            active_step=1,
            container=card(
                rx.vstack(
                    rx.heading("Design", size="4"),
                    rx.text("Configure the project layout, tools, and handoff plan."),
                    spacing="2",
                    width="100%",
                ),
            ),
        ),
        spacing="5",
        width="100%",
    )
