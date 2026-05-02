from varlik_yoneticisi import VarlikYoneticisi
from sayga_ai import SaygaAI
from gorsel_isleyici import GorselIsleyici
from karakter_tasarim import KarakterTasarlayici
from efekt_laboratuvari import EfektLaboratuvari
from veri_isleyici import VeriIsleyici
from arayuz_kontrol import SaygaArayuz
from kaynak_yoneticisi import KaynakYoneticisi
from paketleyici import SaygaPaketleyici
from zaman_yoneticisi import ZamanYoneticisi
from video_kaydedici import VideoKaydedici
from motion_yoneticisi import MotionYoneticisi
from pbr_shader import PBRShader

class SaygaStudyo:
    def __init__(self):
        # Tüm profesyonel modüllerin bağlantısı
        self.depo = VarlikYoneticisi()
        self.ai = SaygaAI()
        self.render = GorselIsleyici()
        self.tasarim = KarakterTasarlayici()
        self.vfx = EfektLaboratuvari()
        self.veri = VeriIsleyici()
        self.arayuz = SaygaArayuz()
        self.kaynak = KaynakYoneticisi()
        self.paket = SaygaPaketleyici()
        self.zaman = ZamanYoneticisi()
        self.kayit = VideoKaydedici()
        self.motion = MotionYoneticisi()
        self.pbr = PBRShader()

    def calistir(self, senaryo="Bos Senaryo", kalite="1080p"):
        self.kaynak.sistem_kontrol()
        
        # 1. AI: Duyguyu ve görsel gereksinimleri analiz eder (Telifsiz Mod)
        v_paketi = self.ai.senaryo_analiz(senaryo)
        
        # 2. Render ve Kayıt Çözünürlüğü Ayarı (4K / 1080p / 720p)
        self.render.render_kalitesi_sec(kalite)
        self.kayit.kayit_profilini_ayarla(kalite)
        
        # 3. Arşivden Kullanıcıya Ait Modeli Çek (Özel isim içermez)
        d_yolu = self.depo.varlik_cek("Kullanici_Projeleri", "aktif_karakter.obj")
        
        # 4. Veri İşleme (Eğer dosya yoksa şablonu kullanır)
        yol = d_yolu if d_yolu else "SISTEM/HAM_SABLON.OBJ"
        islenmis = self.veri.dosya_analizi(yol)
        
        if islenmis["durum"] == "Basarili":
            # 5. PBR Shader ve Model Render Süreci
            ent = self.render.model_ekle(islenmis["yol"], v_paketi["vfx_tipi"], v_paketi["vfx_gucu"])
            
            # 6. Otomatik Rigging ve Karakter Giydirme
            self.tasarim.iskelet_ve_rig_kur(ent)
            
            # 7. Animasyon Döngüsü ve Video Paketleme
            self.zaman.guncelle()
            self.kayit.videoyu_paketle("Sayga_Cikti", kalite)
            
            # 8. Büyük Final: Render Başlatma
            self.render.baslat()
        else:
            # Kritik hata durumunda sessizce bildirir
            pass

if __name__ == "__main__":
    sayga = SaygaStudyo()
    # Örnek: Kullanıcı 4K çıktı almak istiyor
    sayga.calistir("Ofkeli ve destansi bir atmosfer", kalite="4K")
