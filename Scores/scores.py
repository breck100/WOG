import utils
from os.path import exists
def add_scores(difficulty):
    score = (difficulty*3)+5
    if (not exists(utils.SCORES_FILE_NAME)):
        f = open(utils.SCORES_FILE_NAME, 'x')
        f.close()
    f=open(utils.SCORES_FILE_NAME ,'r')
    old_score=f.readline()
    f.close()
    f=open(utils.SCORES_FILE_NAME ,'w')
    if(old_score != ''):
        score=score+int(old_score)
    f.write(str(score))
    f.close


