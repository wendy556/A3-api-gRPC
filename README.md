## API gRPC

#### 0 Github Repo Link

https://github.com/wendy556/A3-api-gRPC

---

#### 1 Protobuf Buffer Definition

**Important: I did the EXTRA CREDIT for data model - Subreddit (5 pt)**

##### 1.1 User

| Name    | Type   | Description                    |
| ------- | ------ | ------------------------------ |
| user_id | string | Unique identifier for the user |

##### 1.2 Post

| Name             | Type       | Description                                                  |
| ---------------- | ---------- | ------------------------------------------------------------ |
| post_id          | int64      | Unique identifier for the post                               |
| title            | string     | Title of the post                                            |
| text             | string     | Text content of the post                                     |
| video_url        | string     | URL of the video associated with the post (if media is video) |
| image_url        | string     | URL of the image associated with the post (if media is image) |
| author           | User       | The user who authored the post                               |
| score            | int64      | Score or votes of the post                                   |
| status           | PostStatus | Status of the post (e.g., NORMAL, LOCKED, HIDDEN)            |
| publication_date | string     | Timestamp of when the post was published (as a string)       |

##### 1.3 Comment

| Name              | Type          | Description                                                  |
| ----------------- | ------------- | ------------------------------------------------------------ |
| comment_id        | int64         | Unique identifier for the comment                            |
| parent_post_id    | int64         | Identifier of the parent post                                |
| parent_comment_id | int64         | Identifier of the parent comment (if this is a nested comment) |
| author            | User          | The user who authored the comment                            |
| text              | string        | Text content of the comment                                  |
| score             | int64         | Score or votes of the comment                                |
| status            | CommentStatus | Status of the comment (e.g., NORMAL_COMMENT, HIDDEN_COMMENT) |
| publication_date  | string        | Timestamp of when the comment was published (as a string)    |

##### 1.4 Subreddit

| Name   | Type            | Description                                              |
| ------ | --------------- | -------------------------------------------------------- |
| name   | string          | Human-readable name of the subreddit                     |
| status | SubredditStatus | Indicates if the subreddit is public, private, or hidden |
| tags   | string repeated | Set of tags associated with the subreddit                |

##### 1.5 CreateRequest

| Name | Type | Description                             |
| ---- | ---- | --------------------------------------- |
| post | Post | The post to be created (optional field) |

##### 1.6 CreatePostResponse

| Name    | Type  | Description                                |
| ------- | ----- | ------------------------------------------ |
| success | bool  | Whether the post creation was successful   |
| post_id | int64 | The unique identifier for the created post |

##### 1.7 VotePostRequest

| Name      | Type  | Description                                       |
| --------- | ----- | ------------------------------------------------- |
| post_id   | int64 | The unique identifier for the post to be voted on |
| user      | User  | The user who is voting                            |
| is_upvote | bool  | True for upvote, false for downvote               |

##### 1.8 VotePostResponse

| Name      | Type  | Description                              |
| --------- | ----- | ---------------------------------------- |
| success   | bool  | Whether the vote was successful          |
| new_score | int64 | The new score of the post after the vote |

##### 1.9 SubredditRequest

| Name | Type   | Description                               |
| ---- | ------ | ----------------------------------------- |
| name | string | The name of the subreddit being requested |

##### 1.10 VoteCommentRequest

| Name       | Type   | Description                          |
| ---------- | ------ | ------------------------------------ |
| comment_id | string | Identifier of the comment to vote on |
| user       | User   | The user who is voting               |
| is_upvote  | bool   | True for upvote, false for downvote  |

##### 1.11 VoteCommentResponse

| Name      | Type  | Description                                 |
| --------- | ----- | ------------------------------------------- |
| success   | bool  | Whether the vote operation was successful   |
| new_score | int32 | The new score of the comment after the vote |

##### 1.12 RetrievePostContentRequest

| Name    | Type   | Description                                    |
| ------- | ------ | ---------------------------------------------- |
| post_id | string | Identifier of the post to retrieve content for |

##### 1.13 RetrievePostContentResponse

| Name    | Type | Description                                  |
| ------- | ---- | -------------------------------------------- |
| success | bool | Whether the content retrieval was successful |
| post    | Post | The content of the post                      |

##### 1.14 CreateCommentRequest

| Name    | Type    | Description                    |
| ------- | ------- | ------------------------------ |
| comment | Comment | The comment data to be created |

##### 1.15 CreateCommentResponse

| Name    | Type  | Description                                 |
| ------- | ----- | ------------------------------------------- |
| success | bool  | Whether the comment creation was successful |
| id      | int64 | The identifier of the newly created comment |

##### 1.16 TopCommentsRequest

| Name    | Type   | Description                                            |
| ------- | ------ | ------------------------------------------------------ |
| post_id | string | The ID of the post to retrieve top comments for        |
| limit   | int32  | The maximum number of top comments to be retrieved (N) |

