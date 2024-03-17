def make_file(file_name=None, default_templete=None):
    if file_name is not None:
        with open(file_name, 'w+') as file:
            file.write(default_templete if default_templete is not None else '')
