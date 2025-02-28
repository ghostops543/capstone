


class prepatient:
    def __init__(self, scores):
        self.scores_list = scores
        self.A1_Score = scores[0]
        self.A2_Score = scores[1]
        self.A3_Score = scores[2]
        self.A4_Score = scores[3]
        self.A5_Score = scores[4]
        self.A6_Score = scores[5]
        self.A7_Score = scores[6]
        self.A8_Score = scores[7]
        self.A9_Score = scores[8]
        self.A10_Score = scores[9]
        self.total = sum(scores)


    def __str__(self):
            return " %s" % (self.scores_list)
scores = [0,0,0,0,0,0,0,0,0,0]
def insert_scores(answer, index):
        scores[index-1] = binarify(answer, index)

def binarify(answer, index):
    if answer == 0 :
        if index == 1 or index == 7 or index == 8 or index == 10:
            return 1
        else:
            return 0
    elif answer == 1 :
        if index == 2 or index == 3 or index == 4 or index == 5 or index == 6 or index == 9:
            return 1
        else:
            return 0







