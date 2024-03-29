from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import astronomy

def test_sdg15(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["2309","1107","1103","1109","1904","1111" ])
    if None in asjc_list:
        cond2_0, _ = True, 'none'
    else:
        cond2_0, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["34","15","16","17","19","21","22","23","25","26","31","12","14","18","20","32","33","10","11"])
    
    cond2_1, _ = does_contain(ti_abs_kw, [
      "forest stewardship council"
,"rainforest alliance"
,"forest certification"
,"forest auditing"
,"deforestation"
,"deforest"
,"afforestation"
,"reforestation"
,"afforest"
,"reforest"
,"sea level rise"
,"sea-level rise"
,"agroforestry"
,"agro-forestry"
,"agro+forestry"
,"desertif"
,"land uses"
,"land use"
,"land degradation"
,"soil degradation"
,"LULUCF"
,"land-use change and forestry"
,"land use change and forestry"
,"land conservation"
,"wetland"
,"mountain"
,"dryland"
,"vegetation cover"
,"mountainous cover"
,"REDD"
,"Reducing Emissions from Deforestation and Degradation"
,"forest management"
,"silviculture" 
," forest."
," forest,"
," forest;"
," forest:"
," forest "
," forests."
," forests,"
," forests;"
," forests:"
," forests "
,"prescribed fire"
,"leaf area index"
,"stand structure"
,"forestry"
,"timber harvest"
,"illegal logging"
,"slash-and-burn"
 ,"slash and burn"
,"fire-fallow cultivation"
,"tree cover"
,"soil restoration"
,"land restoration"
,"drought"
,"sustainable land management"
,"mountain vegetation"
,"ecotourism"
,"sustainable tourism"
        ])



    cond2 = cond2_0 and cond2_1

    cond3, _ = does_contain(ti_abs_kw, [ 
    "biodivers"
,"species richness"
,"overhunt"
,"bioeconom"
,"bio-econom"
,"biological production"
,"earth system"
,"ecological resilience"
,"ecosystem"
,"eco-system"
,"trophic cascade"
,"trophic level"
,"trophic web"
,"threatened species"
,"endangered species"
,"extinction risk"
,"extinction risks"
,"poach"
,"wildlife product"
,"wildlife products"
,"wildlife traffic"
,"wildlife market"
,"wildlife markets"
,"wildlife trafficking"
,"invasive species"
,"alien species"
,"protected area"
,"protected areas"
,"habitat restoration"
,"Red List species"
,"Red List Index"
,"extinction wave"
,"habitat fragmentation"
,"habitat loss"
,"Nagoya Protocol on Access to Genetic Resources"
,"genetic resources"
,"biological invasion"
,"biodiversity-inclusive"
,"community-based conservation"
,"community based conservation"
,"human-wildlife conflict"
,"biodiversity conservation","conservation planning","ecosystem function","ecosystem functioning","ecosystem management","ecosystem services","ethnobotany","exotic species","indicator species","landscape ecology","macroecology","macroinvertebrates","nature conservation","neotropics","phylogeography","plant diversity","reserve selection","species diversity","species-area relationship","vascular plants" ,"conservation biology","conservation of natural resources"])

    cond4, _ = does_contain(ti_abs_kw, [ 
        "tree set","tree set"
,"magnetic resonance","wireless sensor"
,"tree graph","stack tree","decision tree","poset","operad"
,"algebra","tree-wise","tree wise"
,"tree of shapes","mathematics","tree structured data","tree-structured data"
,"marine","ocean" ," sea."
," sea,"
," sea;"
," sea:"
," sea "
," seas."
," seas,"
," seas;"
," seas:"
," seas "
,"submarine"
,"maritime"
,"delta"
,"mangrove"
 ,"estuary"
  ,"estuaries"
 ,"estuarine"  ])
    
    cond5, _ = does_contain(ti_abs_kw, astronomy)

    if (cond1 or cond2 or cond3) and (not cond4) and (not cond5):
        return {"sdg_code": "sdg15", "sdg_label": "15. Life on land"}
    return {}
