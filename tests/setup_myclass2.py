import balder
import features
from myclass2 import MyClass2


class MyClass2InstanceFeature(balder.Feature):
    instance = None

    def create_instance(self):
        self.instance = MyClass2()


class MyClass2ValueAFeature(features.ClassWithAValueFeature):
    instance_feature = MyClass2InstanceFeature()

    @property
    def a_value(self):
        return self.instance_feature.instance.a


class MyClass2ValueBFeature(features.ClassWithBValueFeature):
    instance_feature = MyClass2InstanceFeature()

    @property
    def b_value(self):
        return self.instance_feature.instance.b


class MyClass2ExpectedAVal(features.GetExpectedAValue):
    value = 12


class MyClass2ExpectedBVal(features.GetExpectedBValue):
    value = 13


class SetupMyClass2(balder.Setup):

    class Client2(balder.Device):
        instance = MyClass2InstanceFeature()
        a_value = MyClass2ValueAFeature()
        b_value = MyClass2ValueBFeature()
        a = MyClass2ExpectedAVal()
        b = MyClass2ExpectedBVal()

    @balder.fixture('setup')
    def create_instance(self):
        self.Client2.instance.create_instance()
