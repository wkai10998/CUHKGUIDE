import unittest
from unittest.mock import patch

from werkzeug.security import generate_password_hash

import app as app_module


class AuthSessionTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app_module.app.test_client()

    def test_login_page_exists(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        self.assertIn("登录", response.get_data(as_text=True))

    def test_login_success_sets_session(self):
        fake_user = {
            "id": "11111111-1111-1111-1111-111111111111",
            "name": "Alice",
            "email": "alice@example.com",
            "password_hash": generate_password_hash("secret123"),
            "avatar_seed": "sky",
        }

        with (
            patch.object(app_module, "is_supabase_comments_enabled", return_value=True),
            patch.object(app_module, "get_user_by_email_from_supabase", return_value=fake_user),
        ):
            response = self.client.post(
                "/auth/login",
                data={"email": "alice@example.com", "password": "secret123"},
            )

        self.assertEqual(response.status_code, 302)
        with self.client.session_transaction() as session:
            self.assertEqual(session.get("user_id"), fake_user["id"])
            self.assertEqual(session.get("user_name"), fake_user["name"])
            self.assertEqual(session.get("avatar_seed"), fake_user["avatar_seed"])

    def test_comment_requires_login(self):
        response = self.client.post(
            "/faq/1/comment",
            data={"content": "test comment"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("请先登录后发表评论", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
