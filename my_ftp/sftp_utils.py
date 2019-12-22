import pysftp
import getpass

def connect(data):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    try:
        sftp = pysftp.Connection(host=data['host'],
                                 username=data['username'], password=data['password'], cnopts=cnopts)
        sftp.close()
        return {
            'status': 'Connected successfully'
        }
    except Exception as e:
        return {
            'error': str(e)
        }


def download_file(request_data):
    sftp = None
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    try:
        sftp = pysftp.Connection(host=request_data['host'],
                                 username=request_data['username'], password=request_data['password'], cnopts=cnopts)

        current_dir = '/' if request_data['dir'] == 'root' else request_data['dir']

        sftp.chdir(current_dir)
        sftp.get(sftp.pwd + '/' + request_data['filename'], request_data['filename'])
        return request_data['filename']
    except Exception as e:
        return {
            'error': str(e)
        }
    finally:
        if sftp is not None:
            sftp.close()


def get_dir_content(request_data):
    sftp = None
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    try:
        sftp = pysftp.Connection(host=request_data['host'],
                                 username=request_data['username'], password=request_data['password'], cnopts=cnopts)

        current_dir = '/' if request_data['dir'] == '' else request_data['dir']

        sftp.chdir(current_dir)
        files_in_dir = sftp.listdir()
        files_info = build_folder_ifo(files_in_dir, sftp)
        return {'tree': files_info}
    except Exception as e:
        return {
            'error': str(e)
        }
    finally:
        if sftp is not None:
            sftp.close()


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