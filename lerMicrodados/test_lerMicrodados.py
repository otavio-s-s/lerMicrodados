from .lerMicrodados import ler_PNADcontinua
import pytest


class TestPNADContinua:
    def test_carregadados(self):
        df = ler_PNADcontinua(['2015'])
        assert df.shape == (574034, 864)
