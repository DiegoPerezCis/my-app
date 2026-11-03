
"""Configuración de ImpulsaIA para development y production."""

from __future__ import annotations

import os
from typing import Any

import streamlit as st


DEFAULT_MODEL = "gemini-3.8-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"

VALID_ENVIRONMENTS = {"development", "production"}


def _read_secret(key: str, default: Any = None) -> Any:
    """Lee un secreto de Streamlit sin interrumpir la ejecución."""
    try:
        return st.secrets.get(key, default)
    except Exception:
        return default


def get_settings() -> dict[str, str]:
    """Devuelve la configuración del ambiente activo."""

    environment = (
        os.getenv("APP_ENV")
        or _read_secret("APP_ENV", "development")
    ).strip().lower()

    if environment not in VALID_ENVIRONMENTS:
        raise ValueError(
            "APP_ENV debe ser 'development' o 'production'."
        )

    environment_secrets = _read_secret(environment, {})

    if not hasattr(environment_secrets, "get"):
        environment_secrets = {}

    api_key = (
        os.getenv(f"GEMINI_API_KEY_{environment.upper()}")
        or environment_secrets.get("GEMINI_API_KEY")
        or ""
    )

    model = (
        os.getenv(f"GEMINI_MODEL_{environment.upper()}")
        or environment_secrets.get("GEMINI_MODEL")
        or os.getenv("GEMINI_MODEL")
        or _read_secret("GEMINI_MODEL", DEFAULT_MODEL)
    )

    return {
        "environment": environment,
        "gemini_api_key": str(api_key).strip(),
        "gemini_model": str(model).strip() or DEFAULT_MODEL,
        "gemini_fallback_model": FALLBACK_MODEL,
    }


def create_gemini_client():
    """Crea el cliente Gemini o genera un error claro si falta la clave."""

    from google import genai

    settings = get_settings()

    if not settings["gemini_api_key"]:
        raise RuntimeError(
            "No se encontró la clave de Gemini para el ambiente "
            f"'{settings['environment']}'. Configúrala en Streamlit Secrets."
        )

    return genai.Client(
        api_key=settings["gemini_api_key"]
    )
