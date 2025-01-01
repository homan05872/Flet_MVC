import flet as ft

def main(page: ft.Page):
    page.title = "Table with Fixed Header"

    # 固定ヘッダー部分
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("Column 1", weight="bold", expand=1),
                ft.Text("Column 2", weight="bold", expand=2),
                ft.Text("Column 3", weight="bold", expand=3),
                ft.Text("Column 4", weight="bold", expand=3),
            ],
            alignment="spaceBetween",
        ),
        bgcolor=ft.colors.GREY_300,  # 背景色を指定
        padding=10,      # ヘッダー部分の余白を設定
    )

    # データ部分
    rows = [
        ft.Container(
            content=ft.Row(
                [
                    ft.Text(f"Row {i+1}, Col 1", expand=1),
                    ft.Text(f"Row {i+1}, Col 2", expand=2),
                    ft.Text(f"Row {i+1}, Col 3", expand=3),
                    ft.Text(f"Row {i+1}, Col 4", expand=3),
                ],
                alignment="spaceBetween",
            ),
            padding=10,  # 各行の余白を設定
        )
        for i in range(50)  # 50行作成
    ]

    # スクロール可能なデータ部分
    scrollable_data = ft.ListView(
        controls=rows,
        expand=True,
    )

    # ページに追加
    page.add(
        ft.Column(
            [
                header,  # ヘッダー部分
                scrollable_data,  # スクロール可能なデータ部分
            ],
            expand=True,
        )
    )

ft.app(target=main)
