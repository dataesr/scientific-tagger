from project.server.main.sdg.sdg1 import test_sdg1
from project.server.main.sdg.sdg2 import test_sdg2
from project.server.main.sdg.sdg3 import test_sdg3
from project.server.main.sdg.sdg4 import test_sdg4
from project.server.main.sdg.sdg5 import test_sdg5
from project.server.main.sdg.sdg6 import test_sdg6
from project.server.main.sdg.sdg7 import test_sdg7
from project.server.main.sdg.sdg8 import test_sdg8
from project.server.main.sdg.sdg9 import test_sdg9
from project.server.main.sdg.sdg10 import test_sdg10
from project.server.main.sdg.sdg11 import test_sdg11
from project.server.main.sdg.sdg12 import test_sdg12
from project.server.main.sdg.sdg13 import test_sdg13
from project.server.main.sdg.sdg14 import test_sdg14
from project.server.main.sdg.sdg15 import test_sdg15
from project.server.main.sdg.sdg16 import test_sdg16

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
    res.append(test_sdg9(asjc, ti_abs_kw))
    res.append(test_sdg10(asjc, ti_abs_kw))
    res.append(test_sdg11(asjc, ti_abs_kw))
    res.append(test_sdg12(asjc, ti_abs_kw))
    res.append(test_sdg13(asjc, ti_abs_kw))
    res.append(test_sdg14(asjc, ti_abs_kw))
    res.append(test_sdg15(asjc, ti_abs_kw))
    res.append(test_sdg16(asjc, ti_abs_kw))

    sdg = []
    for ix, r in enumerate(res):
        print(ix, flush=True)
        if len(r)>0 and r not in sdg:
            sdg.append(r)
    return {"sdg_classification": sdg}
