import smtplib
import pytest
from mailer import send


class FakeSMTP(object):
    def __init__(self, *args, **kw):
        # このサンプルでは引数は影響を与えません
        pass

    def quit(self):
        pass

    def sendmail(self, *args, **kw):
        return {}


@pytest.yield_fixture()
def patch_smtplib():
    # setup処理: smtplibに対するモンキーパッチ
    old_smtp = smtplib.SMTP
    smtplib.SMTP = FakeSMTP

    yield

    # teardown処理:
    # smtplibをモンキーパッチ適用前の状態に戻す
    smtplib.SMTP = old_smtp


def test_send(patch_smtplib):
    res = send(
        'john.doe@example.com',
        'john.doe@example.com',
        'topic',
        'body'
    )
    assert res == {}
