import unittest
from unittest.mock import patch

from werkzeug.security import generate_password_hash

import app as app_module


class AuthSessionTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app_module.app.test_client()

    def test_login_route_redirects_to_modal(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/?open_login=1&auth_tab=login", response.location)

    def test_login_success_sets_session(self):
        fake_user = {
            "id": "11111111-1111-1111-1111-111111111111",
            "name": "Alice",
            "email": "alice@example.com",
            "password_hash": generate_password_hash("secret123"),
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
            self.assertIsNone(session.get("avatar_seed"))

    def test_comment_requires_login(self):
        response = self.client.post(
            "/guide/prep/comment",
            data={"step_id": 1, "content": "test comment"},
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/guide/prep?step=1&open_login=1&auth_tab=login", response.location)

    def test_authenticated_header_only_shows_logout_action(self):
        with self.client.session_transaction() as session:
            session["user_id"] = "11111111-1111-1111-1111-111111111111"
            session["user_name"] = "Alice"
            session["user_email"] = "alice@example.com"

        html = self.client.get("/").get_data(as_text=True)
        self.assertIn("退出登录", html)
        self.assertNotIn("保存资料", html)
        self.assertNotIn("恢复默认资料", html)

    def test_auth_login_error_redirects_with_modal_flag(self):
        with patch.object(app_module, "is_supabase_comments_enabled", return_value=True):
            response = self.client.post(
                "/auth/login",
                data={"email": "", "password": ""},
                headers={"Referer": "http://localhost/guide/prep?step=1"},
            )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/guide/prep?step=1&open_login=1&auth_tab=login", response.location)

    def test_auth_register_error_redirects_with_register_tab(self):
        with patch.object(app_module, "is_supabase_comments_enabled", return_value=True):
            response = self.client.post(
                "/auth/register",
                data={"name": "", "email": "bad", "password": "123"},
                headers={"Referer": "http://localhost/programs"},
            )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/programs?open_login=1&auth_tab=register", response.location)

    def test_auth_register_requires_matching_confirm_password(self):
        with patch.object(app_module, "is_supabase_comments_enabled", return_value=True):
            response = self.client.post(
                "/auth/register",
                data={
                    "name": "Alice",
                    "email": "alice@example.com",
                    "password": "secret123",
                    "confirm_password": "secret999",
                },
                follow_redirects=True,
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn("两次输入的密码不一致。", response.get_data(as_text=True))

    def test_auth_register_success_calls_create_user_without_avatar_seed(self):
        with (
            patch.object(app_module, "is_supabase_comments_enabled", return_value=True),
            patch.object(
                app_module,
                "create_user_in_supabase",
                return_value={
                    "id": "11111111-1111-1111-1111-111111111111",
                    "name": "Alice",
                    "email": "alice@example.com",
                },
            ) as create_user,
        ):
            response = self.client.post(
                "/auth/register",
                data={
                    "name": "Alice",
                    "email": "alice@example.com",
                    "password": "secret123",
                    "confirm_password": "secret123",
                },
            )

        self.assertEqual(response.status_code, 302)
        create_user.assert_called_once_with("Alice", "alice@example.com", "secret123")
        with self.client.session_transaction() as session:
            self.assertEqual(session.get("user_name"), "Alice")
            self.assertEqual(session.get("user_email"), "alice@example.com")
            self.assertIsNone(session.get("avatar_seed"))


if __name__ == "__main__":
    unittest.main()
