# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='value.proto',
  package='engula.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bvalue.proto\x12\tengula.v1\"\xc1\x01\n\x05Value\x12\x14\n\nblob_value\x18\x02 \x01(\x0cH\x00\x12\x14\n\ntext_value\x18\x03 \x01(\tH\x00\x12\x15\n\x0bint64_value\x18\x04 \x01(\x12H\x00\x12\x32\n\x0esequence_value\x18\x0e \x01(\x0b\x32\x18.engula.v1.SequenceValueH\x00\x12\x38\n\x11\x41ssociative_value\x18\x0f \x01(\x0b\x32\x1b.engula.v1.AssociativeValueH\x00\x42\x07\n\x05value\"1\n\rSequenceValue\x12 \n\x06values\x18\x01 \x03(\x0b\x32\x10.engula.v1.Value\"B\n\x10\x41ssociativeValue\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\x12 \n\x06values\x18\x02 \x03(\x0b\x32\x10.engula.v1.Valueb\x06proto3'
)




_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='engula.v1.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='blob_value', full_name='engula.v1.Value.blob_value', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_value', full_name='engula.v1.Value.text_value', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='engula.v1.Value.int64_value', index=2,
      number=4, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_value', full_name='engula.v1.Value.sequence_value', index=3,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Associative_value', full_name='engula.v1.Value.Associative_value', index=4,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='engula.v1.Value.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=27,
  serialized_end=220,
)


_SEQUENCEVALUE = _descriptor.Descriptor(
  name='SequenceValue',
  full_name='engula.v1.SequenceValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='engula.v1.SequenceValue.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=271,
)


_ASSOCIATIVEVALUE = _descriptor.Descriptor(
  name='AssociativeValue',
  full_name='engula.v1.AssociativeValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='engula.v1.AssociativeValue.keys', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='engula.v1.AssociativeValue.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=339,
)

_VALUE.fields_by_name['sequence_value'].message_type = _SEQUENCEVALUE
_VALUE.fields_by_name['Associative_value'].message_type = _ASSOCIATIVEVALUE
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['blob_value'])
_VALUE.fields_by_name['blob_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['text_value'])
_VALUE.fields_by_name['text_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['int64_value'])
_VALUE.fields_by_name['int64_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['sequence_value'])
_VALUE.fields_by_name['sequence_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['Associative_value'])
_VALUE.fields_by_name['Associative_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_SEQUENCEVALUE.fields_by_name['values'].message_type = _VALUE
_ASSOCIATIVEVALUE.fields_by_name['values'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['SequenceValue'] = _SEQUENCEVALUE
DESCRIPTOR.message_types_by_name['AssociativeValue'] = _ASSOCIATIVEVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'value_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.Value)
  })
_sym_db.RegisterMessage(Value)

SequenceValue = _reflection.GeneratedProtocolMessageType('SequenceValue', (_message.Message,), {
  'DESCRIPTOR' : _SEQUENCEVALUE,
  '__module__' : 'value_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.SequenceValue)
  })
_sym_db.RegisterMessage(SequenceValue)

AssociativeValue = _reflection.GeneratedProtocolMessageType('AssociativeValue', (_message.Message,), {
  'DESCRIPTOR' : _ASSOCIATIVEVALUE,
  '__module__' : 'value_pb2'
  # @@protoc_insertion_point(class_scope:engula.v1.AssociativeValue)
  })
_sym_db.RegisterMessage(AssociativeValue)


# @@protoc_insertion_point(module_scope)
