import os

@given(u'I\'m logged onto computer')
def step_impl(context):
    context.os = os
#    raise NotImplementedError(u'STEP: Given I\'m logged onto computer')


@when(u'I count no of CPU cores')
def step_impl(context):
    context.os = os
    com = "cat /proc/cpuinfo | grep proces | wc -l"
    wynik = os.popen(com).read().strip()
    context.wynik = wynik
#    raise NotImplementedError(u'STEP: When I count no of CPU cores')


@then(u'I have no of cores equal to 2.')
def step_impl(context):
    assert context.wynik == '2'
#    raise NotImplementedError(u'STEP: Then I have no of cores equal to 2.')
