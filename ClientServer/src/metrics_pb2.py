# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metrics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmetrics.proto\"\x07\n\x05\x45mpty\"N\n\x0eMetricsMessage\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0b\n\x03\x63pu\x18\x02 \x01(\x02\x12\x0b\n\x03ram\x18\x03 \x01(\x02\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t28\n\x0eMetricsService\x12&\n\x0bsendMetrics\x12\x0f.MetricsMessage\x1a\x06.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metrics_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=17
  _EMPTY._serialized_end=24
  _METRICSMESSAGE._serialized_start=26
  _METRICSMESSAGE._serialized_end=104
  _METRICSSERVICE._serialized_start=106
  _METRICSSERVICE._serialized_end=162
# @@protoc_insertion_point(module_scope)
