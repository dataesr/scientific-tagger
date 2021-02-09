from project.server.main.sdg.utils import does_contain, does_contain_list

def test_sdg2(asjc_list, ti_abs_kw):
    cond1, evidence1 = does_contain_list(asjc_list, ["1102", "1106"])

    if None in asjc_list:
        cond2_0, evidence2_0 = True, 'none'
    else:
        cond2_0, evidence2_0 = does_contain_list([asjc[0:2] for asjc in asjc_list], ["15","16","17","19","21","22","23","25","26","31","12","14","18","20","32","33","10","11"])

    cond2_1, evidence2_1 = does_contain(ti_abs_kw, 
            ["land tenure rights"
            ,["smallholder", "farm"]
,"forestry"
,"pastoral"
,"agriculture"
,"fishery"
,"fisheries"
,"food producer"
,"food producers"
,"malnourish"
,"malnutrition"
,"undernourish"
,"undernutrition"
,"agricultural production"
,"agriculture as a production"
,"agricultural productivity"
,"agricultural productivity"
,"agricultural practices"
,"agricultural management"
,"food production"
,"production of food"
,"food productivity"
,"food security"
,"security and food"
,"security of food"
,"food safety"
,"food insecurity"
,"land right"
,"access to land"
,"land rights"
,"land reform"
,"land reforms"
,"resilient agricultural practices"
,["agriculture", "potassium"]
,"fertiliser"
,"soil fertility"
,"soil amendment"
,"crop rotation"
,"crop production"
," crops " ," crops." ," crops,"," crops;" ," crops:"
,"agricultural management"
,"fertilizer"
,"improve land and soil quality"
,"improve land quality"
,"improve soil quality"
,"food nutrition improvement"
,"hidden hunger"
,"end hunger"
,"genetically modified food"
,["gmo", "food"]
,["genetically modified ", "food"]
,"agroforestry practices"
,"agroforestry management"
,"agricultural innovation"
,["food security", "genetic diversity"]
,["food security", "seed and plant banks"]
,["food security", "seed banks"]
,["food security", "plant banks"]
,["food market", "restriction"]
,["food market", "tariff"]
,["food market", "access"]
,["food market", "north south divide"]
,["food market", "development governance"]
,"food governance"
,"food price volatility"
,"food supply chain"
,"food value chain"
,"food commodity market"
,"agricultural sustainability"
,"agrobiodiversity","agroecology"
,"conventional farming system"
,"cover crops"
,"farming systems"
,"grain for green"
,"integrated management practices"
,"organic farming"
,"pastoralism"
,"pastoralists"
,"precision farming"
,"rainfed cultivation"
,"rainwater harvesting"
,"shifting cultivation"])

    cond2 = cond2_0 and cond2_1

    cond3, evidence3 = does_contain(ti_abs_kw, ["poverty and hunger"
,"poverty and hunger"
,"hunger and poverty"
,"extreme hunger"
,"world hunger"
,"hunger in the world"
,"world without hunger"
,"tackling poverty and hunger"
,"combat hunger"
,"combating hunger"
,"ending hunger"
,"end hunger"
,"eradicate hunger"
,"hunger alleviation"
,"alleviate hunger"
,"reduce hunger"
,"hunger reduction"
,"protection against hunger"
,"protect against hunger"
,"people affected by hunger"])

    if cond1 or cond2 or cond3:
        return {"sdg_code": "sdg2", "sdg_label": "2. Zero Hunger"}
    return {}
