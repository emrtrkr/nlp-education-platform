from transformers import pipeline
from utils.config import MODELS, HF_TOKEN
import streamlit as st

class QuestionAnsweringModel:
    def __init__(self):
        self.model_config = MODELS["question_answering"]
        self.pipeline = None
        
    @st.cache_resource
    def _load_model(_self):
        """Question Answering model yükleme - cache ile performans optimizasyonu"""
        try:
            pipeline_obj = pipeline(
                _self.model_config["task"],
                model=_self.model_config["model_name"],
                token=HF_TOKEN
            )
            return pipeline_obj
        except Exception as e:
            st.error(f"QA modeli yüklenemedi: {str(e)}")
            return None
    
    def predict(self, question, context):
        """
        Soru-cevap tahmini yapar
        
        Args:
            question (str): Sorulacak soru
            context (str): Cevabın aranacağı metin (context)
            
        Returns:
            dict: Cevap ve güven skoru içeren dict
        """
        if self.pipeline is None:
            self.pipeline = self._load_model()
            
        if self.pipeline is None:
            raise Exception("QA modeli yüklenemedi!")
            
        # Input validation
        if len(context.strip()) == 0:
            raise Exception("Context boş olamaz!")
            
        if len(question.strip()) == 0:
            raise Exception("Soru boş olamaz!")
            
        # Tahmin yap
        result = self.pipeline({
            'question': question,
            'context': context
        })
        
        return result