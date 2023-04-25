import balder


# you only need something to access the `a` Property of your class 
# (how this is done, is not of interest on scenario-level)
class ClassWithAValueFeature(balder.Feature):
    def a_value(self):
        raise NotImplementedError()


# and you need your expected value
class GetExpectedAValue(balder.Feature):
    @property
    def value(self):
        raise NotImplementedError()