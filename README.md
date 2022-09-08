# Not a Simple Blog made with Django

## Features:

- Create and list Posts (obviously)
- Share Post by email
- Add comments to a Post
- Tagging posts
- Recommending similar posts
- Total quantity, the latest and the more commented Posts
- Search Posts by text contained in Title and/or Body

There are more features coming...

## From a technical point of view

- It uses custom managers to show "published" posts
- It sends emails (to console and to a real email account)
- It uses One to Many relationships (post-comment)
- It uses Many to Many relationships (post-tags)
- It uses ORM's Annotation to list posts by tags similarity
- It uses simple_tag and inclusion_tag, to add the latest and the more commented feature
- It uses PostgreSQL text-search feature for search in multiple fields
