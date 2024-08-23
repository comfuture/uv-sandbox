import os
import sys
import pytest
from typing import Iterable
from fastapi import FastAPI
from fastapi.testclient import TestClient

from uv_sandbox import create_app

project_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_path)


@pytest.fixture(scope="session")
def fastapi_app() -> Iterable[FastAPI]:  # pylint: disable=unused-argument
    """yields fastapi app instance"""
    app = create_app()
    yield app


@pytest.fixture(scope="session")
def client(fastapi_app: FastAPI) -> Iterable[TestClient]:
    """yields fastapi test_client for an app"""
    with TestClient(fastapi_app) as client:
        yield client
