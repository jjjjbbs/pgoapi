# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/UseItemReviveMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory.Item import ItemId_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/UseItemReviveMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nBPOGOProtos/Networking/Requests/Messages/UseItemReviveMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\x1a&POGOProtos/Inventory/Item/ItemId.proto\"^\n\x14UseItemReviveMessage\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\x12\n\npokemon_id\x18\x02 \x01(\x06\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USEITEMREVIVEMESSAGE = _descriptor.Descriptor(
  name='UseItemReviveMessage',
  full_name='POGOProtos.Networking.Requests.Messages.UseItemReviveMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Networking.Requests.Messages.UseItemReviveMessage.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Networking.Requests.Messages.UseItemReviveMessage.pokemon_id', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=245,
)

_USEITEMREVIVEMESSAGE.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2._ITEMID
DESCRIPTOR.message_types_by_name['UseItemReviveMessage'] = _USEITEMREVIVEMESSAGE

UseItemReviveMessage = _reflection.GeneratedProtocolMessageType('UseItemReviveMessage', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMREVIVEMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.UseItemReviveMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.UseItemReviveMessage)
  ))
_sym_db.RegisterMessage(UseItemReviveMessage)


# @@protoc_insertion_point(module_scope)
