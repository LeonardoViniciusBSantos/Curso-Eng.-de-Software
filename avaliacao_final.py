import sys, sqlite3, random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

class Cliente():
    def __init__(self, nome:str = '', cpf:int = 0, nacionalidade:str = '', estado:str = '', cidade:str = '', nome_mae:str = '', senha:str = '', agencia:str = '', conta:str = ''):
        self.nome = nome
        self.cpf = cpf
        self.nacionalidade = nacionalidade
        self.estado = estado
        self.cidade = cidade
        self.nome_mae = nome_mae
        self.senha = senha
        self.agencia = agencia
        self.conta = conta

    def gerar_conta (self):
        self.agencia = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        self.conta = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

        texto_agencia.setText('Agência: ' + self.agencia)
        texto_agencia.adjustSize()

        texto_conta.setText('Conta: ' + self.conta)
        texto_conta.adjustSize()
        
    
def validar():
    x = 0
    if entrada_nome.text() =='':
        texto_nome.setText('Nome completo *')
        texto_nome.setStyleSheet('color:red')
        texto_nome.adjustSize()
    else:
        texto_nome.setStyleSheet('color:black')
        x+=1

    if len(entrada_cpf.text()) != 11:
        texto_cpf.setText('CPF (somente digitos) *')
        texto_cpf.setStyleSheet('color:red')
        texto_cpf.adjustSize()
    else:
        texto_cpf.setStyleSheet('color:black')
        x+=1

    if entrada_nacionalidade.text() =='':
        texto_nacionalidade.setText('Nacionalidade *')
        texto_nacionalidade.setStyleSheet('color:red')
        texto_nacionalidade.adjustSize()
    else:
        texto_nacionalidade.setStyleSheet('color:black')
        x+=1

    if entrada_estado.text() =='':
        texto_estado.setText('Estado *')
        texto_estado.setStyleSheet('color:red')
        texto_estado.adjustSize()
    else:
        texto_estado.setStyleSheet('color:black')
        x+=1 
        
    if entrada_cidade.text() =='':
        texto_cidade.setText('Cidade *')
        texto_cidade.setStyleSheet('color:red')
        texto_cidade.adjustSize()
    else:
        texto_cidade.setStyleSheet('color:black')
        x+=1 
    
    if entrada_endereco.text() =='':
        texto_endereco.setText('Endereço *')
        texto_endereco.setStyleSheet('color:red')
        texto_endereco.adjustSize()
    else:
        texto_endereco.setStyleSheet('color:black')
        x+=1 

    if entrada_mae.text() =='':
        texto_mae.setText('Nome da mãe *')
        texto_mae.setStyleSheet('color:red')
        texto_mae.adjustSize()
    else:
        texto_mae.setStyleSheet('color:black')
        x+=1
        
    if entrada_senha.text() != entrada_confirmacao.text() or entrada_senha.text() == '':
        texto_senha.setText('Crie sua senha *')
        texto_senha.setStyleSheet('color:red')
        texto_senha.adjustSize()

        texto_confirmacao.setText('Confirme sua senha *')
        texto_confirmacao.setStyleSheet('color:red')
        texto_confirmacao.adjustSize()

    else:
        texto_senha.setStyleSheet('color:black')
        texto_confirmacao.setStyleSheet('color:black')
        x+=1

    if x == 8:
        cliente1 = Cliente(entrada_nome.text(),entrada_cpf.text(), entrada_nacionalidade.text(),entrada_estado.text(), entrada_cidade.text(), entrada_mae.text(), entrada_senha.text())
        cliente1.gerar_conta()
    else:
        x = 0 

def conectar_banco ():
    conexao = sqlite3.connect('clientes_bancos.db')
    c = conexao.cursor()
    c.execute('CREATE TABLE if not exists clientes(nome text, cpf text')


cliente1 = Cliente()

app = QApplication(sys.argv)

janela = QWidget()

