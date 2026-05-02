[app]
# Uygulama Kimliği
title = Sayga Studio
package.name = saygastudyo
package.domain = com.saygastudyo

# Dosya Kaynakları (Kodlar ve Logonu buraya ekledik)
source.dir = .
source.include_exts = py,png,jpg,obj,fbx,json
icon.filename = sayga_logo.png

# Versiyon ve SDK Ayarları (Google Play Uyumlu)
version = 1.0.0
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21

# KRİTİK: 1 TB Arşiv Erişimi ve GPU İzinleri
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET, MANAGE_EXTERNAL_STORAGE

# Gereksinimler (Motorun çalışması için gereken kütüphaneler)
requirements = python3,kivy,numpy,pyopengl,requests

# Android Paketleme Detayları
android.arch = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
