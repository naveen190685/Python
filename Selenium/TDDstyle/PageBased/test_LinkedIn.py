import pytest


class Test_LinkedIn:
    # @pytest.mark.linkedIn
    # def test_linkedin_SignIn(self, linkedInHome, linkedInSignIn):
    #     linkedInHome.SignIn()
    #     linkedInSignIn.enterEmail("asdlk")
    #     linkedInSignIn.enterPassword("kuchbhi")
    #     linkedInSignIn.submit()
    #     flag = linkedInSignIn.checkErrorIs("Please enter a valid username")
    #     print(f'Error message found: {flag[1]}')
    #     assert flag[0]

    @pytest.mark.linkedIn
    def test_linkedin_Join(self, linkedInHome, joinNow):
        linkedInHome.Join()
        joinNow.enterEmail("asdlk")
        joinNow.enterPassword("kuchbhi")
        joinNow.AgreeJoin()
        flag = joinNow.checkErrorIs("Please enter a valid email address or mobile number.")
        print(f'Error message found: {flag[1]}')
        assert flag[0]
