"""The project setup page."""

import reflex as rx

from ...components.card import card
from ...components.stepper import StepperStep, horizontal_stepper
from ...templates import template


PROJECT_SETUP_STEPS = [
    StepperStep("Details", "clipboard-list"),
    StepperStep("Design", "drafting-compass"),
    StepperStep("Review", "search-check"),
    StepperStep("Launch", "rocket"),
]


class ProjectSetupState(rx.State):
    active_step: int = 0

    def previous_step(self):
        self.active_step = max(self.active_step - 1, 0)

    def next_step(self):
        self.active_step = min(self.active_step + 1, len(PROJECT_SETUP_STEPS) - 1)


def _setup_step_container() -> rx.Component:
    return card(
        rx.vstack(
            rx.heading(
                rx.match(
                    ProjectSetupState.active_step,
                    (0, "Details"),
                    (1, "Design"),
                    (2, "Review"),
                    (3, "Launch"),
                    "Details",
                ),
                size="4",
            ),
            rx.text(
                rx.match(
                    ProjectSetupState.active_step,
                    (0, "Define the project name, scope, and initial requirements."),
                    (1, "Configure the project layout, tools, and handoff plan."),
                    (2, "Review assumptions, risks, and outstanding setup items."),
                    (3, "Finalize the setup and prepare the project for launch."),
                    "Define the project name, scope, and initial requirements.",
                )
            ),
            rx.hstack(
                rx.button(
                    "Previous",
                    on_click=ProjectSetupState.previous_step,
                    disabled=ProjectSetupState.active_step == 0,
                    variant="soft",
                ),
                rx.button(
                    "Next",
                    on_click=ProjectSetupState.next_step,
                    disabled=ProjectSetupState.active_step
                    == len(PROJECT_SETUP_STEPS) - 1,
                ),
                justify="end",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
    )


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
            active_step=ProjectSetupState.active_step,
            container=_setup_step_container(),
        ),
        spacing="5",
        width="100%",
    )
