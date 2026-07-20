from pathlib import Path
import math

import svgwrite


W, H = 1536, 1024

PALETTE = {
    "background": "#fbfbfa",
    "navy": "#081d4f",
    "green": "#0b5c1e",
    "orange": "#d94b00",
    "purple": "#4a238f",
    "blue": "#00508c",
    "text": "#0b1835",
}

TYPE = {
    "title": 74,
    "label": 31,
    "statement": 25,
    "math": 45,
    "role": 29,
    "footer": 30,
}

LAYOUT = {
    "top": 126,
    "row_height": 164,
    "left_icon": 104,
    "label": 272,
    "statement": 480,
    "math": 900,
    "role": 1110,
    "right_icon": 1410,
    "separator_left": 38,
    "separator_right": 1498,
    "footer_y": 960,
}

ICON = {
    "box": 96,
    "stroke": 3.2,
    "radius": 42,
    "small_radius": 8,
}

ROWS = [
    {
        "color": PALETTE["navy"],
        "title": ("Leading", "Specifications"),
        "line1": "Leading specifications",
        "verb": "specify",
        "line2": "engineering objects.",
        "math": "L → O",
        "role": ("Context and", "Objective"),
        "left_icon": "doc",
        "right_icon": "target",
    },
    {
        "color": PALETTE["green"],
        "title": ("Engineering", "Objects"),
        "line1": "Engineering objects",
        "verb": "specify",
        "line2": "engineering variables.",
        "math": "O → V",
        "role": ("Structure and", "Integration"),
        "left_icon": "cube",
        "right_icon": "network",
    },
    {
        "color": PALETTE["orange"],
        "title": ("Engineering", "Variables"),
        "line1": "Engineering variables",
        "verb": "specify",
        "line2": "observable states.",
        "math": "V → S",
        "role": ("Constraint and", "Optimization"),
        "left_icon": "sliders",
        "right_icon": "gauge",
    },
    {
        "color": PALETTE["purple"],
        "title": ("Observable", "States"),
        "line1": "Observable states",
        "verb": "specify",
        "line2": "measured states.",
        "math": "S → M",
        "role": ("Measurement and", "Validation"),
        "left_icon": "eye",
        "right_icon": "magnify",
    },
    {
        "color": PALETTE["blue"],
        "title": ("Measured", "States"),
        "line1": "Measured states",
        "verb": "inform",
        "line2": "admissible generalizations.",
        "math": "M → G",
        "role": ("Learning and", "Generalization"),
        "left_icon": "wave",
        "right_icon": "check",
    },
]

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "source" / "specification-grammar.svg"


def add_text(
    dwg,
    value,
    x,
    y,
    size,
    *,
    fill=None,
    family="DejaVu Sans",
    weight="normal",
    anchor="start",
    style=None,
):
    kwargs = {
        "insert": (x, y),
        "font_size": size,
        "fill": fill or PALETTE["text"],
        "font_family": family,
        "font_weight": weight,
        "text_anchor": anchor,
    }
    if style:
        kwargs["style"] = style
    return dwg.text(value, **kwargs)


def icon_group(dwg, color):
    return dwg.g(
        fill="none",
        stroke=color,
        stroke_width=ICON["stroke"],
        stroke_linecap="round",
        stroke_linejoin="round",
    )


def draw_doc(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.path(d=f"M {cx-28},{cy-43} H {cx+9} L {cx+28},{cy-24} V {cy+43} H {cx-28} Z"))
    g.add(dwg.path(d=f"M {cx+9},{cy-43} V {cy-24} H {cx+28}"))
    for yy in (-15, 0, 15):
        g.add(dwg.line((cx - 14, cy + yy), (cx + 14, cy + yy)))
    return g


