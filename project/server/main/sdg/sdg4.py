from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import dev_countries

def test_sdg4(asjc_list, ti_abs_kw):

    cond1_0, evidence1_0 = does_contain_list(asjc_list, ["3304","3204","3319","3316"])
    cond1_1, evidence1_1 = does_contain_list(asjc_list, ["3312"])
    cond1_2, evidence1_2 = does_contain(ti_abs_kw, ["education"])

    cond1 = cond1_0 or (cond1_1 and cond1_2)

    cond2, evidence2 = does_contain(ti_abs_kw, [
        "school attendance"
,"attending school"
,"school enrollment"
,"academic achievement"
,"educational development"
,"school enrolment"
,"inclusive education"
,"educational inequality"
,"educational inequalities"
,"education quality"
,"quality of education"
,"educational enrolment"
,"educational enrollment"
,"enrolment in higher education"
,"enrollment in higher education"
,"educational environment"
,"educational access"
,["development aid", "teacher training"]
,"early childhood education"
,"preprimary education"
,"tertiary education"
,"childhood education and care"
,"primary education"
,"basic education"
,"free education"
,"equitable education"
,"affordable education"
,"educational financial aid"
,"school safety"
,"safety in school"
,"educational inequality"
,"educational gap"
,["poverty trap", "schooling"]
,"special education needs"
,"inclusive education system"
,"education exclusion"
,"education dropouts"
,"sustainable development education"
,"education for sustainable development"
,"environmental education"
,"education policy"
,"educational policies"
,"international education"
,"education reform"
,["educational reform", "developing countries"]
,"educational governance"
,"education expenditure"
,"education policy"
,"educational policies"
,"education policies"
                ])

    cond3_0, _ = does_contain(ti_abs_kw, ["school","education","educational"])
    cond3_1, _ = does_contain(ti_abs_kw, ["Africa"
		,"least developed countries"
		,"landlocked country"
		,"developing country"
		,"landlocked countries"
		,"developing countries"
		,"small island developing States"] + dev_countries)
    cond3_2,_ = does_contain(ti_abs_kw, ["vocational training"
		,"information and communication technologies"
		,"information and communication technology"
		,"information communication technologies"
		,"communication and information technologies"])
    cond3_3 = cond3_1 and cond3_2


    cond3_4_tmp = [
  "adult literacy"
  ,"achieve literacy"
  ,"achieve numeracy"
  ,"numeracy rate"
  ,"literacy rate"
  ,["learning opportunities", "gender disparities"]
  ,["learning opportunities", "empowerment"]
  ,"gender disparities in education"
  ,["learning opportunity", "gender disparities"]
  ,["learning opportunity", "empowerment"]
  ,"youth empowerment"   
  ,"women empowerment"
  ,"equal opportunities"
  ,"child labour"
  ,"child labor"
  ,"discriminatory"
  ,["schooling", "gender disparities"]
  ,["schooling", "ethnic disparities"]
  ,["schooling", "racial disparities"]
  ,"global citizenship" 
  ,["developing countries", "school effects"]   
  ,"foreign aid" 
  ,["teacher training", "Africa"]
  ,["teacher training", "least developed countries"]
  ,["teacher training", "landlocked country"]
  ,["teacher training", "developing country"]
  ,["teacher training", "landlocked countries"]
  ,["teacher training", "developing countries"]
  ,["teacher training", "small island developing States"]
  ,"teacher attrition" 
  ]
    cond3_4_tmp += [["teacher training", k] for k in dev_countries]

    cond3_4 = does_contain(ti_abs_kw, cond3_4_tmp)

    cond3_5 = does_contain(ti_abs_kw, ["decent job" ,"with disabilities"])

    cond3 = cond3_0 and (cond3_3 or cond3_4 or cond3_5)

    if cond1 or cond2 or cond3:
        return {"sdg_code": "sdg4", "sdg_label": "4. Quality education"}
    return {}
