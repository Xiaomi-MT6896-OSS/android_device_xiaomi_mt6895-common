#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/mt6895-common',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/xiaomi',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
	('vendor/bin/hw/android.hardware.gnss-service.mediatek',
	'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
    .replace_needed('android.hardware.gnss-V1-ndk_platform.so','android.hardware.gnss-V1-ndk.so'),

    ('vendor/lib64/libnvram.so',
     'vendor/bin/ioprofiler'): blob_fixup()
        .add_needed('libbase_shim.so'),

     'vendor/lib64/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .add_needed('libbase_shim.so'),

    'vendor/lib64/mt6895/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),

    'vendor/lib64/hw/sensors.mediatek.V2.0.so': blob_fixup()
       .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),

    'vendor/lib64/libcodec2_hidl@1.0-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v35.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),

    'vendor/lib64/libcodec2_hidl@1.1-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v35.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),

    'vendor/lib64/libcodec2_hidl@1.2-v31.so': blob_fixup()
        .replace_needed('libstagefright_bufferqueue_helper.so', 'libstagefright_bufferqueue_helper-v35.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0-v31.so')
        .replace_needed('libcodec2_hidl@1.1.so', 'libcodec2_hidl@1.1-v31.so')
        .replace_needed('libcodec2_hidl_plugin.so', 'libcodec2_hidl_plugin-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libui.so', 'libui-v34.so')
        .add_needed('libbase_shim.so'),

    'vendor/lib64/libcodec2_hidl_plugin-v31.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so'),

    ('vendor/lib64/libcodec2_mtk_c2store.so', 'vendor/lib64/libcodec2_vpp_dump_mtk_yuv_plugin.so', 'vendor/lib64/libcodec2_vpp_gc_plugin.so', 'vendor/lib64/libcodec2_vpp_qt_plugin.so', 'vendor/lib64/libcodec2_vpp_rs_plugin.so'): blob_fixup()
        .replace_needed('libcodec2_soft_common.so', 'libcodec2_soft_common-v31.so')
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk-v31.so')
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so')
        .replace_needed('libsfplugin_ccodec_utils.so', 'libsfplugin_ccodec_utils-v31.so'),

    'vendor/bin/mnld': blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),

    'vendor/etc/sensors/hals.conf': blob_fixup()
        .regex_replace('android.hardware.sensors@2.X-subhal-mediatek.so', 'android.hardware.sensors@2.0-subhal-impl-1.0.so')
        .regex_replace('sensors.touch.detect.so', 'sensors.dynamic_sensor_hal.so'),

    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libalsautils.so', 'libalsautils-v31.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    'vendor/bin/mi_thermald': blob_fixup()
        .binary_regex_replace(b'%d/on', b'%d/..'),

    'vendor/etc/init/android.hardware.neuralnetworks-shim-service-mtk.rc': blob_fixup()
        .regex_replace('start', 'enable'),

    'vendor/etc/public.libraries.txt': blob_fixup()
        .add_line_if_missing('libmpbase.so'),

    'vendor/lib/libnvram.so': blob_fixup()
        .add_needed('libbase_shim.so'),

    'vendor/lib/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .add_needed('libbase_shim.so'),

}  # fmt: skip

module = ExtractUtilsModule(
    'mt6895-common',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
