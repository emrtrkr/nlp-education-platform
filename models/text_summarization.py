from transformers import pipeline
from utils.config import MODELS, HF_TOKEN
import streamlit as st

class SummarizationModel:
    def __init__(self):
        self.model_config = MODELS["summarization"]
        self.pipeline = None
        
    @st.cache_resource
    def _load_model(_self):
        """Summarization model yükleme - cache ile performans optimizasyonu"""
        try:
            pipeline_obj = pipeline(
                _self.model_config["task"],
                model=_self.model_config["model_name"],
                token=HF_TOKEN
            )
            return pipeline_obj
        except Exception as e:
            st.error(f"Summarization modeli yüklenemedi: {str(e)}")
            return None
    
    def predict(self, text, max_length=100, min_length=30):
        """
        Metin özetleme tahmini yapar
        
        Args:
            text (str): Özetlenecek metin
            max_length (int): Maksimum özet uzunluğu
            min_length (int): Minimum özet uzunluğu
            
        Returns:
            str: Özet metin
        """
        if self.pipeline is None:
            self.pipeline = self._load_model()
            
        if self.pipeline is None:
            raise Exception("Summarization modeli yüklenemedi!")
            
        # Input validation
        if len(text.strip()) < 50:
            raise Exception("Özetleme için daha uzun bir metin gerekiyor!")
            
        # Çok uzun metinleri böl (BART modeli için token limiti)
        if len(text) > 1000:
            text = text[:1000] + "..."
            
        # Min/Max length kontrolü
        if min_length >= max_length:
            min_length = max_length // 2
            
        try:
            # Tahmin yap
            result = self.pipeline(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False  # Deterministik sonuçlar için
            )
            
            summary = result[0]['summary_text']
            return summary
            
        except Exception as e:
            # BART modeli bazen token limit hatası verebilir
            if "token" in str(e).lower():
                # Daha kısa metin ile tekrar dene
                shorter_text = text[:500]
                result = self.pipeline(
                    shorter_text,
                    max_length=max_length//2,
                    min_length=min_length//2,
                    do_sample=False
                )
                return result[0]['summary_text']
            else:
                raise e