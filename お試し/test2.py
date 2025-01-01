import flet as ft

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

# ページ表示を更新する関数
def update_content(page, content_area):
    if page.route == "/profile":
        content_area.controls.clear()
        content_area.controls.append(profile_content())
    elif page.route == "/settings":
        content_area.controls.clear()
        content_area.controls.append(settings_content())
    else:  # デフォルトは "/home"
        content_area.controls.clear()
        content_area.controls.append(home_content())
    page.update()

# メインページの作成
def main(page: ft.Page):
    page.title = "Flet Sidebar with URL"
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.scroll = "auto"

    # メインコンテンツエリア
    content_area = ft.Column(expand=True)

    # サイドバーの内容
    sidebar = ft.Column(
        [
            ft.ElevatedButton("Home", on_click=lambda e: page.go("/home")),
            ft.ElevatedButton("Profile", on_click=lambda e: page.go("/profile")),
            ft.ElevatedButton("Settings", on_click=lambda e: page.go("/settings")),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    # 初期表示の設定
    update_content(page, content_area)

    # URLが変更されたときの処理
    def route_change(e):
        update_content(page, content_area)

    page.on_route_change = route_change

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

# Fletアプリケーションの起動
ft.app(target=main)
