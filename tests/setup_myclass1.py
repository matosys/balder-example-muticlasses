import balder
import features
from myclass1 import MyClass1


# this is helper feature which manages your class `MyClass1`
class MyClass1InstanceFeature(balder.Feature):
    instance = None

    def create_instance(self):
        self.instance = MyClass1()


# this is the setup implementation of the scenario-level feature `ClassWithAValueFeature` (subclassing it)
class MyClass1ValueAFeature(features.ClassWithAValueFeature):
    # here we reference the helper feature from above (the instance management is done in background automatically)
    instance_feature = MyClass1InstanceFeature()

    # here you overwrite the abstract property from the `ClassWithAValueFeature` on scenario-level
    @property
    def a_value(self):
        return self.instance_feature.instance.a


class MyClass1ValueCFeature(features.ClassWithCValueFeature):
    instance_feature = MyClass1InstanceFeature()

    @property
    def c_value(self):
        return self.instance_feature.instance.c


# just describe the expected value
class MyClass1ExpectedAVal(features.GetExpectedAValue):
    value = 1


class MyClass1ExpectedCVal(features.GetExpectedCValue):
    value = 3


class SetupMyClass1(balder.Setup):

    class Client1(balder.Device):
        instance = MyClass1InstanceFeature()
        a_value = MyClass1ValueAFeature()
        c_value = MyClass1ValueCFeature()
        a = MyClass1ExpectedAVal()
        c = MyClass1ExpectedCVal()

    # this fixture will ensure that your instance is only created once (for ll scenarios that map to this setup)
    @balder.fixture('setup')
    def create_instance(self):
        self.Client1.instance.create_instance()
