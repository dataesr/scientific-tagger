from project.server.main.sdg.utils import does_contain, does_contain_list

def test_sdg3(asjc_list, ti_abs_kw):

    cond1_0, evidence1_0 = does_contain_list([asjc[0:2] for asjc in asjc_list], ["27" ,"29" ,"35" ,"36" ,"24" ,"28" ,"30" ,"32" ])
    cond1_1, evidence1_1 = does_contain_list(asjc_list, ["3306"])
    cond1 = cond1_0 or cond1_1

    cond2_0, evidence2_0 =  does_contain_list([asjc[0:2] for asjc in asjc_list], ["32"])
    cond2_1, evidence2_1 = does_contain(ti_abs_kw, ["hospital","medical staff","doctor","nurse","physician","health"])
    cond2 = cond2_0 and cond2_1

    cond3, evidence3 = does_contain_list(ti_abs_kw, 
            [
                "good health and well-being"
                ,["human", "health"]
                ,["human", "disease"]
                ,["human", "illness"]
                ,["human", "medicine"]
                ,["human", "mortality"]
                ,"battered child syndrome","cardiovascular disease","cardiovascular diseases","chagas","child abuse","child neglect","human wellbeing","human well-being","youth wellbeing","youth well-being","child wellbeing","child well-being","woman wellbeing","woman well-being","women wellbeing","women well-being","children wellbeing","children well-being","wellbeing of children","well-being of children","health of children","children health","wellbeing of women","well-being of women","health of women","women health","wellbeing of youth","well-being of youth","health of youth","youth health","young people’s health","young people health","water-borne disease","water-borne diseases","water borne disease","water borne diseases","tropical disease","tropical diseases","chronic respiratory disease","chronic respiratory diseases","infectious disease","infectious diseases","sexually-transmitted disease","sexually transmitted disease","sexually-transmitted diseases","sexually transmitted diseases","communicable disease","communicable diseases","patient with aids","people with aids","with hiv","hiv virus" ,"hiv/aids","human immunodeficiency virus","tuberculosis","malaria","hepatitis","polio","vaccin","cancer","diabet","maternal mortality","child mortality","childbirth complications","neonatal mortality","neo-natal mortality","premature mortality","infant mortality"
                ])

    cond4, evidence4 = does_contain_list(ti_abs_kw, 
            [
                "quality adjusted l year","maternal health","reproductive health","sexual health","preventable death","preventable deaths","tobacco control","substance abuse","drug abuse","tobacco use","alcohol use","substance addiction","drug addiction","tobacco addiction","alcoholism","suicid","postnatal depression","post-natal depression","zika virus","dengue","schistosomiasis","sleeping sickness","ebola","mental health","mental disorder","mental illness","mental illnesses","measles","neglected disease","neglected diseases","diarrhea","diarrhoea","cholera","dysentery","typhoid fever","traffic accident","traffic accidents","healthy lifestyle","life expectancy","life expectancies","health policy"
                ,["health system", "access"]
                ,["health system", "accessible"]
                ,"health risk","health risks","inclusive health","obesity","coronavirus","covid-19","covid 19","social determinants of health","psychological harm","psychological wellbeing","psychological well-being","psychological well being","public health","telemedecine","telecare","health reason","healthcare"
                ])

    if cond1 or cond2 or cond3 or cond4:
        return {"sdg_code": "sdg3", "sdg_label": "3. Good health and well-being"}
    return {}
