# scenario_tests.py
import balder
from features import ClassWithAValueFeature, GetExpectedAValue


# the scenario for testing the `a` value
class ScenarioTestA(balder.Scenario):
    # you only have one device - your class
    class ClassUnderTest(balder.Device):
        # your device has one feature that provides the value `a` from the class-instance
        klass = ClassWithAValueFeature()
        # and it has one feature that provides the expected value for `a`
        expected_a = GetExpectedAValue()

    # this is your test, similar to
    def test_a(self):
        assert self.ClassUnderTest.klass.a_value == self.ClassUnderTest.expected_a.value
