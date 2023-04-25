import balder


# you only need something to access the `a` Property of your class 
# (how this is done, is not of interest on scenario-level)
class ClassWithAValueFeature(balder.Feature):
    def a_value(self):
        raise NotImplementedError()


class ClassWithBValueFeature(balder.Feature):
    def b_value(self):
        raise NotImplementedError()


class ClassWithCValueFeature(balder.Feature):
    def c_value(self):
        raise NotImplementedError()


# we can also use a parent class for the similar features here
class _GetExpectedValue(balder.Feature):
    @property
    def value(self):
        raise NotImplementedError()


class GetExpectedAValue(_GetExpectedValue):
    pass


class GetExpectedBValue(_GetExpectedValue):
    pass


class GetExpectedCValue(_GetExpectedValue):
    pass
