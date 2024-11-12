import flet as ft

from src.anonymous_msg_bot import do_magic
from threading import Thread
import time


link = ft.TextField(label="Victim link")


def on_get_response(msg):
    console._set_attr("value", console.value + "\n" + str(msg))
    console.update()


def on_launch(e):
    l = link.value
    do_magic(l, on_get_response)


theme = ft.Theme(
    color_scheme_seed="red",
    color_scheme="light",
    use_material3=True,
)

bot_description = ft.TextField(
    label="Bot description",
    max_lines=3,
    min_lines=3,
)
launch_btn = ft.ElevatedButton("Launch", on_click=on_launch)

console = ft.TextField(
    on_change=lambda e: print(e.control.value),
    max_lines=10,
    min_lines=10,
)


def main(page: ft.Page):
    page.title = "nglinkspammer"

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 50

    page.add(
        ft.Column(
            controls=[
                ft.Text("nglinkspammer", size=50),
                link,
                bot_description,
                launch_btn,
                ft.Divider(),
                console,
            ],
        ),
    )

    page.update()


ft.app(main)
