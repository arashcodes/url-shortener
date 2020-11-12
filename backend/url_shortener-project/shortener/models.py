from djongo import models

class Shortener(models.Model):
  url_code = models.IntegerField()
  long_url = models.CharField(max_length=100)
  short_url = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.url_code