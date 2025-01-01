import flet as ft

def main(page: ft.Page):
    page.title = "Scrollable Table Example"
    page.scroll = "adaptive"  # ページのスクロールを許可

    # テーブルのデータを作成
    rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"Row {i+1}, Col 1")),
                ft.DataCell(ft.Text(f"Row {i+1}, Col 2")),
                ft.DataCell(ft.Text(f"Row {i+1}, Col 3")),
            ]
        )
        for i in range(50)  # 50行作成
    ]

    # DataTable を作成
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Column 1")),
            ft.DataColumn(ft.Text("Column 2")),
            ft.DataColumn(ft.Text("Column 3")),
        ],
        rows=rows,
    )

    # テーブルをスクロール可能なコンテナ内に配置
    scrollable_container = ft.Container(
        content=table,
        expand=True,  # 利用可能な領域を占有
        padding=10,
    )

    # 全体の Column に追加
    page.add(
        ft.Column(
            [
                ft.Text("Scrollable Table", size=24, weight="bold"),
                scrollable_container,
            ],
            scroll="auto",  # Column のスクロールを許可
            expand=True,
        )
    )

ft.app(target=main)
