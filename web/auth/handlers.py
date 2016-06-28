from web.auth import views

handlers = [
    (r'/auth/signin', views.sigin),
    (r'/auth/signup', views.sigout),
    (r'/auth/logout', views.logout),
]