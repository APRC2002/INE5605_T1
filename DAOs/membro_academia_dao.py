from DAOs.dao import DAO
from entidade.membroAcademia import MembroAcademia

class MembroAcademiaDAO(DAO):
    def __init__(self):
        super().__init__('mem.pkl')

    def add(self, membro: MembroAcademia):
        if(membro is not None) and isinstance(membro, MembroAcademia):
            super().add(str(membro.id), membro)

    def update(self, membro: MembroAcademia):
        if((membro is not None) and isinstance(membro, MembroAcademia)):
            super().update(str(membro.id), membro)

    def get(self, key: int):
        return super().get(str(key))

    def remove(self, key: int):
        return super().remove(str(key)) 