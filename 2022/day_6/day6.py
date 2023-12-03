
class TuningTrouble():
    ## Fix malfunction communication device
    ## Lock onto signal which is a serious of seemingly random characters
    ## Start-of-packet marker is when four characters are all different
    ## Essentially, how many characters until one repeats

    def __init__(self) -> None:
        self.packet = 0
        self.signal = ''

    def process_data(self, filepath):
        with open(filepath) as f:
            self.signal = f.readline()
    
    def find_packet(self):
        ## Track the start and end of the window
        s = 0
        e = 4

        while e < len(self.signal):
            if len(set(self.signal[s:e])) == 4:
                print(f'First marker after: {e}')
                break
            s += 1
            e += 1
        return

    def main(self, filepath):
        self.process_data(filepath)
        self.find_packet()


class TuningTrouble_v2(TuningTrouble):
    def __init__(self) -> None:
        super().__init__()

    def find_message(self):
        ## Track the start and end of the window
        s = 0
        e = 14

        while e < len(self.signal):
            if len(set(self.signal[s:e])) == 14:
                print(f'First message after: {e}')
                break
            s += 1
            e += 1
        return

    def main(self, filepath):
        self.process_data(filepath)
        self.find_packet()
        self.find_message()

if __name__ == '__main__':

    
    test_file = 'test_data.txt'
    test2_file = 'test2_data.txt'
    test3_file = 'test3_data.txt'
    test4_file = 'test4_data.txt'
    real_file = 'real_data.txt'

    # v1 = TuningTrouble()
    # v1.main(real_file)

    v2 = TuningTrouble_v2()
    v2.main(real_file)
