from web.auth import views

handlers = [
    (r'/auth/signin', views.signin),
    (r'/auth/signup', views.signup),
    (r'/auth/logout', views.logout),
]