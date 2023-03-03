import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class Environmental_fuzzy:

    def __init__(self, musage,rmusage,wusage,eusage,emission,waste):
        self.range=np.arange(1,8,1)
        self.poor=[1,1,4]
        self.average=[3,4,5]
        self.good=[4,7,7]
        self.material_usage_value = musage
        self.recicled_material_value = rmusage
        self.water_usage_value = wusage
        self.energy_usage_value = eusage
        self.emissions_value = emission
        self.waste_value = waste

    def antecedent(self):
        self.material_usage=ctrl.Antecedent(self.range, 'Material usage')
        self.recicled_material_usage=ctrl.Antecedent(self.range, 'Recicled material usage')
        self.water_usage=ctrl.Antecedent(self.range, 'Water usage')
        self.energy_usage=ctrl.Antecedent(self.range, 'Energy usage')
        self.emissions=ctrl.Antecedent(self.range, 'Emissions')
        self.waste=ctrl.Antecedent(self.range, 'Waste')
        self.fis1_env_out = ctrl.Antecedent(self.range, 'Fis 1 env out')
        self.fis2_env_out = ctrl.Antecedent(self.range, 'Fis 2 env out')
        self.fis3_env_out = ctrl.Antecedent(self.range, 'Fis 3 env out')
        self.fis4_env_out = ctrl.Antecedent(self.range, 'Fis 4 env out')

        ##-----Membership Functions
        #FIS1
        self.material_usage['poor'] = fuzz.trimf(self.material_usage.universe, self.poor)
        self.material_usage['average'] = fuzz.trimf(self.material_usage.universe, self.average)
        self.material_usage['good'] = fuzz.trimf(self.material_usage.universe, self.good)

        self.recicled_material_usage['poor'] = fuzz.trimf(self.recicled_material_usage.universe, self.poor)
        self.recicled_material_usage['average'] = fuzz.trimf(self.recicled_material_usage.universe, self.average)
        self.recicled_material_usage['good'] = fuzz.trimf(self.recicled_material_usage.universe, self.good)

        #FIS2
        self.water_usage['poor'] = fuzz.trimf(self.water_usage.universe, self.poor)
        self.water_usage['average'] = fuzz.trimf(self.water_usage.universe, self.average)
        self.water_usage['good'] = fuzz.trimf(self.water_usage.universe, self.good)

        self.energy_usage['poor'] = fuzz.trimf(self.energy_usage.universe, self.poor)
        self.energy_usage['average'] = fuzz.trimf(self.energy_usage.universe, self.average)
        self.energy_usage['good'] = fuzz.trimf(self.energy_usage.universe, self.good)
        #FIS3
        self.emissions['poor'] = fuzz.trimf(self.emissions.universe, self.poor)
        self.emissions['average'] = fuzz.trimf(self.emissions.universe, self.average)
        self.emissions['good'] = fuzz.trimf(self.emissions.universe, self.good)

        self.waste['poor'] = fuzz.trimf(self.waste.universe, self.poor)
        self.waste['average'] = fuzz.trimf(self.waste.universe, self.average)
        self.waste['good'] = fuzz.trimf(self.waste.universe, self.good)
        #FIS4
        self.fis1_env_out['poor'] = fuzz.trimf(self.fis1_env_out.universe, self.poor)
        self.fis1_env_out['average'] = fuzz.trimf(self.fis1_env_out.universe, self.average)
        self.fis1_env_out['good'] = fuzz.trimf(self.fis1_env_out.universe, self.good)

        self.fis2_env_out['poor'] = fuzz.trimf(self.fis2_env_out.universe, self.poor)
        self.fis2_env_out['average'] = fuzz.trimf(self.fis2_env_out.universe, self.average)
        self.fis2_env_out['good'] = fuzz.trimf(self.fis2_env_out.universe, self.good)
        #FIS5
        self.fis3_env_out['poor'] = fuzz.trimf(self.fis3_env_out.universe, self.poor)
        self.fis3_env_out['average'] = fuzz.trimf(self.fis3_env_out.universe, self.average)
        self.fis3_env_out['good'] = fuzz.trimf(self.fis3_env_out.universe, self.good)

        self.fis4_env_out['poor'] = fuzz.trimf(self.fis4_env_out.universe, self.poor)
        self.fis4_env_out['average'] = fuzz.trimf(self.fis4_env_out.universe, self.average)
        self.fis4_env_out['good'] = fuzz.trimf(self.fis4_env_out.universe, self.good)

    def consequent(self):
        #FIS1_ENV
        self.fis1_env= ctrl.Consequent(self.range,'FIS1_ENV')
        self.fis1_env['poor'] = fuzz.trimf(self.fis1_env.universe, self.poor)
        self.fis1_env['average'] = fuzz.trimf(self.fis1_env.universe, self.average)
        self.fis1_env['good'] = fuzz.trimf(self.fis1_env.universe, self.good)

        #FIS2_ENV
        self.fis2_env = ctrl.Consequent(self.range,'FIS2_ENV')
        self.fis2_env['poor'] = fuzz.trimf(self.fis2_env.universe, self.poor)
        self.fis2_env['average'] = fuzz.trimf(self.fis2_env.universe, self.average)
        self.fis2_env['good'] = fuzz.trimf(self.fis2_env.universe, self.good)

        #FIS3_ENV
        self.fis3_env = ctrl.Consequent(self.range,'FIS3_ENV')
        self.fis3_env['poor'] = fuzz.trimf(self.fis3_env.universe, self.poor)
        self.fis3_env['average'] = fuzz.trimf(self.fis3_env.universe, self.average)
        self.fis3_env['good'] = fuzz.trimf(self.fis3_env.universe, self.good)

        #FIS4_ENV
        self.fis4_env = ctrl.Consequent(self.range,'FIS4_ENV')
        self.fis4_env['poor'] = fuzz.trimf(self.fis4_env.universe, self.poor)
        self.fis4_env['average'] = fuzz.trimf(self.fis4_env.universe, self.average)
        self.fis4_env['good'] = fuzz.trimf(self.fis4_env.universe, self.good)

        #FIS4_ENV
        self.fis5_env = ctrl.Consequent(self.range,'FIS5_ENV')
        self.fis5_env['poor'] = fuzz.trimf(self.fis5_env.universe, self.poor)
        self.fis5_env['average'] = fuzz.trimf(self.fis5_env.universe, self.average)
        self.fis5_env['good'] = fuzz.trimf(self.fis5_env.universe, self.good)
    
    def rules(self):
        #FIS1_ENV
        rule1fis1_env = ctrl.Rule(self.material_usage['poor'] & self.recicled_material_usage['poor'], self.fis1_env['poor'])
        rule2fis1_env = ctrl.Rule(self.material_usage['average'] & self.recicled_material_usage['poor'], self.fis1_env['poor'])
        rule3fis1_env = ctrl.Rule(self.material_usage['good'] & self.recicled_material_usage['poor'], self.fis1_env['average'])
        rule4fis1_env = ctrl.Rule(self.material_usage['poor'] & self.recicled_material_usage['average'], self.fis1_env['poor'])
        rule5fis1_env = ctrl.Rule(self.material_usage['average'] & self.recicled_material_usage['average'], self.fis1_env['average'])
        rule6fis1_env = ctrl.Rule(self.material_usage['good'] & self.recicled_material_usage['average'], self.fis1_env['average'])
        rule7fis1_env = ctrl.Rule(self.material_usage['poor'] & self.recicled_material_usage['good'], self.fis1_env['average'])
        rule8fis1_env = ctrl.Rule(self.material_usage['average'] & self.recicled_material_usage['good'], self.fis1_env['average'])
        rule9fis1_env = ctrl.Rule(self.material_usage['good'] & self.recicled_material_usage['good'], self.fis1_env['good'])

        #FIS2_ENV
        rule1fis2_env = ctrl.Rule(self.water_usage['poor'] & self.energy_usage['poor'], self.fis2_env['poor'])
        rule2fis2_env = ctrl.Rule(self.water_usage['average'] & self.energy_usage['poor'], self.fis2_env['poor'])
        rule3fis2_env = ctrl.Rule(self.water_usage['good'] & self.energy_usage['poor'], self.fis2_env['average'])
        rule4fis2_env = ctrl.Rule(self.water_usage['poor'] & self.energy_usage['average'], self.fis2_env['poor'])
        rule5fis2_env = ctrl.Rule(self.water_usage['average'] & self.energy_usage['average'], self.fis2_env['average'])
        rule6fis2_env = ctrl.Rule(self.water_usage['good'] & self.energy_usage['average'], self.fis2_env['average'])
        rule7fis2_env = ctrl.Rule(self.water_usage['poor'] & self.energy_usage['good'], self.fis2_env['average'])
        rule8fis2_env = ctrl.Rule(self.water_usage['average'] & self.energy_usage['good'], self.fis2_env['average'])
        rule9fis2_env = ctrl.Rule(self.water_usage['good'] & self.energy_usage['good'], self.fis2_env['good'])

        #FIS3_ENV = FIS2_ENV RESULT
        rule1fis3_env = ctrl.Rule(self.waste['poor'] & self.emissions['poor'], self.fis3_env['poor'])
        rule2fis3_env = ctrl.Rule(self.waste['average'] & self.emissions['poor'], self.fis3_env['poor'])
        rule3fis3_env = ctrl.Rule(self.waste['good'] & self.emissions['poor'], self.fis3_env['average'])
        rule4fis3_env = ctrl.Rule(self.waste['poor'] & self.emissions['average'], self.fis3_env['poor'])
        rule5fis3_env = ctrl.Rule(self.waste['average'] & self.emissions['average'], self.fis3_env['average'])
        rule6fis3_env = ctrl.Rule(self.waste['good'] & self.emissions['average'], self.fis3_env['average'])
        rule7fis3_env = ctrl.Rule(self.waste['poor'] & self.emissions['good'], self.fis3_env['average'])
        rule8fis3_env = ctrl.Rule(self.waste['average'] & self.emissions['good'], self.fis3_env['average'])
        rule9fis3_env = ctrl.Rule(self.waste['good'] & self.emissions['good'], self.fis3_env['good'])

        #FIS4_ENV = FIS1_ENV + FIS2_ENV
        rule1fis4_env = ctrl.Rule(self.fis1_env_out['poor'] & self.fis2_env_out['poor'], self.fis4_env['poor'])
        rule2fis4_env = ctrl.Rule(self.fis1_env_out['average'] & self.fis2_env_out['poor'], self.fis4_env['poor'])
        rule3fis4_env = ctrl.Rule(self.fis1_env_out['good'] & self.fis2_env_out['poor'], self.fis4_env['average'])
        rule4fis4_env = ctrl.Rule(self.fis1_env_out['poor'] & self.fis2_env_out['average'], self.fis4_env['poor'])
        rule5fis4_env = ctrl.Rule(self.fis1_env_out['average'] & self.fis2_env_out['average'], self.fis4_env['average'])
        rule6fis4_env = ctrl.Rule(self.fis1_env_out['good'] & self.fis2_env_out['average'], self.fis4_env['average'])
        rule7fis4_env = ctrl.Rule(self.fis1_env_out['poor'] & self.fis2_env_out['good'], self.fis4_env['average'])
        rule8fis4_env = ctrl.Rule(self.fis1_env_out['average'] & self.fis2_env_out['good'], self.fis4_env['average'])
        rule9fis4_env = ctrl.Rule(self.fis1_env_out['good'] & self.fis2_env_out['good'], self.fis4_env['good'])


        #FIS5_ENV = FIS4_ENV + FIS3_ENV
        rule1fis5_env = ctrl.Rule(self.fis4_env_out['poor'] & self.fis3_env_out['poor'], self.fis5_env['poor'])
        rule2fis5_env = ctrl.Rule(self.fis4_env_out['average'] & self.fis3_env_out['poor'], self.fis5_env['poor'])
        rule3fis5_env = ctrl.Rule(self.fis4_env_out['good'] & self.fis3_env_out['poor'], self.fis5_env['average'])
        rule4fis5_env = ctrl.Rule(self.fis4_env_out['poor'] & self.fis3_env_out['average'], self.fis5_env['poor'])
        rule5fis5_env = ctrl.Rule(self.fis4_env_out['average'] & self.fis3_env_out['average'], self.fis5_env['average'])
        rule6fis5_env = ctrl.Rule(self.fis4_env_out['good'] & self.fis3_env_out['average'], self.fis5_env['average'])
        rule7fis5_env = ctrl.Rule(self.fis4_env_out['poor'] & self.fis3_env_out['good'], self.fis5_env['average'])
        rule8fis5_env = ctrl.Rule(self.fis4_env_out['average'] & self.fis3_env_out['good'], self.fis5_env['average'])
        rule9fis5_env = ctrl.Rule(self.fis4_env_out['good'] & self.fis3_env_out['good'], self.fis5_env['good'])

        fis1_env_ctrl = ctrl.ControlSystem([rule1fis1_env,rule2fis1_env,rule3fis1_env,rule4fis1_env,rule5fis1_env,rule6fis1_env,rule7fis1_env,rule8fis1_env,rule9fis1_env])
        fis2_env_ctrl = ctrl.ControlSystem([rule1fis2_env,rule2fis2_env,rule3fis2_env,rule4fis2_env,rule5fis2_env,rule6fis2_env,rule7fis2_env,rule8fis2_env,rule9fis2_env])
        fis3_env_ctrl = ctrl.ControlSystem([rule1fis3_env,rule2fis3_env,rule3fis3_env,rule4fis3_env,rule5fis3_env,rule6fis3_env,rule7fis3_env,rule8fis3_env,rule9fis3_env])
        fis4_env_ctrl = ctrl.ControlSystem([rule1fis4_env,rule2fis4_env,rule3fis4_env,rule4fis4_env,rule5fis4_env,rule6fis4_env,rule7fis4_env,rule8fis4_env,rule9fis4_env])
        fis5_env_ctrl = ctrl.ControlSystem([rule1fis5_env,rule2fis5_env,rule3fis5_env,rule4fis5_env,rule5fis5_env,rule6fis5_env,rule7fis5_env,rule8fis5_env,rule9fis5_env])

        self.fissing1_env = ctrl.ControlSystemSimulation(fis1_env_ctrl)
        self.fissing2_env = ctrl.ControlSystemSimulation(fis2_env_ctrl)
        self.fissing3_env = ctrl.ControlSystemSimulation(fis3_env_ctrl)
        self.fissing4_env = ctrl.ControlSystemSimulation(fis4_env_ctrl)
        self.fissing5_env = ctrl.ControlSystemSimulation(fis5_env_ctrl)

    def desfuzzy(self):
        #Input
        self.fissing1_env.input['Material usage'] = self.material_usage_value
        self.fissing1_env.input['Recicled material usage'] = self.recicled_material_value
        self.fissing2_env.input['Water usage'] = self.water_usage_value
        self.fissing2_env.input['Energy usage'] = self.energy_usage_value
        self.fissing3_env.input['Waste'] = self.waste_value
        self.fissing3_env.input['Emissions'] = self.emissions_value
        #Crunch the numbers
        self.fissing1_env.compute()
        self.fissing2_env.compute()
        self.fissing3_env.compute()
        self.fissing4_env.input['Fis 1 env out'] = self.fissing1_env.output['FIS1_ENV']
        self.fissing4_env.input['Fis 2 env out'] = self.fissing2_env.output['FIS2_ENV']
        self.fissing4_env.compute()
        self.fissing5_env.input['Fis 3 env out'] = self.fissing3_env.output['FIS3_ENV']
        self.fissing5_env.input['Fis 4 env out'] = self.fissing4_env.output['FIS4_ENV']
        self.fissing5_env.compute()

    def run(self):
        self.antecedent()
        self.consequent()
        self.rules()
        self.desfuzzy()
    
        fb1={'meta':'Material Usage + Recicled Usage',
            'result':self.fissing1_env.output['FIS1_ENV'],
             'membership_interp':self.infer(self.fis1_env,self.fissing1_env,'FIS1_ENV')}
        
        fb2={'meta':'Water Usage + Energy Usage',
            'result':self.fissing2_env.output['FIS2_ENV'],
             'membership_interp':self.infer(self.fis2_env,self.fissing2_env,'FIS2_ENV')}

        fb3={'meta':'Emissions + Waste',
            'result':self.fissing3_env.output['FIS3_ENV'],
             'membership_interp':self.infer(self.fis3_env,self.fissing3_env,'FIS3_ENV')}

        fb4={'meta':'FB1 + FB2',
            'result':self.fissing4_env.output['FIS4_ENV'],
             'membership_interp':self.infer(self.fis4_env,self.fissing4_env,'FIS4_ENV')}
        
        fb5={'meta':'FB3 + FB4',
            'result':round(self.fissing5_env.output['FIS5_ENV'],2),
             'membership_interp':self.infer(self.fis5_env,self.fissing5_env,'FIS5_ENV')}
        
        return {'name':'Environmental',
                'FB1':fb1,'FB2':fb2,
                'FB3':fb3,'FB4':fb4,'FB5':fb5}

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
    Eco=Environmental_fuzzy(1,6,4,6,5,1)
    r=Eco.run()
    print(r)


    

