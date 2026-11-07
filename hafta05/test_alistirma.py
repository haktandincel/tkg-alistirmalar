# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145


def test_sepet_toplami_bos():
    assert sepet_toplami([]) == 0


def test_sepet_toplami_sifir():
    with pytest.raises(ValueError): 
        sepet_toplami([{"urun": "çay", "fiyat": 20, "adet": 0}]) 

def test_sepet_toplami_adet_negatif():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": -2},
    ]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)

def test_indirim_orani():
    assert indirim_orani(1000) == 15
    assert indirim_orani(500) == 10
    assert indirim_orani(100) == 5
    assert indirim_orani(90) == 0 

def test_indirim_orani_negatif():
    with pytest.raises(ValueError):
        indirim_orani(-1)


def test_en_pahali_urun_liste_bos():
    assert en_pahali_urun([]) is None


def test_esit_fiyatli_iki_urun():
    sepet= [{"urun": "ahmet", "fiyat": 5},
    {"urun": "mehmet", "fiyat": 5}]
    assert en_pahali_urun(sepet) == 'ahmet'


def test_sonraki_daha_pahali():
    sepet= [{"urun": "ahmet", "fiyat": 5},
    {"urun": "mehmet", "fiyat": 8}]
    assert en_pahali_urun(sepet) == 'mehmet'
                           