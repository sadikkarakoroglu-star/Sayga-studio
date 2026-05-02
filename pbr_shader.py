class PBRShader:
    def materyal_hesapla(self, tip):
        if tip == "Metal": return {"metallic": 1.0, "roughness": 0.2}
        return {"metallic": 0.0, "roughness": 0.5}
