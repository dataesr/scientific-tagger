from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import dev_countries

def test_sdg10(asjc_list, ti_abs_kw):
    cond1_0, _ = does_contain_list(asjc_list, ["3312","3317","3320","3305"])
    cond1_1, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["20"])
    cond1_2, _ = does_contain(ti_abs_kw, [
        "migration","immigration","emigration","migrant"
        ])
    cond1 = (cond1_0 or cond1_1) and cond1_2

    cond2_0, _ = does_contain(ti_abs_kw, [
            ["equality", "economic"],
            ["equality", "financial"],
            ["equality", "socio-economic"],
            ["equality", "socioeconomic"],
            ["inequality", "economic"],
            ["inequality", "financial"],
            ["inequality", "socio-economic"],
            ["inequality", "socioeconomic"],
            ["inequalities", "economic"],
            ["inequalities", "financial"],
            ["inequalities", "socio-economic"],
            ["inequalities", "socioeconomic"]
            ])
    
    cond2_1, _ = does_contain(ti_abs_kw, [
        "economic reform policy"
,"economic reform policies"
,"inequality among countries"
,"inequalities among countries"
,"World Trade Organization agreements"
,"inequalities of outcome"
,"inequality of outcome"
,"outcome inequality"
,"outcome inequalities"
,"political inclusion"
,"economic inclusion"
,"social inclusion"
,"social protection policy"
,"social protection policies"
,"foreign direct investment"
,"development gap"
,"development gaps"
,"migrant remittance"
,"responsible migration"
,"migration policy"
,"migration policies"
,"north-south divide"
,"social exclusion"
,"economic marginalization"
,"economic marginalisation"
,"income inequality"
,"income inequalities"
,"discriminatory law"
,"discriminatory policies"
,"discriminatory policy"
,"wage inequality"
,"wage inequalities"
,"income inequality"
,"income inequalities"
,"economic empowerment"
,"economic transformation"
,"differential treatment for developing countries" ])
    
    cond2_2, _ = does_contain(ti_abs_kw, [
        ["global market", "empowerment"],
        ["global market", "regulation"],
        ["international market", "empowerment"],
        ["international market", "regulation"]
        ])
    
    cond2_3, _ = does_contain(ti_abs_kw, [
"financial flows"
,"decision-making"
,"enhanced representation"
,"global international economy"
,"global economy"
,"global value chain"
,"financial institutions"
,"international economic"
])

    cond2_4_tmp = ["Africa","least developed countries","landlocked country","developing country"
,"landlocked countries","developing countries","small island developing States"] + dev_countries
    cond2_4, _ = does_contain(ti_abs_kw, cond2_4_tmp)

    cond2_5 = cond2_3 and cond2_4

    cond2 = cond2_1 or cond2_2 or cond2_5 

    if cond1 or cond2:
        return {"sdg_code": "sdg10", "sdg_label": "10. Reduced inequalities"}
    return {}
