[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it blank to exclude none)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it blank to exclude none)
#source.exclude_dirs = tests, bin

# (list) List of exclusions in source files
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# specify 'python3', 'kivy' (or other libraries your bot/app needs)
requirements = python3,kivy

# (list) Custom source folders for requirements
#requirements.source.dirname = ../(at)core

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) List of services to declare
#services = NAME:gs://path/to/script,NAME2:gs://path/to/script

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = bin

# (str) Path to build output (default is .buildozer)
#build_dir = .buildozer

# (str) The Android NDK to use. If empty, it will be downloaded automatically.
android.ndk = 

# (str) The Android SDK to use. If empty, it will be downloaded automatically.
android.sdk = 

# (str) ANT to use. If empty, it will be downloaded automatically.
android.ant = 

# (str) PYTHON to use. If empty, it will be downloaded automatically.
android.python = python3

# (str) The Android API to use for building the application
android.api = 33

# (str) Minimum API to use for Android.
android.minapi = 21

# (str) Android SDK version to use
#android.sdk_version = 33

# (str) Android NDK version to use
#android.ndk_version = 25b

# (str) Android build tools version to use
#android.build_tools_version = 33.0.2

# (bool) If True, automatically accept android SDK license
android.accept_sdk_license = True

# (list) Supported architectures
# تم حصرها على معمارية واحدة لتسريع البناء وتفادي أخطاء السيرفر
supported_architectures = armeabi-v7a

# (str) python-for-android git branch to use, if not using master
#p4a.branch = master
