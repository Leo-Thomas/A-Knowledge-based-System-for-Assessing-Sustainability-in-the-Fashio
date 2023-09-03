import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class Social_fuzzy:

    def __init__(self, esatis,cusatis,cosatis):
        self.range=np.arange(1,8,1)
        self.poor=[1,1,4]
        self.average=[2,4,6]
        self.good=[4,7,7]
        self.employee_satisfaction_value = esatis
        self.customer_satisfaction_value = cusatis
        self.community_satisfaction_value = cosatis

    def antecedent(self):
        self.employee_satisfaction=ctrl.Antecedent(self.range, 'Employee Satisfaction')
        self.customer_satisfaction=ctrl.Antecedent(self.range, 'Customer Satisfaction')
        self.comunity_satisfaction=ctrl.Antecedent(self.range, 'Community Satisfaction')
        self.fis1_soc_out = ctrl.Antecedent(self.range, 'Fis1 soc out') 

        ##-----Membership Functions
        #FB1
        self.employee_satisfaction['poor'] = fuzz.trimf(self.employee_satisfaction.universe, self.poor)
        self.employee_satisfaction['average'] = fuzz.trimf(self.employee_satisfaction.universe, self.average)
        self.employee_satisfaction['good'] = fuzz.trimf(self.employee_satisfaction.universe, self.good)
        
        self.customer_satisfaction['poor'] = fuzz.trimf(self.customer_satisfaction.universe, self.poor)
        self.customer_satisfaction['average'] = fuzz.trimf(self.customer_satisfaction.universe, self.average)
        self.customer_satisfaction['good'] = fuzz.trimf(self.customer_satisfaction.universe, self.good)

        #FB2
        self.comunity_satisfaction['poor'] = fuzz.trimf(self.comunity_satisfaction.universe, self.poor)
        self.comunity_satisfaction['average'] = fuzz.trimf(self.comunity_satisfaction.universe, self.average)
        self.comunity_satisfaction['good'] = fuzz.trimf(self.comunity_satisfaction.universe, self.good)

        self.fis1_soc_out['poor'] = fuzz.trimf(self.fis1_soc_out.universe, self.poor)
        self.fis1_soc_out['average'] = fuzz.trimf(self.fis1_soc_out.universe, self.average)
        self.fis1_soc_out['good'] = fuzz.trimf(self.fis1_soc_out.universe, self.good)

    def consequent(self):
        #FIS1_SOC
        self.fis1_soc = ctrl.Consequent(self.range,'FIS1_SOC', defuzzify_method='mom')
        self.fis1_soc['poor'] = fuzz.trimf(self.fis1_soc.universe, self.poor)
        self.fis1_soc['average'] = fuzz.trimf(self.fis1_soc.universe, self.average)
        self.fis1_soc['good'] = fuzz.trimf(self.fis1_soc.universe, self.good)
        #FIS2_SOC
        self.fis2_soc = ctrl.Consequent(self.range,'FIS2_SOC', defuzzify_method='mom')
        self.fis2_soc['poor'] = fuzz.trimf(self.fis1_soc.universe, self.poor)
        self.fis2_soc['average'] = fuzz.trimf(self.fis1_soc.universe, self.average)
        self.fis2_soc['good'] = fuzz.trimf(self.fis1_soc.universe, self.good)
    
    
    def rules(self):
        #FIS1_SOC
        rule1fis1_soc = ctrl.Rule(self.employee_satisfaction['poor'] & self.customer_satisfaction['poor'], self.fis1_soc['poor'])
        rule2fis1_soc = ctrl.Rule(self.employee_satisfaction['average'] & self.customer_satisfaction['poor'], self.fis1_soc['poor'])
        rule3fis1_soc = ctrl.Rule(self.employee_satisfaction['good'] & self.customer_satisfaction['poor'], self.fis1_soc['average'])
        rule4fis1_soc = ctrl.Rule(self.employee_satisfaction['poor'] & self.customer_satisfaction['average'], self.fis1_soc['poor'])
        rule5fis1_soc = ctrl.Rule(self.employee_satisfaction['average'] & self.customer_satisfaction['average'], self.fis1_soc['average'])
        rule6fis1_soc = ctrl.Rule(self.employee_satisfaction['good'] & self.customer_satisfaction['average'], self.fis1_soc['average'])
        rule7fis1_soc = ctrl.Rule(self.employee_satisfaction['poor'] & self.customer_satisfaction['good'], self.fis1_soc['average'])
        rule8fis1_soc = ctrl.Rule(self.employee_satisfaction['average'] & self.customer_satisfaction['good'], self.fis1_soc['average'])
        rule9fis1_soc = ctrl.Rule(self.employee_satisfaction['good'] & self.customer_satisfaction['good'], self.fis1_soc['good'])

        #FIS2_SOC
        rule1fis2_soc = ctrl.Rule(self.fis1_soc_out['poor'] & self.comunity_satisfaction['poor'], self.fis2_soc['poor'])
        rule2fis2_soc = ctrl.Rule(self.fis1_soc_out['average'] & self.comunity_satisfaction['poor'], self.fis2_soc['poor'])
        rule3fis2_soc = ctrl.Rule(self.fis1_soc_out['good'] & self.comunity_satisfaction['poor'], self.fis2_soc['average'])
        rule4fis2_soc = ctrl.Rule(self.fis1_soc_out['poor'] & self.comunity_satisfaction['average'], self.fis2_soc['poor'])
        rule5fis2_soc = ctrl.Rule(self.fis1_soc_out['average'] & self.comunity_satisfaction['average'], self.fis2_soc['average'])
        rule6fis2_soc = ctrl.Rule(self.fis1_soc_out['good'] & self.comunity_satisfaction['average'], self.fis2_soc['average'])
        rule7fis2_soc = ctrl.Rule(self.fis1_soc_out['poor'] & self.comunity_satisfaction['good'], self.fis2_soc['average'])
        rule8fis2_soc = ctrl.Rule(self.fis1_soc_out['average'] & self.comunity_satisfaction['good'], self.fis2_soc['average'])
        rule9fis2_soc = ctrl.Rule(self.fis1_soc_out['good'] & self.comunity_satisfaction['good'], self.fis2_soc['good'])

        fis1_soc_ctrl = ctrl.ControlSystem([rule1fis1_soc,rule2fis1_soc,rule3fis1_soc,rule4fis1_soc,rule5fis1_soc,rule6fis1_soc,rule7fis1_soc,rule8fis1_soc,rule9fis1_soc])
        fis2_soc_ctrl = ctrl.ControlSystem([rule1fis2_soc,rule2fis2_soc,rule3fis2_soc,rule4fis2_soc,rule5fis2_soc,rule6fis2_soc,rule7fis2_soc,rule8fis2_soc,rule9fis2_soc])

        self.fissing1_soc = ctrl.ControlSystemSimulation(fis1_soc_ctrl)
        self.fissing2_soc = ctrl.ControlSystemSimulation(fis2_soc_ctrl)

    def desfuzzy(self):
        #Input
        self.fissing1_soc.input['Employee Satisfaction'] = self.employee_satisfaction_value
        self.fissing1_soc.input['Customer Satisfaction'] = self.customer_satisfaction_value
        #Crunch the numbers
        self.fissing1_soc.compute()
        self.fissing2_soc.input['Community Satisfaction'] = self.community_satisfaction_value
        self.fissing2_soc.input['Fis1 soc out'] = self.fissing1_soc.output['FIS1_SOC']
        self.fissing2_soc.compute()

    def run(self):
        self.antecedent()
        self.consequent()
        self.rules()
        self.desfuzzy()
    
        fb1={'meta':'Employee Satisfaction + Customer Satisfaction',
            'result':self.fissing1_soc.output['FIS1_SOC'],
             'membership_interp':self.infer(self.fis1_soc,self.fissing1_soc,'FIS1_SOC')}
        
        fb2={'meta':'Lead Time + On time delivery',
            'result':round(self.fissing2_soc.output['FIS2_SOC'],2),
             'membership_interp':self.infer(self.fis2_soc,self.fissing2_soc,'FIS2_SOC')}

        return {'name':'Social',
                'FB1':fb1,'FB2':fb2}

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
    Eco=Social_fuzzy(1,1,1)
    r=Eco.run()
    print(r)


    

