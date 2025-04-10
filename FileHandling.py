
class FileHandling:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        data = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    key, value = line.strip().split(": ", 1)
                    data[key] = value
        except FileNotFoundError:
            print("File Not Found")
        return data

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

    def update_field(self, field, newValue):
        data = self.read_file()
        if field in data:
            data[field] = str(newValue)
            self.write_file(data)

    def update_history(self, template, **kwargs):
        with open(self.filename, 'a') as file:
            file.write(template.format(**kwargs) + "\n")