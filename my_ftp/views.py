import json

import my_ftp.ftp_utils
import my_ftp.sftp_utils

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def connect(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        if json_data['isSFTP']:
            response = my_ftp.sftp_utils.connect(json_data)
        else:
            response = my_ftp.ftp_utils.connect(json_data)

        return JsonResponse(response)
    return HttpResponse(status=405)


@csrf_exempt
def get_dir_content(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        if json_data['isSFTP']:
            response = my_ftp.sftp_utils.get_dir_content(json_data)
        else:
            response = my_ftp.ftp_utils.get_dir_content(json_data)

        return JsonResponse(response)
    return HttpResponse(status=405)


@csrf_exempt
def download_file(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        if json_data['isSFTP']:
            filename = my_ftp.sftp_utils.download_file(json_data)
        else:
            filename = my_ftp.ftp_utils.download_file(json_data)
        return JsonResponse(filename)
    return HttpResponse(status=405)
