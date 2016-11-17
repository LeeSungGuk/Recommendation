# -*- coding: utf-8 -*-

from recommendation.DBDao.similaritydao import similaritydao
from recommendation.Util.similarity_function import similarity_function

class BatchSimilarity(object):

    def __init__(self):
        self.sdao = similaritydao()
        self.sf = similarity_function()

    def make_dict(self):
        user_vector = self.sdao.select_rating_info_new()
        user_ids = user_vector.keys()

        for user_id1 in user_ids:
            for user_id2 in user_ids:
                if(user_id1 == user_id2): continue

                uv1 = user_vector[user_id1]
                uv2 = user_vector[user_id2]

                similarity = self.sf.consie(uv1, uv2)

                if(similarity != 0):
                    print(user_id1, user_id2, similarity)
                    #self.sdao.simiilarity_insert(user_id1, user_id2, similarity)
                    self.sdao.simiilarity_insert_new(user_id1, user_id2, similarity)

if __name__ == '__main__':
    sbs = BatchSimilarity()
    sbs.make_dict()