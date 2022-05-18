from app.models import Post,User
from app import db

def setUp(self):
        self.user_Valarie = User(username = 'Valarie',password = 'potato', email = 'valarie.chelagat@student.moringaschool')
        self.new_post = Post(quotes_id=12345,quotes_author='Chiri',image_path="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeach%2F&psig=AOvVaw3nzvZvCcSayCStrkEIZz75&ust=1652903331694000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLi5wZPx6PcCFQAAAAAdAAAAABAD",quotes_post='The world is md',user = self.user_Valarie )

def tearDown(self):
        Post.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_post.quotes_id,12345)
        self.assertEquals(self.new_post.quotes_author,'Chiri')
        self.assertEquals(self.new_post.image_path,"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeach%2F&psig=AOvVaw3nzvZvCcSayCStrkEIZz75&ust=1652903331694000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLi5wZPx6PcCFQAAAAAdAAAAABAD")
        self.assertEquals(self.new_post.quotes_post,'The world is mad')
        self.assertEquals(self.new_post.user,self.user_Valarie)

def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

def test_get_post_by_id(self):

        self.new_post.save_post()
        got_post = Post.get_post(12345)
        self.assertTrue(len(got_post) == 1)