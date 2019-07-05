%define vendor sony

%define rpm_vendor qualcomm

%define droid_target_aarch64 1

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define straggler_files \
/bin \
/bt_firmware \
/bugreports \
/cache \
/d \
/dsp \
/firmware \
/odm \
/persist \
/product \
/sdcard \
/verity_key \
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries / /vendor
Requires: droid-system
Requires: droid-system-vendor

%define pre_actions /bin/sh setup-sources.sh

%define droid_src_build 1

Source99: droid-hal-common.inc

