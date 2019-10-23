from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = "Make Money"
    site_title = "Make Money Every Day"


admin_site = MyAdminSite()
