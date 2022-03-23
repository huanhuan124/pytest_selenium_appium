
import yaml
import pytest
class TestYaml:
    @pytest.mark.parametrize("env", yaml.safe_load())
    def test_yaml(self,env):
        pass