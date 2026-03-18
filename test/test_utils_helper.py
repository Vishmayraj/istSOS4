import sys
import os
import pytest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
API_DIR = os.path.join(PROJECT_ROOT, 'api')

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, API_DIR)

from api.app.utils.utils import reject_computed_fields

class TestRejectComputedFields:
    """reject_computed_fields raises when payload contains read-only computed keys."""

    def test_observedArea_raises(self):
        with pytest.raises(Exception, match="observedArea"):
            reject_computed_fields({"observedArea": "some value"}, ["observedArea", "phenomenonTime"])

    def test_phenomenonTime_raises(self):
        with pytest.raises(Exception, match="phenomenonTime"):
            reject_computed_fields({"phenomenonTime": "2025-01-01"}, ["observedArea", "phenomenonTime"])

    def test_valid_payload_does_not_raise(self):
        reject_computed_fields({"name": "test", "description": "desc"}, ["observedArea", "phenomenonTime"])