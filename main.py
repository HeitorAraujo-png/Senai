from query import Query
import os

make = Query()
os.system('cls')
make.testes()
print('Use o atalho CTRL + C para parar! ')
try:
    while True:
        if (cria:=input('Você deseja cadastrar um medico, paciente ou um exame? [MEDICO/PACIENTE/EXAME]: ').strip().lower()) == 'medico':
            os.system('cls')
            make.medico()
        elif cria == 'paciente':
            os.system('cls')
            make.paciente()
        elif cria == 'exame':
            os.system('cls')
            make.exame()
        else:
            os.system('cls')
            print(f'Você escreveu "{cria}", não tem essa opção! ')
        if cria == 'admincomands':
            if (tabelas:=input('Qual tabela você gostaira de ver? [MEDICOS/PACIENTES/CONSULTA]: ').strip().lower()) == 'consulta':
                make.consultas()
            elif tabelas == 'medicos':
                make.medicos()
            elif tabelas == 'pacientes':
                make.pacientes()
except KeyboardInterrupt:
    print('\nPrograma parou!')
