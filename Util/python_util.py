#-*- coding: utf-8 -*-

class python_util(object):

    def __init__(self):
        pass

    # Tuple to Dictionary
    def tuple_to_dic(self, result_tuple):
        user_vector = {}
        prev_usesr = None

        for row in result_tuple:
            cur_user = int(row.user_id)
            movie_id = int(row.movie_id)
            rating = int(row.rating)

            if (prev_usesr == None or prev_usesr != cur_user):
                uv = {}
                uv[movie_id] = rating
                user_vector[cur_user] = uv
            else:
                user_vector[cur_user][movie_id] = rating

            prev_usesr = cur_user

        return user_vector