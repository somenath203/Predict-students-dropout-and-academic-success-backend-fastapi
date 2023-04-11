from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd 
import pickle


app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# studentSuccessPredictorData = pd.read_csv('data.csv')

model = pickle.load(open('predict_student_dropout_academic_success.pkl', 'rb'))


class StudentInfoModel(BaseModel):
    course: int
    daytime_evening_attendance: int
    prev_qualification: int
    prev_qualification_grade: int
    admission_grade: int
    educational_special_needs: int
    tution_fees_upto_date: int
    gender: int
    scholarship_holder: int 
    age_of_enrollement: int 
    cirricular_units_first_unit_sem_credited: int
    cirricular_units_first_unit_sem_enrolled: int 
    cirricular_units_first_unit_sem_evaluations: int 
    cirricular_units_first_unit_sem_approved: int
    cirricular_units_first_unit_sem_grade: int 
    cirricular_units_first_unit_sem_without_evaluations: int 
    cirricular_units_second_unit_sem_credited: int 
    cirricular_units_second_unit_sem_enrolled: int 
    cirricular_units_second_unit_sem_evaluations: int 
    cirricular_units_second_unit_sem_approved: int 
    cirricular_units_second_unit_sem_grade: int 
    cirricular_units_second_unit_sem_without_evaluations: int



@app.post('/')
async def welcome_msg():
    return {
        'success' : True,
        'message' : 'The server of "predict student dropout and academic success" is running successfully'
    } 
    
    
@app.post('/predict')
async def predict(studentInfo: StudentInfoModel):
    course: studentInfo.course
    daytimeEveningAttendance: studentInfo.daytime_evening_attendance
    previousQualification: studentInfo.prev_qualification
    previousQualificationGrade: studentInfo.prev_qualification_grade
    admissionGrade: studentInfo.admission_grade
    educationSpecialNeeds: studentInfo.educational_special_needs
    tutionFeesUptoDate: studentInfo.tution_fees_upto_date
    gender: studentInfo.gender
    scholarshipHolder: studentInfo.scholarship_holder
    ageOfEnrollement: studentInfo.age_of_enrollement
    cirricularUnitFirstSemCredited: studentInfo.cirricular_units_first_unit_sem_credited
    cirricularUnitFirstSemEnrolled: studentInfo.cirricular_units_first_unit_sem_enrolled
    cirricularUnitFirstSemEvaluation: studentInfo.cirricular_units_first_unit_sem_evaluations
    cirricularUnitFirstSemApproved: studentInfo.cirricular_units_first_unit_sem_approved
    cirricularUnitFirstSemGrade: studentInfo.cirricular_units_first_unit_sem_grade
    cirricularUnitFirstSemWithoutEvalutaion: studentInfo.cirricular_units_first_unit_sem_without_evaluations
    cirricularUnitSecondSemCredited: studentInfo.cirricular_units_second_unit_sem_credited
    cirricularUnitSecondSemEnrolled: studentInfo.cirricular_units_second_unit_sem_enrolled
    cirricularUnitSecondSemEvaluation: studentInfo.cirricular_units_second_unit_sem_evaluations
    cirricularUnitSecondSemApproved: studentInfo.cirricular_units_second_unit_sem_approved
    cirricularUnitSecondSemGrade: studentInfo.cirricular_units_second_unit_sem_grade
    cirricularUnitSecondSemWithoutEvaluation: studentInfo.cirricular_units_second_unit_sem_without_evaluations