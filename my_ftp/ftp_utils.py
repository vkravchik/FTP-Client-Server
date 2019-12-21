from ftplib import FTP
import getpass

def connect(data):
    try:
        ftp = FTP()
        ftp.connect(data['host'])
        ftp.login(data['username'], data['password'])

        return {
            'status': 'Connected Success'
        }
    except Exception as e:
        return {
            str(e)
        }


def download_file(data):
    try:
        ftp = FTP()
        ftp.connect(data['host'])
        ftp.login(data['username'], data['password'])

        ftp.cwd(data['dir'])

        user = getpass.getuser()
        out = "C:\\Users\\" + user + "\\Downloads\\" + data['filename']

        with open(out, 'wb') as f:
            ftp.retrbinary('RETR ' + data['filename'], f.write)

        return {
            'status': 'Download success'
        }
    except Exception as e:
        return {
            str(e)
        }


def get_dir_content(request_data):
    ftp = FTP()
    try:
        ftp.connect(request_data['host'])
        ftp.login(request_data['username'], request_data['password'])

        current_dir = '/' if request_data['dir'] == '' else request_data['dir']

        if current_dir != '/':
            ftp.cwd(current_dir)

        files_in_dir = ftp.nlst()
        files_info = build_folder_ifo(files_in_dir, ftp)
        return {'tree': files_info}
    except Exception as e:
        return {
            'error': str(e)
        }
    finally:
        ftp.quit()


def build_folder_ifo(files, ftp):
    info = []
    for file in files:
        if ftp.nlst(file) == [file]:
            info.append({
                'name': file,
                'type': 'file'
            })
        else:
            info.append({
                'name': file,
                'type': 'folder'
            })
    return info