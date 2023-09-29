import os
import pathlib
import subprocess


def test_install(tmp_path: pathlib.Path) -> None:
    start_dir = os.getcwd()
    try:
        os.chdir(tmp_path)
        subprocess.run(["git", "init"], check=True, capture_output=True)
        hook_path = tmp_path / ".git" / "hooks" / "pre-commit"
        assert not hook_path.exists()
        subprocess.run(
            ["install-black-isort-hook"], check=True, capture_output=True
        )
        assert hook_path.exists()
        subprocess.run([hook_path], check=True, capture_output=True)
    finally:
        os.chdir(start_dir)
