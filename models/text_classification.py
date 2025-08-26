from transformers import pipeline
from utils.config import MODELS, HF_TOKEN
import streamlit as st

class TextClassificationModel:
    def __init__(self):
        self.model_config = MODELS["text_classification"]
        self.pipeline = None
        
    @st.cache_resource
    def _load_model(_self):
        """Model yükleme - cache ile performans optimizasyonu"""
        try:
            pipeline_obj = pipeline(
                _self.model_config["task"],
                model=_self.model_config["model_name"],
                token=HF_TOKEN
            )
            return pipeline_obj
        except Exception as e:
            st.error(f"Model yüklenemedi: {str(e)}")
            return None
    
    def predict(self, text):
        """
        Metin sınıflandırma tahmini yapar
        
        Args:
            text (str): Sınıflandırılacak metin
            
        Returns:
            list: Tahmin sonuçları (label, score içeren dict listesi)
        """
        if self.pipeline is None:
            self.pipeline = self._load_model()
            
        if self.pipeline is None:
            raise Exception("Model yüklenemedi!")
            
        # Tahmin yap
        result = self.pipeline(text)
        
        return result