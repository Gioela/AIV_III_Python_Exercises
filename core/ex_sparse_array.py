class GegSparseArray:

    def __init__(self) -> None:
        self._length = 0
        self._elements = []

    @property
    def length(self):
        return self._length

    @property
    def elements(self):
        return self._elements

    def __add__(self, other):
        ...