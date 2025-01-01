import flet as ft

def main(page: ft.Page):

    t = ft.Text(value="Program", color="blue")

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "キャンセルされました。"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    
    def get_directry_result(e: ft.FilePickerResultEvent):
        selected_directry.value = e.path if e.path else "キャンセルされました。"
        print(e.path)
        selected_directry.update()
    
    get_directry_dialog = ft.FilePicker(on_result=get_directry_result)
    selected_directry = ft.Text()


    page.overlay.extend([pick_files_dialog,get_directry_dialog])

    page.add(
        ft.Row(
            [t]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "ファイルを開く",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    "保存フォルダを指定",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: get_directry_dialog.get_directory_path(
                    ),
                    disabled=page.web
                ),
                selected_directry,
            ]
        )
    )

ft.app(target=main)
