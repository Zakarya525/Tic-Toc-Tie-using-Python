from random import *
class testing:
    B = ['1','2','3','4','5','6','7','8','9']
    def board(self):
        print("{} | {} | {}".format(self.B[0],self.B[1],self.B[2]))
        print("---------")
        print("{} | {} | {}".format(self.B[3],self.B[4],self.B[5]))
        print("---------")
        print("{} | {} | {}".format(self.B[6],self.B[7],self.B[8]))

    def input(self):
        one = int(input("Player 1: "))
        self.B[one-1] = 'X'
        self.board()
        if self.check():
            print("Player 1 win!")
            exit(0)
        two = int(input("Player 2: "))
        self.B[two-1] = '0'
        self.board()
        if self.check():
            print("Player 2 win!")
            exit(0)

    def check_rows(self):
        if self.B[0] == 'X' and self.B[1] == 'X' and self.B[2] == 'X' or self.B[0] == '0' and self.B[1] == '0' and self.B[2] == '0':
            return True
        if self.B[3] == 'X' and self.B[4] == 'X' and self.B[5] == 'X' or self.B[3] == '0' and self.B[4] == '0' and self.B[5] == '0':
            return True
        if self.B[6] == 'X' and self.B[7] == 'X' and self.B[8] == 'X' or self.B[6] == '0' and self.B[7] == '0' and self.B[8] == '0':
            return True
    def check_cols(self):
        if self.B[0] == 'X' and self.B[3] == 'X' and self.B[6] == 'X' or self.B[0] == '0' and self.B[3] == '0' and self.B[6] == '0':
            return True
        if self.B[1] == 'X' and self.B[4] == 'X' and self.B[7] == 'X' or self.B[1] == '0' and self.B[4] == '0' and self.B[7] == '0':
            return True
        if self.B[2] == 'X' and self.B[5] == 'X' and self.B[8] == 'X' or self.B[2] == '0' and self.B[5] == '0' and self.B[8] == '0':
            return True
    def check_diag(self):
        if self.B[0] == 'X' and self.B[4] == 'X' and self.B[8] == 'X' or self.B[0] == '0' and self.B[4] == '0' and self.B[8] == '0':
            return True
        if self.B[2] == 'X' and self.B[4] == 'X' and self.B[6] == 'X' or self.B[2] == '0' and self.B[4] == '0' and self.B[6] == '0':
            return True
    def check(self):
        if self.check_rows():
            return True
        if self.check_cols():
            return True
        if self.check_diag():
            return True
