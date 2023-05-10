from src.database.dbconfig import session
from src.models.tabela_emoldb import TabelaEmol as TabelaEmolDB
from src.models.tabela_emol import TabelaEmol


class TabelaEmolCore():
    def create_tabela_emol(self, tabela_emol: TabelaEmol):
        with session:
            new_tabela_emol = TabelaEmolDB(**tabela_emol.dict())
            session.add(new_tabela_emol)
            session.commit()
            return new_tabela_emol
        
    def listar_tabelas_emol(self):
        with session:
            tabelas_emol = session.query(TabelaEmolDB).all()
            return tabelas_emol
"""       
    def delete_tabela_emol(self, codigo_ato: str):
        with session:
            tabela_emol = session.query(TabelaEmolDB).filter(TabelaEmolDB.codigo_ato == codigo_ato).first()
            if not tabela_emol:
                return False
            session.delete(tabela_emol)
            session.commit()
            return True
"""