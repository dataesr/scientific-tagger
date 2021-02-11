from project.server.main.sdg.utils import does_contain, does_contain_list

def test_sdg11(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["3103"])
    if cond1:
        return {}
    
    cond2, _ = does_contain(ti_abs_kw, [
       "sustainable cities and communities"])
    cond3, _ = does_contain_list(asjc_list, ["3322"])
    
    cond4_0, _ = does_contain(ti_abs_kw, [
       " city " ," city." ," city," ," city;" ," city:"  
," cities " ," cities." ," cities," ," cities;" ," cities:" 
,"human settlement","human settlements","urban","metropolitan","metropole","town","municipal","municipality","municipalities"])
    
    cond4_1, _ = does_contain_list(asjc_list, ["2311","3305","3313"])
    cond4 = cond4_0 and cond4_1

    cond5_0, _ = does_contain(ti_abs_kw, [
    " city " ," city." ," city," ," city;" ," city:"
," cities " ," cities." ," cities," ," cities;" ," cities:"
,"human settlement","human settlements","urban","metropolitan","metropole","town","municipal","municipality","municipalities"])
    cond5_1, _ = does_contain(ti_abs_kw, [
    "gentrification" 
,"congestion" 
,"habitat" 
,"city planning"
,"transportation" 
,"public transport" 
,"housing" 
,"slum" 
,"sendai framework" 
,"Disaster Risk Reduction" 
,"DRR" 
,"smart city" 
,"smart cities" 
,"resilient building" 
,"resilient buildings" 
,"sustainable building" 
,"sustainable development" 
,"green roof"
,"sustainable buildings"
,"sustainable construction" 
,"building design" 
,"buildings design" 
,"urbanisation" 
,"urbanization" 
,"zero energy building" 
,"zero energy buildings" 
,"zero-energy building" 
,"zero-energy buildings" 
,"zero net energy building"
,"net-zero energy building"
,"net zero building"
,"zero-net energy building"
,"net zero energy building"
,"net-zero building"
,"green building"
,"basic service" 
,"basic services" 
,"governance" 
,"citizen participation" 
,"collaborative planning" 
,"participatory planning" 
,"inclusiveness" 
,"cultural heritage" 
,"natural heritage" 
,"UNESCO" 
,"disaster","flood"," storm","hurricane","water-related hazard","water related hazard"
,"ecological footprint" 
,"environmental footprint" 
,"waste" 
,"wastewater"
,"pollution" 
,"pollutant" 
,"waste water" 
,"water quality" 
,"quality of the water" 
,"sewage" 
,"sewer" 
,"water management"
,"recycling" 
,"circular economy" 
,"air quality" 
,"green space" 
,"green spaces" 
,"nature inclusive" 
,"nature inclusive building" 
,"nature inclusive buildings"])

    cond5 = cond5_0 and cond5_1
    

    if cond2 or cond3 or cond4 or cond5:
        return {"sdg_code": "sdg11", "sdg_label": "11. Sustainable cities anc communities"}
    return {}
