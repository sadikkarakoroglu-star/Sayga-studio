class SaygaAI:
    def __init__(self):
        # Telife girmeyen görsel parametreler
        self.ruh_halleri = {
            "ofkeli": {"isik": "Kirmizi", "vfx": 5.0, "kam": "Yakin"},
            "dingin": {"isik": "Mavi", "vfx": 1.0, "kam": "Genis"},
            "destansi": {"isik": "Altin", "vfx": 8.0, "kam": "Alt"}
        }

    def senaryo_analiz(self, metin):
        metin = metin.lower()
        # Varsayılan değerler: Karakter ismi yerine ID kullanılır
        karar = {
            "aktif_model_id": "Kullanici_Modeli_01",
            "vfx_tipi": "Enerji_Aura",
            "isik_rengi": "Beyaz",
            "vfx_gucu": 1.0,
            "kamera": "Standart"
        }
        
        # Kullanıcının girdiği duyguya göre görseli şekillendir
        for duygu, ayar in self.ruh_halleri.items():
            if duygu in metin:
                karar["isik_rengi"] = ayar["isik"]
                karar["vfx_gucu"] = ayar["vfx"]
                karar["kamera"] = ayar["kam"]
        
        return karar
