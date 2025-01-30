
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('admission_panel.urls')),
    path('',include('admissions.urls')),
    path('',include('blog.urls')),
    path('',include('contacts.urls')),
    path('',include('instructor_portal.urls')),
    path('',include('job_placement.urls')),
    path('',include('student_portal.urls')),
    path('',include('testimonials.urls')),
    path('',include('courses.urls'))

]
