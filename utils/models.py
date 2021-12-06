from django.db import models #繼承

class TimestampModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True) #建立資料的時間
    update_at = models.DateTimeField(auto_now=True) #更新資料的時間

    class Meta:
        abstract = True #設定為抽象，此model就可以被繼承
