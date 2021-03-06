from kai.packet import Packet
from pprint import pp
from converter import DB, serialize

# def recurse_vars(obj):
#     out = vars(obj).copy()
#     for key, val in vars(obj).items():
#         if key.startswith('_'):
#             del out[key]
#             continue
#         if not type(val).__module__ == 'builtins':
#             print(key, val)
#             out[key] = recurse_vars(val)
#     return out


db = DB()
# Basic Info
d = Packet.from_bytes(b"\xdd\x03\x00\x1b\x118\x00b\x00\xa4\x04\xb0\x00\x00'n\x02\x82\x00\x00" + b'\x00\x00!\x0e\x03\x0b\x02\x0b"\x0b\x10\xfcBw')
d = Packet.from_bytes(bytes.fromhex('dd 03 00 1b 10 3c fe 0e 02 d7 04 b0 00 00 27 6e 00 00 00 00 00 00 21 3d 03 0b 02 0b 37 0b 47 fb 69 77'))
pp(serialize(d))
db.insert(d)

# Cells
d2 = Packet.from_bytes(b'\xdd\x04\x00\x16\x0f\xa7\x0f\xa5\x0f\xa1\x0f\x98\x0f\x9e\x0f\xa0\x0f\xb1\x0f\xbb' + b'\x0f\xb1\x0f\xa6\x0f\xa7\xf8\x18w',)
pp(serialize(d2))
db.insert(d2)
cells = [c.volt for c in d2.body.data.cells]
print(sum(cells))

# HW
d2 = Packet.from_bytes(b'\xdd\x05\x00\x11SP15S001-P13S-30' + b'A\xfb\xfdw')
pp(serialize(d2))

# Settings
d2 = Packet.from_bytes(b'\xdd\x10\x00\x02\x07\xd0\xff\x27\x77')
pp(serialize(d2))
# pp(vars(d2.body))

# Request
d2 = Packet.from_bytes(b'\xdd\xa5\x05\x00\xff\xfbw')
pp(serialize(d2))
pp(isinstance(d2.body, Packet.ReadReq))

# Write
d2 = Packet.from_bytes(b'\xDD\x5A\x10\x02\x4E\x20\xFF\x80\x77')
pp(serialize(d2))
pp(isinstance(d2.body, Packet.WriteReq))

