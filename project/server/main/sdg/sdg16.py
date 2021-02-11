from project.server.main.sdg.utils import does_contain, does_contain_list

def test_sdg16(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["3306", "3308", "3311", "3312", "3320", "3321"])

    if None in asjc_list:
        cond2_0, _ = True, 'none'
    else: 
        cond2_0, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["15","16","17","19","21","22","23","25","26","31","12","14","18","20","32","33","10","11"])
    
    
    cond2_1, _ = does_contain(ti_abs_kw, [
   "peace justice and strong institutions"
,"actual innocence"
,"false confession"
,"armed conflict"
,"armed conflicts"
,"civil conflict"
,"civil conflicts"
,"civil war"
,"illicit financial"
,["war", "conflict"]
,["war", "warfare"]
,["war", "democracy"]
,["war", "Geneva Convention"]
,["war", "treaty"]
,["war", "peace"]
,"peacekeeping"
,["corruption", "institution"]
,["corruption", "public official"]
,["corruption", "government"]
,["corruption", "bribery"]
,["corruption", "conflict"]
,"crime"
,"crimes"
,"criminal"
,"democratic deficit"
        ])

    cond2_2, _ = does_contain(ti_abs_kw, ["democratisation","democratization"])
    cond2_3, _ = does_contain(ti_abs_kw, ["institutional"
,"conflict"
,"decision-making"
,"society"
,"politics"
,"financial aid"])

    cond2_4, _ = does_contain(ti_abs_kw, 
    ["ethnic conflict"
,"ethnic conflicts"
,"exoneration"
,"genocid"
,"homicide"
,"murder"
,"human trafficking"
,"justice system"
,"system of justice"
,"equal access to justice"
,"arbitrary justice"
,"refugee"
,"terroris"
,"violence"
,"torture"
,"effective rule of law"
,"arms flow"
,"transparent institution"
,"transparent institutions"
,"good governance"
,"legal identity for all"
,"provide legal identity"
,"freedom of information"
,"human rights institution"
,"human rights activists"
,"fundamental freedom"
,"fundamental freedoms"
,"violent conflict"
,"violent conflicts"
,"peaceful society"
,"effective institution"
,"effective institutions"
,"accountable institution"
,"accountable institutions"
,"inclusive institution"
,"inclusive institutions"
,"child abuse"
,"child exploitation"
,"child trafficking"
,"child torture"
,"torture of children"
,"children abuse"
,"children exploitation"
,"children trafficking"
,"children torture"
,"arbitrary detention"
,"unsentenced detention"
,"judicial system"
,"criminal tribunal"
,"inclusive society"
,"inclusive societies"
,"responsive institution"
,"responsive institutions"
,"fair society"
,"fair societies"
,"legal remedy"
,"legal remedies"
,"independence of judiciary"
,"independent judiciary"
,"separation of powers"
,"extremism"
,"war crime"
,"peaceful society"
,"organized crime"
,"illicit transfer"
,"illicit money"
,"arms trafficking"
,"cybercrime","cybercriminality"
,"insurgence"
,"local participation"
 ,"sustainability initiative"
,"democratic institution"
,"political instability"
,["decision-making", "responsive"]
,["decision-making", "inclusive"]
,["decision-making", "participatory"]
,["decision-making", "representative"]
,"Aarhus Convention"
,"press freedom"
,"freedom of speech"
])
    cond2 = (cond2_0 and ( cond2_1  or (cond2_2 and cond2_3) or cond2_4 ))

    if cond1 or cond2:
        return {"sdg_code": "sdg16", "sdg_label": "16. Peace, justice and strong institutions"}
    return {}
