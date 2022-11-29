data_files = [
    {
        "name": "iris",
        "drop_columns": ["Id"],
        "encode_columns": ["Species"],
        "target": "Species",
        "sep": ",",
        "no_scale":["Species"]
    },
    {
        "name": "parkinsons",
        "drop_columns": [],
        "encode_columns": ["name"],
        "target": "status",
        "sep": ",",
        "no_scale":["status"]
    },
    {
        "name": "cirrhosis",
        "drop_columns": ["ID"],
        "encode_columns": ["Drug", "Status", "Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema", "Stage"],
        "target": "Stage",
        "sep": ",",
        "no_scale":["Stage", "Drug", "Status", "Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema"]
    },
    {
        "name": "diabetes",
        "drop_columns": [],
        "encode_columns": [],
        "target": "Outcome",
        "sep": ",",
        "no_scale":["Outcome", "Age", "BMI", "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "DiabetesPedigreeFunction"]
    },
    {
        "name": "heart_disease",
        "drop_columns": [],
        "encode_columns": [],
        "target": "condition",
        "sep": ",",
        "no_scale":["condition", "sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]
    },
    {
        "name": "sonar",
        "drop_columns": [],
        "encode_columns": ["Class"],
        "target": "Class",
        "sep": ",",
        "no_scale":["Class"]
    },
    {
        "name": "stroke",
        "drop_columns": ["id"],
        "encode_columns": ["gender", "ever_married", "work_type", "Residence_type", "smoking_status"],
        "target": "stroke",
        "sep": ",",
        "no_scale":["stroke", "gender", "ever_married", "work_type", "Residence_type", "smoking_status"]
    },
    # {
    #     "name": "covtype",
    #     "drop_columns": [],
    #     "encode_columns": [],
    #     "target": "Cover_Type",
    #     "sep": ",",
    #     "no_scale":["Cover_Type"]
    # },
    {
        "name": "wine",
        "drop_columns": [],
        "encode_columns": [],
        "target": "quality",
        "sep": ";",
        "no_scale":["quality"]
    },
    {
        "name": "breast",
        "drop_columns": ["id", "Unnamed: 32"],
        "encode_columns": ["diagnosis"],
        "target": "diagnosis",
        "sep": ",",
        "no_scale":["diagnosis"]
    }
]
