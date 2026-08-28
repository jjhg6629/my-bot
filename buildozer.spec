[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Path to your source code directory
source.dir = .

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it blank to exclude none)
#source.exclude_exts = spec

# (list) List of directory to exclude (let it blank to exclude none)
#source.exclude_dirs = tests, bin

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

[buildozer]

# (int) Log level
log_level = 2

# (str) Path to build artifact storage
bin_dir = bin

# (str) The Android API to use for building the application
android.api = 33

# (str) Minimum API to use for Android
android.minapi = 21

# (bool) If True, automatically accept android SDK license
android.accept_sdk_license = True

# (list) Supported architectures
supported_architectures = armeabi-v7a
