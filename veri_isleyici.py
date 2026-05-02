import os
class VeriIsleyici:
    def dosya_analizi(self, yol):
        if not yol or not os.path.exists(yol): return {"durum": "Hata"}
        return {"durum": "Basarili", "yol": yol}
