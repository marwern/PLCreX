from lark import Lark, tree
from pathlib import Path

def translation(
        src: Path,
        txt: bool = False,
        dot: bool = False):
    with open(r'.\data\STgrammar.lark', 'rt') as file:
        grammar = file.read()
    parser = Lark(grammar, maybe_placeholders=False, keep_all_tokens=False)

    with open(src, 'rt') as file:
        source = file.read()

        # write (pretty) tree as .txt
        if txt:
            txt_export = open(fr'.\exports\tree\txt\{Path(src).name}.txt', "w")
            txt_export.write(str(parser.parse(source).pretty()))

        # write tree as .dot file
        if dot:
            tree.pydot__tree_to_dot(parser.parse(source), fr'.\exports\tree\dot\{Path(src).name}.dot')
        return