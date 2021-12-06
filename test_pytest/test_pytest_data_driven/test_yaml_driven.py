import pytest
import yaml

class TestDataDriven():
    @pytest.mark.parametrize("env", yaml.safe_load(open("../../data/env.yml")))
    def test_demo(self,env):
        if "SIT" in env:
            print("这是测试环境")
            print("测试环境的IP是：",env["SIT"])
        elif "DEV" in env:
            print("这是开发环境")
            print("开发环境的IP是：", env["DEV"])

    def test_yaml(self):
        print(yaml.safe_load(open("../../data/env.yml")))

