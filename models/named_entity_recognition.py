from transformers import pipeline
from utils.config import MODELS, HF_TOKEN
import streamlit as st

class NERModel:
    def __init__(self):
        self.model_config = MODELS["ner"]
        self.pipeline = None
        
    @st.cache_resource
    def _load_model(_self):
        """NER model yükleme - cache ile performans optimizasyonu"""
        try:
            pipeline_obj = pipeline(
                _self.model_config["task"],
                model=_self.model_config["model_name"],
                token=HF_TOKEN,
                aggregation_strategy="simple"  # Aynı entity'yi birleştir
            )
            return pipeline_obj
        except Exception as e:
            st.error(f"NER modeli yüklenemedi: {str(e)}")
            return None
    
    def predict(self, text):
        """
        Named Entity Recognition tahmini yapar
        
        Args:
            text (str): Varlık tanıma yapılacak metin
            
        Returns:
            list: Bulunan varlıklar (entity_group, word, score içeren dict listesi)
        """
        if self.pipeline is None:
            self.pipeline = self._load_model()
            
        if self.pipeline is None:
            raise Exception("NER modeli yüklenemedi!")
            
        # Tahmin yap
        entities = self.pipeline(text)
        
        # Sonuçları temizle ve filtrele
        filtered_entities = []
        for entity in entities:
            # Minimum güven eşiği
            if entity['score'] > 0.5:
                # Word'deki ## işaretlerini temizle (BERT tokenization)
                clean_word = entity['word'].replace('##', '').replace(' ', '')
                entity['word'] = clean_word
                filtered_entities.append(entity)
        
        return filtered_entities