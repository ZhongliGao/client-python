# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: function.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='function.proto',
  package='engula.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x66unction.proto\x12\tengula.v1*\x95\x01\n\x08\x46unction\x12\x08\n\x04NOOP\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x0b\x12\x07\n\x03SUB\x10\x0c\x12\x07\n\x03LEN\x10\x15\x12\x07\n\x03GET\x10\x16\x12\x07\n\x03SET\x10\x17\x12\n\n\x06\x44\x45LETE\x10\x18\x12\n\n\x06\x41PPEND\x10\x1f\x12\x0c\n\x08POP_BACK\x10 \x12\r\n\tPOP_FRONT\x10!\x12\r\n\tPUSH_BACK\x10\"\x12\x0e\n\nPUSH_FRONT\x10#b\x06proto3'
)

_FUNCTION = _descriptor.EnumDescriptor(
  name='Function',
  full_name='engula.v1.Function',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOOP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADD', index=1, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB', index=2, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LEN', index=3, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET', index=4, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SET', index=5, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=6, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APPEND', index=7, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POP_BACK', index=8, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POP_FRONT', index=9, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUSH_BACK', index=10, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUSH_FRONT', index=11, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=30,
  serialized_end=179,
)
_sym_db.RegisterEnumDescriptor(_FUNCTION)

Function = enum_type_wrapper.EnumTypeWrapper(_FUNCTION)
NOOP = 0
ADD = 11
SUB = 12
LEN = 21
GET = 22
SET = 23
DELETE = 24
APPEND = 31
POP_BACK = 32
POP_FRONT = 33
PUSH_BACK = 34
PUSH_FRONT = 35


DESCRIPTOR.enum_types_by_name['Function'] = _FUNCTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
