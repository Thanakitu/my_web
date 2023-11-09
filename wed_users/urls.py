from django.urls import include, path

from wed_users import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register", view=views.register, name="register"),
    path("register/thankyou", view=views.register_thankyou, name="register_thankyou"),
    path("activate/<str:uidb64>/<str:token>", view=views.activate, name="activate"),
    path("dashboard", view=views.dashboard, name="dashboard"),
    path("profile", view=views.profile, name="profile"),
]