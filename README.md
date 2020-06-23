# draw_bqsql_table_dependencies
bqのテーブルの依存関係を描くやつ


$ python3 draw.py sample

出力結果

```{plantuml}
@startuml
skinparam padding 10 /'paddingの調整'/
left to right direction /'左から右に伸ばして行く'/
hide members /'diagramを左から右に伸ばして行く'/
hide circle /'classマークを消す'/
"project.dataset.table1" <|-- "project.dataset.table5"

@enduml
```
