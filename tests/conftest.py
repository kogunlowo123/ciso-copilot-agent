"""Test configuration for CISO Copilot Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ciso-copilot-agent", "category": "Executive"}
