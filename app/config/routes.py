
from system.core.router import routes

routes['default_controller'] = 'BlackBelts'
routes['POST']['/process'] = 'BlackBelts#process'
routes['GET']['/friends'] = 'BlackBelts#friends'
routes['GET']['/user/<user_id>'] = 'BlackBelts#user'
routes['GET']['/friend/<user_id>'] = 'BlackBelts#friend'
routes['GET']['/unfriend/<user_id>'] = 'BlackBelts#unfriend'
routes['GET']['/logout'] = 'BlackBelts#logout'