def draw_target(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    for radius in (42, 24, 8):
        g.add(dwg.circle((cx, cy), r=radius))
    for x1, y1, x2, y2 in (
        (cx - 50, cy, cx - 32, cy),
        (cx + 32, cy, cx + 50, cy),
        (cx, cy - 50, cx, cy - 32),
        (cx, cy + 32, cx, cy + 50),
    ):
        g.add(dwg.line((x1, y1), (x2, y2)))
    return g


def draw_cube(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    top = (cx, cy - 42)
    upper_left = (cx - 36, cy - 21)
    upper_right = (cx + 36, cy - 21)
    bottom_left = (cx - 36, cy + 23)
    bottom_right = (cx + 36, cy + 23)
    bottom = (cx, cy + 44)
    g.add(dwg.polygon([top, upper_right, bottom_right, bottom, bottom_left, upper_left]))
    g.add(dwg.line(top, (cx, cy)))
    g.add(dwg.line(upper_left, (cx, cy)))
    g.add(dwg.line(upper_right, (cx, cy)))
    g.add(dwg.line((cx, cy), bottom))
    return g


def draw_network(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    nodes = ((cx, cy - 34), (cx - 30, cy + 26), (cx + 30, cy + 26))
    g.add(dwg.line(nodes[0], nodes[1]))
    g.add(dwg.line(nodes[0], nodes[2]))
    g.add(dwg.line(nodes[1], nodes[2]))
    for node in nodes:
        g.add(dwg.circle(node, r=14, fill=PALETTE["background"]))
    return g


def draw_sliders(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    rows = ((cy - 27, cx + 14), (cy, cx - 18), (cy + 27, cx + 8))
    for yy, knob_x in rows:
        g.add(dwg.line((cx - 42, yy), (cx + 42, yy)))
        g.add(dwg.circle((knob_x, yy), r=8, fill=PALETTE["background"]))
    return g


def draw_gauge(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.path(d=f"M {cx-42},{cy+25} A 42,42 0 0 1 {cx+42},{cy+25}"))
    for angle in (-60, -30, 0, 30, 60):
        theta = math.radians(angle - 90)
        g.add(
            dwg.line(
                (cx + 32 * math.cos(theta), cy + 32 * math.sin(theta)),
                (cx + 42 * math.cos(theta), cy + 42 * math.sin(theta)),
            )
        )
    g.add(dwg.line((cx, cy + 12), (cx + 23, cy - 14)))
    g.add(dwg.circle((cx, cy + 12), r=7, fill=PALETTE["background"]))
    return g


def draw_eye(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.path(d=f"M {cx-46},{cy} Q {cx},{cy-38} {cx+46},{cy} Q {cx},{cy+38} {cx-46},{cy} Z"))
    g.add(dwg.circle((cx, cy), r=15))
    return g


def draw_magnify(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.circle((cx - 9, cy - 9), r=30))
    g.add(dwg.line((cx + 13, cy + 13), (cx + 39, cy + 39)))
    return g


def draw_wave(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.circle((cx, cy), r=42))
    g.add(
        dwg.path(
            d=(
                f"M {cx-28},{cy+3} "
                f"L {cx-18},{cy+3} "
                f"L {cx-12},{cy-16} "
                f"L {cx-4},{cy+18} "
                f"L {cx+4},{cy-22} "
                f"L {cx+12},{cy+10} "
                f"L {cx+18},{cy+2} "
                f"L {cx+28},{cy+2}"
            )
        )
    )
    return g


def draw_check(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.circle((cx, cy), r=42))
    g.add(dwg.path(d=f"M {cx-20},{cy} L {cx-5},{cy+15} L {cx+23},{cy-18}"))
    return g


ICON_DRAWERS = {
    "doc": draw_doc,
    "target": draw_target,
    "cube": draw_cube,
    "network": draw_network,
    "sliders": draw_sliders,
    "gauge": draw_gauge,
    "eye": draw_eye,
    "magnify": draw_magnify,
    "wave": draw_wave,
    "check": draw_check,
}


def draw_icon(dwg, name, cx, cy, color):
    try:
        return ICON_DRAWERS[name](dwg, cx, cy, color)
    except KeyError as exc:
        raise ValueError(f"Unknown icon: {name}") from exc


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    dwg = svgwrite.Drawing(str(OUT), size=(W, H), viewBox=f"0 0 {W} {H}")
    dwg.add(dwg.rect(insert=(0, 0), size=(W, H), fill=PALETTE["background"]))

    dwg.add(
        add_text(
            dwg,
            "Specification Grammar",
            W / 2,
            82,
            TYPE["title"],
            fill=PALETTE["navy"],
            family="DejaVu Serif",
            anchor="middle",
        )
    )

    for index, row in enumerate(ROWS):
        y0 = LAYOUT["top"] + index * LAYOUT["row_height"]
        cy = y0 + 76

        if index > 0:
            dwg.add(
                dwg.line(
                    (LAYOUT["separator_left"], y0 - 4),
                    (LAYOUT["separator_right"], y0 - 4),
                    stroke=row["color"],
                    stroke_width=1.4,
                    opacity=0.78,
                )
            )

        dwg.add(draw_icon(dwg, row["left_icon"], LAYOUT["left_icon"], cy, row["color"]))

        dwg.add(add_text(dwg, row["title"][0], LAYOUT["label"], cy - 14, TYPE["label"],
                         fill=row["color"], weight="bold", anchor="middle"))
        dwg.add(add_text(dwg, row["title"][1], LAYOUT["label"], cy + 30, TYPE["label"],
                         fill=row["color"], weight="bold", anchor="middle"))

        dwg.add(add_text(dwg, row["line1"], LAYOUT["statement"], cy - 28, TYPE["statement"]))
        dwg.add(add_text(dwg, row["verb"], LAYOUT["statement"], cy + 5, TYPE["statement"],
                         fill=row["color"], weight="bold"))
        dwg.add(add_text(dwg, row["line2"], LAYOUT["statement"], cy + 38, TYPE["statement"]))

        dwg.add(add_text(dwg, row["math"], LAYOUT["math"], cy + 10, TYPE["math"],
                         fill=row["color"], family="DejaVu Serif", anchor="middle",
                         style="font-style:italic"))

        dwg.add(add_text(dwg, row["role"][0], LAYOUT["role"], cy - 10, TYPE["role"],
                         fill=row["color"]))
        dwg.add(add_text(dwg, row["role"][1], LAYOUT["role"], cy + 30, TYPE["role"],
                         fill=row["color"]))

        dwg.add(draw_icon(dwg, row["right_icon"], LAYOUT["right_icon"], cy, row["color"]))

    footer_y = LAYOUT["footer_y"]
    dwg.add(dwg.line((LAYOUT["separator_left"], footer_y), (356, footer_y),
                     stroke=PALETTE["navy"], stroke_width=2))
    dwg.add(dwg.line((1180, footer_y), (LAYOUT["separator_right"], footer_y),
                     stroke=PALETTE["navy"], stroke_width=2))
    dwg.add(
        add_text(
            dwg,
            "Admissible generalizations trail leading specifications.",
            W / 2,
            982,
            TYPE["footer"],
            fill=PALETTE["navy"],
            family="DejaVu Serif",
            anchor="middle",
        )
    )

    dwg.save(pretty=True)


if __name__ == "__main__":
    build()
