# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class CellVoltages(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.cells = []
        i = 0
        while not self._io.is_eof():
            self.cells.append(self._root.Voltage(self._io, self, self._root))
            i += 1


    class Voltage(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_u2be()

        @property
        def volt(self):
            """Cell voltage (V)."""
            if hasattr(self, '_m_volt'):
                return self._m_volt if hasattr(self, '_m_volt') else None

            self._m_volt = (self.raw * 0.01)
            return self._m_volt if hasattr(self, '_m_volt') else None



