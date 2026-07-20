from pathlib import Path
import cairosvg

ROOT=Path(__file__).resolve().parents[1]
svg=ROOT/'source'/'specification-grammar.svg'
out=ROOT/'exports'; out.mkdir(exist_ok=True)

cairosvg.svg2pdf(url=str(svg), write_to=str(out/'specification-grammar.pdf'))
for width in (1600,2400,3200):
    cairosvg.svg2png(url=str(svg), write_to=str(out/f'specification-grammar-{width}.png'), output_width=width)
print('Exported PDF and PNG assets.')
