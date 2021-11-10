from django.urls import path

from main.views import WorkersView, ProjectsView, WorkLogView, CreateNewLogView, EndLogView

urlpatterns = [
    path('workers/', WorkersView.as_view()),
    path('projects/', ProjectsView.as_view()),
    path('start/<int:worker_id>/<int:project_id>/', CreateNewLogView.as_view()),
    path('end/<int:worker_id>/<int:project_id>/', EndLogView.as_view()),
    path('report/', WorkLogView.as_view())
]
