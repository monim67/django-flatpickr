import shutil
from pathlib import Path

from pytest_django.live_server_helper import LiveServer
from pywebcopy import save_website


def test_build(live_server: LiveServer) -> None:
    pages = Path.cwd() / "pages"
    if pages.exists():
        shutil.rmtree(pages)
    save_website(
        url=live_server.url,
        project_folder=str(pages.parent),
        project_name=pages.name,
        bypass_robots=True,
    )
    pages.joinpath("localhost").replace(pages / "demo")
    url_replacements = [
        (
            "../github.com/monim67/django-flatpickr",
            "https://github.com/monim67/django-flatpickr",
        ),
        (
            "../bulma.io/957351442",
            "https://bulma.io/",
        ),
        (
            "/static/django_flatpickr/",
            "/django-flatpickr/demo/static/django_flatpickr/",
        ),
    ]
    mjs_file = pages / "demo/static/django_flatpickr/js/django-flatpickr.mjs"
    if mjs_file.exists():
        mjs_file.rename(mjs_file.with_suffix(".js"))
    for file in pages.glob("demo/*.html"):
        file_text = file.read_text()
        for search_text, replace_text in url_replacements:
            file_text = file_text.replace(search_text, replace_text)
        file.write_text(file_text)
