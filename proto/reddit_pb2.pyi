from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL: _ClassVar[PostStatus]
    LOCKED: _ClassVar[PostStatus]
    HIDDEN: _ClassVar[PostStatus]

class CommentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL_COMMENT: _ClassVar[CommentStatus]
    HIDDEN_COMMENT: _ClassVar[CommentStatus]

class SubredditStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL_SUBREDDIT: _ClassVar[SubredditStatus]
    LOCKED_SUBREDDIT: _ClassVar[SubredditStatus]
    HIDDEN_SUBREDDIT: _ClassVar[SubredditStatus]
NORMAL: PostStatus
LOCKED: PostStatus
HIDDEN: PostStatus
NORMAL_COMMENT: CommentStatus
HIDDEN_COMMENT: CommentStatus
NORMAL_SUBREDDIT: SubredditStatus
LOCKED_SUBREDDIT: SubredditStatus
HIDDEN_SUBREDDIT: SubredditStatus

class User(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("post_id", "title", "text", "video_url", "image_url", "author", "score", "status", "publication_date")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    title: str
    text: str
    video_url: str
    image_url: str
    author: User
    score: int
    status: PostStatus
    publication_date: str
    def __init__(self, post_id: _Optional[int] = ..., title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., status: _Optional[_Union[PostStatus, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("comment_id", "parent_post_id", "parent_comment_id", "author", "text", "score", "status", "publication_date")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    parent_post_id: int
    parent_comment_id: int
    author: User
    text: str
    score: int
    status: CommentStatus
    publication_date: str
    def __init__(self, comment_id: _Optional[int] = ..., parent_post_id: _Optional[int] = ..., parent_comment_id: _Optional[int] = ..., author: _Optional[_Union[User, _Mapping]] = ..., text: _Optional[str] = ..., score: _Optional[int] = ..., status: _Optional[_Union[CommentStatus, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Subreddit(_message.Message):
    __slots__ = ("name", "status", "tags")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: SubredditStatus
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[SubredditStatus, str]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class SubredditRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ("success", "post_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    post_id: int
    def __init__(self, success: bool = ..., post_id: _Optional[int] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ("post_id", "user", "is_upvote")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    IS_UPVOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    user: User
    is_upvote: bool
    def __init__(self, post_id: _Optional[int] = ..., user: _Optional[_Union[User, _Mapping]] = ..., is_upvote: bool = ...) -> None: ...

class VotePostResponse(_message.Message):
    __slots__ = ("success", "new_score")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    NEW_SCORE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    new_score: int
    def __init__(self, success: bool = ..., new_score: _Optional[int] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ("comment_id", "user", "is_upvote")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    IS_UPVOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    user: User
    is_upvote: bool
    def __init__(self, comment_id: _Optional[str] = ..., user: _Optional[_Union[User, _Mapping]] = ..., is_upvote: bool = ...) -> None: ...

class VoteCommentResponse(_message.Message):
    __slots__ = ("success", "new_score")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    NEW_SCORE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    new_score: int
    def __init__(self, success: bool = ..., new_score: _Optional[int] = ...) -> None: ...

class RetrievePostContentRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class RetrievePostContentResponse(_message.Message):
    __slots__ = ("success", "post")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    success: bool
    post: Post
    def __init__(self, success: bool = ..., post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class CreateCommentResponse(_message.Message):
    __slots__ = ("success", "id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    id: int
    def __init__(self, success: bool = ..., id: _Optional[int] = ...) -> None: ...

class TopCommentsRequest(_message.Message):
    __slots__ = ("post_id", "limit")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    limit: int
    def __init__(self, post_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class SubCommentDetails(_message.Message):
    __slots__ = ("comment", "has_replies")
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    has_replies: bool
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ..., has_replies: bool = ...) -> None: ...

class TopCommentsResponse(_message.Message):
    __slots__ = ("comments",)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[SubCommentDetails]
    def __init__(self, comments: _Optional[_Iterable[_Union[SubCommentDetails, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ("comment_id", "limit")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    limit: int
    def __init__(self, comment_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class CommentBranch(_message.Message):
    __slots__ = ("parent_comment", "sub_comments")
    PARENT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    SUB_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    parent_comment: Comment
    sub_comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, parent_comment: _Optional[_Union[Comment, _Mapping]] = ..., sub_comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchResponse(_message.Message):
    __slots__ = ("branches",)
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedCompositeFieldContainer[CommentBranch]
    def __init__(self, branches: _Optional[_Iterable[_Union[CommentBranch, _Mapping]]] = ...) -> None: ...

class MonitorUpdatesRequest(_message.Message):
    __slots__ = ("post_id", "comment_ids")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    comment_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, post_id: _Optional[str] = ..., comment_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class MonitorUpdatesResponse(_message.Message):
    __slots__ = ("post_update", "comment_update")
    POST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    post_update: Post
    comment_update: Comment
    def __init__(self, post_update: _Optional[_Union[Post, _Mapping]] = ..., comment_update: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...
