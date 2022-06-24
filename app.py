import time
from PyQt5 import QtWidgets
from layout.tela import Ui_MainWindow
from functions.enviarEmail import EnviarEmail

class Tela(QtWidgets.QMainWindow):

    def __init__(self, *args, **argvs):
        super(Tela, self).__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.listGlobals = []
        self.ui.pushButton.clicked.connect(self.get_dados)
        self.ui.pushButton_2.clicked.connect(self.get_arquivo)
        self.ui.pushButton_3.clicked.connect(self.get_arquivo_extra)

    def get_dados(self, ):
        email = self.ui.lineEdit_2.text()
        senha = self.ui.lineEdit_3.text()
        arquivo = self.ui.lineEdit.text()
        assunto = self.ui.lineEdit_4.text()
        corpo_Email = self.ui.textEdit.toPlainText()
        corpo_Email_massa = self.ui.lineEdit_6.text()

        if not email or not senha:
            QtWidgets.QMessageBox.warning( self, 'Atenção', 'Informe o email.')

        if corpo_Email_massa:
            self.dados_extras(arquivo=corpo_Email_massa)

        if not arquivo:
            QtWidgets.QMessageBox.warning( self, 'Atenção', 'Informe o caminho do arquivo.')
            return


        with open(f"{arquivo}")as file:
            for i, j in zip(file, self.listGlobals):
                i = i.replace('\n', '')
                i = i.replace('\t', '')
                corpo_E = '{}\n{}'.format(corpo_Email,j)
                enviar = EnviarEmail()
                env = enviar.enviaremail(emaildest=i, assunto=assunto, remetente=email, senha=senha, corpo_Email=corpo_E)
                time.sleep(0.5)
                if env != True:
                    QtWidgets.QMessageBox.information( self, 'Atenção', 'email não enviado.\n{}'.format(env))

        QtWidgets.QMessageBox.information( self, 'Atenção', 'Processo finalizado.')
    def get_arquivo(self, ):
        try:

            salvar = QtWidgets.QFileDialog.getOpenFileName()[0]
            if salvar == '':
                return
            if not '.txt' in salvar:
                QtWidgets.QMessageBox.warning(
                    self, 'Atenção', 'Extenção não aceita. \n{}'.format(salvar))
                return

            self.ui.lineEdit.setText(salvar)
            
        except Exception as erro:
            QtWidgets.QMessageBox.information(self, 'Erro', '{}'.format(erro))
            return

    def get_arquivo_extra(self,):
        try:

            salvar = QtWidgets.QFileDialog.getOpenFileName()[0]
            if salvar == '':
                return
            if not '.txt' in salvar:
                QtWidgets.QMessageBox.warning(
                    self, 'Atenção', 'Extenção não aceita. \n{}'.format(salvar))
                return

          
            self.ui.lineEdit_6.setText(salvar)
            
        except Exception as erro:
            QtWidgets.QMessageBox.information(self, 'Erro', '{}'.format(erro))
            return

    def dados_extras(self, arquivo):

        self.listGlobals = []
        with open(f"{arquivo}")as file:
            for linha in file:
                linha = linha.replace('\n', ' ')
                linha = linha.replace('\t', ' ')
                self.listGlobals.append(linha)

if __name__ == "__main__":
    import logging
    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
    logging.basicConfig(filename='evidences.log',filemode='w', level=logging.INFO, format=log_format, encoding='UTF-8')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    tela = Tela()
    tela.show()
    sys.exit(app.exec_())
