# Eğitim içerikleri ve açıklamalar

EDUCATIONAL_CONTENT = {
    "text_classification": {
        "title": "📝 Text Classification (Metin Sınıflandırma)",
        "description": """
        **Ne İşe Yarar?**
        Text Classification, metinleri önceden tanımlanmış kategorilere ayıran bir NLP görevidir. 
        En yaygın örneği sentiment analysis (duygu analizi) dir.
        
        **Nasıl Çalışır?**
        - Model metni okur ve analiz eder
        - Önceden eğitildiği kategoriler arasından en uygun olanı seçer
        - Her kategori için bir güven skoru verir
        
        **Gerçek Hayat Kullanımları:**
        - 📧 Email spam detection
        - 🛒 E-ticaret ürün yorumu analizi  
        - 📰 Haber kategorilendirme
        - 💬 Sosyal medya duygu analizi
        - 🎬 Film/kitap değerlendirmeleri
        
        **Bu Örnekte:**
        Sentiment Analysis kullanıyoruz - metninizin pozitif mi negatif mi olduğunu belirliyor.
        """,
        "examples": [
            "I love this product, it's amazing!",
            "This movie was terrible and boring.",
            "The food was okay, nothing special.",
            "Best purchase I've ever made!"
        ]
    },
    
    "ner": {
        "title": "👤 Named Entity Recognition (İsimli Varlık Tanıma)",
        "description": """
        **Ne İşe Yarar?**
        NER, metinlerdeki önemli varlıkları (kişi, yer, organizasyon, tarih vb.) otomatik olarak bulur ve sınıflandırır.
        
        **Nasıl Çalışır?**
        - Metni kelime kelime analiz eder
        - Her kelimenin hangi kategori olabileceğini tahmin eder
        - Birbirine bağlı kelimeleri gruplar (Steve Jobs → tek kişi)
        
        **Varlık Türleri:**
        - 👤 PER (Person): Kişi isimleri
        - 🏢 ORG (Organization): Şirket, kurum isimleri  
        - 📍 LOC (Location): Yer isimleri
        - 🔢 MISC (Miscellaneous): Diğer önemli varlıklar
        
        **Gerçek Hayat Kullanımları:**
        - 📄 CV ve özgeçmiş analizi
        - 📰 Haber metinlerinden bilgi çıkarma
        - 🏥 Tıbbi kayıtlardan hasta/ilaç bilgisi
        - 💼 Sözleşme analizinde taraf/tarih bulma
        
        **Bu Örnekte:**
        İngilizce metinlerdeki kişi, yer ve organizasyon isimlerini bulacak.
        """,
        "examples": [
            "Apple Inc. was founded by Steve Jobs in Cupertino, California.",
            "Microsoft CEO Satya Nadella announced new products in Seattle.",
            "The meeting between Joe Biden and Emmanuel Macron took place in Paris.",
            "Google's headquarters in Mountain View employs thousands of engineers."
        ]
    },
    
    "question_answering": {
        "title": "❓ Question Answering (Soru-Cevap Sistemi)",
        "description": """
        **Ne İşe Yarar?**
        Verilen bir metin içerisinden, sorulan sorunun cevabını otomatik olarak bulur ve çıkarır.
        
        **Nasıl Çalışır?**
        - Soru ve context (bağlam) metni alır
        - Soruyu anlar ve ne aradığını çözer  
        - Context içinde cevabı bulur
        - Bulduğu cevabın ne kadar güvenilir olduğunu belirtir
        
        **Önemli Not:**
        Model SADECE verdiğiniz metin içinden cevap arar. Genel bilgi sorularına cevap vermez.
        
        **Gerçek Hayat Kullanımları:**
        - 📚 Dokümantasyon arama sistemleri
        - 🤖 Customer service chatbotları
        - 📖 Eğitim platformlarında otomatik soru-cevap
        - 📋 Uzun raporlardan hızlı bilgi çıkarma
        - 🏥 Tıbbi kayıtlarda spesifik bilgi arama
        
        **Bu Örnekte:**
        Verdiğiniz metin içerisinden sorularınızı cevaplayacak.
        """,
        "examples": [
            {
                "context": "Artificial Intelligence (AI) is transforming many industries. It was first coined as a term in 1956 by John McCarthy. Today, AI is used in healthcare, finance, and transportation.",
                "questions": [
                    "Who coined the term AI?",
                    "When was AI first named?", 
                    "What industries use AI today?"
                ]
            }
        ]
    },
    
    "summarization": {
        "title": "📄 Text Summarization (Metin Özetleme)",
        "description": """
        **Ne İşe Yarar?**
        Uzun metinleri, ana fikirlerini koruyarak kısa ve öz bir şekilde özetler.
        
        **İki Tür Özetleme:**
        - **Extractive**: Metindeki önemli cümleleri seçer ve birleştirir
        - **Abstractive**: Yeni cümleler oluşturarak özet yazar (daha gelişmiş)
        
        **Nasıl Çalışır?**
        - Metni paragraf paragraf analiz eder
        - En önemli bilgileri tespit eder
        - Gereksiz detayları çıkarır
        - Ana konuları koruyarak kısa özet oluşturur
        
        **Gerçek Hayat Kullanımları:**
        - 📰 Haber özetleme servisleri
        - 📚 Araştırma makalesi özetleri
        - 💼 İş raporlarının executive summary'si
        - 📧 Uzun email zincirlerinin özeti
        - 🎓 Ders notlarından kısa çıkarımlar
        
        **Bu Örnekte:**
        Uzun metinlerinizi 2-3 cümlelik özete dönüştürecek.
        """,
        "examples": [
            """Artificial Intelligence has become one of the most transformative technologies of our time. From healthcare to finance, from transportation to entertainment, AI is revolutionizing how we work and live. Machine learning algorithms can now diagnose diseases, predict market trends, and even create art. Deep learning models have achieved superhuman performance in games like chess and Go. Natural Language Processing has enabled chatbots and virtual assistants that can understand and respond to human queries. However, AI also raises important ethical questions about privacy, job displacement, and algorithmic bias."""
        ]
    },
    
    "text_generation": {
        "title": "✨ Text Generation (Metin Üretimi)", 
        "description": """
        **Ne İşe Yarar?**
        Verilen bir başlangıç metni alarak, mantıklı ve tutarlı bir şekilde devamını getirir.
        
        **Nasıl Çalışır?**
        - Başlangıç metnini analiz eder
        - Bir sonraki en olası kelimeleri tahmin eder
        - Bu süreci tekrarlayarak uzun metinler oluşturur
        - Context'i koruyarak tutarlılık sağlar
        
        **Parametreler:**
        - **Max Length**: Üretilecek maksimum kelime sayısı
        - **Temperature**: Yaratıcılık seviyesi (düşük=güvenli, yüksek=yaratıcı)
        - **Top-p**: Kelime seçiminde çeşitlilik
        
        **Gerçek Hayat Kullanımları:**
        - ✍️ İçerik yazarları için ilham kaynağı
        - 📝 Blog yazıları için taslak oluşturma
        - 💌 Email templates üretme
        - 📖 Hikaye ve roman yazımında yardım
        - 💼 İş sunumları için içerik üretimi
        
        **Bu Örnekte:**
        GPT-2 modeli kullanıyoruz - başlangıç cümlenizi yaratıcı şekilde tamamlayacak.
        """,
        "examples": [
            "The future of artificial intelligence is",
            "Once upon a time in a small village",
            "The most important skill for a programmer is",
            "Climate change will affect our planet by"
        ]
    }
}