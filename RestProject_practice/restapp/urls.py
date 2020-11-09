
from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home),
    path('addEmp/',v.CreateEmp.as_view()),
    path('empList/',v.EmpListView.as_view()),
    path('clEmp/',v.CreateEmpListView.as_view()),
    path('getEmp/<int:pk>/',v.GetEmp.as_view()),
    path('updateEmp/<int:pk>/',v.UpdateEmp.as_view()),
    path('deleteEmp/<int:pk>/',v.DeleteEmp.as_view()),
    path('rupdateEmp/<int:pk>/',v.RUpdateEmp.as_view()),
    path('rdeleteEmp/<int:pk>/',v.RDeleteEmp.as_view()),
    path('rudEmp/<int:pk>/',v.RUDEmp.as_view()),
    
    # ----------------- Account -----------------------
    path('addAcc/',v.CreateAcc.as_view()),
    path('accList/',v.AccListView.as_view()),
    path('alAcc/',v.CreateAccListView.as_view()),
    path('rudAcc/<int:pk>/',v.RUDAcc.as_view()),
]
