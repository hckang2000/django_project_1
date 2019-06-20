from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name = '제목')
    contents = models.TextField(verbose_name = '내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE # 일대다 매칭을 의미하는 필드. 사용자가 탈퇴하면 작성했던 글들을 모두 삭제한다는 의미, foreignkey 는 1대 n 의 관계를 의미함. 
    , verbose_name = '작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name="태그") #다대다 매칭을 의미하는 필드
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'