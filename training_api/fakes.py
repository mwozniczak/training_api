from random import randint, choice

from polyfactory.factories.pydantic_factory import ModelFactory

from .models import *

class UserFactory(ModelFactory[User]):
    @classmethod
    def email(cls) -> str:
        return cls.__faker__.email()
    
    @classmethod
    def user_name(cls) -> str:
        return cls.__faker__.user_name()
    
    @classmethod
    def full_name(cls) -> str:
        return cls.__faker__.name()
    
    @classmethod
    def recent_comments(cls) -> list[str]:
        count = cls.__random__.randint(1, 5)
        return [
            f"/comment/{cls.__faker__.uuid4()}"
            for _ in range(count)
        ]

class PostFactory(ModelFactory[Post]):
    @classmethod
    def post_uri(cls) -> str:
        return f"/posts/{cls.__faker__.slug()}"

    @classmethod
    def title(cls) -> str:
        return cls.__faker__.paragraph(1)
    
    @classmethod
    def body(cls) -> str:
        return "\n\n".join(cls.__faker__.paragraphs(20))

class CommentFactory(ModelFactory[Comment]):
    @classmethod
    def comment_id(cls) -> str:
        return cls.__faker__.uuid4()
    
    @classmethod
    def comment(cls) -> str:
        return "\n\n".join(
            cls.__faker__.paragraphs(nb=cls.__random__.randint(1,5))
        )

class NewPostNotificationFactory(ModelFactory[NewPostNotification]):
    @classmethod
    def post_uri(cls):
        return PostFactory.post_uri()


class CommentLikeNotificationFactory(ModelFactory[CommentLikeNotification]):
    @classmethod
    def comment_id(cls) -> str:
        return CommentFactory.comment_id()


class PostLikeNotificationFactory(ModelFactory[PostLikeNotification]):
    @classmethod
    def post_uri(cls):
        return PostFactory.post_uri()

class RecentNotificationFactory(ModelFactory[RecentNotifications]):
    @classmethod
    def items(cls) -> list:
        return [
            choice(
                (NewPostNotificationFactory, CommentLikeNotificationFactory, PostLikeNotificationFactory)
            ).build()
            for _ in range(randint(5, 20))
        ]