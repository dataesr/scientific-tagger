from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import astronomy

def test_sdg6(asjc_list, ti_abs_kw):
    cond1, _ = does_contain(ti_abs_kw, ["clean water and sanitation"])
    cond2, _ = does_contain_list(asjc_list, ["2312"])
    
    cond3_0, _ = does_contain(ti_abs_kw, ["water","sanitation"])
    cond3_1, _ = does_contain(ti_abs_kw, ["ecosystem","eco-system","handwashing","hand-washing","hygiene","hygienic","hygienic toilet","hygienic toilets","latrine","pollutant","pollutant removal","pollution","quality","endocrine disruptor"])
    cond3 = cond3_0 and cond3_1

    cond4, _ =  does_contain(ti_abs_kw, ["antifouling membrane","anti-fouling membrane","antifouling membranes","anti-fouling membranes","water access","access to water","urban runoff","water availability","available water","availability of water","water conservation","conservation of water","water desalination","desalination of water","water management","management of water","management of the water","water pollutant","polluted water","pollutants in water","pollutants from water","pollution of water","pollution in water","pollution water","pollution in the water","water and pollution","pollutants water","water by pollutants","water from pollutants","water purification","purification of water","water quality","quality of water","water recycling","recycling water","recycle water","water reuse","reuse of water","water reusing","water scarcity","scarcity of water","water security","security of water","water shortage","shortage of water","water source","source of water","sources of water","water supplies","supply of water","water toxicology","toxicology of water","water treatment","treatment of water","treatment of the water","treatment for water","water after treatment","waste water","waste in water","water footprint","water use","water using","use of water","using water","use the water","use of this water","water we use","use and water","water and use","use that water","use in the water","anti-fouling membrane","aquatic ecotoxicology","aquatic toxicology","black water","blue water","clean water","groundwater","ground-water" ,"manage water","open defecation","safe water","sanitation","sewage","sewer","toilet","wastewater","water ecotoxicology","water efficiency","water infrastructure","water resource","water resources management","water supply","drinking water","fresh water","freshwater","green water","grey water","ground water","potable water","water contamination","contaminated water","water contaminants","contaminants from water","contaminants in water","contamination of water","contaminants in the water","emissions into water","contamination in water","water and contaminants","contaminants over water","contaminants of water","water grabbing","water stressed countries","water inventory","watershed management","soil and water conservation","sanitation and water conservation","water policy","water pricing","water balance","water framework directive","river basin management" 
,["water", "biological treatment"]
,["water", "denitrification"]
,["water", "flocculation"]
,["water", "membrane bioreactor"]
,["water", "membrane filtration"]
,["water", "membrane fouling"]
,["water", "microfiltration"]
,["water", "nanofiltration"]
,["water", "nitrogen removal"]
,["water", "nutrient removal"]
,["water", "phosphorus removal"]
,["water", "reverse osmosis"]
,["water", "sequencing batch reactor"]
,["water", "ultrafiltration"]
])

    cond5_0, _ = does_contain(ti_abs_kw, astronomy)
    cond5_1, _ = does_contain(ti_abs_kw, ["graph partition","hierarchical watershed"])
    cond5 = not(cond5_0 or cond5_1)

    if (cond1 or cond2 or cond3 or cond4) and cond5:
        return {"sdg_code": "sdg6", "sdg_label": "6. Clean water and sanitation"}
    return {}
