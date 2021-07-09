import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A0S6Gi1jsZg3dEXpPdEgvs1J3PzhsEDG9Hr7cDrBSdpBY7sEbzXQtSZobXwIpxCC5dtCOsf39Y75iVhhEltN286zPIHQSkdyR1tKclnJWm5O-R-kkJVjYHx4dE23ISCB1cFquJY'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer :- ")
    file_to  = input("Enter the full path to upload to dropbox :-")
    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()
    
    
