import flet as ft

# メインコンテンツの更新関数
def update_main_content(content_area, content):
    content_area.controls.clear()  # 現在のコンテンツをクリア
    content_area.controls.append(content)  # 新しいコンテンツを追加
    content_area.update()

# サイドバーの内容
def create_sidebar(content_area):
    sidebar = ft.Column(
        [
            ft.ElevatedButton("Home", on_click=lambda e: update_main_content(content_area, home_content())),
            ft.ElevatedButton("Profile", on_click=lambda e: update_main_content(content_area, profile_content())),
            ft.ElevatedButton("Settings", on_click=lambda e: update_main_content(content_area, settings_content())),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )
    return sidebar

# 各ページのコンテンツ
def home_content():
    return ft.Column(
        [
            ft.Text("Home Page"),
            ft.Text("This is the home page content."),
        ],
        spacing=20,
    )

def profile_content():
    return ft.Column(
        [
            ft.Text("Profile Page"),
            ft.Text("This is the profile page content."),
        ],
        spacing=20,
    )

def settings_content():
    return ft.Column(
        [
            ft.Text("Settings Page"),
            ft.Text("This is the settings page content."),
        ],
        spacing=20,
    )

# メインページの作成
def main(page: ft.Page):
    page.title = "Flet Sidebar Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = "auto"

    # メインコンテンツエリア
    content_area = ft.Column(expand=True)

    # サイドバーを作成
    sidebar = create_sidebar(content_area)

    # 初期のメインコンテンツを表示
    content_area.controls.append(home_content())

    # 全体レイアウト
    page.add(
        ft.Row(
            [
                ft.Container(sidebar, width=200, height=page.height, bgcolor=ft.Colors.BLUE_100),  # サイドバー
                content_area  # メインコンテンツエリア
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )
    )

    page.update()

# Fletアプリケーションの起動
ft.app(target=main)