##### 1.17 SubCommentDetails

| Name        | Type    | Description                                               |
| ----------- | ------- | --------------------------------------------------------- |
| comment     | Comment | Details of the comment                                    |
| has_replies | bool    | Indicates whether the comment has replies (true or false) |

##### 1.18 TopCommentsResponse

| Name     | Type                | Description                                   |
| -------- | ------------------- | --------------------------------------------- |
| comments | SubCommentDetails[] | List of details for the most popular comments |

##### 1.19 ExpandCommentBranchRequest

| Name       | Type   | Description                                                  |
| ---------- | ------ | ------------------------------------------------------------ |
| comment_id | string | The ID of the comment to expand                              |
| limit      | int32  | The maximum number of top comments to retrieve for each branch (N) |

##### 1.20 CommentBranch

| Name           | Type      | Description                                   |
| -------------- | --------- | --------------------------------------------- |
| parent_comment | Comment   | The parent comment                            |
| sub_comments   | Comment[] | List of sub-comments under the parent comment |

##### 1.21 ExpandCommentBranchResponse

| Name     | Type            | Description                                      |
| -------- | --------------- | ------------------------------------------------ |
| branches | CommentBranch[] | List of comment branches with their sub-comments |

##### 1.22 MonitorUpdatesRequest

| Name        | Type            | Description                                               |
| ----------- | --------------- | --------------------------------------------------------- |
| post_id     | string          | The ID of the post to monitor                             |
| comment_ids | string repeated | List of comment IDs to monitor, can be added continuously |

##### 1.23 MonitorUpdatesResponse

| Name           | Type    | Description                           |
| -------------- | ------- | ------------------------------------- |
| post_update    | Post    | Contains score update for the post    |
| comment_update | Comment | Contains score update for the comment |

---

#### 2 Service Definitions

**Important: I did the EXTRA CREDIT for service definitions - Moniter Updates (5 pt)**

##### 2.1 CreatePost

| Input         | Output             | Description                                     |
| ------------- | ------------------ | ----------------------------------------------- |
| CreateRequest | CreatePostResponse | Creates a new post and returns the created post |

##### 2.2 VotePost

| Input           | Output           | Description                                         |
| --------------- | ---------------- | --------------------------------------------------- |
| VotePostRequest | VotePostResponse | Submits a vote for a post and returns the new score |

##### 2.3 RetrievePostContent

| Input                      | Output                      | Description                     |
| -------------------------- | --------------------------- | ------------------------------- |
| RetrievePostContentRequest | RetrievePostContentResponse | Retrieves the content of a post |

##### 2.4 CreateComment

| Input                | Output                | Description                                           |
| -------------------- | --------------------- | ----------------------------------------------------- |
| CreateCommentRequest | CreateCommentResponse | Creates a new comment and returns the created comment |

##### 2.5 VoteComment

| Input              | Output              | Description                                            |
| ------------------ | ------------------- | ------------------------------------------------------ |
| VoteCommentRequest | VoteCommentResponse | Submits a vote for a comment and returns the new score |

##### 2.6 GetTopComments

| Input              | Output              | Description                                                  |
| ------------------ | ------------------- | ------------------------------------------------------------ |
| TopCommentsRequest | TopCommentsResponse | Retrieves a list of the top N most upvoted comments under a specific post |

##### 2.7 ExpandCommentBranch

| Input                      | Output                      | Description                                                  |
| -------------------------- | --------------------------- | ------------------------------------------------------------ |
| ExpandCommentBranchRequest | ExpandCommentBranchResponse | Expands a comment branch to show the top N most upvoted comments and their respective top N child comments |

##### 2.8 MonitorUpdates

| Input                          | Output                          | Description                                                  |
| ------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| MonitorUpdatesRequest (stream) | MonitorUpdatesResponse (stream) | Initiates a stream where the client can monitor score updates for a post and its comments in real-time |

##### 2.9 CreateSubreddit

| Input     | Output    | Description                            |
| --------- | --------- | -------------------------------------- |
| Subreddit | Subreddit | Creates a new subreddit and returns it |

##### 2.10 GetSubredditInfo

| Input            | Output    | Description                             |
| ---------------- | --------- | --------------------------------------- |
| SubredditRequest | Subreddit | Retrieves information about a subreddit |

#### 3 Storage Backend

Note: A one paragraph writeup on the storage backend being used.



---

#### 4 Github Link

* Server Class:
* Client Class:

---

#### 5 Test

Note: Links to the implementation of the high level function and its test

---

#### 6 Extra Credit

* Data model - Subreddit (**5 pt**), I did in Protobuf Buffer Definition
* Service design - Moniter Updates (**5 pt**), I did it in Service Definitions