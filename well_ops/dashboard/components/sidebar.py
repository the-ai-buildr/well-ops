"""Sidebar component for the app."""

import reflex as rx

from .. import styles
from .navigation import nav_sections


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.

    """
    return rx.hstack(
        rx.color_mode_cond(
            rx.image(src="assets/reflex_black.svg", height="1.5em"),
            rx.image(src="assets/reflex_white.svg", height="1.5em"),
        ),
        rx.spacer(),
        align="center",
        width="100%",
        padding="2em",
        margin="2em",
    )


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.

    """
    return rx.hstack(
        rx.link(
            rx.text("Docs", size="3"),
            href="#",
            color_scheme="gray",
            underline="none",
        ),
        rx.link(
            rx.text("Blog", size="3"),
            href="#",
            color_scheme="gray",
            underline="none",
        ),
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.9", "scale": "0.95"}),
        justify="start",
        align="center",
        width="100%",
        padding="2em",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    return rx.flex(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *nav_sections(
                    child_padding_left="2em",
                    icon_size=18,
                    padding_left="0.75em",
                    text_size="3",
                ),
                spacing="0",
                width="100%",
            ),
            rx.spacer(),
            sidebar_footer(),
            justify="end",
            align="end",
            width=styles.sidebar_content_width,
            height="100dvh",
            padding="2em",
        ),
        display=["none", "none", "none", "none", "none", "flex"],
        max_width=styles.sidebar_width,
        width=styles.sidebar_width,
        height="100%",
        position="sticky",
        justify="end",
        top="0px",
        left="0px",
        flex="1",
        bg=rx.color("blue", 2),
    )
