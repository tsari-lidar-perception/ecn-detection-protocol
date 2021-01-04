# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: detection.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='detection.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x64\x65tection.proto\"9\n\x07Point3D\x12\x0e\n\x01x\x18\x01 \x01(\x01:\x03nan\x12\x0e\n\x01y\x18\x02 \x01(\x01:\x03nan\x12\x0e\n\x01z\x18\x03 \x01(\x01:\x03nan\"a\n\x05\x42ox3D\x12\x18\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\x08.Point3D\x12\x0e\n\x06length\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x0f\n\x07heading\x18\x05 \x01(\x02\",\n\x06Header\x12\x0f\n\x07version\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"\x98\x01\n\x06Object\x12\n\n\x02id\x18\x01 \x01(\r\x12\x1a\n\x04type\x18\x02 \x01(\x0e\x32\x0c.Object.Type\x12\x12\n\nconfidence\x18\x03 \x01(\x02\x12\x13\n\x03\x62ox\x18\x04 \x01(\x0b\x32\x06.Box3D\"=\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07VEHICLE\x10\x01\x12\x0e\n\nPEDESTRIAN\x10\x02\x12\x0b\n\x07\x43YCLIST\x10\x03\"=\n\tDetection\x12\x17\n\x06header\x18\x01 \x01(\x0b\x32\x07.Header\x12\x17\n\x06object\x18\x02 \x03(\x0b\x32\x07.Object'
)



_OBJECT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Object.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VEHICLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PEDESTRIAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CYCLIST', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=315,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_OBJECT_TYPE)


_POINT3D = _descriptor.Descriptor(
  name='Point3D',
  full_name='Point3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Point3D.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='Point3D.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='Point3D.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=76,
)


_BOX3D = _descriptor.Descriptor(
  name='Box3D',
  full_name='Box3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='center', full_name='Box3D.center', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='Box3D.length', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='Box3D.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='Box3D.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='Box3D.heading', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=175,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Header.version', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Header.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=221,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Object.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Object.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Object.confidence', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='box', full_name='Object.box', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBJECT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=376,
)


_DETECTION = _descriptor.Descriptor(
  name='Detection',
  full_name='Detection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Detection.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object', full_name='Detection.object', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=439,
)

_BOX3D.fields_by_name['center'].message_type = _POINT3D
_OBJECT.fields_by_name['type'].enum_type = _OBJECT_TYPE
_OBJECT.fields_by_name['box'].message_type = _BOX3D
_OBJECT_TYPE.containing_type = _OBJECT
_DETECTION.fields_by_name['header'].message_type = _HEADER
_DETECTION.fields_by_name['object'].message_type = _OBJECT
DESCRIPTOR.message_types_by_name['Point3D'] = _POINT3D
DESCRIPTOR.message_types_by_name['Box3D'] = _BOX3D
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['Detection'] = _DETECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Point3D = _reflection.GeneratedProtocolMessageType('Point3D', (_message.Message,), {
  'DESCRIPTOR' : _POINT3D,
  '__module__' : 'detection_pb2'
  # @@protoc_insertion_point(class_scope:Point3D)
  })
_sym_db.RegisterMessage(Point3D)

Box3D = _reflection.GeneratedProtocolMessageType('Box3D', (_message.Message,), {
  'DESCRIPTOR' : _BOX3D,
  '__module__' : 'detection_pb2'
  # @@protoc_insertion_point(class_scope:Box3D)
  })
_sym_db.RegisterMessage(Box3D)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'detection_pb2'
  # @@protoc_insertion_point(class_scope:Header)
  })
_sym_db.RegisterMessage(Header)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'detection_pb2'
  # @@protoc_insertion_point(class_scope:Object)
  })
_sym_db.RegisterMessage(Object)

Detection = _reflection.GeneratedProtocolMessageType('Detection', (_message.Message,), {
  'DESCRIPTOR' : _DETECTION,
  '__module__' : 'detection_pb2'
  # @@protoc_insertion_point(class_scope:Detection)
  })
_sym_db.RegisterMessage(Detection)


# @@protoc_insertion_point(module_scope)
