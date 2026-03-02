from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100))
    telefone = Column(String(20))


class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    custo_unitario = Column(Numeric(10, 2), nullable=False)
    unidade_medida = Column(String(20), nullable=False)


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer,primary_key=True)
    nome = Column(String(100), nullable=False)
    margem_lucro_percentual = Column(Numeric(5, 2), nullable=False)