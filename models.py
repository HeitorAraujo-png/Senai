from sqlalchemy.orm import sessionmaker, create_session , declarative_base
from sqlalchemy import Column, String, ForeignKey, PrimaryKeyConstraint, Float, Integer, create_engine
Base = declarative_base()
engine = create_engine('sqlite:///sql.db')
Session = sessionmaker(bind=engine)
session = Session()

class Medico(Base):
    __tablename__ = 'medicos'
    id_medico = Column(Integer, autoincrement=True, primary_key=True)
    nome_medico = Column(String, nullable=False)
    tel_medico = Column(String)
    especialidade = Column(String, nullable=False)
    
    def __init__(self, nome, tel, espc):
        self.nome_medico = nome
        self.tel_medico = tel
        self.especialidade = espc
        
class Paciente(Base):
    __tablename__ = 'pacientes'
    id_paciente = Column(Integer, autoincrement=True, primary_key=True)
    nome_paciente = Column(String, nullable=False)
    tel_paciente = Column(String)
    
    def __init__(self, nome, tel):
        self.nome_paciente = nome
        self.tel_paciente = tel
        
class Exame(Base):
    __tablename__ = 'exames'
    id_exame = Column(Integer, autoincrement=True, primary_key=True)
    id_medico = Column(String, ForeignKey(Medico.id_medico), nullable=False)
    id_paciente = Column(String, ForeignKey(Paciente.id_paciente), nullable=False)
    exame = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    
    def __init__(self, id_medico, id_paciente, exame, valor):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.exame = exame
        self.valor = valor

Base.metadata.create_all(engine)