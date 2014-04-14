"""
    This test will use the default permissions found in
    flaskbb.utils.populate
"""
from flaskbb.utils.permissions import *


def test_moderator_permissions_in_forum(
        forum, moderator_user, topic, topic_moderator):
    """Test the moderator permissions in a forum where the user is a
    moderator.
    """

    moderator_user.permissions = moderator_user.get_permissions()

    assert moderator_user in forum.moderators

    assert can_post_reply(moderator_user, forum)
    assert can_post_topic(moderator_user, forum)
    assert can_edit_post(moderator_user, topic.user_id, forum)

    assert can_moderate(moderator_user, forum)
    assert can_delete_post(moderator_user, topic.user_id, forum)
    assert can_delete_topic(moderator_user, topic.user_id, forum)

    assert can_lock_topic(moderator_user, forum)
    assert can_merge_topic(moderator_user, forum)
    assert can_move_topic(moderator_user, forum)


def test_moderator_permissions_without_forum(
        forum, moderator_user, topic, topic_moderator):
    """Test the moderator permissions in a forum where the user is not a
    moderator.
    """

    forum.moderators.remove(moderator_user)
    moderator_user.permissions = moderator_user.get_permissions()

    assert not moderator_user in forum.moderators
    assert not can_moderate(moderator_user, forum)

    assert can_post_reply(moderator_user, forum)
    assert can_post_topic(moderator_user, forum)

    assert not can_edit_post(moderator_user, topic.user_id, forum)
    assert not can_delete_post(moderator_user, topic.user_id, forum)
    assert not can_delete_topic(moderator_user, topic.user_id, forum)

    assert not can_lock_topic(moderator_user, forum)
    assert not can_merge_topic(moderator_user, forum)
    assert not can_move_topic(moderator_user, forum)

    # Test with own topic
    assert can_delete_post(moderator_user, topic_moderator.user_id, forum)
    assert can_delete_topic(moderator_user, topic_moderator.user_id, forum)
    assert can_edit_post(moderator_user, topic_moderator.user_id, forum)


def test_normal_permissions(forum, user, topic):
    """Test the permissions for a normal user."""
    user.permissions = user.get_permissions()

    assert not can_moderate(user, forum)

    assert can_post_reply(user, forum)
    assert can_post_topic(user, forum)

    assert can_edit_post(user, topic.user_id, forum)
    assert not can_delete_post(user, topic.user_id, forum)
    assert not can_delete_topic(user, topic.user_id, forum)

    assert not can_lock_topic(user, forum)
    assert not can_merge_topic(user, forum)
    assert not can_move_topic(user, forum)


def test_admin_permissions(forum, admin_user, topic):
    """Test the permissions for a admin user."""
    admin_user.permissions = admin_user.get_permissions()

    assert can_moderate(admin_user, forum)

    assert can_post_reply(admin_user, forum)
    assert can_post_topic(admin_user, forum)

    assert can_edit_post(admin_user, topic.user_id, forum)
    assert can_delete_post(admin_user, topic.user_id, forum)
    assert can_delete_topic(admin_user, topic.user_id, forum)

    assert can_lock_topic(admin_user, forum)
    assert can_merge_topic(admin_user, forum)
    assert can_move_topic(admin_user, forum)


def test_super_moderator_permissions(forum, super_moderator_user, topic):
    """Test the permissions for a super moderator user."""
    super_moderator_user.permissions = super_moderator_user.get_permissions()

    assert can_moderate(super_moderator_user, forum)

    assert can_post_reply(super_moderator_user, forum)
    assert can_post_topic(super_moderator_user, forum)

    assert can_edit_post(super_moderator_user, topic.user_id, forum)
    assert can_delete_post(super_moderator_user, topic.user_id, forum)
    assert can_delete_topic(super_moderator_user, topic.user_id, forum)

    assert can_lock_topic(super_moderator_user, forum)
    assert can_merge_topic(super_moderator_user, forum)
    assert can_move_topic(super_moderator_user, forum)
