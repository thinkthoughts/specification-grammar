from pathlib import Path
import svgwrite

W,H=1536,1024
BG='#fbfbfa'; NAVY='#081d4f'; GREEN='#0b5c1e'; ORANGE='#d94b00'; PURPLE='#4a238f'; BLUE='#00508c'; TEXT='#0b1835'
ROWS=[
    dict(color=NAVY, label=('Leading','Specifications'), line1='Leading specifications', verb='specify', line2='engineering objects.', math='L → O', role=('Context and','Objective'), left='doc', right='target'),
    dict(color=GREEN, label=('Engineering','Objects'), line1='Engineering objects', verb='specify', line2='engineering variables.', math='O → V', role=('Structure and','Integration'), left='cube', right='network'),
    dict(color=ORANGE, label=('Engineering','Variables'), line1='Engineering variables', verb='specify', line2='observable states.', math='V → S', role=('Constraint and','Optimization'), left='sliders', right='gauge'),
    dict(color=PURPLE, label=('Observable','States'), line1='Observable states', verb='specify', line2='measured states.', math='S → M', role=('Measurement and','Validation'), left='eye', right='magnify'),
    dict(color=BLUE, label=('Measured','States'), line1='Measured states', verb='inform', line2='admissible generalizations.', math='M → G', role=('Learning and','Generalization'), left='wave', right='check'),
]

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'source'/'specification-grammar.svg'

def text(dwg, s, x,y, size, fill=TEXT, family='DejaVu Sans', weight='normal', anchor='start', style=None):
    kw=dict(insert=(x,y), font_size=size, fill=fill, font_family=family, font_weight=weight, text_anchor=anchor)
    if style:
        kw['style']=style
    return dwg.text(s, **kw)

def line_icon(dwg, kind, cx, cy, color):
    g=dwg.g(fill='none', stroke=color, stroke_width=3, stroke_linecap='round', stroke_linejoin='round')
    if kind=='doc':
        g.add(dwg.path(d=f'M {cx-28},{cy-44} H {cx+10} L {cx+28},{cy-25} V {cy+44} H {cx-28} Z'))
        g.add(dwg.path(d=f'M {cx+10},{cy-44} V {cy-25} H {cx+28}'))
        for yy in (-15,0,15): g.add(dwg.line((cx-14,cy+yy),(cx+14,cy+yy)))
    elif kind=='target':
        for r in (42,24,8): g.add(dwg.circle((cx,cy),r=r))
        g.add(dwg.line((cx-50,cy),(cx-32,cy))); g.add(dwg.line((cx+32,cy),(cx+50,cy)))
        g.add(dwg.line((cx,cy-50),(cx,cy-32))); g.add(dwg.line((cx,cy+32),(cx,cy+50)))
    elif kind=='cube':
        pts=[(cx,cy-48),(cx+38,cy-25),(cx+38,cy+25),(cx,cy+48),(cx-38,cy+25),(cx-38,cy-25)]
        g.add(dwg.polygon(pts)); g.add(dwg.line((cx,cy-48),(cx,cy+48))); g.add(dwg.line((cx-38,cy-25),(cx,cy))); g.add(dwg.line((cx+38,cy-25),(cx,cy)))
    elif kind=='network':
        for dx,dy in [(0,-34),(-28,28),(28,28)]: g.add(dwg.circle((cx+dx,cy+dy),r=16))
        g.add(dwg.line((cx,cy-18),(cx-20,cy+14))); g.add(dwg.line((cx,cy-18),(cx+20,cy+14))); g.add(dwg.line((cx-12,cy+28),(cx+12,cy+28)))
    elif kind=='sliders':
        ys=[cy-28,cy,cy+28]; xs=[cx+10,cx-20,cx+10]
        for yy,xx in zip(ys,xs):
            g.add(dwg.line((cx-42,yy),(cx+42,yy))); g.add(dwg.circle((xx,yy),r=8,fill=BG))
    elif kind=='gauge':
        g.add(dwg.path(d=f'M {cx-42},{cy+25} A 42,42 0 0 1 {cx+42},{cy+25}'))
        for a in [-60,-30,0,30,60]:
            import math
            r1,r2=32,42; th=math.radians(a-90)
            g.add(dwg.line((cx+r1*math.cos(th),cy+r1*math.sin(th)),(cx+r2*math.cos(th),cy+r2*math.sin(th))))
        g.add(dwg.line((cx,cy+10),(cx+24,cy-17))); g.add(dwg.circle((cx,cy+10),r=7,fill=BG))
    elif kind=='eye':
        g.add(dwg.path(d=f'M {cx-48},{cy} Q {cx},{cy-42} {cx+48},{cy} Q {cx},{cy+42} {cx-48},{cy} Z'))
        g.add(dwg.circle((cx,cy),r=16))
    elif kind=='magnify':
        g.add(dwg.circle((cx-8,cy-8),r=31)); g.add(dwg.line((cx+14,cy+14),(cx+40,cy+40)))
    elif kind=='wave':
        g.add(dwg.circle((cx,cy),r=44));
        g.add(dwg.path(d=f'M {cx-28},{cy+4} L {cx-18},{cy+4} L {cx-12},{cy-18} L {cx-4},{cy+20} L {cx+4},{cy-24} L {cx+12},{cy+10} L {cx+18},{cy+2} L {cx+29},{cy+2}'))
    elif kind=='check':
        g.add(dwg.circle((cx,cy),r=44)); g.add(dwg.path(d=f'M {cx-20},{cy} L {cx-5},{cy+16} L {cx+24},{cy-18}'))
    return g

