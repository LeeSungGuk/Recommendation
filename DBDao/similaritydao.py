#-*- coding: utf-8 -*-

from recommendation.DBConnection.connection import Session
from recommendation.Util.python_util import python_util


class similaritydao(object):

    session = Session()

    def __init__(self):
        self.py_util = python_util()

    def select_rating_info(self):

        result = self.session.execute('select user_id, movie_id, rating from ratings order by user_id')

        #data to change dict type.
        user_vector = self.py_util.tuple_to_dic(result)

        return user_vector

    def select_rating_info_new(self):

        result = self.session.execute('select user_id, movie_id, rating from ratings_test order by user_id')

        #data to change dict type.
        user_vector = self.py_util.tuple_to_dic(result)

        return user_vector

    def simiilarity_insert(self, user1, user2, similarity):
        self.session.execute('insert into similarity values(:user1, :user2, :similarity)'
                             , {'user1' : user1, 'user2':user2, 'similarity': similarity} )
        self.session.commit()

    def simiilarity_insert_new(self, user1, user2, similarity):
        self.session.execute('insert into similarity_ratings values(:user1, :user2, :similarity)'
                             , {'user1' : user1, 'user2':user2, 'similarity': similarity} )
        self.session.commit()

    def get_similar_users_who_rated(self, user_id, movie_id, nneighbors):

        result = self.session.execute('select r.user_id ' \
                                           ', r.rating ' \
                                           ', s.similarity ' \
                                           ', r.movie_id as movie_id ' \
                                           ', s.user_id1 '  \
                                       'from ratings r, similarity s ' \
                                      'where 1 = 1 ' \
                                        'and r.user_id = s.user_id2 ' \
                                        'and s.user_id1 = :user_id ' \
                                        'and r.movie_id = :movie_id ' \
                                      'order by s.similarity desc ' \
                                     'limit :nneighbors '
                                      , {'user_id' : user_id, 'movie_id': movie_id , 'nneighbors' : nneighbors}
                                     )
        return result

    def get_predict_movie_rating(self, user_id, movie_id):

        result = self.session.execute( 'select round(ts.rating_similarity / ts.total_similarity, 2) as predict_movie_rating ' \
                                             ', ts.movie_id ' \
                                             ', ts.user_id1 ' \
                                          'from (select sum(r.rating * s.similarity) as rating_similarity ' \
	                                                ' , sum(s.similarity) as total_similarity ' \
                                                    ', r.movie_id ' \
                                                    ', s.user_id1 ' \
                                                    'from ratings r, similarity s ' \
                                                    'where 1 = 1 ' \
                                                      'and r.user_id = s.user_id2 ' \
                                                      'and (s.user_id1 = :user_id and s.user_id1 is not null)' \
                                                      'and (r.movie_id = :movie_id  and r.movie_id is not null)' \
                                                      'order by s.similarity desc ' \
                                                      #'limit :nneighbors '  \
                                                 ') ts'
                                       , {'user_id' : user_id, 'movie_id': movie_id }
        )

        return result

    def get_similar_users_who_rated_new(self, user_id, movie_id, nneighbors):
            result = self.session.execute('select r.user_id ' \
                                          ', r.rating ' \
                                          ', s.similarity ' \
                                          ', r.movie_id as movie_id ' \
                                          ', s.user_id1 ' \
                                          'from ratings_test r, similarity_ratings s ' \
                                          'where 1 = 1 ' \
                                          'and r.user_id = s.user_id2 ' \
                                          'and s.user_id1 = :user_id ' \
                                          'and r.movie_id = :movie_id ' \
                                          'order by s.similarity desc ' \
                                          'limit :nneighbors '
                                          , {'user_id': user_id, 'movie_id': movie_id, 'nneighbors': nneighbors}
                                          )
            return result

    def get_predict_movie_rating_new(self, user_id, movie_id):
        result = self.session.execute(
                                        'select round(ts.rating_similarity / ts.total_similarity, 2) as predict_movie_rating ' \
                                                    ', ts.movie_id ' \
                                                    ', ts.user_id1 ' \
                                          'from (select sum(r.rating * s.similarity) as rating_similarity ' \
                                                            ' , sum(s.similarity) as total_similarity ' \
                                                            ', r.movie_id ' \
                                                            ', s.user_id1 ' \
                                                 'from ratings_test r, similarity_ratings s ' \
                                                'where 1 = 1 ' \
                                                 'and r.user_id = s.user_id2 ' \
                                                 'and (s.user_id1 = :user_id and s.user_id1 is not null)' \
                                                 'and (r.movie_id = :movie_id  and r.movie_id is not null)' \
                                               'order by s.similarity desc ' \
                                                # 'limit :nneighbors '  \
                                                ') ts'
                                                , {'user_id': user_id, 'movie_id': movie_id}
                                        )

        return result