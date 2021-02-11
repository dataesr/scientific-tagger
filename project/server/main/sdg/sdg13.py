from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import astronomy

def test_sdg13(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["3103"])
    if cond1:
        return {}
    
    cond2_0, _ = does_contain_list(asjc_list, ["2300","2301","2302","2303","2304","2305","2306","2307","2308","2309","2310","2311","2312"])
    cond2_1, _ = does_contain(ti_abs_kw, ["climate","atmospher","climatic"])
    cond2 = cond2_0 and cond2_1

    cond3, _ = does_contain_list(asjc_list, ["1902","2306"])

    cond4, _ = does_contain(ti_abs_kw, [
    "climate action"
,"climate adaptation"
,"climate change adaptation"
,"climate change"
,"climate capitalism"
,"greenhouse gas"
,"greenhouse effect"
,"extreme events"
,"kyoto protocol"
,"permafrost thaw"
    ,"permafrost melt"
,"permafrost degradation"
,"thawing permafrost"
,"melting permafrost"
," radiative forcing"
," climate forcing"
,"ipcc"
,"Intergovernmental Panel on Climate Change"
,"climate effect"
,"climate effects"
,"climate equity"
,"climate feedback"
,"climate finance"
,"climate change financing"
,"climate forcing"
,"climate forecast"
,"climate-economy model"
,"climate and in environmental change"
,"climate governance"
,"climate impact"
,"climate impacts"
,"climate issues"
,"climate investment"
,"climate and energy analysis"
,"climate and energy analyses"
,"climate goal"
,"climate justice"
,"climate mitigation"
,"climate model"
,"climate models"
,"climate modeling"
,"climate modelling"
,"climate negotiation"
,"climate negotiations"
,"climate policy"
,"climate policies"
,"climate risk"
,"climate risks"
,"climate services"
,"climate service"
,"climate prediction"
,"climate predictions"
,"climate projection"
,"climate projections"
,"climate simulation"
,"climate simulations"
,"climate signal"
,"climate signals"
,"climate tipping point"
,"ecoclimatology"
,"eco-climatology"
,"Green Climate Fund"
,"regional climate"
,"regional climates"
,"climate smart"
,"global warming"
,"Global atmospheric changes"
,"unfccc"
,"United Nations Framework Convention on Climate Change" ])
    
    cond5, _ = does_contain(ti_abs_kw, astronomy)

    if (cond2 or cond3 or cond4) and (not cond5):
        return {"sdg_code": "sdg13", "sdg_label": "13. Climate action"}
    return {}
