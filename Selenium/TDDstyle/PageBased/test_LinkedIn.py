import pytest
class Test_LinkedIn:
    @pytest.mark.linkedIn
    def test_linkedin_SignIn(self, land, signIn):
        land.SignIn()
        signIn.enterEmail("asdlk")
        signIn.enterPassword("kuchbhi")




