from project.server.main.sdg.sdg1 import test_sdg1
from project.server.main.sdg.sdg2 import test_sdg2
from project.server.main.sdg.sdg3 import test_sdg3
from project.server.main.sdg.sdg4 import test_sdg4
from project.server.main.sdg.sdg5 import test_sdg5
from project.server.main.sdg.sdg6 import test_sdg6
from project.server.main.sdg.sdg7 import test_sdg7
from project.server.main.sdg.sdg8 import test_sdg8

def test_sdg(asjc, ti_abs_kw):
    res = []
    res.append(test_sdg1(asjc, ti_abs_kw))
    res.append(test_sdg2(asjc, ti_abs_kw))
    res.append(test_sdg3(asjc, ti_abs_kw))
    res.append(test_sdg4(asjc, ti_abs_kw))
    res.append(test_sdg5(asjc, ti_abs_kw))
    res.append(test_sdg6(asjc, ti_abs_kw))
    res.append(test_sdg7(asjc, ti_abs_kw))
    res.append(test_sdg8(asjc, ti_abs_kw))

    sdg = []
    for r in res:
        if len(r)>0 and r not in sdg:
            sdg.append(r)
    return {"sdg_classification": sdg}
