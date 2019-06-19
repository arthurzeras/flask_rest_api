# -*- coding: utf-8 -*-

from app.users.resources import SignUp
from flask_restful import Api, Resource
from app.users.resources_admin import AdminUserPageList, AdminUserResource

class Index(Resource):
  def get(self):
    return {'hello': 'world by apps'}

api = Api()


def configure_api(app):
  api.add_resource(Index, '/')

  # rotas para o endpoint de usuarios
  api.add_resource(SignUp, '/users')

  # rotas para os admins
  api.add_resource(AdminUserResource, '/admin/users/<string:user_id>')
  api.add_resource(AdminUserPageList, '/admin/users/page/<int:page_id>')

  # inicializamos a api com as configurações do flask vinda por parâmetro
  api.init_app(app)