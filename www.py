from application import app
from web.controller.index import route_index
from web.controller.user.User import route_user
from web.controller.static import route_static
from web.controller.account.Account import route_account
from web.controller.finance.Finance import route_finance
from web.controller.food.Food import route_food
from web.controller.member.Member import route_member
from web.controller.stat.Stat import route_stat


app.register_blueprint(route_index,url_prefix="/")
app.register_blueprint(route_user,url_prefix="/user")
app.register_blueprint(route_account,url_prefix="/account")
app.register_blueprint(route_finance,url_prefix="/finance")
app.register_blueprint(route_food,url_prefix="/food")
app.register_blueprint(route_member,url_prefix="/member")
app.register_blueprint(route_stat,url_prefix="/stat")
#不设置为static的话application中static_folder不需要设置为None
app.register_blueprint(route_static,url_prefix="/static")


