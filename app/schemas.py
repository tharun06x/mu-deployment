from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from datetime import date

class Details(BaseModel):
    age:Annotated[int,Field(...,title="Age of the patient",gt=0,le=120)]
    gender:Annotated[Literal['Male','Female'],Field(title='Gender of the patient')] 	
    diagnosis_date:Annotated[date,Field(title='Date of Diagnosis',description='The date should be in the form yyyy-mm-dd',examples=['2023-10-16','2017-04-07'])] 	
    cancer_stage:Annotated[Literal['Stage I','Stage II','Stage III','Stage IV'],Field(title='Cancer Stage')] 	
    family_history:Annotated[Literal['Yes','No'],Field(title='Family History of Cancer')]
    smoking_status:Annotated[Literal['Passive Smoker','Former Smoker','Never Smoked','Current Smoker'],Field(title='Smoking Status',description='If the patient is a smoker')] 	
    bmi:Annotated[float,Field(title='BMI',gt=10,lt=50)] 	
    cholesterol_level:Annotated[float,Field(title='Cholesterol level',gt=50,le=300)] 	
    hypertension:Annotated[Literal[1,0],Field(title='Hypertension Condition')] 	
    asthma:Annotated[Literal[1,0],Field(title='Asthma Condition')] 	
    cirrhosis:Annotated[Literal[1,0],Field(title='Cirrhosis Condition')]
    other_cancer:Annotated[Literal[1,0],Field(title='other Cancer Condition')]	
    treatment_type:Annotated[Literal['Chemotherapy','Surgery','Combined'],Field(title='Treatment type')]	 	
    end_treatment_date:Annotated[date,Field(title='Ending Date of Diagnosis',description='The date should be in the form yyyy-mm-dd',examples=['2023-11-30','2017-03-17'])]
    @computed_field
    @property
    def totalduration(self)->int:
        return(self.end_treatment_date-self.diagnosis_date).days