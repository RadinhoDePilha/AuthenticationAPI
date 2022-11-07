import pytest
from .authentication import is_authenticated


class TestsAuthentication:
    def test_authentication_none_admin(self):
        assert is_authenticated('admin', None) is False

    def test_authentication_none_editor(self):
        assert is_authenticated('editor', None) is False

    def test_authentication_none_super(self):
        assert is_authenticated('super', None) is False

    def test_authentication_empty_admin(self):
        assert is_authenticated('admin', '') is False

    def test_authentication_empty_editor(self):
        assert is_authenticated('editor', '') is False

    def test_authentication_empty_super(self):
        assert is_authenticated('super', '') is False

    def test_authentication_with_admin_admin(self):
        assert is_authenticated('admin', 'admin') is True

    def test_authentication_with_admin_editor(self):
        assert is_authenticated('admin', 'editor') is False

    def test_authentication_with_admin_super(self):
        assert is_authenticated('admin', 'super') is True

    def test_authentication_with_super_editor(self):
        assert is_authenticated('super', 'editor') is False

    def test_authentication_with_super_admin(self):
        assert is_authenticated('super', 'admin') is False

    def test_authentication_with_super_super(self):
        assert is_authenticated('super', 'super') is True

    def test_authentication_with_editor_admin(self):
        assert is_authenticated('editor', 'admin') is True

    def test_authentication_with_editor_super(self):
        assert is_authenticated('editor', 'super') is True

    def test_authentication_with_editor_editor(self):
        assert is_authenticated('editor', 'editor') is True
