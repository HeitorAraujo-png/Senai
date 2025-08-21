from models import session, Medico, Paciente, Exame
from prettytable import PrettyTable

class Query:
    
    def __init__(self):
        pass 
   
    def commit(self, query):
        try:
            session.add(query)
            session.commit()
        except Exception as e:
            print(f'Erro: {e}')
    
    def medico(self):
        nome = input('Digite seu nome: ').strip().title()
        tel = input('Digite seu numero de telefone: ').strip().title()
        espc = input('Digite usa especialidade: ').strip().title()
        if nome and espc:
            query = Medico(nome, tel, espc)
            self.commit(query)
        else:
            if not nome:
                print('Seu nome é obrigatorio!')
            if not espc:
                print('Sua especialidade é obrigatoria!')
                
    def paciente(self):
        nome = input('Digite seu nome: ').strip().title()
        tel = input('Digite seu numero de telefone: ').strip().title()
        if nome:
            query = Paciente(nome, tel)
            self.commit(query)
        else:
            print('Seu nome é obrigatorio!')
            
    def exame(self):
        id_m = int(input('Digite o id do medico: '))
        id_p = int(input('Digite o id do paciente: '))
        exame = input('Digite o exame: ').strip().capitalize()
        try:
            valor = float(input('Digite o valor: '))
        except:
            valor = float(input('Digite o valor NUMERAL: '))
            
        if id_m and id_p and exame and valor:
            query = Exame(id_m, id_p, exame, valor)
            self.commit(query)
        else:
            if not id_m:
                print('O id do medico é obrigatorio!')
            if not id_p:
                print('O id do paciente é obrigatorio!')
            if not exame:
                print('O exame é obrigatorio!')
            if not valor:
                print('O valor é obrigatorio')
                
    def consultas(self):
        query = session.query(Exame).all()
        table = PrettyTable()
        table.field_names = ["Nome Paciente", "Telefone Paciente", "Nome Medico", "Especialidade", "Telefone Medico", "Exame", "Valor exame"]
        for i in query:
            table.add_row([
                session.query(Paciente).where(Paciente.id_paciente == i.id_paciente).first().nome_paciente, 
                session.query(Paciente).where(Paciente.id_paciente == i.id_paciente).first().tel_paciente,
                session.query(Medico).where(Medico.id_medico == i.id_medico).first().nome_medico,
                session.query(Medico).where(Medico.id_medico == i.id_medico).first().especialidade,
                session.query(Medico).where(Medico.id_medico == i.id_medico).first().tel_medico,
                session.query(Exame).where(Exame.id_medico == i.id_medico, Exame.id_paciente == i.id_paciente, Exame.id_exame == i.id_exame).first().exame,
                session.query(Exame).where(Exame.id_medico == i.id_medico, Exame.id_paciente == i.id_paciente, Exame.id_exame == i.id_exame).first().valor
                ], divider=True)
        print(table)
            
    def medicos(self):
        querys = session.query(Medico).all()
        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Especialidade", "Telefone"]
        for i in querys:
            table.add_row([i.id_medico, i.nome_medico, i.especialidade, i.tel_medico], divider=True)
        print(table)
    
    def pacientes(self):
        query = session.query(Paciente).all()
        table = PrettyTable()
        table.field_names = ["ID", "Nome", "Telefone"]
        for i in query:
            table.add_row([i.id_paciente, i.nome_paciente, i.tel_paciente], divider=True)
        print(table)
            
    def testes(self):
        pass
import os
make = Query()
os.system('cls')
make.testes()