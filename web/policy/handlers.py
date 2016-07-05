from web.policy import views
handlers = [
    (r'/policy/rule', views.Rule),
    (r'/policy/rule/create',views.RuleCreate),
    (r'/policy/strategy', views.Rule),
]

