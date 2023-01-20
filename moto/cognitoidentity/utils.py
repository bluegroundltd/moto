from moto.moto_api._internal import mock_random


def get_random_identity_id(region: str) -> str:
    return f"{region}:{mock_random.uuid4()}"


def get_static_identity_pool_id(region: str, cognito_static_identity_pool_id: str) -> str:
    return f"{region}:{cognito_static_identity_pool_id}"
