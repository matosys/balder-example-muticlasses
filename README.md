# BalderExample for testing similar classes

## Install balder

```shell
$ pip install baldertest
```

## Run Balder

```shell

$ balder --working-dir tests

+----------------------------------------------------------------------------------------------------------------------+
| BALDER Testsystem                                                                                                    |
|  python version 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0] | balder version 0.1.0b6                           |
+----------------------------------------------------------------------------------------------------------------------+
Collect 2 Setups and 3 Scenarios
  resolve them to 4 mapping candidates

================================================== START TESTSESSION ===================================================
SETUP SetupMyClass1
  SCENARIO ScenarioTestA
    VARIATION ScenarioTestA.ClassUnderTest:SetupMyClass1.Client1
      TEST ScenarioTestA.test_a [.]
  SCENARIO ScenarioTestC
    VARIATION ScenarioTestC.ClassUnderTest:SetupMyClass1.Client1
      TEST ScenarioTestC.test_c [.]
SETUP SetupMyClass2
  SCENARIO ScenarioTestA
    VARIATION ScenarioTestA.ClassUnderTest:SetupMyClass2.Client2
      TEST ScenarioTestA.test_a [.]
  SCENARIO ScenarioTestB
    VARIATION ScenarioTestB.ClassUnderTest:SetupMyClass2.Client2
      TEST ScenarioTestB.test_b [.]
================================================== FINISH TESTSESSION ==================================================
TOTAL NOT_RUN: 0 | TOTAL FAILURE: 0 | TOTAL ERROR: 0 | TOTAL SUCCESS: 4 | TOTAL SKIP: 0 | TOTAL COVERED_BY: 0

```