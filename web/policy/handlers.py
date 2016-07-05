from web.policy import views
handlers = [
    (r'/policy/rule', views.Rule),
    (r'/policy/rule/(?P<rule_id>\d+)',views.Rule),
    (r'/policy/rule/create',views.RuleCreate),
    (r'/policy/strategy', views.Rule),
]

