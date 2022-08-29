import pytest

@pytest.fixture(params=[1,2,3])
def setup(request):
    retval = request.param
    print("\nSetup! retval = {}".format(retval))
    return retval


def test123(setup):
    print("\nSetup = {}".format(setup))
    assert True