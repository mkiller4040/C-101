from os import access
import dropbox

class DataTransfer :
    def __init__(self, accessToken) :
        self.accessToken = accessToken
        
    def fileUpload(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)
         
    
def main() :
    accessToken = 'FCoVhfvWQ00AAAAAAAAAAcDawNs_Rv_RolYenGTGxZSipCXMSsLJZcDQBg1CXLg-'
    transferObj = DataTransfer(accessToken)
    filefrom = 'C:/Users/monit/OneDrive/Documents/cookie_clicker.txt'
    fileto = "/cookie_clicker_save.txt"
    transferObj.fileUpload(filefrom, fileto)
    print("File Has Been Uploaded")


main()