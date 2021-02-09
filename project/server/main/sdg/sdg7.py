from project.server.main.sdg.utils import does_contain, does_contain_list
from project.server.main.sdg.sdg_expressions import astronomy

def test_sdg7(asjc_list, ti_abs_kw):
    cond1, _ = does_contain_list(asjc_list, ["2100", "2101", "2102", "2103", "2104", "2105"])
    
    if None in asjc_list:
        cond2, evidence2_0 = True, 'none'
    else:
        cond2, _ = does_contain_list([asjc[0:2] for asjc in asjc_list], ["15","16","17","19","21","22","23","25","26","31","12","14","18","20","32","33","10","11"])
   

    cond3, _ = does_contain(ti_abs_kw, 
    ["renewable energy","renewable energies","energy efficiency" 
,"energy efficient","energy efficiencies","efficient energy" 
,"efficiency energy","efficiency of energy" 
,"energy self-sufficiency","solar power system" 
,"solar-generated energy","solar energy management" 
,"sustainable energy","universal electrification" 
,"rural electrification","rooftop solar" 
,"use of renewable energy","energy use efficiency" 
,"energy consumption","energy supply","electricity supply" 
,"low-carbon energy","nuclear power"
,"alternative energy" 
,"alternative energies","biodiesel" 
,"bioenergy","bioenergies","biofuel","biogas","energy crops","enhanced geothermal system","geothermal heat pump","geothermal heating","geothermal resource","geothermics","ground source heat pump","ground-coupled heat pump","hydropower","microbial fuel cell","solar cell","solar collector","thermal energy storage","water energy","wave energy" 
,"wind generator","wind park"
 ,"CO2 geological sequestration"
 ,"CO2 sequestration"
 ,"carbon sequestration"
   ,"carbon storage"
 ,"rooftop photovoltaic" 
 ,"active solar energy"
 ,"passive solar energy"
 ,"tidal energy"
 ,"tidal power"
   ,"geothermal power"
 ,"solar thermal power"
  ,"solar-thermal power"
  ,"hydroelectric power" 
  ,"solar building"
,"modern energy"
,"nuclear energy"
,"nuclear fuel cycle"
,"energy mix"
 ,"home solar system"
,"fossil fuel energies"
,"fossil fuel energy"
 ,"solar park"
 ,"nonrenewable energy"
 ,"hydro-electric power"
,"converting biomass"
,"convert biomass"
 ,"biomass conversion"
 ,"biomass energy"
 ,"geothermal plants"
 ,"geothermal energy"]
    )

    cond4, _ = does_contain(ti_abs_kw, 
    ["supply energy","supplying energy","energy conversion","energy transition","energy management","energy access","access to energy","clean energy technology","energy infrastructure","energy equity","energy justice","energy poverty","energy policy","energy policies","policy on energy","2000 Watt society","smart micro-grid","smart grid","smart microgrid","smart micro-grids","smart grids","smart microgrids","smart meter","smart meters","affordable electricity","affordable energy","electricity consumption","electrical power consumption","reliable electricity","reliable electrical power","power transmission network","clean fuel","access to electricity","clean cooking fuel","fuel poverty","energiewende"
,"photovoltaic","solar resource","solar panel","photocatalytic water splitting","wind power","solar energy system","solar energy power plant","wind energy","wind turbine","wind farm","wind power Generation","hydrogen production","water splitting","lithium-ion batteries","lithium-ion battery","heat network","district heat","district heating","heating equipment","residential energy consumption","domestic energy consumption","energy security","rural electrification","energy ladder","energy access","energy conservation","low-carbon society","hybrid renewable energy system","hybrid renewable energy systems","fuel switching"
,"energy governance"
,["photochemistry", "renewable energy"]
])
    cond5, _ = does_contain(ti_abs_kw, astronomy)
    cond6, _ = does_contain(ti_abs_kw, [
        ["energy conservation", "dissipative"],
        ["energy conservation", "dissipation"],
        ["energy conservation", "energy variable"],
        ["energy conservation", "energy–momentum conservation"],
        ["energy conservation", "pseudo-energy"]
        ])

    if cond1 or (cond2 and (cond3 or cond4)) and (not cond5) and (not cond6):
        return {"sdg_code": "sdg7", "sdg_label": "7. Affordable and clean energy"}
    return {}
