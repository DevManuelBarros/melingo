"""
Datos de entrada de la aplicación.
"""
 
class settingsMeli():
    def __init__(self):
        #APP ID
        self.client_id = 4638553981988438
        #Secret Key
        self.client_secret = 'tYBfpIOp61NlNOem9VulDoKR122hLYWf'
        self.redirect_uri = 'http://localhost:8000/melingo/'
        self.callbacks = 'http://localhost:8000'