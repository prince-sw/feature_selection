data_files = [
    {
        "name": "iris",
        "drop_columns": ["Id"],
        "encode_columns": ["Species"],
        "target": "Species",
        "sep": ","
    },
    {
        "name": "parkinsons",
        "drop_columns": [],
        "encode_columns": ["name"],
        "target": "status",
        "sep": ","
    },
    {
        "name": "cirrhosis",
        "drop_columns": ["ID"],
        "encode_columns": ["Drug", "Status", "Sex", "Ascites", "Hepatomegaly", "Spiders", "Edema"],
        "target": "Stage",
        "sep": ","
    },
    {
        "name": "diabetes",
        "drop_columns": [],
        "encode_columns": [],
        "target": "Outcome",
        "sep": ","
    },
        {
        "name": "heart_disease",
        "drop_columns": [],
        "encode_columns": [],
        "target": "condition",
        "sep": ","
    },
    {
        "name": "sonar",
        "drop_columns": [],
        "encode_columns": [],
        "target": "R",
        "sep": ","
    },
        {
        "name": "stroke",
        "drop_columns": ["id"],
        "encode_columns": ["gender", "ever_married", "work_type", "Residence_type", "smoking_status"],
        "target": "stroke",
        "sep": ","
    },
        {
        "name": "covtype",
        "drop_columns": [],
        "encode_columns": [],
        "target": "Cover_Type",
        "sep": ","
    },
    {
        "name": "wine",
        "drop_columns": [],
        "encode_columns": [],
        "target": "quality",
        "sep": ";"
    },
        {
        "name": "breast",
        "drop_columns": ["id"],
        "encode_columns": [],
        "target": "diagnosis",
        "sep": ","
    }
]
