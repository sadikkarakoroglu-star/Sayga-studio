class GorselIsleyici:
    def __init__(self):
        self.su_anki_ayar = None

    def render_kalitesi_sec(self, kalite="1080p"):
        # 4K, 1080p veya 720p arasında seçim yapar
        self.su_anki_ayar = kalite
        print(f">> [GPU]: Render modu {kalite} olarak ayarlandi.")

    def model_ekle(self, yol, efekt, guc):
        # Seçilen çözünürlüğe göre Anti-Aliasing (tırtık giderme) seviyesini ayarlar
        aa_seviyesi = "8x" if self.su_anki_ayar == "4K" else "2x"
        return f"Entity_Rendered_{aa_seviyesi}"

    def baslat(self):
        # Ekrana son görüntüyü basar
        pass
