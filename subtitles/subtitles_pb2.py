# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subtitles.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fsubtitles.proto\"B\n\x0fGenerateRequest\x12\x13\n\x0bsource_file\x18\x01 \x01(\t\x12\x1a\n\x12\x64\x65stination_folder\x18\x02 \x01(\t\"M\n\x10GenerateResponse\x12\x0e\n\x06source\x18\x01 \x01(\t\x12)\n\x07results\x18\x02 \x03(\x0b\x32\x18.GenerateResponseResults\"=\n\x17GenerateResponseResults\x12\r\n\x05model\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t2>\n\tSubtitles\x12\x31\n\x08Generate\x12\x10.GenerateRequest\x1a\x11.GenerateResponse\"\x00\x62\x06proto3')



_GENERATEREQUEST = DESCRIPTOR.message_types_by_name['GenerateRequest']
_GENERATERESPONSE = DESCRIPTOR.message_types_by_name['GenerateResponse']
_GENERATERESPONSERESULTS = DESCRIPTOR.message_types_by_name['GenerateResponseResults']
GenerateRequest = _reflection.GeneratedProtocolMessageType('GenerateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEREQUEST,
  '__module__' : 'subtitles_pb2'
  # @@protoc_insertion_point(class_scope:GenerateRequest)
  })
_sym_db.RegisterMessage(GenerateRequest)

GenerateResponse = _reflection.GeneratedProtocolMessageType('GenerateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATERESPONSE,
  '__module__' : 'subtitles_pb2'
  # @@protoc_insertion_point(class_scope:GenerateResponse)
  })
_sym_db.RegisterMessage(GenerateResponse)

GenerateResponseResults = _reflection.GeneratedProtocolMessageType('GenerateResponseResults', (_message.Message,), {
  'DESCRIPTOR' : _GENERATERESPONSERESULTS,
  '__module__' : 'subtitles_pb2'
  # @@protoc_insertion_point(class_scope:GenerateResponseResults)
  })
_sym_db.RegisterMessage(GenerateResponseResults)

_SUBTITLES = DESCRIPTOR.services_by_name['Subtitles']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENERATEREQUEST._serialized_start=19
  _GENERATEREQUEST._serialized_end=85
  _GENERATERESPONSE._serialized_start=87
  _GENERATERESPONSE._serialized_end=164
  _GENERATERESPONSERESULTS._serialized_start=166
  _GENERATERESPONSERESULTS._serialized_end=227
  _SUBTITLES._serialized_start=229
  _SUBTITLES._serialized_end=291
# @@protoc_insertion_point(module_scope)
