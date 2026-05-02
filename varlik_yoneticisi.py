import os
class VarlikYoneticisi:
    def __init__(self):
        self.ana_depo = "/sdcard/Sayga_Studyo_Depo/"
        self.kategoriler = ["Modeller", "Karakterler", "Silahlar", "Araclar", "Ev_Esyalari", "Ciktilar"]
        self.depo_hazirla()
    def depo_hazirla(self):
        os.makedirs(self.ana_depo, exist_ok=True)
        for kat in self.kategoriler:
            os.makedirs(os.path.join(self.ana_depo, kat), exist_ok=True)
    def varlik_cek(self, kategori, isim):
        yol = os.path.join(self.ana_depo, kategori, isim)
        return yol if os.path.exists(yol) else None
