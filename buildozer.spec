[app]
title = FruitMinerApp
package.name = fruitminer
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy,zlib
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 31
android.ndk = 23b
android.ndk_api = 21