import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class Final_fuzzy:

    def __init__(self, fbeco,fbenv,fbsoc):
        self.range=np.arange(1,8,1)
        self.poor=[1,1,4]
        self.average=[2,4,6]
        self.good=[4,7,7]
        self.fb_economic_value = fbeco
        self.fb_environmental_value = fbenv
        self.fb_social_value = fbsoc

    def antecedent(self):
        self.fis_final_eco=ctrl.Antecedent(self.range, 'Fis final eco')
        self.fis_final_env=ctrl.Antecedent(self.range, 'Fis final env')
        self.fis_final_soc=ctrl.Antecedent(self.range, 'Fis final soc')

        ##-----Membership Functions
        #FB1
        self.fis_final_eco['poor'] = fuzz.trimf(self.fis_final_eco.universe, self.poor)
        self.fis_final_eco['average'] = fuzz.trimf(self.fis_final_eco.universe, self.average)
        self.fis_final_eco['good'] = fuzz.trimf(self.fis_final_eco.universe, self.good)
        
        self.fis_final_env['poor'] = fuzz.trimf(self.fis_final_env.universe, self.poor)
        self.fis_final_env['average'] = fuzz.trimf(self.fis_final_env.universe, self.average)
        self.fis_final_env['good'] = fuzz.trimf(self.fis_final_env.universe, self.good)

        #FB2
        self.fis_final_soc['poor'] = fuzz.trimf(self.fis_final_soc.universe, self.poor)
        self.fis_final_soc['average'] = fuzz.trimf(self.fis_final_soc.universe, self.average)
        self.fis_final_soc['good'] = fuzz.trimf(self.fis_final_soc.universe, self.good)

    def consequent(self):
        #FIS1_SOC
        self.fis_final = ctrl.Consequent(self.range,'FIS_FINAL', defuzzify_method='mom')
        self.fis_final['poor'] = fuzz.trimf(self.fis_final.universe, self.poor)
        self.fis_final['average'] = fuzz.trimf(self.fis_final.universe, self.average)
        self.fis_final['good'] = fuzz.trimf(self.fis_final.universe, self.good)
    
    def rules(self):
        rule1_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['poor'] & self.fis_final_soc['poor'], self.fis_final['poor'])
        rule2_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['poor'] & self.fis_final_soc['average'], self.fis_final['poor'])
        rule3_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['poor'] & self.fis_final_soc['good'], self.fis_final['poor'])
        rule4_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['average'] & self.fis_final_soc['poor'], self.fis_final['poor'])
        rule5_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['average'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule6_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['average'] & self.fis_final_soc['good'], self.fis_final['average'])
        rule7_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['good'] & self.fis_final_soc['poor'], self.fis_final['poor'])
        rule8_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['good'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule9_final = ctrl.Rule(self.fis_final_eco['poor'] & self.fis_final_env['good'] & self.fis_final_soc['good'], self.fis_final['average'])

        rule10_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['poor'] & self.fis_final_soc['poor'], self.fis_final['poor'])
        rule11_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['poor'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule12_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['poor'] & self.fis_final_soc['good'], self.fis_final['average'])
        rule13_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['average'] & self.fis_final_soc['poor'], self.fis_final['average'])
        rule14_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['average'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule15_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['average'] & self.fis_final_soc['good'], self.fis_final['average'])
        rule16_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['good'] & self.fis_final_soc['poor'], self.fis_final['average'])
        rule17_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['good'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule18_final = ctrl.Rule(self.fis_final_eco['average'] & self.fis_final_env['good'] & self.fis_final_soc['good'], self.fis_final['average'])

        rule19_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['poor'] & self.fis_final_soc['poor'], self.fis_final['poor'])
        rule20_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['poor'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule21_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['poor'] & self.fis_final_soc['good'], self.fis_final['average'])
        rule22_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['average'] & self.fis_final_soc['poor'], self.fis_final['average'])
        rule23_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['average'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule24_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['average'] & self.fis_final_soc['good'], self.fis_final['average'])
        rule25_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['good'] & self.fis_final_soc['poor'], self.fis_final['average'])
        rule26_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['good'] & self.fis_final_soc['average'], self.fis_final['average'])
        rule27_final = ctrl.Rule(self.fis_final_eco['good'] & self.fis_final_env['good'] & self.fis_final_soc['good'], self.fis_final['good'])


        fis_final_ctrl = ctrl.ControlSystem([rule1_final,rule2_final,rule3_final,rule4_final,rule5_final,rule6_final,rule7_final,rule8_final,rule9_final,
                                     rule10_final,rule11_final,rule12_final,rule13_final,rule14_final,rule15_final,rule16_final,rule17_final,rule18_final,
                                     rule19_final,rule20_final,rule21_final,rule22_final,rule23_final,rule24_final,rule25_final,rule26_final,rule27_final])

        self.fissing_final = ctrl.ControlSystemSimulation(fis_final_ctrl)

    def desfuzzy(self):
        self.fissing_final.input['Fis final eco'] = self.fb_economic_value
        self.fissing_final.input['Fis final env'] = self.fb_environmental_value
        self.fissing_final.input['Fis final soc'] = self.fb_social_value
        self.fissing_final.compute()

    def run(self):
        self.antecedent()
        self.consequent()
        self.rules()
        self.desfuzzy()
    
        fb_final={'meta':'FB_ECO + FB_ENV + FB_SOC',
            'result':round(self.fissing_final.output['FIS_FINAL'],2),
             'membership_interp':self.infer(self.fis_final,self.fissing_final,'FIS_FINAL')}

        return {'name':'Susteinability Score',
                'FB_FINAL':fb_final}

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
    Eco=Final_fuzzy(5,5,5)
    r=Eco.run()
    print(r)
    print(Eco)


    

