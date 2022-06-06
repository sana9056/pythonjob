def get_file_name(path):
    return path.split('/')[-1].split('.')[0]


print(get_file_name('/var/logs/nginx/error.log'))