def build():
    dwg=svgwrite.Drawing(str(OUT), size=(W,H), viewBox=f'0 0 {W} {H}')
    dwg.add(dwg.rect(insert=(0,0), size=(W,H), fill=BG))
    dwg.add(text(dwg,'Specification Grammar',W/2,82,74,NAVY,'DejaVu Serif','normal','middle'))
    top=126; row_h=164
    x_left_icon=104; x_label=272; x_stmt=480; x_math=900; x_role=1110; x_right_icon=1410
    for i,row in enumerate(ROWS):
        y0=top+i*row_h; cy=y0+76
        if i>0: dwg.add(dwg.line((38,y0-4),(1498,y0-4),stroke=row['color'],stroke_width=1.4,opacity=.78))
        dwg.add(line_icon(dwg,row['left'],x_left_icon,cy,row['color']))
        dwg.add(text(dwg,row['label'][0],x_label,cy-14,31,row['color'],'DejaVu Sans','bold','middle'))
        dwg.add(text(dwg,row['label'][1],x_label,cy+30,31,row['color'],'DejaVu Sans','bold','middle'))
        dwg.add(text(dwg,row['line1'],x_stmt,cy-28,25,TEXT))
        dwg.add(text(dwg,row['verb'],x_stmt,cy+5,25,row['color'],'DejaVu Sans','bold'))
        dwg.add(text(dwg,row['line2'],x_stmt,cy+38,25,TEXT))
        dwg.add(text(dwg,row['math'],x_math,cy+10,45,row['color'],'DejaVu Serif','normal','middle',style='font-style:italic'))
        dwg.add(text(dwg,row['role'][0],x_role,cy-10,29,row['color'],'DejaVu Sans','normal'))
        dwg.add(text(dwg,row['role'][1],x_role,cy+30,29,row['color'],'DejaVu Sans','normal'))
        dwg.add(line_icon(dwg,row['right'],x_right_icon,cy,row['color']))
    fy=960
    dwg.add(dwg.line((38,fy),(356,fy),stroke=NAVY,stroke_width=2))
    dwg.add(dwg.line((1180,fy),(1498,fy),stroke=NAVY,stroke_width=2))
    dwg.add(text(dwg,'Admissible generalizations trail leading specifications.',W/2,982,30,NAVY,'DejaVu Serif','normal','middle'))
    dwg.save(pretty=True)

if __name__=='__main__':
    build()
