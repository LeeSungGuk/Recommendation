#-*- coding: utf-8 -*-

from recommendation.DBConnection.connection import Session

class ratingdao(object):

    def __init__(self):
        self.session = Session()

    def get_unrated_movies(self, user_id):

        result = self.session.execute(' select movie_id '  \
                                        'from movies '     \
                                        'where 1 = 1 '  \
                                           'and movie_id not in (select m.movie_id '  \
					                                            ' from ratings r, movies m '  \
					                                             ' where 1 = 1 '  \
					                                             '   and r.movie_id = m.movie_id ' \
					                                             '   and r.user_id = :user_id)', {'user_id' : user_id}
                                      )
        return result
