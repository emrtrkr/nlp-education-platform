# 🤖 NLP Eğitim Platformu

5 Temel NLP Modelini öğrenmek ve uygulamak için interaktif Streamlit uygulaması.

## 🎯 Özellikler

Bu platform aşağıdaki NLP görevlerini kapsar:

1. **📝 Text Classification** - Metin sınıflandırma (Sentiment Analysis)
2. **👤 Named Entity Recognition** - İsimli varlık tanıma  
3. **❓ Question Answering** - Soru-cevap sistemi
4. **📄 Text Summarization** - Metin özetleme
5. **✨ Text Generation** - Yaratıcı metin üretimi

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- Hugging Face hesabı ve API token

### Adımlar

1. **Repo'yu klonla:**
```bash
git clone <repo-url>
cd nlp_education_project
```

2. **Gerekli paketleri yükle:**
```bash
pip install -r requirements.txt
```

3. **Environment dosyasını oluştur:**
```bash
# .env dosyası oluştur ve içine şunu ekle:
HF_TOKEN=your_huggingface_token_here
```

4. **Uygulamayı çalıştır:**
```bash
streamlit run main.py
```

## 📁 Proje Yapısı

```
nlp_education_project/
│
├── main.py                 # Ana Streamlit uygulaması
├── .env                    # Environment variables
├── requirements.txt        # Gerekli kütüphaneler
│
├── models/                 # Model sınıfları
│   ├── text_classification.py
│   ├── named_entity_recognition.py
│   ├── question_answering.py
│   ├── text_summarization.py
│   └── text_generation.py
│
├── utils/                  # Yardımcı dosyalar
│   ├── config.py          # Konfigürasyon
│   └── content.py         # Eğitim içerikleri
│
└── data/                  # Örnek veriler
    └── sample_texts/
```

## 🛠️ Kullanılan Teknolojiler

- **Streamlit**: Web arayüzü
- **Transformers**: Hugging Face modelleri
- **PyTorch**: Backend framework
- **Python-dotenv**: Environment variable yönetimi

## 📚 Kullanılan Modeller

1. **Text Classification**: `distilbert-base-uncased-finetuned-sst-2-english`
2. **NER**: `dbmdz/bert-large-cased-finetuned-conll03-english`  
3. **Question Answering**: `distilbert-base-cased-distilled-squad`
4. **Summarization**: `facebook/bart-large-cnn`
5. **Text Generation**: `gpt2`

## 🎓 Eğitim İçeriği

Her model için şunlar sağlanır:
- ✅ Detaylı açıklamalar (Ne işe yarar?)
- ✅ Kullanım alanları (Nerede kullanılır?)  
- ✅ Interaktif demo
- ✅ Örnek metinler
- ✅ Gerçek hayat senaryoları

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📞 İletişim

Sorularınız için:
- GitHub Issues açın
- Email: [your-email]

## 📄 Lisans

MIT License - Detaylar için `LICENSE` dosyasına bakın.

---

**Happy Learning! 🚀**