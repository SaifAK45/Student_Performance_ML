import os,sys
from dataclasses import dataclass

import pandas as pd 
import numpy as np 

from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class  DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(self):
        # This function is responsible for data transformation
        try:
            numerical_coloumns = ['reading_score','writing_score']
            categorical_coloumns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            nums_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
            logging.info('numerical coloumns encoding completed')
            logging.info(f'numerical coloumns{numerical_coloumns}')

            cate_pipeline = Pipeline(
            steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder(handle_unknown='ignore')),
                    ('scaler', StandardScaler(with_mean=False))
                    ]
                    )
            logging.info('categorical coloumns encoding completed')
            logging.info(f'categorical coloumns{categorical_coloumns}')

            preprocessor = ColumnTransformer(
                [
                    ('numer_pipeline',nums_pipeline,numerical_coloumns),
                    ('cate_pipeline',cate_pipeline,categorical_coloumns)
                ],remainder='passthrough'
            )

            return preprocessor

        
        except Exception as e:
            raise CustomException(e,sys)    


    def initiate_data_tranformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train & test data compeleted')

            logging.info('obtaining the preprocessor object')
            preprocessor_object = self.get_data_transformation_obj()

            target_col = 'math_score'
            numerical_col = ['reading_score','writing_score']
            categorical_col = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            input_feature_train_df = train_df.drop(columns=[target_col],axis=1)
            target_feature_train_df = train_df[target_col]     # This is same like X,y split

            input_feature_test_df = test_df.drop(columns=[target_col],axis=1)
            target_feature_test_df = test_df[target_col] 
            logging.info('Applying preprocessing on train and test dataframe')

            input_feature_train_arr = preprocessor_object.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info('Saved preprocessing object...')

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_object
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e,sys)