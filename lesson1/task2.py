import os


def print_directory_contents(sPath):
    def get_directory_files(sPath):
        struct = []
        for file_or_directory in os.listdir(sPath):
            full_name = os.path.join(os.path.abspath(sPath), file_or_directory)
            if os.path.isfile(full_name):
                struct.append((os.path.abspath(sPath), file_or_directory))
            else:
                struct.extend(get_directory_files(full_name))
        return struct

    return print(get_directory_files(sPath))


print_directory_contents('C:\PycharmProjects\pythonjob\lesson1')
