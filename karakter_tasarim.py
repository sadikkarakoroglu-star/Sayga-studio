class KarakterTasarlayici:
    def __init__(self):
        self.aktif_proje = None

    def sifir_sablon_yukle(self):
        # Kullanıcıya başlangıç için telifsiz, ham bir insan bedeni sunar
        print("[SİSTEM]: Ham tasarım şablonu yüklendi.")
        return "Base_Mesh_V1"

    def iskelet_ve_rig_kur(self, model_ent):
        # Kullanıcının yüklediği herhangi bir modele otomatik kemik sistemi kurar
        print(f"[RIG]: {model_ent} için evrensel iskelet yapısı oluşturuldu.")

    def ekipman_bagla(self, model, parca_yolu):
        # Kullanıcının 1 TB arşivinden seçtiği zırh/kıyafet/silahı modele takar
        print(f"[MODÜLER]: {parca_yolu} modele entegre edildi.")
