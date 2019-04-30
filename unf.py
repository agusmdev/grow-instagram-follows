"""
This template is written by @cormo1990
What does this quickstart script aim to do?
- Basic follow/unfollow activity.
NOTES:
- I don't want to automate comment and too much likes because I want to do
this only for post that I really like the content so at the moment I only
use the function follow/unfollow.
- I use two files "quickstart", one for follow and one for unfollow.
- I noticed that the most important thing is that the account from where I
get followers has similar contents to mine in order to be sure that my
content could be appreciated. After the following step, I start unfollowing
the user that don't followed me back.
- At the end I clean my account unfollowing all the users followed with
InstaPy.
"""

# imports
from instapy import InstaPy
from instapy.util import smart_run

# login credentials

insta_username = 'agusmarchi97'
insta_password = 'aweawe123aweawe123'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  bypass_suspicious_attempt=True,
                  headless_browser=True,
                  nogui=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                   # potency_ratio=-1.42,
                                    delimit_by_numbers=True,
                                   # max_followers=4590,
                                    min_followers=50,
                                    min_following=300,
                                    min_posts=6,)
                                    #max_posts=2000)

    session.set_skip_users(private_percentage=20,
                           skip_no_profile_pic=True,
                           skip_business=False)

    session.set_do_follow(enabled=True, percentage=100, times=1)
    # session.set_dont_include(["friend1", "friend2", "friend3"])
    # session.set_dont_like(["pizza", "#store"])

    # activities

    """ Massive Follow of users followers (I suggest to follow not less than
    3500/4000 users for better results)...
    """

    accs = ['giorgiopetrone', 'paeztadeo', 'santiagomonier1']
    
    #session.follow_user_followers(accs, amount=4500,
     #                             randomize=True, interact=False)

    """ First step of Unfollow action - Unfollow not follower users...
    """
    #session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
     #                      style="FIFO",
      #                     unfollow_after=12 * 60 * 60, sleep_delay=601)

    """ Second step of Massive Follow...
    """
    #session.follow_user_followers(accs, amount=4500,
     #                             randomize=False, interact=False)

    """ Second step of Unfollow action - Unfollow not follower users...
    """
    session.unfollow_users(amount=15000, InstapyFollowed=(True, "all"),
                           style="FIFO",
                           unfollow_after=0, sleep_delay=200)

    """ Clean all followed user - Unfollow all users followed by InstaPy...
    """
    # session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
    #                        style="FIFO", unfollow_after=24 * 60 * 60,
    #                        sleep_delay=601)
