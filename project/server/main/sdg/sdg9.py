from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import infra, dev_countries

def test_sdg9(asjc_list, ti_abs_kw):
    cond1_0, _ = does_contain_list(asjc_list, ["3303"])
    cond1_1, _ = does_contain(ti_abs_kw, ["innovation","industrial","industrialization","industrialisation","industry","industries","manufacturing","infrastructure","enterprise","entrepreneur"])
    cond1_2, _ = does_contain(ti_abs_kw, infra)
    cond1 = cond1_0 and (cond1_1 or cond1_2)
    
    cond2, _ = does_contain_list(asjc_list, ["2209", "1705", "1405"])
    cond3, _ = does_contain_list(asjc_list, ["2205","1909","2215","2213","2216","3313"])

    cond4_0, _ = does_contain(ti_abs_kw, [
        "Industry, Innovation and Infrastructure"
,"industrial growth"
,"industrial diversification"
,"industrial innovation"
,"sustainable industrialization"
,"sustainable industrialisation"
,"inclusive industrialization"
,"inclusive industrialisation"
,"infrastructural development"
,"infrastructural investment"
,"infrastructure investment"
,"public infrastructure"
,"resilient infrastructure"
,"transborder infrastructure"
,"public infrastructures"
,"resilient infrastructures"
,"transborder infrastructures"
,["industrial emissions", "mitigation"] 
,"industrial waste management"
,"industrial waste treatment"
,"clean industrial processes"
        ])

    cond4_1_tmp = ["Africa","least developed countries","landlocked country","developing country"
,"landlocked countries","developing countries","small island developing States"] + dev_countries
    cond4_1, _ = does_contain(ti_abs_kw, cond4_1_tmp)

    cond4_2, _ = does_contain(ti_abs_kw, [
    "domestic technology development"
,"research and development"
,"access to the Internet"
,"security in cloud","social network privacy","cryptography","network security","network privacy"
,"information and communications technology"
,"transportation services"
,"mobile connectivity"
,"broadband access"
,"mobile cellular signal"
,"online access"
,"3G"
,"Internet through a third generation"])

    cond4_3, _ = does_contain(ti_abs_kw, [
            "financial support"
,"technological support"
,"technical support"
,"financial services"
,"affordable credit"])

    cond4_4, _ = does_contain(ti_abs_kw, [
        "enterprise","entrepreneur"
,"small-scale industrial"])

    cond4_5 = cond4_3 and cond4_4

    cond4_6, _ = does_contain(ti_abs_kw, [
        "infrastructural Development"
,"microenterprise"
,"micro-enterprise"
,"small enterprise"
,"medium enterprise"
,"small enterprises"
,"medium enterprises"
,"small entrepreneur"
,"medium entrepreneur"
,"small entrepreneurs"
,"medium entrepreneurs"
,"value chain management"
,"manufacturing innovation"
,"sustainable production"
,"sustainable manufacturing"
,"manufacturing investment"
,"sustainable transportation"
,"accessible transportation"
,"hybrid and alternative drive vehicles","hybrid electric vehicle","hybrid vehicle","light rail transit","liquid nitrogen powered engine ","sustainable mobility","sustainable transport and mobility","sustainable urban mobility","transport emission reduction","transport planning","transport sustainability","vehicle safety","wheel-rail system"
])
    cond4_7, _ = does_contain(ti_abs_kw, [
        "inclusive transportation"
,"R&D investment"
,"green product"
,"green products"
,"sustainable manufacturing"
,["cradle to cradle", "industry","industries"]
,"closed loop supply chain"
,"process innovation"
,"product innovation"
,"innovation policies"
,"innovation policy"
,"inclusive innovation"])

    cond4 = cond4_0 or ( cond4_1 and ( cond4_2 or ( cond4_4 and cond4_3 )) ) or cond4_6 or cond4_7

    if cond1 or cond2 or cond3 or cond4:
        return {"sdg_code": "sdg9", "sdg_label": "9. Industry, innovation and infrastructure"}
    return {}
