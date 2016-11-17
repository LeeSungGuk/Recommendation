#-*- coding: utf-8 -*-

import pickle

from recommendation.DBDao.similaritydao import similaritydao
from recommendation.DBDao.ratingdao import ratingdao
from recommendation.DBConnection.connection import r


class predict_rating(object):

    def __init__(self):
        self.rdao = ratingdao()
        self.sdao = similaritydao()

    def get_unrated_movies(self, user_id ):

        try:
            unrated_movies = self.rdao.get_unrated_movies(user_id)

        except Exception as e:
            print(e)

        return unrated_movies

    def get_unrated_movies_new(self, user_id ):

        try:
            unrated_movies = self.rdao.get_unrated_movies_new(user_id)

        except Exception as e:
            print(e)

        return unrated_movies

    def get_predict_rating(self, user_id):
        unrated_movies = self.get_unrated_movies_new(user_id)

        for unrated_movies_row in unrated_movies:
            try:
                predicted_rating = self.sdao.get_predict_movie_rating_new(user_id, int(unrated_movies_row.movie_id))

                #similar_user_tuple = self.sdao.get_similar_users_who_rated(user_id, unrated_movies_row.movie_id, 10)
                #similar_user_id = np.array( sorted( suser_id for suser_id in similar_user_tuple))
                #print(predicted_rating)

            except Exception as e:
                print(e)

            for row in predicted_rating :
                if( row.predict_movie_rating != None):
                    print('User id :{1}  -> Movie ID: {0}  predicted rating ? : {2}'.format( \
                                    int(row.movie_id), int(row.user_id1), row.predict_movie_rating \
                                    )
                        )

    def get_predict_rating_new(self, user_id):
        unrated_movies = self.get_unrated_movies_new(user_id)

        for unrated_movies_row in unrated_movies:
            try:
                predicted_rating = self.sdao.get_predict_movie_rating_new(user_id, int(unrated_movies_row.movie_id))

            except Exception as e:
                print(e)

            for row in predicted_rating:
                if (row.predict_movie_rating != None):
                    print('User id :{1}  -> Movie ID: {0}  predicted rating ? : {2}'.format( \
                        int(row.movie_id), int(row.user_id1), row.predict_movie_rating \
                        )
                    )
                # Redis memory insert data.
                self.insert_redis(row)

    def insert_redis(self, dic_data):

        bdic_data = pickle.dumps(dic_data)

        r.set('predict', bdic_data)

    def get_predict_rating_web(self, user_id):
        data = []
        unrated_movies = self.get_unrated_movies(user_id)

        for unrated_movies_row in unrated_movies:
            try:
                predicted_rating = self.sdao.get_predict_movie_rating(user_id, int(unrated_movies_row.movie_id))

            except Exception as e:
                print(e)

            for row in predicted_rating :
                if( row.predict_movie_rating != None):
                    print('User id :{1}  -> Movie ID: {0}  predicted rating ? : {2}'.format( \
                        int(row.movie_id), int(row.user_id1), row.predict_movie_rating \
                        )
                    )
                    predict = {}
                    predict['movie_id'] = int(row.movie_id)
                    predict['user_id'] = int(row.user_id1)
                    predict['predict_movie_rating'] = row.predict_movie_rating

                    data.append(predict)
        return data


if __name__ == '__main__':
    sbs = predict_rating()
    sbs.get_predict_rating_new(1)
