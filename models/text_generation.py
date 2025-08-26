from transformers import pipeline
from utils.config import MODELS, HF_TOKEN
import streamlit as st

class TextGenerationModel:
    def __init__(self):
        self.model_config = MODELS["text_generation"]
        self.pipeline = None
        
    @st.cache_resource
    def _load_model(_self):
        """Text Generation model yükleme - cache ile performans optimizasyonu"""
        try:
            pipeline_obj = pipeline(
                _self.model_config["task"],
                model=_self.model_config["model_name"],
                token=HF_TOKEN
            )
            return pipeline_obj
        except Exception as e:
            st.error(f"Text Generation modeli yüklenemedi: {str(e)}")
            return None
    
    def predict(self, prompt, max_length=100, temperature=0.7):
        """
        Metin üretme tahmini yapar
        
        Args:
            prompt (str): Başlangıç metni
            max_length (int): Maksimum üretilecek uzunluk  
            temperature (float): Yaratıcılık seviyesi (0.1-2.0)
            
        Returns:
            list: Üretilen metin içeren dict listesi
        """
        if self.pipeline is None:
            self.pipeline = self._load_model()
            
        if self.pipeline is None:
            raise Exception("Text Generation modeli yüklenemedi!")
            
        # Input validation
        if len(prompt.strip()) == 0:
            raise Exception("Başlangıç metni boş olamaz!")
            
        # Prompt çok uzunsa kısalt
        if len(prompt) > 200:
            prompt = prompt[:200]
            
        # Temperature sınırları kontrol et
        temperature = max(0.1, min(2.0, temperature))
        
        try:
            # Tahmin yap
            result = self.pipeline(
                prompt,
                max_length=max_length,
                temperature=temperature,
                do_sample=True,  # Çeşitlilik için sampling kullan
                top_p=0.9,       # Top-p sampling
                pad_token_id=50256,  # GPT-2 için pad token
                num_return_sequences=1  # Tek sonuç döndür
            )
            
            return result
            
        except Exception as e:
            if "token" in str(e).lower() or "length" in str(e).lower():
                # Token limiti hatası durumunda daha kısa dene
                result = self.pipeline(
                    prompt,
                    max_length=min(max_length, 50),
                    temperature=temperature,
                    do_sample=True,
                    pad_token_id=50256,
                    num_return_sequences=1
                )
                return result
            else:
                raise e