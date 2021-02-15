from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import astronomy

def test_sdg14(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["1910","1104"])
    cond2, _ = does_contain(ti_abs_kw, [
        "life below water" 
,"oceanic circulation model"
,"Guidelines on the Transfer of Marine Technology"
,"oceanic circulation models"
,"oceanic circulation modelling"
,"oceanic circulation modeling"
,"coral bleach"
,"coral bleaching"
,"ice-ocean" 
,"mangrove ecosystem"
,"marine protected area"
,"marine protected areas"
,"marine conservation"
,"marine land slide"
,"marine pollution"
,"marine environment"
,"United Nations Convention on the Law of the Sea"
,"unclos"
,"Law of the Sea"
,"marine quota"
,"fishing quota"
,"marine biodiversity"
,"marine economy"
,"marine policy"
,"marine resource"
,"marine debris"
,"sea-level rise"
,"sea level rise"
,"marine reserves"
,"marine reserve"
,"ocean acidification"
,"marine acidity"
,"sea acidification"
,"sustainable use of oceans"
,"sustainable use of the oceans"
,["acidification", "seawater"]
,"coastal ecosystem"
,"coastal water"
,"marine ecosystem"
,"productive ocean"
,"healthy ocean"
,"World Trade Organization fisheries"
,"World Trade Organization on fisheries"
,"oceans and seas"
        ])
    
    if None in asjc_list:
        cond3_0, _ = True, 'none'
    else:
        cond3_0, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["34","15","16","17","19","21","22","23","25","26","31","12","14","18","20","32","33","10","11"])


    cond3_1, _ = does_contain(ti_abs_kw, [
    "marine"
,"submarine"
,"maritime"
,"ocean"
,"oceans"
," sea."
," sea,"
," sea;"
," sea:"
," sea "
," seas."
," seas,"
," seas;"
," seas:"
," seas "
," lake "
," lake."
," lake,"
," lake;"
," lake:"
," lake:"
,"delta"
,"wetland"
,"river"
,"fluvial"
,"mangrove"  
,"estuary"  
,"estuaries"  
,"estuarine"])


    cond3_2, _ = does_contain(ti_abs_kw, [
"water cycle"
,"water cycles"
,"plastic"
,"litter"
,"anthropogenic particles"	
,"biogeochemical cycle"
,"biogeochemical cycles"
,"sustainable aquaculture"
,"eutrophicat"
,"coastal management"
,"coastal habitat"
,"coastal habitats"
,"fishery"
,"fisheries"
,"overfishing"
,"farmed acquatic animal","fish biomass","fish farming","fish stocking","mariculture" 
,"unregulated fishing"
,"unreported fishing"
,"restore fish stock"
,"illegal fishing"
,"sustainable yield"
,"ecotourism"
,"sustainable tourism"
,"community based conservation"
,"community-based conservation"
,"nutrient runoff"
,"destructive fishing"
,"species richness"
,"species diversity"
,"diversity of species"
,"diversity of the species"
,"traditional ecological knowledge"
,"small Island development states" ])
    
    cond3 = cond3_0 and cond3_1 and cond3_2
    cond4, _ = does_contain(ti_abs_kw, astronomy)

    if (cond1 or cond2 or cond3) and (not cond4):
        return {"sdg_code": "sdg14", "sdg_label": "14. Life below water"}
    return {}
