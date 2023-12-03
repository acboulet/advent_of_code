class PerLineImport():
    def __init__(self, datafile) -> None:
        self.datafile = datafile

    
    def import_file(self):
        with open(self.datafile, 'r') as file:
            for line in file:
                self.process_lines(line)

    def process_lines(self, line):
        print(line.rstrip())
