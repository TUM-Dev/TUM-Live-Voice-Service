# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subtitles.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsubtitles.proto\x12\rlive.voice.v1\"H\n\x0eReceiveRequest\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x12\x11\n\tsubtitles\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"K\n\x0fGenerateRequest\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x12\x13\n\x0bsource_file\x18\x02 \x01(\t\x12\x10\n\x08language\x18\x03 \x01(\t\"\x07\n\x05\x45mpty2W\n\x11SubtitleGenerator\x12\x42\n\x08Generate\x12\x1e.live.voice.v1.GenerateRequest\x1a\x14.live.voice.v1.Empty\"\x00\x32T\n\x10SubtitleReceiver\x12@\n\x07Receive\x12\x1d.live.voice.v1.ReceiveRequest\x1a\x14.live.voice.v1.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'subtitles_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECEIVEREQUEST._serialized_start=34
  _RECEIVEREQUEST._serialized_end=106
  _GENERATEREQUEST._serialized_start=108
  _GENERATEREQUEST._serialized_end=183
  _EMPTY._serialized_start=185
  _EMPTY._serialized_end=192
  _SUBTITLEGENERATOR._serialized_start=194
  _SUBTITLEGENERATOR._serialized_end=281
  _SUBTITLERECEIVER._serialized_start=283
  _SUBTITLERECEIVER._serialized_end=367
# @@protoc_insertion_point(module_scope)
