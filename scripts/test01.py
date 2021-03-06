import allure
import pytest


class Test_01:

    @allure.step(title='我是测试步骤001')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('a',[1,2,3])
    def test_001(self,a):
        assert  a !=2

    @pytest.mark.parametrize('b',[4,5,6])
    def test_002(self,b):
        allure.attach('描述','我是测试步骤test_002的描述...')
        assert b != 3

