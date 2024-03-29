from project.server.main.sdg.utils import does_contain, does_contain_list

def test_sdg12(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["2311","2304","2305"])
    
    cond2_0, _ = does_contain(ti_abs_kw, [
        "consumer behaviour" 
,"consumer behavior"
,"behavior of the consumer"
,"behaviour of the consumer"
,"behavioral economics"
,"behavioural economics"
,"supply chain"
        ])
    cond2_1, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["23"])
    cond2 = cond2_0 and cond2_1

    cond3_0, _ = does_contain(ti_abs_kw, [
    "consumer behaviour"
,"consumer behavior"
,"behavior of the consumer"
,"behaviour of the consumer"
,"behavioral economics"
,"behavioural economics"
,"supply chain" ])
    cond3_1, _ = does_contain(ti_abs_kw, [
"environment"
,"sustainability"
,"sustainable"
,"ecological","ecology" ])
    cond3 = cond3_0 and cond3_1

    cond4, _ = does_contain(ti_abs_kw, [
    "responsible consumption and production" 
,"ethical consumerism"
,"environmental pollution"
,"environmental impact assessment"
,"clean production"
,"cleaner production"
,"hazardous waste"
,"biodegradable"
,"biocompatible"
,"radioactive waste"
,"nuclear waste"
,"consumption of plastic"
,"plastic consumption"
,"reusable bag"
,"plastic straw"
,"plastic bottle"
,"hazardous chemical"
,"pollution control"
,"responsible consumption"
,"responsible production"
,"sustainable clothing consumption"
,"responsible clothing consumption"
,"sustainable textile production"
,"responsible textile production"
,"hazardous chemicals"
,"toxic chemical"
,"toxic chemicals"
,"chemical pollution"
,"ozone depletion"
,"post-harvest loss"
,"pesticide pollution"
,"pesticide stress"
,"pesticide reduction"
,"life cycle assessment"
,"life-cycle assessment"
," life cycle of economic activities"
," life cycle of economic activity"
," life-cycle of economic activities"
," life-cycle of economic activity"
,"life cycle analysis"
,"life-cycle analysis"
,"product life cycle"
,"product life-cycle"
,"products life cycle"
,"products life-cycle"
,"material consumption"
,"material footprint"
,"material efficiency"
,"environmentally sound technologies"
,"environmentally sound technology"
,"life cycle of a service"
,"life-cycle of a service"
,"life cycle of a product"
,"life-cycle of a product"
,"life cycle of services"
,"life-cycle of services"
,"life cycle of products"
,"life-cycle of products"
,"life cycle analyses"
,"lifecycle environmental impact"
,"life-cycle analysis"
,"life-cycle analyses"
,"low carbon economy"
,"low-carbon economy"
,"low carbon economies"
,"low-carbon economies"
,"environmental footprint"
,"material footprint"
,"harvest efficiency"
,"solid waste"
,"waste generation"
,"corporate social responsibility"
,"corporate political responsibility"
,"corporate sustainability"
,"household energy behavior"
,"household energy behaviour"
,"household environmental behaviour"
,"household environmental behavior"
,"household environmental attitude"
,"waste recycling"
,"recycle waste"
,"recycle water"
,"water recycling"
,"purify water"
,"water purifying"
,"resource recycling"
,"resource reuse"
,"adaptative reuse"
,"biobased economy"
,"sustainable lifestyle"
,"zero waste"
,"sustainability label"
,"sustainability labelling"
,"global resource extraction"
,"material flow accounting"
,"societal metabolism"
,"food spill"
,"food loss"
,"food waste"
,"throw away food"
,"resource spill"
,"resource efficiency"
,"sustainable food consumption"
,"sustainable consumption"
,"sustainable production"
,"food-related energy consumption"
,"food-related energy waste"
,"food related energy consumption"
,"food related energy waste"
,"green consumption"
,"green economy"
,"green production"
,"sustainable supply chain"
,"wasteful consumption"
,"circular economy"
,"cradle to cradle"
,"sustainable procurement"
,"sustainable tourism"
,"fossil-fuel subsidies"
,"fossil-fuel expenditure"
,"fossil fuel subsidies"
,"fossil fuel expenditure"
,"sustainability label"
,"sustainability labelling"
,["consumption", "resource use"]
,["consumption", "spill"]
,["production", "resource use"]
,["production", "spill"]
,"eco-efficiency","ecoefficiency","ecological footprint" 
,"ecospace","eco-supply chain","eco supply chain" 
,"environmental management accounting","environmental product policy" 
,"fair trade","green consumerism","green core competence" 
,"green innovation","green marketing","green process innovation" 
,"green product innovation","greening of industry" 
,"industrial ecology","industrial sustainability" 
,"industrial symbiosis","integrated product policy" 
,"life cycle costing","life-cycle thinking","life-cycle costing" 
,"life cycle thinking","natural resource accounting" 
,"pollution prevention","product service system" 
,"product stewardship","rebound effect","steady-state economy" 
,"sustainable chemistry","sustainable consumption and production" 
,"sustainable production and consumption" 
,"waste management","waste minimization"
,"waste activated sludge","waste utilization","pylorysis","composting","biogasification","energy from waste","waste collection","biowaste","leachate treatment","packaging waste","source separation","source reduction","waste valorization","household waste","leaching test"  ,"waste disposal"  ,"fatigue damage"
])

    if cond1 or cond2 or cond3 or cond4:
        return {"sdg_code": "sdg12", "sdg_label": "12. Responsible consumption and production"}
    return {}
