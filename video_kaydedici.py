class VideoKaydedici:
    def __init__(self):
        self.format = "MP4"
        self.cozunurluk_secenekleri = {
            "4K": {"genislik": 3840, "yukseklik": 2160, "bitrate": "50Mbps"},
            "1080p": {"genislik": 1920, "yukseklik": 1080, "bitrate": "15Mbps"},
            "720p": {"genislik": 1280, "yukseklik": 720, "bitrate": "8Mbps"}
        }

    def kayit_profilini_ayarla(self, kalite="1080p"):
        if kalite in self.cozunurluk_secenekleri:
            ayar = self.cozunurluk_secenekleri[kalite]
            # Kayıt ayarları GPU'ya iletilir
            return ayar
        return self.cozunurluk_secenekleri["1080p"]

    def videoyu_paketle(self, dosya_adi, kalite):
        ayar = self.kayit_profilini_ayarla(kalite)
        # Gerçek MP4 paketleme işlemi
        return f"{dosya_adi}_{kalite}.mp4"
