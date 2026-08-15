# Common device tree for MediaTek MT6895 (Dimensity 8200) Xiaomi devices

This repository holds the SoC-common part of the device trees for the
MediaTek MT6895 (Dimensity 8200) Xiaomi devices supported by this project:

- `yuechu` — Xiaomi Civi 3 / Redmi Note 12T Pro (Dimensity 8200-Ultra)
- `pearl` — Redmi K70E / POCO X6 Pro

It follows the layout used by the `xaga-risingos-devs` mt6895-common tree:
each device tree (`device/xiaomi/<device>`) inherits `mt6895.mk`
(product side) and `BoardConfigCommon.mk` (board side), while the
SoC-common proprietary blobs live in `vendor/xiaomi/mt6895-common`.

## Layout

- `BoardConfigCommon.mk` — board config shared by all MT6895 devices
- `mt6895.mk` — product makefile shared by all MT6895 devices
- `configs/` — shared audio/media/wifi/thermal/rsc/permissions configs
- `init/` — shared init rc files and fstabs
- `modules/` — insmod helper scripts
- `overlay/`, `overlay-lineage/` — MT6895 RROs
- `sepolicy/` — shared sepolicy (dolby-specific rules live device-side)
- `power/`, `udfps/`, `libmisight/` — SoC-common native sources
- `proprietary-files.txt` — SoC-common blobs extracted from the yuechu
  OS3.0.10.0.VMICNXM dump
- `extract-files.py` — extraction script for the common blobs

## Blob ownership

Version-coupled stacks are deliberately kept device-side (they differ
between yuechu OS3.0.10.0 and pearl OS3.0.3.0):

- Radio / Engineer Mode / IMS
- Keymint / MITEE / TEE user-space stack (tee-supplicant, teecli, gz, ...)
- Audio calibration / smart-PA libs (AW882xx on yuechu)
- Dolby DAP engine (yuechu only)

The common tree only carries SoC-generic blobs that are identical in
behaviour across both devices.
