data_files = [
    {
        "name": "iris",
        "drop_columns": ["Id"],
        "encode_columns": ["Species"],
        "target": "Species",
        "sep": ",",
        "no_scale":["Species"],
        "is_multiclass":True
    },
    {
        "name": "parkinsons",
        "drop_columns": [],
        "encode_columns": ["name"],
        "target": "status",
        "sep": ",",
        "no_scale":["status"],
        "is_multiclass":False
    },
    {
        "name": "cirrhosis",
        "drop_columns": ["ID"],
        "encode_columns": ["Drug", "Status", "Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema", "Stage"],
        "target": "Stage",
        "sep": ",",
        "no_scale":["Stage", "Drug", "Status", "Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema"],
        "is_multiclass":True
    },
    {
        "name": "diabetes",
        "drop_columns": [],
        "encode_columns": [],
        "target": "Outcome",
        "sep": ",",
        "no_scale":["Outcome", "Age", "BMI", "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "DiabetesPedigreeFunction"],
        "is_multiclass":False
    },
    {
        "name": "heart_disease",
        "drop_columns": [],
        "encode_columns": [],
        "target": "condition",
        "sep": ",",
        "no_scale":["condition", "sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"],
        "is_multiclass":False
    },
    {
        "name": "sonar",
        "drop_columns": [],
        "encode_columns": ["Class"],
        "target": "Class",
        "sep": ",",
        "no_scale":["Class"],
        "is_multiclass":False
    },
    {
        "name": "stroke",
        "drop_columns": ["id"],
        "encode_columns": ["gender", "ever_married", "work_type", "Residence_type", "smoking_status"],
        "target": "stroke",
        "sep": ",",
        "no_scale":["stroke", "gender", "ever_married", "work_type", "Residence_type", "smoking_status"],
        "is_multiclass":False
    },
    {
        "name": "abalone",
        "drop_columns": [],
        "encode_columns": [],
        "target": "Age Class",
        "sep": ",",
        "no_scale":["Age Class"],
        "is_multiclass":True
    },
    {
        "name": "wine",
        "drop_columns": [],
        "encode_columns": [],
        "target": "quality",
        "sep": ",",
        "no_scale":["quality"],
        "is_multiclass":False
    },
    {
        "name": "breast",
        "drop_columns": ["id", "Unnamed: 32"],
        "encode_columns": ["diagnosis"],
        "target": "diagnosis",
        "sep": ",",
        "no_scale":["diagnosis"],
        "is_multiclass":False
    }
]
