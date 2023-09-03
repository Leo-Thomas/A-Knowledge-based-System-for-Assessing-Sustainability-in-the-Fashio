import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class Economic_fuzzy:

    def __init__(self, mcost,lcost,ltime,timedeli,pquality):
        self.range=np.arange(1,8,1)
        self.poor=[1,1,4]
        self.average=[2,4,6]
        self.good=[4,7,7]
        self.material_cost_value = mcost
        self.labour_cost_value = lcost
        self.lead_time_value = ltime
        self.on_time_delivery_value = timedeli
        self.product_quality_value = pquality

    def antecedent(self):
        #FIS1
        self.material_cost=ctrl.Antecedent(self.range, 'Material cost')
        self.labour_cost=ctrl.Antecedent(self.range, 'Labour cost')
        #FIS2
        self.lead_time=ctrl.Antecedent(self.range, 'Lead time')
        self.on_time_delivery=ctrl.Antecedent(self.range, 'On-time delivery')
        #FIS4
        self.product_quality=ctrl.Antecedent(self.range, 'Product quality')
        self.fis3_eco_out = ctrl.Antecedent(self.range, 'Fis3 eco out')
        #FIS31
        self.fis1_eco_out = ctrl.Antecedent(self.range, 'Fis1 eco out')
        self.fis2_eco_out = ctrl.Antecedent(self.range, 'Fis2 eco out')
        ##-----Membership Functions
        self.material_cost['poor'] = fuzz.trimf(self.material_cost.universe, self.poor)
        self.material_cost['average'] = fuzz.trimf(self.material_cost.universe, self.average)
        self.material_cost['good'] = fuzz.trimf(self.material_cost.universe, self.good)
        
        self.labour_cost['poor'] = fuzz.trimf(self.labour_cost.universe, self.poor)
        self.labour_cost['average'] = fuzz.trimf(self.labour_cost.universe, self.average)
        self.labour_cost['good'] = fuzz.trimf(self.labour_cost.universe, self.good)

        #FIS2
        self.lead_time['poor'] = fuzz.trimf(self.lead_time.universe, self.poor)
        self.lead_time['average'] = fuzz.trimf(self.lead_time.universe, self.average)
        self.lead_time['good'] = fuzz.trimf(self.lead_time.universe, self.good)

        self.on_time_delivery['poor'] = fuzz.trimf(self.on_time_delivery.universe, self.poor)
        self.on_time_delivery['average'] = fuzz.trimf(self.on_time_delivery.universe, self.average)
        self.on_time_delivery['good'] = fuzz.trimf(self.on_time_delivery.universe, self.good)
        #FIS3
        self.fis1_eco_out['poor'] = fuzz.trimf(self.fis1_eco_out.universe, self.poor)
        self.fis1_eco_out['average'] = fuzz.trimf(self.fis1_eco_out.universe, self.average)
        self.fis1_eco_out['good'] = fuzz.trimf(self.fis1_eco_out.universe, self.good)

        self.fis2_eco_out['poor'] = fuzz.trimf(self.fis2_eco_out.universe, self.poor)
        self.fis2_eco_out['average'] = fuzz.trimf(self.fis2_eco_out.universe, self.average)
        self.fis2_eco_out['good'] = fuzz.trimf(self.fis2_eco_out.universe, self.good)
        #FIS4
        self.product_quality['poor'] = fuzz.trimf(self.product_quality.universe, self.poor)
        self.product_quality['average'] = fuzz.trimf(self.product_quality.universe, self.average)
        self.product_quality['good'] = fuzz.trimf(self.product_quality.universe, self.good)

        self.fis3_eco_out['poor'] = fuzz.trimf(self.fis3_eco_out.universe, self.poor)
        self.fis3_eco_out['average'] = fuzz.trimf(self.fis3_eco_out.universe, self.average)
        self.fis3_eco_out['good'] = fuzz.trimf(self.fis3_eco_out.universe, self.good)



    def consequent(self):
        #FIS1_ECO
        self.fis1_eco = ctrl.Consequent(self.range,'FIS1_ECO',defuzzify_method='mom')
        self.fis1_eco['poor'] = fuzz.trimf(self.fis1_eco.universe, self.poor)
        self.fis1_eco['average'] = fuzz.trimf(self.fis1_eco.universe, self.average)
        self.fis1_eco['good'] = fuzz.trimf(self.fis1_eco.universe, self.good)
        #FIS2_ECO
        self.fis2_eco = ctrl.Consequent(self.range,'FIS2_ECO', defuzzify_method='mom')
        self.fis2_eco['poor'] = fuzz.trimf(self.fis2_eco.universe, self.poor)
        self.fis2_eco['average'] = fuzz.trimf(self.fis2_eco.universe, self.average)
        self.fis2_eco['good'] = fuzz.trimf(self.fis2_eco.universe, self.good)
        #FIS3_ECO
        self.fis3_eco = ctrl.Consequent(self.range,'FIS3_ECO', defuzzify_method='mom')
        self.fis3_eco['poor'] = fuzz.trimf(self.fis3_eco.universe, self.poor)
        self.fis3_eco['average'] = fuzz.trimf(self.fis3_eco.universe, self.average)
        self.fis3_eco['good'] = fuzz.trimf(self.fis3_eco.universe, self.good)
        #FIS4_ECO
        self.fis4_eco = ctrl.Consequent(self.range,'FIS4_ECO', defuzzify_method='mom')
        self.fis4_eco['poor'] = fuzz.trimf(self.fis4_eco.universe, self.poor)
        self.fis4_eco['average'] = fuzz.trimf(self.fis4_eco.universe, self.average)
        self.fis4_eco['good'] = fuzz.trimf(self.fis4_eco.universe, self.good)
    
    def rules(self):
        #FIS1_ECO
        rule1fis1_eco = ctrl.Rule(self.material_cost['poor'] & self.labour_cost['poor'], self.fis1_eco['poor'])
        rule2fis1_eco = ctrl.Rule(self.material_cost['average'] & self.labour_cost['poor'], self.fis1_eco['poor'])
        rule3fis1_eco = ctrl.Rule(self.material_cost['good'] & self.labour_cost['poor'], self.fis1_eco['average'])
        rule4fis1_eco = ctrl.Rule(self.material_cost['poor'] & self.labour_cost['average'], self.fis1_eco['poor'])
        rule5fis1_eco = ctrl.Rule(self.material_cost['average'] & self.labour_cost['average'], self.fis1_eco['average'])
        rule6fis1_eco = ctrl.Rule(self.material_cost['good'] & self.labour_cost['average'], self.fis1_eco['average'])
        rule7fis1_eco = ctrl.Rule(self.material_cost['poor'] & self.labour_cost['good'], self.fis1_eco['average'])
        rule8fis1_eco = ctrl.Rule(self.material_cost['average'] & self.labour_cost['good'], self.fis1_eco['average'])
        rule9fis1_eco = ctrl.Rule(self.material_cost['good'] & self.labour_cost['good'], self.fis1_eco['good'])
        #FIS2_ECO
        rule1fis2_eco = ctrl.Rule(self.lead_time['poor'] & self.on_time_delivery['poor'], self.fis2_eco['poor'])
        rule2fis2_eco = ctrl.Rule(self.lead_time['average'] & self.on_time_delivery['poor'], self.fis2_eco['poor'])
        rule3fis2_eco = ctrl.Rule(self.lead_time['good'] & self.on_time_delivery['poor'], self.fis2_eco['average'])
        rule4fis2_eco = ctrl.Rule(self.lead_time['poor'] & self.on_time_delivery['average'], self.fis2_eco['poor'])
        rule5fis2_eco = ctrl.Rule(self.lead_time['average'] & self.on_time_delivery['average'], self.fis2_eco['average'])
        rule6fis2_eco = ctrl.Rule(self.lead_time['good'] & self.on_time_delivery['average'], self.fis2_eco['average'])
        rule7fis2_eco = ctrl.Rule(self.lead_time['poor'] & self.on_time_delivery['good'], self.fis2_eco['average'])
        rule8fis2_eco = ctrl.Rule(self.lead_time['average'] & self.on_time_delivery['good'], self.fis2_eco['average'])
        rule9fis2_eco = ctrl.Rule(self.lead_time['good'] & self.on_time_delivery['good'], self.fis2_eco['good'])
        #FIS3_ECO
        rule1fis3_eco = ctrl.Rule(self.fis1_eco_out['poor'] & self.fis2_eco_out['poor'], self.fis3_eco['poor'])
        rule2fis3_eco = ctrl.Rule(self.fis1_eco_out['average'] & self.fis2_eco_out['poor'], self.fis3_eco['poor'])
        rule3fis3_eco = ctrl.Rule(self.fis1_eco_out['good'] & self.fis2_eco_out['poor'], self.fis3_eco['average'])
        rule4fis3_eco = ctrl.Rule(self.fis1_eco_out['poor'] & self.fis2_eco_out['average'], self.fis3_eco['poor'])
        rule5fis3_eco = ctrl.Rule(self.fis1_eco_out['average'] & self.fis2_eco_out['average'], self.fis3_eco['average'])
        rule6fis3_eco = ctrl.Rule(self.fis1_eco_out['good'] & self.fis2_eco_out['average'], self.fis3_eco['average'])
        rule7fis3_eco = ctrl.Rule(self.fis1_eco_out['poor'] & self.fis2_eco_out['good'], self.fis3_eco['average'])
        rule8fis3_eco = ctrl.Rule(self.fis1_eco_out['average'] & self.fis2_eco_out['good'], self.fis3_eco['average'])
        rule9fis3_eco = ctrl.Rule(self.fis1_eco_out['good'] & self.fis2_eco_out['good'], self.fis3_eco['good'])

        #FIS4_ECO
        rule1fis4_eco = ctrl.Rule(self.product_quality['poor'] & self.fis3_eco_out['poor'], self.fis4_eco['poor'])
        rule2fis4_eco = ctrl.Rule(self.product_quality['average'] & self.fis3_eco_out['poor'], self.fis4_eco['poor'])
        rule3fis4_eco = ctrl.Rule(self.product_quality['good'] & self.fis3_eco_out['poor'], self.fis4_eco['average'])
        rule4fis4_eco = ctrl.Rule(self.product_quality['poor'] & self.fis3_eco_out['average'], self.fis4_eco['poor'])
        rule5fis4_eco = ctrl.Rule(self.product_quality['average'] & self.fis3_eco_out['average'], self.fis4_eco['average'])
        rule6fis4_eco = ctrl.Rule(self.product_quality['good'] & self.fis3_eco_out['average'], self.fis4_eco['average'])
        rule7fis4_eco = ctrl.Rule(self.product_quality['poor'] & self.fis3_eco_out['good'], self.fis4_eco['average'])
        rule8fis4_eco = ctrl.Rule(self.product_quality['average'] & self.fis3_eco_out['good'], self.fis4_eco['average'])
        rule9fis4_eco = ctrl.Rule(self.product_quality['good'] & self.fis3_eco_out['good'], self.fis4_eco['good'])

        fis1_eco_ctrl = ctrl.ControlSystem([rule1fis1_eco,rule2fis1_eco,rule3fis1_eco,rule4fis1_eco,rule5fis1_eco,rule6fis1_eco,rule7fis1_eco,rule8fis1_eco,rule9fis1_eco])
        fis2_eco_ctrl = ctrl.ControlSystem([rule1fis2_eco,rule2fis2_eco,rule3fis2_eco,rule4fis2_eco,rule5fis2_eco,rule6fis2_eco,rule7fis2_eco,rule8fis2_eco,rule9fis2_eco])
        fis3_eco_ctrl = ctrl.ControlSystem([rule1fis3_eco,rule2fis3_eco,rule3fis3_eco,rule4fis3_eco,rule5fis3_eco,rule6fis3_eco,rule7fis3_eco,rule8fis3_eco,rule9fis3_eco])
        fis4_eco_ctrl = ctrl.ControlSystem([rule1fis4_eco,rule2fis4_eco,rule3fis4_eco,rule4fis4_eco,rule5fis4_eco,rule6fis4_eco,rule7fis4_eco,rule8fis4_eco,rule9fis4_eco])

        self.fissing1_eco = ctrl.ControlSystemSimulation(fis1_eco_ctrl)
        self.fissing2_eco = ctrl.ControlSystemSimulation(fis2_eco_ctrl)
        self.fissing3_eco = ctrl.ControlSystemSimulation(fis3_eco_ctrl)
        self.fissing4_eco = ctrl.ControlSystemSimulation(fis4_eco_ctrl)

    def desfuzzy(self):
        #Input
        self.fissing1_eco.input['Material cost'] = self.material_cost_value
        self.fissing1_eco.input['Labour cost'] = self.labour_cost_value
        self.fissing2_eco.input['Lead time'] = self.lead_time_value
        self.fissing2_eco.input['On-time delivery'] = self.on_time_delivery_value
        #Crunch the numbers
        self.fissing1_eco.compute()
        self.fissing2_eco.compute()
        self.fissing3_eco.input['Fis1 eco out'] = self.fissing1_eco.output['FIS1_ECO']
        self.fissing3_eco.input['Fis2 eco out'] = self.fissing2_eco.output['FIS2_ECO']
        self.fissing3_eco.compute()
        self.fissing4_eco.input['Product quality'] = self.product_quality_value
        self.fissing4_eco.input['Fis3 eco out'] = self.fissing3_eco.output['FIS3_ECO']
        self.fissing4_eco.compute()

    def run(self):
        self.antecedent()
        self.consequent()
        self.rules()
        self.desfuzzy()
    
        fb1={'meta':'Material Cost + Labour Cost',
            'result':self.fissing1_eco.output['FIS1_ECO'],
             'membership_interp':self.infer(self.fis1_eco,self.fissing1_eco,'FIS1_ECO')}
        
        fb2={'meta':'Lead Time + On time delivery',
            'result':self.fissing2_eco.output['FIS2_ECO'],
             'membership_interp':self.infer(self.fis2_eco,self.fissing2_eco,'FIS2_ECO')}

        fb3={'meta':'FB1 + FB2',
            'result':self.fissing3_eco.output['FIS3_ECO'],
             'membership_interp':self.infer(self.fis3_eco,self.fissing3_eco,'FIS3_ECO')}

        fb4={'meta':'Product Quality + FB3',
            'result':round(self.fissing4_eco.output['FIS4_ECO'],2),
             'membership_interp':self.infer(self.fis4_eco,self.fissing4_eco,'FIS4_ECO')}
        return {'name':'Economic',
                'FB1':fb1,'FB2':fb2,
                'FB3':fb3,'FB4':fb4}

    def infer(self,fbox,fboxing,name):
        RESULT= fboxing.output[name]
        poor=fuzz.interp_membership(fbox.universe, fbox['poor'].mf, RESULT)
        average=fuzz.interp_membership(fbox.universe, fbox['average'].mf, RESULT)
        good = fuzz.interp_membership(fbox.universe, fbox['good'].mf, RESULT)
        result = {'poor':poor,'average':average,'good':good}
        winner = np.argmax([poor,average,good])
        result['label']=list(result.items())[winner][0]
        return result


if __name__=='__main__':
    Eco=Economic_fuzzy(1,6,1,6,1)
    r=Eco.run()
    print(r)


    

