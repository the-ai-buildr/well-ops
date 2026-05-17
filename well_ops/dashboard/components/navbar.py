"""Navbar component for the app."""

import reflex as rx

from .. import styles
from .navigation import nav_sections


def navbar_footer() -> rx.Component:
    """Navbar footer.

    Returns:
        The navbar footer component.

    """
    return rx.hstack(
        rx.link(
            rx.text("Docs", size="3"),
            href="#",
            color_scheme="gray",
            underline="none",
        ),
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.8", "scale": "0.9"}),
        justify="start",
        align="center",
        width="100%",
        padding="0.5em",
    )


def menu_button() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon("align-justify"),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.heading("Well-Ops", size="5", weight="bold"),
                        rx.spacer(),
                        rx.drawer.close(rx.icon(tag="x")),
                        justify="end",
                        align="center",
                        width="100%",
                        padding="0.25em",
                    ),
                    rx.divider(),
                    rx.vstack(
                        *nav_sections(
                            child_padding_left="0.85em",
                            icon_size=20,
                            padding_left="0.85em",
                            text_size="4",
                        ),
                        spacing="1",
                        width="100%",
                        padding_top="0.5em",
                    ),
                    rx.spacer(),
                    navbar_footer(),
                    spacing="1",
                    width="100%",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="1em",
                bg=rx.color("gray", 1),
            ),
            width="100%",
        ),
        direction="left",
    )


def navbar() -> rx.Component:
    """The navbar.

    Returns:
        The navbar component.

    """
    return rx.el.nav(
        rx.hstack(
            menu_button(),
            rx.spacer(),
            align="center",
            width="100%",
            height="42px",
            padding_x=["1em", "1em", "1em"],
        ),
        display=["block", "block", "block", "block", "block", "none"],
        position="sticky",
        background_color=rx.color("gray", 1),
        top="0px",
        z_index="5",
        border_bottom=styles.border,
    )
