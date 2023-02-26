from economic_fuzzy import Economic_fuzzy
from environmental_fuzzy import Environmental_fuzzy
from social_fuzzy import Social_fuzzy
from second_stage_fuzzy import Final_fuzzy


def system(material_cost, labour_cost, lead_time, on_time_delivery, product_quality, 
           material_usage, recicled_used, water_usage, energy_usage, emissions, waste, 
           employee_satis, customer_satis, community_satis):
    """ Main function to execute the fuzzy logic procedure for the knowledge-based system"""

    eco=Economic_fuzzy(material_cost,labour_cost,lead_time,on_time_delivery,product_quality).run()

    env = Environmental_fuzzy(material_usage,recicled_used,water_usage,energy_usage,emissions,waste).run()

    soc=Social_fuzzy(employee_satis,customer_satis,community_satis).run()

    final_stage = Final_fuzzy(eco['FB4']['result'],env['FB5']['result'],soc['FB2']['result']).run()

    print(final_stage['name']+':',final_stage['FB_FINAL']['result'],final_stage['FB_FINAL']['membership_interp']['label'])
    return [eco,env,soc,final_stage]


if __name__=='__main__':
    send=system(1,1,1,1,1,1,1,1,1,1,1,1,1,1)