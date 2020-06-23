import re
import sys
from pathlib import Path

RE_DESTINATION = re.compile(r"(?:CREATE TABLE|INSERT INTO|CREATE OR REPLACE TABLE)[\s \n]+`(.+?)`")
RE_ORIGIN = re.compile(r"(?:FROM|JOIN)[\s \n]+`(.+?)`")

PLANTUML_TEMPLATE = """skinparam padding 10 /'paddingの調整'/
left to right direction /'左から右に伸ばして行く'/
hide members /'diagramを左から右に伸ばして行く'/
hide circle /'classマークを消す'/
{}
"""


def make_table_dependencies_for_plantuml(sql):
    # 作成テーブルを取得
    if len(RE_DESTINATION.findall(sql)) != 1:
        raise Exception("CREATE TABLE|CREATE OR REPLACE TABLE|INSERT INTO句が存在しません。")
    else:
        destination_table = RE_DESTINATION.findall(sql)[0]

    # 自己参照を除いた参照元テーブルを取得
    origin_tables = [table for table in RE_ORIGIN.findall(sql) if table != destination_table]
    if len(origin_tables) == 0:
        raise Exception("依存関係が存在しません")
    return [f'"{table}" <|-- "{destination_table}"' for table in origin_tables]


def generate_plantuml(sql_directory):
    print("```{plantuml}")
    print("@startuml")
    for name in sorted(Path(sql_directory).glob("*.sql")):
        print(
            PLANTUML_TEMPLATE.format(
                "\n".join(make_table_dependencies_for_plantuml(open(name).read()))
            )
        )
    print("@enduml")
    print("```")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    generate_plantuml(path)
