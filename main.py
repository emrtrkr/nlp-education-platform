import streamlit as st
import sys
import os

# Path ayarları
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.config import PAGE_CONFIG, HF_TOKEN
from utils.content import EDUCATIONAL_CONTENT
from models.text_classification import TextClassificationModel
from models.named_entity_recognition import NERModel
from models.question_answering import QuestionAnsweringModel
from models.text_summarization import SummarizationModel
from models.text_generation import TextGenerationModel

# Streamlit sayfa konfigürasyonu
st.set_page_config(**PAGE_CONFIG)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .model-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
    }
    .example-text {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Ana başlık
    st.markdown("""
    <div class="main-header">
        <h1>🤖 NLP Eğitim Platformu</h1>
        <h3>5 Temel NLP Modelini Öğren ve Uygula</h3>
        <p>Hugging Face Transformers ile Doğal Dil İşleme Dünyasına Adım At!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar - Model seçimi
    st.sidebar.title("🎯 Model Seçimi")
    st.sidebar.markdown("Öğrenmek istediğiniz NLP görevini seçin:")
    
    tab_names = [
        "🏠 Ana Sayfa",
        "📝 Text Classification", 
        "👤 Named Entity Recognition",
        "❓ Question Answering",
        "📄 Text Summarization",
        "✨ Text Generation"
    ]
    
    # Ana tabs
    tabs = st.tabs(tab_names)
    
    # Ana Sayfa
    with tabs[0]:
        show_home_page()
    
    # Text Classification
    with tabs[1]:
        show_text_classification()
    
    # Named Entity Recognition  
    with tabs[2]:
        show_ner()
        
    # Question Answering
    with tabs[3]:
        show_question_answering()
        
    # Text Summarization
    with tabs[4]:
        show_summarization()
        
    # Text Generation
    with tabs[5]:
        show_text_generation()

def show_home_page():
    st.markdown("## 👋 Hoş Geldiniz!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Bu Platform Ne İşe Yarar?
        
        Bu eğitim platformu, **5 temel NLP görevini** interaktif olarak öğrenmenizi sağlar:
        
        1. **📝 Text Classification**: Metinleri kategorilere ayırma
        2. **👤 Named Entity Recognition**: Metindeki önemli varlıkları bulma  
        3. **❓ Question Answering**: Metin içinden soru cevaplama
        4. **📄 Text Summarization**: Uzun metinleri özetleme
        5. **✨ Text Generation**: Yaratıcı metin üretme
        
        ### Nasıl Kullanılır?
        
        - Yukarıdaki **tab'lere** tıklayarak farklı modellere geçiş yapın
        - Her model için **detaylı açıklamalar** okuyun
        - **Örnek metinler** ile test edin
        - Kendi metinlerinizi deneyerek öğrenin!
        """)
    
    with col2:
        st.markdown("### 🎯 Öğrenme Hedefleri")
        st.success("✅ NLP temel görevlerini anlama")
        st.success("✅ Hugging Face modellerini kullanma") 
        st.success("✅ Gerçek hayat uygulamalarını görme")
        st.success("✅ Pratik deneyim kazanma")
        
        st.markdown("### 🚀 Hemen Başlayın!")
        st.info("👆 Yukarıdaki tab'lerden herhangi birine tıklayarak başlayabilirsiniz!")

def show_text_classification():
    content = EDUCATIONAL_CONTENT["text_classification"]
    
    st.markdown(f"## {content['title']}")
    
    # Eğitim içeriği
    with st.expander("📚 Bu Model Hakkında Bilgi Al", expanded=True):
        st.markdown(content['description'])
    
    # Model kullanımı
    st.markdown("### 🛠️ Modeli Deneyin")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Örnek metin seçimi için session state kullan
        if 'selected_text' not in st.session_state:
            st.session_state.selected_text = ""
        
        # Örnek metinler
        st.markdown("**Örnek metinlerden birini seçin:**")
        for i, example in enumerate(content['examples']):
            if st.button(f"📄 Örnek {i+1}", key=f"example_{i}"):
                st.session_state.selected_text = example
        
        # Kullanıcı input - session state değeriyle başlat
        user_input = st.text_area(
            "Analiz etmek istediğiniz metni yazın:",
            value=st.session_state.selected_text,
            placeholder="Örnek: I love this product, it's amazing!",
            height=100
        )
    
    with col2:
        if st.button("🔍 Analiz Et", type="primary"):
            if user_input:
                with st.spinner("Model analiz ediyor..."):
                    try:
                        model = TextClassificationModel()
                        result = model.predict(user_input)
                        
                        st.success("✅ Analiz Tamamlandı!")
                        
                        # Sonuçları göster
                        label = result[0]['label']
                        score = result[0]['score']
                        
                        if label == "POSITIVE":
                            st.markdown(f"### 😊 **Pozitif** ({score:.2%} güven)")
                            st.success("Bu metin pozitif bir duygu içeriyor!")
                        else:
                            st.markdown(f"### 😞 **Negatif** ({score:.2%} güven)")  
                            st.error("Bu metin negatif bir duygu içeriyor!")
                            
                    except Exception as e:
                        st.error(f"Hata oluştu: {str(e)}")
            else:
                st.warning("⚠️ Lütfen analiz edilecek metni yazın!")

def show_ner():
    content = EDUCATIONAL_CONTENT["ner"]
    
    st.markdown(f"## {content['title']}")
    
    with st.expander("📚 Bu Model Hakkında Bilgi Al", expanded=True):
        st.markdown(content['description'])
    
    st.markdown("### 🛠️ Modeli Deneyin")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Örnek metin seçimi için session state
        if 'selected_ner_text' not in st.session_state:
            st.session_state.selected_ner_text = ""
        
        # Örnek metinler
        st.markdown("**Örnek metinlerden birini seçin:**")
        for i, example in enumerate(content['examples']):
            if st.button(f"📄 Örnek {i+1}", key=f"ner_example_{i}"):
                st.session_state.selected_ner_text = example
        
        # Kullanıcı input
        user_input = st.text_area(
            "Varlık tanıma yapılacak metni yazın:",
            value=st.session_state.selected_ner_text,
            placeholder="Örnek: Apple Inc. was founded by Steve Jobs in Cupertino.",
            height=100
        )
    
    with col2:
        if st.button("🔍 Varlıkları Bul", type="primary"):
            if user_input:
                with st.spinner("Model varlıkları tespit ediyor..."):
                    try:
                        model = NERModel()
                        entities = model.predict(user_input)
                        
                        st.success("✅ Analiz Tamamlandı!")
                        
                        if entities:
                            st.markdown("### 🎯 Bulunan Varlıklar:")
                            for entity in entities:
                                entity_type = entity['entity_group']
                                word = entity['word']
                                score = entity['score']
                                
                                # Emoji seçimi
                                emoji = "👤" if entity_type == "PER" else "🏢" if entity_type == "ORG" else "📍" if entity_type == "LOC" else "🔤"
                                
                                st.markdown(f"{emoji} **{word}** → {entity_type} ({score:.2%})")
                        else:
                            st.info("Bu metinde tanınabilir varlık bulunamadı.")
                            
                    except Exception as e:
                        st.error(f"Hata oluştu: {str(e)}")
            else:
                st.warning("⚠️ Lütfen analiz edilecek metni yazın!")

def show_question_answering():
    content = EDUCATIONAL_CONTENT["question_answering"]
    
    st.markdown(f"## {content['title']}")
    
    with st.expander("📚 Bu Model Hakkında Bilgi Al", expanded=True):
        st.markdown(content['description'])
    
    st.markdown("### 🛠️ Modeli Deneyin")
    
    # Context ve soru için session state
    if 'selected_qa_context' not in st.session_state:
        st.session_state.selected_qa_context = ""
    if 'selected_qa_questions' not in st.session_state:
        st.session_state.selected_qa_questions = []
    
    # Context girişi
    context = st.text_area(
        "📄 Context (Bağlam metni):",
        value=st.session_state.selected_qa_context,
        placeholder="Buraya sorunun cevabını içeren metni yazın...",
        height=150
    )
    
    # Soru girişi
    question = st.text_input(
        "❓ Soru:", 
        placeholder="Context hakkında sormak istediğiniz soruyu yazın..."
    )
    
    # Örnek context ve sorular
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("📋 Örnek Context Yükle"):
            example = content['examples'][0]
            st.session_state.selected_qa_context = example['context']
            st.session_state.selected_qa_questions = example['questions']
            st.rerun()
    
    with col2:
        if st.session_state.selected_qa_questions:
            st.markdown("**Örnek sorular:**")
            for i, q in enumerate(st.session_state.selected_qa_questions):
                if st.button(f"❓ {q[:30]}...", key=f"qa_question_{i}"):
                    # Soruyu otomatik doldur (JavaScript ile yapılması gerekiyor, basit çözüm için info göster)
                    st.info(f"Örnek soru: {q}")
                    st.markdown("👆 Bu soruyu yukarıdaki soru kutusuna kopyalayın")
    
    if st.button("🔍 Soruyu Cevapla", type="primary"):
        if context and question:
            with st.spinner("Model cevabı arıyor..."):
                try:
                    model = QuestionAnsweringModel()
                    result = model.predict(question, context)
                    
                    st.success("✅ Cevap Bulundu!")
                    
                    answer = result['answer']
                    score = result['score']
                    
                    st.markdown("### 💬 Cevap:")
                    st.markdown(f"**{answer}**")
                    st.markdown(f"*Güven skoru: {score:.2%}*")
                    
                    if score < 0.1:
                        st.warning("⚠️ Düşük güven skoru - cevap context'te net olarak bulunamadı.")
                        
                except Exception as e:
                    st.error(f"Hata oluştu: {str(e)}")
        else:
            st.warning("⚠️ Lütfen hem context hem de soruyu yazın!")

def show_summarization():
    content = EDUCATIONAL_CONTENT["summarization"]
    
    st.markdown(f"## {content['title']}")
    
    with st.expander("📚 Bu Model Hakkında Bilgi Al", expanded=True):
        st.markdown(content['description'])
    
    st.markdown("### 🛠️ Modeli Deneyin")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Session state için summarization
        if 'selected_summary_text' not in st.session_state:
            st.session_state.selected_summary_text = ""
        
        # Örnek metin yükleme
        if st.button("📄 Örnek Uzun Metin Yükle"):
            st.session_state.selected_summary_text = content['examples'][0]
            st.rerun()
        
        user_input = st.text_area(
            "Özetlemek istediğiniz uzun metni yazın:",
            value=st.session_state.selected_summary_text,
            placeholder="Buraya özetlenmesini istediğiniz uzun metni yazın...",
            height=200
        )
    
    with col2:
        st.markdown("#### ⚙️ Ayarlar")
        max_length = st.slider("Maksimum özet uzunluğu:", 50, 200, 100)
        min_length = st.slider("Minimum özet uzunluğu:", 10, 100, 30)
        
        if st.button("📝 Özetle", type="primary"):
            if user_input:
                if len(user_input) < 100:
                    st.warning("⚠️ Özetleme için daha uzun bir metin gerekiyor (en az 100 karakter)")
                else:
                    with st.spinner("Model özet hazırlıyor..."):
                        try:
                            model = SummarizationModel()
                            summary = model.predict(user_input, max_length, min_length)
                            
                            st.success("✅ Özet Hazırlandı!")
                            
                            col_orig, col_summ = st.columns(2)
                            
                            with col_orig:
                                st.markdown("#### 📄 Orijinal Metin")
                                st.markdown(f"**Uzunluk:** {len(user_input)} karakter")
                                st.text_area("", user_input, height=200, disabled=True)
                            
                            with col_summ:
                                st.markdown("#### 📋 Özet")
                                st.markdown(f"**Uzunluk:** {len(summary)} karakter")
                                st.text_area("", summary, height=200, disabled=True)
                                
                                # Sıkıştırma oranı
                                compression_ratio = len(user_input) / len(summary)
                                st.metric("Sıkıştırma Oranı", f"{compression_ratio:.1f}x")
                                
                        except Exception as e:
                            st.error(f"Hata oluştu: {str(e)}")
            else:
                st.warning("⚠️ Lütfen özetlenecek metni yazın!")

def show_text_generation():
    content = EDUCATIONAL_CONTENT["text_generation"]
    
    st.markdown(f"## {content['title']}")
    
    with st.expander("📚 Bu Model Hakkında Bilgi Al", expanded=True):
        st.markdown(content['description'])
    
    st.markdown("### 🛠️ Modeli Deneyin")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Session state için text generation
        if 'selected_gen_text' not in st.session_state:
            st.session_state.selected_gen_text = ""
        
        user_input = st.text_input(
            "Başlangıç metnini yazın:",
            value=st.session_state.selected_gen_text,
            placeholder="Örnek: The future of artificial intelligence is...",
        )
        
        st.markdown("**Örnek başlangıçlardan birini seçin:**")
        for i, example in enumerate(content['examples']):
            if st.button(f"✨ Örnek {i+1}: {example[:30]}...", key=f"gen_example_{i}"):
                st.session_state.selected_gen_text = example
                st.rerun()
    
    with col2:
        st.markdown("#### ⚙️ Üretim Ayarları")
        max_length = st.slider("Maksimum uzunluk:", 50, 200, 100)
        temperature = st.slider("Yaratıcılık (Temperature):", 0.1, 2.0, 0.7, 0.1)
        
        st.markdown("*Düşük temperature: Güvenli, tahmin edilebilir*")
        st.markdown("*Yüksek temperature: Yaratıcı, sürprizli*")
        
        if st.button("✨ Metin Üret", type="primary"):
            if user_input:
                with st.spinner("Model metin üretiyor..."):
                    try:
                        model = TextGenerationModel()
                        generated_text = model.predict(user_input, max_length, temperature)
                        
                        st.success("✅ Metin Üretildi!")
                        
                        st.markdown("### 📝 Üretilen Metin:")
                        st.markdown("---")
                        
                        # Başlangıç ve üretilen kısmı ayır
                        original_length = len(user_input)
                        full_text = generated_text[0]['generated_text']
                        new_text = full_text[original_length:].strip()
                        
                        # Sonucu göster
                        st.markdown(f"**Başlangıç:** {user_input}")
                        st.markdown(f"**Devamı:** {new_text}")
                        
                        st.markdown("---")
                        st.markdown("**Tam Metin:**")
                        st.write(full_text)
                        
                    except Exception as e:
                        st.error(f"Hata oluştu: {str(e)}")
            else:
                st.warning("⚠️ Lütfen başlangıç metnini yazın!")

# Token kontrolü
def check_token():
    if not HF_TOKEN:
        st.error("🚨 Hugging Face token bulunamadı!")
        st.markdown("""
        Lütfen `.env` dosyasına şunu ekleyin:
        ```
        HF_TOKEN=your_huggingface_token_here
        ```
        """)
        st.stop()
        return False
    return True

if __name__ == "__main__":
    # Token kontrolü
    check_token()
    
    # Ana uygulamayı çalıştır
    main()