"""Reusable horizontal stepper components."""

from dataclasses import dataclass

import reflex as rx

from .. import styles


@dataclass(frozen=True)
class StepperStep:
    title: str
    icon: str = "circle"


def _step_marker(step: StepperStep, index: int, active_step: int) -> rx.Component:
    is_complete = active_step > index
    is_active = active_step == index
    is_reached = active_step >= index

    return rx.vstack(
        rx.box(
            rx.cond(
                is_complete,
                rx.icon("check", size=16, stroke_width=2),
                rx.icon(step.icon, size=16, stroke_width=2),
            ),
            align_items="center",
            background_color=rx.cond(
                is_reached,
                styles.accent_bg_color,
                styles.gray_bg_color,
            ),
            border="1px solid",
            border_color=rx.cond(
                is_reached,
                styles.accent_text_color,
                rx.color("gray", 6),
            ),
            border_radius="999px",
            color=rx.cond(
                is_reached,
                styles.accent_text_color,
                styles.gray_color,
            ),
            display="flex",
            height="2rem",
            justify_content="center",
            width="2rem",
        ),
        rx.vstack(
            rx.text(
                step.title,
                color=rx.cond(is_reached, styles.accent_text_color, styles.text_color),
                size="2",
                weight=rx.cond(is_active, "medium", "regular"),
                text_align="center",
            ),
            align="center",
            spacing="1",
        ),
        align="center",
        min_width="5rem",
        spacing="2",
    )


def _step_connector(index: int, active_step: int) -> rx.Component:
    return rx.box(
        background_color=rx.cond(
            active_step > index,
            styles.accent_text_color,
            rx.color("gray", 5),
        ),
        flex="1",
        height="1px",
        min_width="2rem",
        margin_top="1rem",
    )


def horizontal_stepper(
    steps: list[StepperStep],
    *,
    active_step: int = 0,
    container: rx.Component | None = None,
 ) -> rx.Component:
    """Render a configurable horizontal multi-step indicator.

    Args:
        steps: Ordered step definitions. The list length controls the number of steps.
        active_step: Zero-based index of the current step.
        container: Optional content to render below the stepper.
    """
    return rx.vstack(
        rx.hstack(
            *[
                rx.fragment(
                    _step_marker(step, index, active_step),
                    _step_connector(index, active_step)
                    if index < len(steps) - 1
                    else rx.fragment(),
                )
                for index, step in enumerate(steps)
            ],
            align="start",
            width="100%",
        ),
        container or rx.fragment(),
        spacing="2",
        width="100%",
    )
