import webbrowser as web

class Browser:
    def openPage(self, site = '', search = ''):

        site.upper()

        if site == 'GOOGLE' and search != '':
            web.open("https://www.google.com/search?q={}".format(search))
        elif site == 'GOOGLE':
            web.open("https://www.google.com/")
        elif site == 'FACEBOOK':
            web.open("https://www.facebook.com/")
        elif site == 'INSTAGRAM':
            web.open("https://www.instagram.com/")
        elif site == 'GITHUB':
            web.open("https://github.com/")
        elif site == 'LINKEDIN':
            web.open("https://www.linkedin.com/")

        return True
    
    def controllers(self, command=''):
         
        commadUpper = command.upper()

        try:
            
            if 'GOOGLE' and 'PESQUISAR' in commadUpper:
                 self.openPage('GOOGLE', command) 

            elif 'GOOGLE' in commadUpper:
                 self.openPage('GOOGLE')
            
            elif 'FACEBOOK' in commadUpper:
                 self.openPage('FACEBOOK')

            elif 'GITHUB' in commadUpper:
                 self.openPage('GITHUB')
            
            elif 'LINKEDIN' in commadUpper:
                 self.openPage('LINKEDIN')
            
            elif 'INSTAGRAM' in commadUpper:
                 self.openPage('INSTAGRAM')

            elif 'DESLIGAR' and 'KURAMA' in commadUpper:
                print('Encerrando...')
                return False

        except Exception as error:
            raise error