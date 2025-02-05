# stdlib
import random

# 3rd party
import pytest
from bs4 import BeautifulSoup
from domdf_python_tools.paths import PathPlus
from pytest_regressions.file_regression import FileRegressionFixture
from sphinx.application import Sphinx


def test_build_example(app: Sphinx):
	app.build()
	app.build()


@pytest.mark.sphinx("html", srcdir="test-root")
@pytest.mark.parametrize("page", ["_debug/index.html"], indirect=True)
def test_html_output(page: BeautifulSoup, file_regression: FileRegressionFixture):
	pass


@pytest.mark.sphinx("latex", srcdir="test-root")
def test_latex_output(app: Sphinx):
	random.seed("5678")

	assert app.builder.name.lower() == "latex"
	app.build()

	assert not PathPlus(app.outdir / "_debug" / "index.html").is_file()  # type: ignore[operator]
	assert not PathPlus(app.outdir / "_debug").is_dir()  # type: ignore[operator]
