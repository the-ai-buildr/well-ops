"""Shared navigation helpers for desktop and mobile menus."""

import reflex as rx

from .. import styles

ROUTE_ORDER = [
    "/",
    "/tools/index",
    "/tools/stamp",
    "/table",
    "/about",
    "/settings/profile",
    "/settings/settings",
]

GROUP_ICONS = {
    "apps": "app-window",
    "settings": "settings",
    "tools": "wrench",
}

ROUTE_ICONS = {
    "/": "home",
    "/about": "book-open",
    "/settings/profile": "user",
    "/settings/settings": "settings",
    "/table": "table-2",
    "/tools/index": "wrench",
    "/tools/stamp": "stamp",
}


def _normalize_route(route: str | None) -> str:
    route = route or "/"
    return route if route.startswith("/") else f"/{route}"


def _title_from_route(route: str) -> str:
    if route == "/":
        return "Overview"
    return route.strip("/").split("/")[-1].replace("-", " ").title()


def _group_title(group: str) -> str:
    return group.replace("-", " ").title()


def _row_style(active) -> dict:
    return {
        "_hover": {
            "background_color": rx.cond(
                active,
                styles.accent_bg_color,
                styles.gray_bg_color,
            ),
            "color": rx.cond(active, styles.accent_text_color, styles.text_color),
            "opacity": "1",
        },
        "opacity": rx.cond(active, "1", "0.9"),
    }


def get_nav_sections() -> list[dict]:
    from reflex.page import DECORATED_PAGES

    route_order = {route: index for index, route in enumerate(ROUTE_ORDER)}
    pages = [
        page_dict
        for page_list in DECORATED_PAGES.values()
        for _, page_dict in page_list
    ]
    ordered_pages = sorted(
        pages,
        key=lambda page: route_order.get(
            _normalize_route(page["route"]),
            len(route_order),
        ),
    )

    sections = []
    groups = {}
    for page in ordered_pages:
        route = _normalize_route(page["route"])
        entry = {
            "icon": ROUTE_ICONS.get(route, "layout-dashboard"),
            "route": route,
            "title": page.get("title", _title_from_route(route)),
        }
        route_parts = route.strip("/").split("/")

        if route == "/" or len(route_parts) == 1:
            sections.append({"kind": "item", "entry": entry})
            continue

        group_key = route_parts[0]
        group = groups.get(group_key)
        if group is None:
            group = {
                "icon": GROUP_ICONS.get(group_key, "folder"),
                "items": [],
                "key": group_key,
                "kind": "group",
                "title": _group_title(group_key),
            }
            groups[group_key] = group
            sections.append(group)

        if route_parts[-1] == "index":
            group["entry"] = entry
            group["icon"] = entry["icon"]
            group["title"] = entry["title"]
            continue

        group["items"].append(entry)

    return [
        {"kind": "item", "entry": section["entry"]}
        if section["kind"] == "group" and not section["items"] and "entry" in section
        else section
        for section in sections
    ]


def nav_link(
    entry: dict,
    *,
    icon_size: int,
    padding_left: str,
    text_size: str,
 ) -> rx.Component:
    active = rx.State.router.page.path == entry["route"]

    return rx.link(
        rx.hstack(
            rx.icon(entry["icon"], size=icon_size),
            rx.text(entry["title"], size=text_size, weight="regular"),
            color=rx.cond(active, styles.accent_text_color, styles.text_color),
            style=_row_style(active),
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            spacing="2",
            padding="0.6em",
            padding_left=padding_left,
        ),
        underline="none",
        href=entry["route"],
        width="100%",
    )


def nav_group(
    section: dict,
    *,
    child_padding_left: str,
    icon_size: int,
    padding_left: str,
    text_size: str,
) -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            header=rx.hstack(
                rx.icon(section["icon"], size=icon_size),
                rx.text(section["title"], size=text_size, weight="medium"),
                align="center",
                border_radius=styles.border_radius,
                color=styles.gray_color,
                padding="0.6em",
                padding_left=padding_left,
                spacing="2",
                style={"opacity": "0.9"},
                width="100%",
            ),
            content=rx.vstack(
                *[
                    nav_link(
                        item,
                        icon_size=icon_size,
                        padding_left=child_padding_left,
                        text_size=text_size,
                    )
                    for item in section["items"]
                ],
                border_left=styles.border,
                spacing="0",
                width="100%",
            ),
            padding="0",
            value=section["key"],
        ),
        collapsible=True,
        padding="0",
        style={
            ".AccordionItem": {
                "border_top": "0",
                "border_bottom": "0",
                "margin_top": "0",
            },
            ".AccordionTrigger": {
                "box_shadow": "none",
                "color": styles.gray_color,
                "font_size": "inherit",
                "line_height": "inherit",
                "outline": "none",
                "padding": "0",
                "_hover": {"background_color": styles.gray_bg_color},
            },
            ".AccordionChevron": {"color": styles.gray_color},
        },
        type="single",
        variant="ghost",
        width="100%",
    )


def nav_sections(
    *,
    child_padding_left: str,
    icon_size: int,
    padding_left: str,
    text_size: str,
) -> list[rx.Component]:
    return [
        nav_link(
            section["entry"],
            icon_size=icon_size,
            padding_left=padding_left,
            text_size=text_size,
        )
        if section["kind"] == "item"
        else nav_group(
            section,
            child_padding_left=child_padding_left,
            icon_size=icon_size,
            padding_left=padding_left,
            text_size=text_size,
        )
        for section in get_nav_sections()
    ]
