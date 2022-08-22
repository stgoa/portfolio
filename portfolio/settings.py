# -*- coding: utf-8 -*-
"""Project's settings."""
import logging
from enum import Enum
from enum import IntEnum
from pathlib import Path
from typing import Optional

from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic import SecretStr
from pydantic import confloat

# pylint: disable=no-name-in-module


def init_dotenv():
    """Find and load `.env`."""

    candidate = find_dotenv(usecwd=True)

    if not candidate:
        # raise IOError("No se encuentra el archivo `.env`.")
        return

    load_dotenv(candidate)


class Settings(BaseSettings):
    """Common project's settings."""

    PACKAGE_PATH: Path = Path(__file__).parent

    PROJECT_PATH: Path = PACKAGE_PATH.parent

    JSON_RESUME_PATH: Path = Path(PROJECT_PATH, "resume.json")

    JSON_LINKEDIN_PATH: Path =  Path(PROJECT_PATH, "Santiago_Armstrong.resume.json")

    GIT_REPO_PATH: Optional[Path] = None

    UPDATE_JSON_PATH : Optional[Path] = Path(PROJECT_PATH,"update.json")



    class Config:
        """Inner config for settings."""

        env_prefix = "PORTFOLIO_"
        use_enum_values = True


def init_project_settings():
    """Init settings."""
    init_dotenv()
    return Settings()