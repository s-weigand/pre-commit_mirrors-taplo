"""Render templates to update to new version."""
import os
from pathlib import Path

import httpx
from jinja2 import Template

HERE = Path(__file__).parent
REPO_ROOT = HERE.parent.parent


def get_latest_version() -> str:
    """Get latest stable version from ``crates.io``.

    Returns
    -------
    str
    """
    resp = httpx.get("https://crates.io/api/v1/crates/taplo-cli")
    return resp.json()["crate"]["max_stable_version"]


def render_templates(taplo_version: str) -> None:
    """Renders templates with new ``taplo_version`` if the value has changed.

    Parameters
    ----------
    taplo_version: str
    """
    version_file_path = REPO_ROOT / ".version"
    if version_file_path.is_file() is False:
        version_file_path.touch()
    current_version = version_file_path.read_text(encoding="utf8")
    if taplo_version != current_version:
        hook_template = Template(
            (HERE / ".pre-commit-hooks-template.yaml").read_text(encoding="utf8")
        )
        (REPO_ROOT / ".pre-commit-hooks.yaml").write_text(
            hook_template.render({"taplo_version": taplo_version}), encoding="utf8"
        )
        readme_template = Template(
            (HERE / "readme-template.md").read_text(encoding="utf8")
        )
        (REPO_ROOT / "README.md").write_text(
            readme_template.render({"taplo_version": taplo_version}), encoding="utf8"
        )
        version_file_path.write_text(taplo_version, encoding="utf8")
        gh_output = os.getenv("GITHUB_OUTPUT", None)
        if gh_output is not None:
            with Path(gh_output).open("a", encoding="utf8") as f:
                f.writelines(
                    [
                        f"taplo_version={taplo_version}\n",
                        f"current_version={current_version}\n",
                    ]
                )


if __name__ == "__main__":
    latest_version = get_latest_version()
    render_templates(latest_version)
