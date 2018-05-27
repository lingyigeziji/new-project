import allure
import pytest


class Test_01:

    @allure.step(title='测试步骤001')
    @pytest.mark.parametrize('a',[1,2,3])
    def test_001(self,a):
        assert  a !=2

    @pytest.mark.parametrize('b',[4,5,6])
    def test_002(self,b):
        allure.sttach('描述','我是测试步骤test_002的描述...')
        assert b != 3

