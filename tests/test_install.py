import pathlib
import subprocess

import pytest


def test_install(  # noqa: D103
    tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)
    subprocess.check_call(["git", "init"])
    hook_path = tmp_path / ".git" / "hooks" / "pre-commit"
    assert not hook_path.exists() and not hook_path.is_symlink()
    subprocess.run(
        "install-black-isort-hook", check=True, stdin=subprocess.DEVNULL
    )
    assert hook_path.is_symlink()
    assert (
        "are you sure?"
        in subprocess.run(
            "install-black-isort-hook",
            capture_output=True,
            text=True,
            stdin=subprocess.DEVNULL,
        ).stderr
    )
    hook_path.unlink()
    assert (
        "` to `"
        in subprocess.run(
            "install-black-isort-hook",
            capture_output=True,
            text=True,
            stdin=subprocess.DEVNULL,
        ).stderr
    )
    subprocess.check_call(hook_path)
