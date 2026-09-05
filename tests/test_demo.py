import os
import shutil
from pathlib import Path

import pytest
from pytest_django.live_server_helper import LiveServer
from website_downloader.crawler import CrawlOptions, crawl_site

# live_server forces transactional_db; serialized_rollback must be applied
# consistently across the whole session for any test using live_server, to
# avoid ContentType/data collisions with other live_server tests.
pytestmark = pytest.mark.django_db(serialized_rollback=True)


def test_build(live_server: LiveServer, tmp_path: Path) -> None:
    pages = tmp_path if os.getenv("TOX_ENV_NAME") else Path.cwd() / "pages"
    demo = pages / "demo"
    if demo.exists():
        shutil.rmtree(demo)
    demo.mkdir(parents=True, exist_ok=True)
    crawl_options = CrawlOptions(start_url=live_server.url, root=demo, max_pages=500)
    stats = crawl_site(crawl_options)
    assert stats.errors == 0
