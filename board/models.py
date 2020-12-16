from django.db import models
from order.models import *
from product.models import *
from user.models import *

class Board(models.Model):
    uploader        = models.CharField(max_length=45)
    created_at      = models.DateTimeField(
                        auto_now = True,
                        )
    content         = models.CharField(max_length=45)
    theme           = models.CharField(max_length=45)
    class Meta:
        db_table = "boards"

class BoardImage(models.Model):
    board_id    = models.ForeignKey(
                    'Board',
                    on_delete = models.CASCADE
                    )
    image_url   = models.CharField(max_length=2000)
    class Meta:
        db_table = "boardimages"

class BoardLike(models.Model):
    member_id = models.ForeignKey('user.Member',on_delete  = models.CASCADE)
    is_like   = models.BooleanField()
    board_id  = models.ForeignKey('Board',on_delete  = models.CASCADE)
    class Meta:
        db_table = "boardlikes"

class Comment(models.Model):
    content     = models.CharField(max_length=500)
    created_at  = models.DateTimeField(
                    auto_now = True,
                    )
    board_id    = models.ForeignKey(
                    'Board',
                    on_delete = models.CASCADE
                    )
    comment_id  = models.ForeignKey(
                    'self',
                    on_delete = models.CASCADE
                    )
    class Meta:
        db_table = "comments"

class CommentLike(models.Model):
    comment_id = models.ForeignKey('Comment',on_delete  = models.CASCADE)
    member_id = models.ForeignKey('user.Member',on_delete  = models.CASCADE)
    is_like = models.BooleanField()
    class Meta:
        db_table = "commentlikes"

