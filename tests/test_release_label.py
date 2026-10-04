"""Verify the custom release label on our own OpenCart deployments."""

import pytest
from playwright.sync_api import expect


@pytest.mark.deployment
def test_release_label(page):
    """Check that our deployed release label is visible and correct."""
    release_label = page.locator("#deployment-release")

    expect(release_label).to_be_visible()
    expect(release_label).to_have_text(
        "Release v1.1 - Jenkins deployment practice"
    )