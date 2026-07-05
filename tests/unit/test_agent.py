"""CISO Copilot Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_assess_security_posture():
    """Test Assess overall security posture with maturity scoring."""
    tools = AgentTools()
    result = await tools.assess_security_posture(framework="test", scope="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_compliance():
    """Test Track security compliance status across frameworks."""
    tools = AgentTools()
    result = await tools.track_compliance(frameworks="test", include_gaps=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_assess_cyber_risk():
    """Test Assess cyber risk using quantitative risk methodology."""
    tools = AgentTools()
    result = await tools.assess_cyber_risk(risk_scenarios="test", methodology="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_monitor_security_metrics():
    """Test Monitor key security program metrics (MTTD, MTTR, incidents)."""
    tools = AgentTools()
    result = await tools.monitor_security_metrics(metrics="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ciso_copilot_agent_agent import CisoCopilotAgentAgent
    agent = CisoCopilotAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
