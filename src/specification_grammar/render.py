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
        stroke_width=3,
        stroke_linecap="round",
        stroke_linejoin="round",
    )


def draw_doc(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.path(d=f"M {cx-28},{cy-44} H {cx+10} L {cx+28},{cy-25} V {cy+44} H {cx-28} Z"))
    g.add(dwg.path(d=f"M {cx+10},{cy-44} V {cy-25} H {cx+28}"))
    for yy in (-15, 0, 15):
        g.add(dwg.line((cx - 14, cy + yy), (cx + 14, cy + yy)))
    return g


def draw_target(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    for radius in (42, 24, 8):
        g.add(dwg.circle((cx, cy), r=radius))
    g.add(dwg.line((cx - 50, cy), (cx - 32, cy)))
    g.add(dwg.line((cx + 32, cy), (cx + 50, cy)))
    g.add(dwg.line((cx, cy - 50), (cx, cy - 32)))
    g.add(dwg.line((cx, cy + 32), (cx, cy + 50)))
    return g


def draw_cube(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    points = [
        (cx, cy - 48),
        (cx + 38, cy - 25),
        (cx + 38, cy + 25),
        (cx, cy + 48),
        (cx - 38, cy + 25),
        (cx - 38, cy - 25),
    ]
    g.add(dwg.polygon(points))
    g.add(dwg.line((cx, cy - 48), (cx, cy + 48)))
    g.add(dwg.line((cx - 38, cy - 25), (cx, cy)))
    g.add(dwg.line((cx + 38, cy - 25), (cx, cy)))
    return g


def draw_network(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    for dx, dy in ((0, -34), (-28, 28), (28, 28)):
        g.add(dwg.circle((cx + dx, cy + dy), r=16))
    g.add(dwg.line((cx, cy - 18), (cx - 20, cy + 14)))
    g.add(dwg.line((cx, cy - 18), (cx + 20, cy + 14)))
    g.add(dwg.line((cx - 12, cy + 28), (cx + 12, cy + 28)))
    return g


def draw_sliders(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    for yy, xx in zip((cy - 28, cy, cy + 28), (cx + 10, cx - 20, cx + 10)):
        g.add(dwg.line((cx - 42, yy), (cx + 42, yy)))
        g.add(dwg.circle((xx, yy), r=8, fill=PALETTE["background"]))
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
    g.add(dwg.line((cx, cy + 10), (cx + 24, cy - 17)))
    g.add(dwg.circle((cx, cy + 10), r=7, fill=PALETTE["background"]))
    return g


def draw_eye(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.path(d=f"M {cx-48},{cy} Q {cx},{cy-42} {cx+48},{cy} Q {cx},{cy+42} {cx-48},{cy} Z"))
    g.add(dwg.circle((cx, cy), r=16))
    return g


def draw_magnify(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.circle((cx - 8, cy - 8), r=31))
    g.add(dwg.line((cx + 14, cy + 14), (cx + 40, cy + 40)))
    return g


def draw_wave(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.circle((cx, cy), r=44))
    g.add(
        dwg.path(
            d=(
                f"M {cx-28},{cy+4} L {cx-18},{cy+4} "
                f"L {cx-12},{cy-18} L {cx-4},{cy+20} "
                f"L {cx+4},{cy-24} L {cx+12},{cy+10} "
                f"L {cx+18},{cy+2} L {cx+29},{cy+2}"
            )
        )
    )
    return g


def draw_check(dwg, cx, cy, color):
    g = icon_group(dwg, color)
    g.add(dwg.circle((cx, cy), r=44))
    g.add(dwg.path(d=f"M {cx-20},{cy} L {cx-5},{cy+16} L {cx+24},{cy-18}"))
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
