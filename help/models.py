from django.db import models


class HelpPage(models.Model):
    header = models.CharField(max_length=50,
                              verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    url_tag = models.CharField(max_length=20,
                               unique=True,
                               blank=True,
                               verbose_name="URL тег адреса",)

    def save(self, *args, **kwargs):
        """
        Добавляет перед url_tag символ "/", если его нет.
        Убирает символ "/" в конце url_tag, если он есть.
        """
        if len(self.url_tag) == 0 or self.url_tag[0] != '/':
            self.url_tag = '/' + self.url_tag
        if len(self.url_tag) >= 2 and self.url_tag[-1] == '/':
            self.url_tag = self.url_tag[:-1]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Помощь"
        verbose_name_plural = 'Помощь'
