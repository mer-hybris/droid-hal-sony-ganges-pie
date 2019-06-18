%define device kirin
%define vendor sony

%define rpm_device i4113
%define rpm_vendor qualcomm

%define vendor_pretty Sony
%define device_pretty Xperia 10 - Dual SIM

%define droid_target_aarch64 1

%define have_custom_img_boot 1
%define have_custom_img_recovery 1
%define lunch_device aosp_%{rpm_device}-user

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

%include rpm/dhd/droid-hal-device.inc
