from src.data_access import blogpost_repository, user_repository
from src.plugins import password_manager

from .add_blogpost import build_add_blogpost
from .edit_blogpost import build_edit_blogpost
from .list_blogposts import build_list_blogposts
from .login import build_login
from .remove_blogpost import build_remove_blogpost
from .retrieve_blogpost import build_retrieve_blogpost
from .retrieve_all_blogposts import build_retrieve_all_blogposts
from .signup import build_signup

# auth
login = build_login(user_repository, password_manager)
signup = build_signup(user_repository, password_manager)

# blogposts CRUD
add_blogpost = build_add_blogpost(blogpost_repository)
retrieve_blogpost = build_retrieve_blogpost(blogpost_repository)
retrieve_all_blogposts = build_retrieve_all_blogposts(blogpost_repository)
edit_blogpost = build_edit_blogpost(blogpost_repository)
remove_blogpost = build_remove_blogpost(blogpost_repository)

# blogposts misc
list_blogposts = build_list_blogposts(blogpost_repository, user_repository)
