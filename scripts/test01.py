import allure
import pytest


class Test_01:

    @allure.step(title='测试步骤001')
    @pytest.mark.parametrize('a',[1,2,3])
    def test_001(self,a):
        assert  a !=2