janela.resize(700,650)
janela.setStyleSheet('background-color:#EFF249')

janela.setWindowTitle("Banco do Leo (cadastro)")

titulo = QLabel('Forneça as informações para o cadastro:', janela)
titulo.setStyleSheet('font-size: 18px; font-weight: bold')
titulo.move(20, 10) 

texto_nome = QLabel('Nome completo *', janela)
texto_nome.move(20, 50) 

entrada_nome = QLineEdit('', janela)
entrada_nome.setGeometry(20, 70, 400, 20)
entrada_nome.setStyleSheet('background-color:white')

texto_cpf = QLabel('CPF (somente digitos) *', janela)
texto_cpf.move(20, 100) 

entrada_cpf = QLineEdit('', janela)
entrada_cpf.setGeometry(20, 120, 200, 20)
entrada_cpf.setStyleSheet('background-color:white')

texto_nacionalidade = QLabel('Nacionalidade *', janela)
texto_nacionalidade.move(20, 150) 

entrada_nacionalidade = QLineEdit('', janela)
entrada_nacionalidade.setGeometry(20, 170, 200, 20)
entrada_nacionalidade.setStyleSheet('background-color:white')

texto_estado = QLabel('Estado *', janela)
texto_estado.move(230, 150) 

entrada_estado = QLineEdit('', janela)
entrada_estado.setGeometry(230, 170, 200, 20)
entrada_estado.setStyleSheet('background-color:white')

texto_cidade = QLabel('Cidade *', janela)
texto_cidade.move(440, 150) 

entrada_cidade = QLineEdit('', janela)
entrada_cidade.setGeometry(440, 170, 200, 20)
entrada_cidade.setStyleSheet('background-color:white')

texto_endereco = QLabel('Endereço *', janela)
texto_endereco.move(20, 200) 

entrada_endereco = QLineEdit('', janela)
entrada_endereco.setGeometry(20, 220, 500, 20)
entrada_endereco.setStyleSheet('background-color:white')

texto_telefone = QLabel('Telefone', janela)
texto_telefone.move(20, 250) 

entrada_telefone = QLineEdit('', janela)
entrada_telefone.setGeometry(20, 270, 200, 20)
entrada_telefone.setStyleSheet('background-color:white')

texto_renda = QLabel('Renda mensal', janela)
texto_renda.move(20, 300) 

entrada_renda = QLineEdit('', janela)
entrada_renda.setGeometry(20, 320, 200, 20)
entrada_renda.setStyleSheet('background-color:white')

texto_mae = QLabel('Nome da mãe *', janela)
texto_mae.move(20, 350) 

entrada_mae = QLineEdit('', janela)
entrada_mae.setGeometry(20, 370, 400, 20)
entrada_mae.setStyleSheet('background-color:white')

texto_pai = QLabel('Nome do pai', janela)
texto_pai.move(20, 400) 

entrada_pai = QLineEdit('', janela)
entrada_pai.setGeometry(20, 420, 200, 20)
entrada_pai.setStyleSheet('background-color:white')

texto_senha = QLabel('Crie sua senha *', janela)
texto_senha.move(20, 450) 

entrada_senha = QLineEdit('', janela)
entrada_senha.setGeometry(20, 470, 200, 20)
entrada_senha.setStyleSheet('background-color:white')

texto_confirmacao = QLabel('Confirme sua senha *', janela)
texto_confirmacao.move(230, 450) 

entrada_confirmacao = QLineEdit('', janela)
entrada_confirmacao.setGeometry(230, 470, 200, 20)
entrada_confirmacao.setStyleSheet('background-color:white')


texto_agencia = QLabel('', janela)
texto_agencia.move(230,540)

texto_conta = QLabel('', janela)
texto_conta.move(230,560)

botao = QPushButton("Criar conta", janela)
botao.setGeometry(20,540,120,40)
botao.setStyleSheet('background-color:blue; color:white')


botao.clicked.connect(validar)


janela.show()
app.exec()