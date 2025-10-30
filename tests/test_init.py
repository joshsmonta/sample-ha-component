"""Test component setup."""
from homeassistant.setup import async_setup_component

from custom_components.github_custom.const import DOMAIN


async def test_async_setup(hass):
    """Test the component gets setup."""
    assert await async_setup_component(hass, DOMAIN, {}) is True

async def test_flow_user_step_no_input(hass):
    """Test appropriate error when no input is provided."""
    _result = await hass.config_entries.flow.async_init(
        config_flow.DOMAIN, context={"source": "user"}
    )
    result = await hass.config_entries.flow.async_configure(
        _result["flow_id"], user_input={}
    )
    assert {"base": "missing"} == result["errors"]
