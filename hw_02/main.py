from functools import reduce
from typing import List


def gen_latex_table(list: List[List[str]]) -> str:
    if len(list) == 0:
        raise Exception('List is empty')
    if min(map(lambda l: len(l), list)) == 0:
        raise Exception('Invalid list')
    if min(map(lambda l: len(l), list)) != max(map(lambda l: len(l), list)):
        raise Exception('Invalid list')

    def get_col_str():
        return reduce(
            lambda a, b: f'{a}|{b}',
            map(
                lambda _: "c",
                list[0]
            )
        )

    def get_table_content_str():
        return reduce(
            lambda row1, row2: row1 + row2,
            map(
                lambda row: f'{row} \\\\\n',
                map(
                    lambda row: reduce(
                        lambda el1, el2: f'{el1} & {el2}',
                        row
                    ),
                    list
                )
            )
        )

    return f'\\begin{{tabular}}{{{get_col_str()}}}\n' \
           f'\\hline\n' \
           f'{get_table_content_str()}' \
           f'\\hline\n' \
           f'\\end{{tabular}}\n'


def gen_latex_document(content: str) -> str:
    return f'\\documentclass{{article}}\n' \
           f'\\begin{{document}}\n' \
           f'{content}' \
           f'\\end{{document}}\n'


if __name__ == "__main__":
    with open("artifacts/table.tex", "w+") as tex_file:
        tex_file.write(
            gen_latex_document(
                gen_latex_table(
                    [["1", "2", "3"],
                     ["11", "22", "33"],
                     ["111", "222", "333"]]
                )
            )
        )
