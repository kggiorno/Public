from database import Database 
from models.post import Post 
from models.blog import Blog

Database.initialize() 

blog = Blog(author="Sample Author",
			title="KGG's Blog",
			description="Sample description")

blog.new_post()

blog.save_to_db()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())

