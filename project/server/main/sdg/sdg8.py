from project.server.main.sdg.utils import does_contain, does_contain_list

def test_sdg8(asjc_list, ti_abs_kw):
    cond1_0, _ = does_contain_list(asjc_list, ["1407"])
    cond1_1, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["20"])
    cond1_2, _ = does_contain(ti_abs_kw, ["sustainable","sustainability","ecological","ecology" ])
    cond1 = (cond1_0 or cond1_1) and cond1_2
    
    cond2_0, _ = does_contain_list(asjc_list, ["3303"])
    cond2_1, _ = does_contain(ti_abs_kw, ["worker","workfare","employment","profession","employee","human resource","work participation","recruitment","workplace","career" ])
    cond2 = cond2_0 and cond2_1

    cond3, _ = does_contain(ti_abs_kw, 
            ["decent work or economic growth"  
,"economic growth" 
,"economic development policy" 
,"employment policy"
,"decent work"
,"fair income"
,"inclusive economic growth" 
,"sustainable growth"
,"sustainable economic growth" 
,"economic development" 
,"economic globalization" 
,"economic globalisation" 
,"economic productivity" 
,"low-carbon economy" 
,"inclusive growth" 
,"microfinanc" 
,"micro-financ" 
,"micro-credit" 
,"microcredit" 
,"equal income" 
,"equal wages" 
,"decent job" 
,"decent jobs" 
,"quality job" 
,"quality jobs" 
,"job creation" 
,"full employment" 
,"employment protection" 
,"informal employment" 
,"precarious employment" 
,"unemployment" 
,"precarious job" 
,"precarious jobs" 
,"microenterprise" 
,"micro-enterprise" 
,"small enterprise" 
,"medium enterprise" 
,"small enterprises" 
,"medium enterprises" 
,"small entrepreneur" 
,"starting entrepreneur" 
,"medium entrepreneur" 
,"small entrepreneurs" 
,"medium entrepreneurs" 
,"starting entrepreneurs" 
,"social entrepreneurship" 
,"safe working environment" 
,"labor market institution" 
,"labor market institutions" 
,"labour market institution" 
,"labour market institutions" 
,"forced labour" 
,"forced labor" 
,"child labour" 
,"child labor" 
,"labour right" 
,"labor right" 
,"labour rights" 
,"labor rights" 
,"Global Jobs Pact"
,"Enhanced Integrated Framework for Trade-Related Assistance for the Least Developed Countries"
,"modern slavery" 
,"human trafficking" 
,"child soldier" 
,"child soldiers" 
,"global jobs" 
,"living wage" 
,"minimum wage" 
,"circular economy" 
,"inclusive economy" 
,"rural economy" 
,"Foreign Development Investment" 
,"Aid for Trade" 
,"trade unions" 
,"trade union" 
,"working poor" 
,"Not in Education, Employment, or Training" 
,"carbon offset" 
,"ecological offset" 
,"carbon offsetting" 
,"carbon offsets" 
,"carbon price" 
,"offset project" 
,"offset projects" 
,"environmental economic" 
,"economic diversification" 
,"material footprint" 
,"resource efficiency" 
,["cradle to cradle", "economy"] 
,"economic decoupling" 
,"labour market disparities" 
,"sustainable tourism" 
,"ecotourism"
,"sustainable tourism"
,"community-based tourism" 
,"tourism employment" 
,"sustainable tourism policy" 
,"financial access" 
,"financial inclusion" 
,"access to banking"  ])

    if cond1 or cond2 or cond3:
        return {"sdg_code": "sdg8", "sdg_label": "8. Decent work and economic growth"}
    return {}